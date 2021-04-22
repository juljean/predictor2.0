from import_export import resources
from .models import CryptBD

class CryptResource(resources.ModelResource):
    class Meta:
        model = CryptBD