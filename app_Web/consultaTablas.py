from conex import get_connection

def listar_tablas():
    connection = get_connection()
    if connection is None:
        print("❌ No se pudo establecer conexión")
        return

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            AND table_type = 'BASE TABLE';
        """)
        tablas = cursor.fetchall()

        print("📦 Tablas en la base de datos:")
        for tabla in tablas:
            print(f"- {tabla[0]}")

        cursor.close()
        connection.close()
        print("🔒 Conexión cerrada")
    except Exception as e:
        print(f"❌ Error al consultar las tablas: {e}")

if __name__ == "__main__":
    listar_tablas()
