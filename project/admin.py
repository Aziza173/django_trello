from django.contrib import admin
from .models import Project, Board, Column, Task

class BoardAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    filter_horizontal = ("members",)


admin.site.register(Project)
admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Task)