from django.apps import apps
from django.conf import settings
from django.contrib.contenttypes.fields import (
    GenericForeignKey as BaseGenericForeignKey
)


class GenericForeignKey(BaseGenericForeignKey):
    def __init__(self, *args, **kwargs):
        self.related_models = kwargs.pop('related_models', None)
        super().__init__(*args, **kwargs)

    def get_related_models(self):
        if self.related_models is None:
            self.related_models = [
                m
                for m in apps.get_models()
                if m._meta.app_label in settings.PROJECT_APPS
            ]
        elif callable(self.related_models):
            self.related_models = list(self.related_models())
        return [
            apps.get_model(
                *m.split('.')
            ) if isinstance(m, str) else m for m in self.related_models
        ]
