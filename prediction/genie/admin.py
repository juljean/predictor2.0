from django.contrib import admin
from .models import CryptBD

from import_export.admin import ImportExportActionModelAdmin
@admin.register(CryptBD)
class CryptAdmin(ImportExportActionModelAdmin):
    list_display = ("date", "close")
    pass
#admin.site.register(Crypt_base)
