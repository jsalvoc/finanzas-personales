from django.db import models

str_habilitado = "Habilitado"
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"
str_codigo = "Código"
str_nombre = "Nombre"
str_descripcion = "Descripción"
str_email = "Email"
str_telefono = "Teléfono"


class PerfilAcceso(models.Model):
    codigo = models.CharField(str_codigo, max_length=20, null=False)
    nombre = models.CharField(str_nombre, max_length=50, null=False)
    descripcion = models.CharField(str_descripcion, max_length=200, null=True)
    nivel_permiso = models.CharField("Nivel de Permiso", max_length=30, default="ESTANDAR", null=False)
    habilitado = models.BooleanField(str_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Perfiles de acceso y roles de seguridad para usuarios de la plataforma financiera."

    def __str__(self):
        return f"{self.nombre} ({self.nivel_permiso})"


class TipoCuenta(models.Model):
    codigo = models.CharField(str_codigo, max_length=15, null=False)
    nombre = models.CharField(str_nombre, max_length=50, null=False)
    descripcion = models.CharField(str_descripcion, max_length=150, null=True)
    habilitado = models.BooleanField(str_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Catálogo de tipos de cuentas financieras (Corriente, Vista, Ahorro, Efectivo, Inversión)."

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Usuario(models.Model):
    nombre = models.CharField(str_nombre, max_length=150, null=False)
    rut = models.CharField("RUT", max_length=12, null=False)
    correo = models.EmailField(str_email, null=False)
    telefono = models.CharField(str_telefono, max_length=15, null=True)
    perfil = models.ForeignKey(PerfilAcceso, on_delete=models.CASCADE, null=False)
    habilitado = models.BooleanField(str_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Usuarios individuales que interactúan con la plataforma realizando operaciones financieras."

    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class Categoria(models.Model):
    nombre = models.CharField(str_nombre, max_length=50, null=False)
    descripcion = models.CharField(str_descripcion, max_length=150, null=True)
    tipo = models.CharField("Tipo de Categoría", max_length=20, null=False)
    es_privada = models.BooleanField("Información Privada", default=False, null=False)
    habilitado = models.BooleanField(str_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Clasificación de movimientos y presupuestos según tipo (INGRESO, GASTO, AHORRO) y privacidad."

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Cuenta(models.Model):
    nombre = models.CharField(str_nombre, max_length=60, null=False)
    institucion = models.CharField("Institución Financiera", max_length=60, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE, null=False)
    saldo_inicial = models.DecimalField("Saldo Inicial", max_digits=12, decimal_places=0, null=False)
    saldo_actual = models.DecimalField("Saldo Actual", max_digits=12, decimal_places=0, default=0, null=False)
    es_privada = models.BooleanField("Cuenta Privada", default=True, null=False)
    habilitado = models.BooleanField(str_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Cuentas financieras o billeteras asociadas a un usuario para el control de saldos y movimientos."

    def __str__(self):
        return f"{self.nombre} - {self.usuario.nombre}"


class Presupuesto(models.Model):
    nombre = models.CharField(str_nombre, max_length=80, null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    monto_limite = models.DecimalField("Monto Límite", max_digits=12, decimal_places=0, null=False)
    monto_ejecutado = models.DecimalField("Monto Ejecutado", max_digits=12, decimal_places=0, default=0, null=False)
    fecha_inicio = models.DateField("Fecha Inicio", null=False)
    fecha_fin = models.DateField("Fecha Fin", null=False)
    estado = models.CharField("Estado Presupuesto", max_length=20, default="ACTIVO", null=False)
    habilitado = models.BooleanField(str_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Planificación de presupuestos por usuario y categoría con seguimiento de monto ejecutado."

    def __str__(self):
        return f"{self.nombre} - Límite: ${self.monto_limite}"


class Transaccion(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    tipo_movimiento = models.CharField("Tipo de Movimiento", max_length=20, default="GASTO", null=False)
    monto = models.DecimalField("Monto Transacción", max_digits=12, decimal_places=0, null=False)
    fecha = models.DateField("Fecha Transacción", null=False)
    descripcion = models.CharField(str_descripcion, max_length=200, null=True)
    estado = models.CharField("Estado Transacción", max_length=20, default="COMPLETADA", null=False)
    es_excepcional = models.BooleanField("Situación Excepcional", default=False, null=False)
    habilitado = models.BooleanField(str_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Registro histórico de transacciones financieras que afectan el estado de las cuentas."

    def __str__(self):
        return f"{self.tipo_movimiento}: ${self.monto} ({self.estado})"


class HistorialAuditoria(models.Model):
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE, null=False)
    usuario_responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    estado_anterior = models.CharField("Estado Anterior", max_length=20, null=True)
    estado_nuevo = models.CharField("Estado Nuevo", max_length=20, null=False)
    motivo = models.CharField("Motivo del Cambio", max_length=255, null=True)
    fecha_cambio = models.DateTimeField("Fecha de Auditoría", auto_now_add=True)
    habilitado = models.BooleanField(str_habilitado, default=True, null=False)

    class Meta:
        db_table_comment = "Registro de auditoría y trazabilidad ante cambios de estado en las transacciones."

    def __str__(self):
        return f"Auditoría TX #{self.transaccion.id}: {self.estado_anterior} -> {self.estado_nuevo}"


class IndicadorGestion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    periodo = models.CharField("Período (AAAA-MM)", max_length=15, null=False)
    total_ingresos = models.DecimalField("Total Ingresos", max_digits=12, decimal_places=0, default=0, null=False)
    total_gastos = models.DecimalField("Total Gastos", max_digits=12, decimal_places=0, default=0, null=False)
    porcentaje_uso_presupuesto = models.DecimalField("Uso de Presupuesto (%)", max_digits=5, decimal_places=2, default=0, null=False)
    tendencia = models.CharField("Tendencia de Comportamiento", max_length=30, default="ESTABLE", null=False)
    habilitado = models.BooleanField(str_habilitado, default=True, null=False)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)

    class Meta:
        db_table_comment = "Indicadores de gestión para analizar tendencias, utilización de recursos y comportamiento."

    def __str__(self):
        return f"Indicador {self.periodo} - {self.usuario.nombre}"
