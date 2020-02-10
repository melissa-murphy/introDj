from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from uuid import uuid4


class Notes(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class NoteUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default="Smith")
    note_type = models.CharField(max_length=50, blank=True)


class NoteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified')

class PersonalNote(Notes):
    user = models.ForeignKey(User, on_delete=models.CASCADE)