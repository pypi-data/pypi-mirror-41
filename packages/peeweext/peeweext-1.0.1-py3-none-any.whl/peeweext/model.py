import inspect

import peewee as pw
import pendulum
from blinker import signal

from .validation import ValidationError
from .fields import DatetimeTZField

pre_save = signal('pre_save')
post_save = signal('post_save')
pre_delete = signal('pre_delete')
post_delete = signal('post_delete')
pre_init = signal('pre_init')


class ModelMeta(pw.ModelBase):
    """Model meta class, provide validation."""

    def __init__(cls, name, bases, attrs):
        """Store validator."""
        super().__init__(name, bases, attrs)
        setattr(cls, '_validators', {})  # {'field_name': `callable`}
        # add validator by model`s validation method
        for k, v in attrs.items():
            if k.startswith('validate_') and inspect.isfunction(v):
                fn = k[9:]  # 9 = len('validate_')
                if fn in cls._meta.fields:
                    cls._validators[fn] = v


class Model(pw.Model, metaclass=ModelMeta):
    created_at = DatetimeTZField(default=pendulum.now)
    updated_at = DatetimeTZField(default=pendulum.now)

    def __init__(self, *args, **kwargs):
        pre_init.send(type(self), instance=self)
        self._validate_errors = {}  # eg: {'field_name': 'error information'}
        super().__init__(*args, **kwargs)
        self.delete = self._delete

    def save(self, *args, **kwargs):
        skip_validation = kwargs.pop('skip_validation', False)
        if not skip_validation:
            if not self.is_valid:
                raise ValidationError(str(self._validate_errors))

        pk_value = self._pk
        created = kwargs.get('force_insert', False) or not bool(pk_value)
        pre_save.send(type(self), instance=self, created=created)
        ret = super().save(*args, **kwargs)
        post_save.send(type(self), instance=self, created=created)
        return ret

    def delete_instance(self, *args, **kwargs):
        model = type(self)
        pre_delete.send(model, instance=self)
        recursive = kwargs.get('recursive', False)
        delete_nullable = kwargs.get('delete_nullable', False)
        if recursive:
            dependencies = self.dependencies(delete_nullable)
            for query, fk in reversed(list(dependencies)):
                fk_model = fk.model
                if fk.null and not delete_nullable:
                    fk_model.update(**{fk.name: None}).where(query).execute()
                else:
                    fk_model.delete().where(query).execute()
        ret = model.delete().where(self._pk_expr()).execute()
        post_delete.send(type(self), instance=self)
        return ret

    def _delete(self, *args, **kwargs):
        raise UserWarning(
            "Use delete() in instance is forbidden! Try to use "
            "delete_instance()"
        )

    def _validate(self):
        """Validate model data and save errors
        """
        errors = {}

        for name, validator in self._validators.items():
            value = getattr(self, name)

            try:
                validator(self, value)
            except ValidationError as e:
                errors[name] = str(e)

        self._validate_errors = errors

    @property
    def errors(self):
        self._validate()
        return self._validate_errors

    @property
    def is_valid(self):
        return not self.errors


def _touch_model(sender, instance, created):
    if issubclass(sender, Model):
        instance.updated_at = pendulum.now()


pre_save.connect(_touch_model)
