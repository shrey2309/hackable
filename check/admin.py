from django.contrib import admin

from .models import Todo_safe, Todo_unsafe, user

admin.site.register(Todo_unsafe)
admin.site.register(Todo_safe)
admin.site.register(user)
