# Proyecto Django: ProyectoFinalStrazzolini

Este proyecto es una aplicación web desarrollada con Django que permite explorar recomendaciones auténticas sobre destinos, alojamientos y experiencias de viaje. Los usuarios pueden leer experiencias, inspirarse para futuros viajes y compartir contenido dentro de la plataforma.

## Funcionalidades principales

### Página de inicio
- Vista principal de la aplicación.
- Debajo del mensaje de bienvenida se encuentra un buscador de lugares por nombre, que permite acceder a los resultados de la búsqueda.

### About
- Sección “Acerca de mí” con información del autor del proyecto.

### Gestión de Lugares
- Listado de todos los lugares publicados.
- Visualización del detalle de cada lugar.
- Creación, edición y eliminación de lugares (funcionalidades disponibles solo para usuarios autenticados).

### Gestión de Alojamientos
- Listado de los alojamientos disponibles.

### Gestión de Experiencias
- Listado de experiencias publicadas por los usuarios.

### Gestión de Usuarios
- Registro de nuevos usuarios.
- Login y Logout.
- Perfil de usuario con posibilidad de edición.
- Cambio de contraseña.
- Sistema de mensajería para comunicarse con otros usuarios o el administrador.

## Cómo ejecutar el proyecto

1. Clonar el repositorio.
2. Crear y activar un entorno virtual.
3. Instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Ejecutar las migraciones:

    ```bash
    python manage.py migrate
    ```

5. Iniciar el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

6. Acceder desde el navegador a:

    ```
    http://localhost:8000
    ```

## Video de demostración
- Drive: https://drive.google.com/file/d/1yPmf5m6BpH2r8em00NZ139QV7f5Nf8GC/view?usp=sharing
