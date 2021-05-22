from django.contrib import admin
from .models import BtcBD

from import_export.admin import ImportExportActionModelAdmin

@admin.register(BtcBD)
class CryptAdmin(ImportExportActionModelAdmin):
    list_display = ("date", "close")
#admin.site.register(Crypt_base)
