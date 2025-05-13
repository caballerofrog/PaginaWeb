from conex import get_connection

def ver_personas():
    connection = get_connection()
    if connection is None:
        print("❌ No se pudo establecer conexión")
        return

    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM "Persona";')
        personas = cursor.fetchall()

        print("👥 Registros en la tabla PERSONA:")
        for persona in personas:
            print(f"- ID: {persona[0]}, Nombre: {persona[1]}")

        cursor.close()
        connection.close()
        print("🔒 Conexión cerrada")
    except Exception as e:
        print(f"❌ Error al consultar la tabla Persona: {e}")

if __name__ == "__main__":
    ver_personas()
