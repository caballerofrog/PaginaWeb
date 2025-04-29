import psycopg2


try:
    conexion = psycopg2.connect(
        host = "db.cjyzztlyyvlgbkfaifvc.supabase.co",
        user = "postgres",
        password = "-SrM@gus123-",
        database = "postgres",
        port = "5432"
    )
    print("✅ Conexion exitosa...")
except Exception as ex:
    print("Error: ", ex)