# FinanzasCentral - API REST de Finanzas Personales (Proyecto 27)

Plataforma financiera desarrollada con **Django** y **Django REST Framework (DRF)** para centralizar la gestión de presupuestos, cuentas, movimientos financieros, seguimiento de auditoría ante cambios de estado e indicadores de gestión.

## 1. Estructura del Proyecto

- `drf/`: Configuración principal del proyecto Django (`settings.py` desacoplado con `python-decouple`, `urls.py`).
- `gestionfinanzas_app/`: Aplicación principal con el modelo de datos (`models.py`), registro en administrador (`admin.py`), serializadores (`serializer.py`), controladores CRUD (`views.py`), enrutador REST (`urls.py`), migraciones (`migrations/`) y datos iniciales (`fixtures/`).
- `scripts_sql/configuracion_bd.sql`: Script SQL obligatorio para crear la base de datos MySQL, el usuario y asignar privilegios.
- `.env`: Variables de entorno con credenciales de conexión a MySQL y `SECRET_KEY`.
- `requirements.txt`: Lista estandarizada de dependencias del entorno virtual.

## 2. Modelo de Datos Implementado

1. **PerfilAcceso**: Perfiles de seguridad y niveles de permiso (`TOTAL`, `LECTURA_ESCRITURA`, `SOLO_LECTURA`).
2. **TipoCuenta**: Catálogo de tipos de cuentas (Cuenta Corriente, Cuenta Vista/RUT, Ahorro, Efectivo).
3. **Usuario**: Usuarios individuales que operan diariamente en la plataforma (RUT, contacto y perfil asociado).
4. **Categoria**: Clasificación de ingresos, gastos y ahorros con control de visibilidad pública o privada (`es_privada`).
5. **Cuenta**: Cuentas bancarias o billeteras de cada usuario con seguimiento de `saldo_inicial` y `saldo_actual`.
6. **Presupuesto**: Límites presupuestarios por categoría y rango de fechas con control de monto ejecutado y estado.
7. **Transaccion**: Movimientos diarios (`INGRESO`, `GASTO`, `TRANSFERENCIA`) con validación de estados (`PENDIENTE`, `COMPLETADA`, `OBSERVADA`, `ANULADA`) y marcado de situaciones excepcionales (`es_excepcional`).
8. **HistorialAuditoria**: Registro histórico de auditoría para cada cambio de estado en las transacciones.
9. **IndicadorGestion**: Resumen de indicadores financieros por usuario y período (ingresos, gastos, porcentaje de uso presupuestario y tendencia).

## 3. Instalación y Puesta en Marcha Paso a Paso

### Paso 1: Activar el Ambiente Virtual e Instalar Dependencias
```powershell
python -m venv ambiente
.\ambiente\Scripts\Activate
pip install -r requirements.txt
```

### Paso 2: Configurar la Base de Datos en MySQL
Ejecutar el script `scripts_sql/configuracion_bd.sql` en tu motor MySQL (MySQL Workbench, phpMyAdmin de XAMPP/Laragon o consola MySQL):
```sql
CREATE DATABASE IF NOT EXISTS finanzas_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER IF NOT EXISTS 'finanzas_user'@'localhost' IDENTIFIED BY 'Finanzas2026!';
GRANT ALL PRIVILEGES ON finanzas_db.* TO 'finanzas_user'@'localhost';
FLUSH PRIVILEGES;
```

### Paso 3: Verificar el archivo `.env`
En la raíz del proyecto (junto a `manage.py`) se incluye el archivo `.env` con las variables leídas por `drf/settings.py`:
```env
SECRET_KEY='django-insecure-+y2+wl@@8)=ym5*&b!ljq7=)xr2&vv4hx_03a&5yd9a@u*&f-_'
DEBUG=True
NAME='finanzas_db'
HOST='localhost'
PORT='3306'
USER='finanzas_user'
PASSWORD='Finanzas2026!'
```

### Paso 4: Crear y Aplicar Migraciones en MySQL
```powershell
python manage.py makemigrations
python manage.py migrate
```

### Paso 5: Cargar Datos Iniciales (`fixtures`) (Opcional recomendado)
```powershell
python manage.py loaddata data_perfiles data_tipos_cuenta data_categorias
```

### Paso 6: Crear Superusuario e Iniciar el Servidor
```powershell
python manage.py createsuperuser
python manage.py runserver
```

## 4. Endpoints REST Disponibles (CRUD Completo: GET, POST, PUT, PATCH, DELETE)

- **Raíz de la API (DefaultRouter)**: `http://127.0.0.1:8000/gestionfinanzas_app/`
- **Perfiles de Acceso**: `http://127.0.0.1:8000/gestionfinanzas_app/perfiles-acceso/`
- **Tipos de Cuenta**: `http://127.0.0.1:8000/gestionfinanzas_app/tipos-cuenta/`
- **Usuarios**: `http://127.0.0.1:8000/gestionfinanzas_app/usuarios/`
- **Categorías**: `http://127.0.0.1:8000/gestionfinanzas_app/categorias/`
- **Cuentas**: `http://127.0.0.1:8000/gestionfinanzas_app/cuentas/`
- **Presupuestos**: `http://127.0.0.1:8000/gestionfinanzas_app/presupuestos/`
- **Transacciones**: `http://127.0.0.1:8000/gestionfinanzas_app/transacciones/`
- **Historial de Auditoría**: `http://127.0.0.1:8000/gestionfinanzas_app/historial-auditoria/`
- **Indicadores de Gestión**: `http://127.0.0.1:8000/gestionfinanzas_app/indicadores-gestion/`
