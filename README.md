# 🔗 Redis Link Shortener Backend

Backend de Redis Link Shortener (acortador de URLs). Proyecto construido con **Flask** y **Redis** para el almacenamiento de datos.

<p align='center'>
  <img src='https://github.com/Gdr18/Url_Shortener_Frontend/assets/118227919/f1ec58ae-b08e-4c36-9b48-e1f791c979a4' alt='redis_link_shortener_gif' width='50%'></img>
</p>
<p  align='center'>
  <a href="https://redis-link-shortener-backend.fly.dev">Deploy (Fly.io)</a>
</p><br>

---

## 🚀 Tecnologías

- Python 3.11+
- Flask
- Redis
- Flask-CORS (CORS para permitir peticiones desde el frontend)
- python-dotenv

---

## ✨ Funcionalidades

- Acortamiento de URLs largas a URLs cortas personalizadas
- Almacenamiento eficiente de URLs en Redis
- Redirección automática desde URLs cortas a URLs originales
- Listado de todas las URLs acortadas
- API REST para integración con frontend

---

## ⚙️ Instalación local

1. Clona este repositorio:
```bash
git clone https://github.com/Gdr18/redis-link-shortener-backend.git 
cd redis-link-shortener-backend
```
2. Crea y activa un entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate
```
3. Instala las dependencias:
```bash
pip install -r requirements.txt
```
4. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno si quieres personalizar la configuración:
```bash
DB_HOST = localhost # [OPCIONAL] O el host de tu servidor Redis
DB_PORT = 6379 # [OPCIONAL] O el puerto de tu servidor Redis.
DB_PASSWORD = tu_contraseña_de_redis # [OPCIONAL] En el caso de que tengas una base de datos de redis desplegada.
DB_USERNAME = tu_nombre_de_usuario_de_redis # [OPCIONAL] En el caso de que tengas una base de datos de redis desplegada.
FRONTEND_PROD = tu_url_de_producción # [OPCIONAL] En el caso de que el frontend lo tengas desplegado en la nube.
FRONTEND_MODE_DEV = tu_url_modo_desarrollo # [OPCIONAL] En el caso de que utilices frontend en entorno local.
FRONTEND_MODE_PROD = tu_url_modo_producción # [OPCIONAL] En el caso de que utilices frontend en entorno local.
PORT = 3000 # [OPCIONAL] O el puerto flask que desees.
```
5. Asegúrate de tener Redis ejecutándose en tu sistema local o desplegado en la nube.

6. Ejecuta la aplicación:
```bash
python app.py
```

⚠️ La app funcionará sin este archivo si lo utilizas en un entorno local y con los valores por defecto del servidor de Redis.

---

## 📓 Prueba la API

Puedes probar todos los endpoints desde la colección de Postman:

🔗 [Colección de Postman Local](https://www.postman.com/maintenance-participant-28116252/workspace/gdor-comparte/collection/26739293-12e6659d-c495-4dfa-86d0-eda808b8d03c?action=share&creator=26739293)
___

👩‍💻 Autor
Gádor García Martínez
GitHub: https://github.com/Gdr18
LinkedIn: https://www.linkedin.com/in/g%C3%A1dor-garc%C3%ADa-mart%C3%ADnez-99a33717b/
