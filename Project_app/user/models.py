from django.db import models
from django.db import models
import uuid
# Create your models here.


class Projects(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=800)
    tags = models.ManyToManyField('Tag',blank=True)
    price = models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote'),
    )
    #one to many
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_created=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)



class Tag(models.Model):
    name = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name