from django.db import models
import uuid

# Create your models here.
# class BaseModel(models.Model):
#     uid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         abstract = True


class Students(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
