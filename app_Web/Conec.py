import psycopg2
from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()

# Leer variables correctamente
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DB_NAME")

# Verificar lectura de variables
print("🔍 HOST:", HOST)

# Conectar a la base de datos
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("✅ Conexión exitosa")

    cursor = connection.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("🕒 Hora actual:", result)

    cursor.close()
    connection.close()
    print("🔒 Conexión cerrada")

except Exception as e:
    print(f"❌ Error al conectar: {e}")
