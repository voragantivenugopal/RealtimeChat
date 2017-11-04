from simpleeval import simple_eval
from django.db import models
from swampdragon.models import SelfPublishModel
from .serializers import RealEditorSerializer


class RealEditor(SelfPublishModel, models.Model):

    serializer_class = RealEditorSerializer
    message = models.CharField(max_length=255)
    editor_text = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.editor_text = self.message
        super(RealEditor, self).save(*args, **kwargs)

    def __str__(self):
        return '%s'.format(self.editor_text)
