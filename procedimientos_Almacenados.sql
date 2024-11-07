CREATE PROCEDURE InsertarPrestamo
    @CodigoUsuario INT,
    @CodigoEjemplar INT,
    @FechaPrestamo DATETIME,
    @FechaDevolucion DATE
AS
BEGIN
    INSERT INTO BIBLIOTECA.USUARIO_EJEMPLAR (CODIGO_USUARIO, CODIGO_EJEMPLAR, FECHA_PRESTAMO, FECHA_DEVOLUCION)
    VALUES (@CodigoUsuario, @CodigoEjemplar, @FechaPrestamo, @FechaDevolucion);

    PRINT 'Préstamo registrado exitosamente';
END;
GO

CREATE PROCEDURE ConsultarLibros
    @CodigoLibro INT = NULL,
    @Titulo VARCHAR(50) = NULL,
    @ISBN VARCHAR(15) = NULL,
    @Paginas INT = NULL,
    @Editorial VARCHAR(25) = NULL
AS
BEGIN
    SELECT * 
    FROM BIBLIOTECA.LIBRO
    WHERE 
        (@CodigoLibro IS NULL OR CODIGO_LIBRO = @CodigoLibro) AND
        (@Titulo IS NULL OR TITULO LIKE '%' + @Titulo + '%') AND
        (@ISBN IS NULL OR ISBN = @ISBN) AND
        (@Paginas IS NULL OR PAGINAS = @Paginas) AND
        (@Editorial IS NULL OR EDITORIAL LIKE '%' + @Editorial + '%');
END;
GO

CREATE PROCEDURE ActualizarAutor
    @Codigo INT,
    @Nombre VARCHAR(30)
AS
BEGIN
    UPDATE BIBLIOTECA.AUTOR
    SET NOMBRE = @Nombre
    WHERE CODIGO = @Codigo;

    PRINT 'Autor actualizado exitosamente';
END;
GO


CREATE PROCEDURE EliminarEstudiante
    @CodigoUsuario INT
AS
BEGIN
    DELETE FROM BIBLIOTECA.USUARIO
    WHERE CODIGO_USUARIO = @CodigoUsuario;

    PRINT 'Estudiante eliminado exitosamente';
END;
GO
