from django.contrib import admin

from .models import Bovespa


class BovespaAdmin(admin.ModelAdmin):
    list_display =['Ticker','Date', 'Open', 'High','Low','Close','Volume']
    search_fields = ["Ticker"]
    list_filter = ["Ticker", "Date"]
    list_editable = ["Close"]
    class Meta:
        model = Bovespa

admin.site.register(Bovespa, BovespaAdmin)
