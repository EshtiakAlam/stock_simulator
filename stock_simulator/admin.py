from django.contrib import admin
from .models import Company, TradingStatus, News

admin.site.register(Company)
admin.site.register(TradingStatus)
admin.site.register(News)
# Register your models here.
