from sqlalchemy import create_engine, text

DB_URL = "postgresql+psycopg2://user_python:123456@localhost:5432/db_weather"

# Creamos el engine con client_encoding UTF-8
engine = create_engine(
    DB_URL,
    connect_args={"client_encoding": "utf8"}  # forzamos UTF-8 para la comunicación
)

try:
    with engine.connect() as conn:
        # Ejecutamos un SELECT simple
        result = conn.execute(text("SELECT * FROM weather"))

        # Iteramos sobre las filas
        for row in result:
            # Convertimos cada campo a str de forma segura
            safe_row = [str(col) if col is not None else None for col in row]
            print(safe_row)

    print("Conexión y SELECT ejecutados correctamente.")

except Exception as e:
    # Usamos repr para ver cualquier carácter raro sin romper
    print("Error de conexión o ejecución:", repr(e))