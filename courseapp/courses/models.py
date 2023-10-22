from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.TextField(max_length=100, null=True)
    description = models.TextField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
