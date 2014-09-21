from django.contrib import admin

from whisky import models

# Register your models here.

admin.site.register(models.Country)
admin.site.register(models.Region)
admin.site.register(models.Distillery)
admin.site.register(models.Whisky)
admin.site.register(models.Brand)
admin.site.register(models.UserScore)
