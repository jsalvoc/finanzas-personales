from django.shortcuts import render

def index(request):
    nombre_plataforma = "FinanzasCentral"
    version_api = 1.0
    sistema_activo = True
    
    movimientos_recientes = [
        {"id_transaccion": "TX1001", "descripcion": "Pago de servicios básicos", "monto": 25000, "clasificacion": "gasto"},
        {"id_transaccion": "TX1002", "descripcion": "Compra de insumos operacionales", "monto": 150000, "clasificacion": "costo"},
        {"id_transaccion": "TX1003", "descripcion": "Mermas por daño de inventario", "monto": 12000, "clasificacion": "perdida"},
        {"id_transaccion": "TX1004", "descripcion": "Licencias de software", "monto": 45000, "clasificacion": "gasto"},
    ]
    
    total_operaciones = len(movimientos_recientes)
    
    contexto = {
        'plataforma': nombre_plataforma,
        'version': version_api,
        'estado': "Operativo" if sistema_activo else "En Mantenimiento",
        'movimientos': movimientos_recientes,
        'total_operaciones': total_operaciones,
    }
    
    return render(request, 'index.html', contexto)

def error_404(request, exception):
    contexto = {
        'mensaje_error': "El registro o ruta financiera que buscas no existe en nuestros sistemas."
    }
    return render(request, '404.html', contexto, status=404)