from django.contrib import admin
from .models import Notes
from .models import NoteAdmin
from .models import PersonalNote

# Register your models here.
admin.site.register(Notes, NoteAdmin, )
admin.site.register(PersonalNote, )
