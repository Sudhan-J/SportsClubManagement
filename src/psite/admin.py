from django.contrib import admin
from psite.models import Employee,Event,Customer,Branch,BOOK,ATTEND

# Register your models here.
admin.site.register(Employee)
admin.site.register(Event)
admin.site.register(Customer)
admin.site.register(Branch)
admin.site.register(BOOK)
admin.site.register(ATTEND)