from django.db import models

# Create your models here.


class BaseModel(models.Model):
    isDelete = models.BooleanField(default=False, verbose_name='delete')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='create')
    modifyTime = models.DateTimeField(auto_now=True, verbose_name='modify')

    class Meta:
        abstract = True
