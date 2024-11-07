#para ejecutar las pruebas se debe realizar quitar los # de los main y las llamadas
import pyodbc
from datetime import datetime

def connect_to_sql_server():
    server = 'localhost' #Instancia de la base de datos
    database = 'TEST'
    username = 'pythonUser'
    password = '12345678'

    #Connection string for SQL Server
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        #Establish Connection
        connection = pyodbc.connect(conn_str)
        print("Connection established successfully")
        return connection
    except pyodbc.Error as e:
        print("Connection Failed")
        return None

connect_to_sql_server()


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
#if __name__ == '__main__':
 #   codigo_usuario = 10003
  #  codigo_ejemplar = 101
   # fecha_prestamo = datetime.now()  # Fecha actual
    #fecha_devolucion = datetime(2024, 11, 15)  # Fecha de devolución

   # insertar_prestamo(codigo_usuario, codigo_ejemplar, fecha_prestamo, fecha_devolucion)



def consultar_libros(codigo_libro=None, titulo=None, isbn=None, paginas=None, editorial=None):
    conn = connect_to_sql_server()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                EXEC ConsultarLibros @CodigoLibro = ?, @Titulo = ?, @ISBN = ?, @Paginas = ?, @Editorial = ?
            """, (codigo_libro, titulo, isbn, paginas, editorial)) 
            
            # Obtener y mostrar los resultados
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            print("Error en la consulta:", e)
        finally:
            cursor.close()
            conn.close()

# Ejemplo de uso
#if __name__ == '__main__':
    # Consultar por título
   # consultar_libros(titulo='EL Quijote')

    # Consultar por ISBN
  #  consultar_libros(isbn='4781234567890')

    # Consultar por editorial
   # consultar_libros(editorial='Editorial Anaya')

    # Consultar por cantidad de páginas
  #  consultar_libros(paginas=863)



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

# Ejemplo de uso
#if __name__ == '__main__':
    # Actualizar el nombre del autor con código 1
   #actualizar_autor(codigo=1, nombre='Gabriel García Márquez')


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

# Ejemplo de uso
#if __name__ == '__main__':
    # Eliminar el estudiante con código 1
    #eliminar_estudiante(codigo_usuario=2)