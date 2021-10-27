from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models.deletion import CASCADE

class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()    