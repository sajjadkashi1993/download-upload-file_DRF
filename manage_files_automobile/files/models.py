from django.db import models
from core.models import BaseModel


class Automobile(BaseModel):
    manufacturer=models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)


class Part(BaseModel):
    automobile = models.ForeignKey(Automobile, on_delete=models.CASCADE,related_name="parts")
    name = models.CharField(max_length=150)


class File(BaseModel):
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to='uploads/')
