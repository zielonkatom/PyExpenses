from django.contrib import admin
from .models import Expenses, Earnings
# Register your models here.

admin.site.register(Earnings)
admin.site.register(Expenses)