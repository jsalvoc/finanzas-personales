from django.contrib import admin
from .models import PerfilAcceso
from .models import TipoCuenta
from .models import Usuario
from .models import Categoria
from .models import Cuenta
from .models import Presupuesto
from .models import Transaccion
from .models import HistorialAuditoria
from .models import IndicadorGestion

# Register your models here.
admin.site.register(PerfilAcceso)
admin.site.register(TipoCuenta)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Cuenta)
admin.site.register(Presupuesto)
admin.site.register(Transaccion)
admin.site.register(HistorialAuditoria)
admin.site.register(IndicadorGestion)
