# TiendaOnline

TiendaOnline es una aplicación web desarrollada con Django para la gestión de una tienda online. Permite administrar productos, categorías, usuarios y un carrito de compras, ofreciendo una experiencia simple y funcional para la venta de productos.

---

## Esquema de Base de Datos

![Esquema Base de Datos](imagen_db.png)

---

## Requisitos previos

- Python 3.x instalado  
- Docker y Docker Compose instalados

---

## Inicialización del proyecto

1. **Cloná el repositorio**

```bash
git clone https://github.comLautaroMabrass/Sistema-Django
```

2. **Configura el entorno virtual**

```bash
python3 -m venv venv
source venv/bin/activate   
# En Windows: venv\Scripts\activate
```

3. **Instala dependencias**

```bash
pip install -r requirements.txt
```

4. **Levantar el contenedor Docker**

```bash
docker-compose up -d
```

5. **Ejecuta migraciones**

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

6. **Ejecuta el servidor local**

```bash
python3 manage.py runserver
```
Se ejecutara en el puerto 8000: http://127.0.0.1:8000/