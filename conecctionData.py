import pyodbc
from datetime import datetime

def connect_to_sql_server():
    server = 'localhost' # Instancia de la base de datos
    database = 'TEST'
    username = 'pythonUser'
    password = '12345678'

    # Connection string for SQL Server
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        # Establish Connection
        connection = pyodbc.connect(conn_str)
        print("Connection established successfully")
        return connection
    except pyodbc.Error as e:
        print("Connection Failed:", e)
        return None

def insertar_prestamo(codigo_usuario, codigo_ejemplar, fecha_prestamo, fecha_devolucion):
    conn = connect_to_sql_server()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                EXEC InsertarPrestamo @CodigoUsuario = ?, @CodigoEjemplar = ?, @FechaPrestamo = ?, @FechaDevolucion = ?
            """, (codigo_usuario, codigo_ejemplar, fecha_prestamo, fecha_devolucion))
            conn.commit()
            print("Préstamo registrado exitosamente")
        except pyodbc.Error as e:
            print("Error al registrar el préstamo:", e)
        finally:
            cursor.close()
            conn.close()

def consultar_libros(codigo_libro=None, titulo=None, isbn=None, paginas=None, editorial=None):
    conn = connect_to_sql_server()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                EXEC ConsultarLibros @CodigoLibro = ?, @Titulo = ?, @ISBN = ?, @Paginas = ?, @Editorial = ?
            """, (codigo_libro, titulo, isbn, paginas, editorial))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("Error en la consulta:", e)
        finally:
            cursor.close()
            conn.close()

def actualizar_autor(codigo, nombre):
    conn = connect_to_sql_server()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                EXEC ActualizarAutor @Codigo = ?, @Nombre = ?
            """, (codigo, nombre))
            conn.commit()
            print("Autor actualizado exitosamente")
        except pyodbc.Error as e:
            print("Error al actualizar el autor:", e)
        finally:
            cursor.close()
            conn.close()

def eliminar_estudiante(codigo_usuario):
    conn = connect_to_sql_server()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                EXEC EliminarEstudiante @CodigoUsuario = ?
            """, (codigo_usuario,))
            conn.commit()
            print("Estudiante eliminado exitosamente")
        except pyodbc.Error as e:
            print("Error al eliminar el estudiante:", e)
        finally:
            cursor.close()
            conn.close()

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Insertar Préstamo")
        print("2. Consultar Libros")
        print("3. Actualizar Autor")
        print("4. Eliminar Estudiante")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            codigo_usuario = int(input("Código del Usuario: "))
            codigo_ejemplar = int(input("Código del Ejemplar: "))
            fecha_prestamo = datetime.now()  # Fecha actual
            fecha_devolucion = datetime.strptime(input("Fecha de Devolución (YYYY-MM-DD): "), '%Y-%m-%d')
            insertar_prestamo(codigo_usuario, codigo_ejemplar, fecha_prestamo, fecha_devolucion)
        
        elif opcion == '2':
            titulo = input("Título del Libro (dejar vacío si no aplica): ")
            isbn = input("ISBN (dejar vacío si no aplica): ")
            paginas = input("Número de Páginas (dejar vacío si no aplica): ")
            editorial = input("Editorial (dejar vacío si no aplica): ")
            consultar_libros(titulo=titulo or None, isbn=isbn or None, paginas=int(paginas) if paginas else None, editorial=editorial or None)
        
        elif opcion == '3':
            codigo = int(input("Código del Autor: "))
            nombre = input("Nuevo Nombre del Autor: ")
            actualizar_autor(codigo, nombre)
        
        elif opcion == '4':
            codigo_usuario = int(input("Código del Estudiante: "))
            eliminar_estudiante(codigo_usuario)
        
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el menú
if __name__ == '__main__':
    menu()
