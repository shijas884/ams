from django.contrib import admin
from orm.models import Company,Slot,Schedule,Visitors

# Register your models here.
admin.site.register(Company)
admin.site.register(Schedule)
admin.site.register(Slot)
admin.site.register(Visitors)

