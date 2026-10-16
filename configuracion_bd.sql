-- 1. Crear la base de datos
CREATE DATABASE IF NOT EXISTS finanzas_db
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci;

-- 2. Crear el usuario local y remoto para la aplicación
CREATE USER IF NOT EXISTS 'finanzas_user'@'localhost' IDENTIFIED BY 'Finanzas2026!';
CREATE USER IF NOT EXISTS 'finanzas_user'@'%' IDENTIFIED BY 'Finanzas2026!';

-- 3. Asignar todos los privilegios sobre la base de datos del proyecto al usuario
GRANT ALL PRIVILEGES ON finanzas_db.* TO 'finanzas_user'@'localhost';
GRANT ALL PRIVILEGES ON finanzas_db.* TO 'finanzas_user'@'%';

-- 4. Aplicar cambios de privilegios inmediatamente
FLUSH PRIVILEGES;

-- Seleccionar la base de datos para verificar
USE finanzas_db;
