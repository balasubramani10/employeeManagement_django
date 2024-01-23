from django.contrib import admin
from .models import *
# Register your models here.

class Branch_Address(admin.StackedInline):
    model = Branch_Address


class Branch_Admin(admin.ModelAdmin):
    inlines = [Branch_Address]

admin.site.register(Department)
admin.site.register(Branch, Branch_Admin)


