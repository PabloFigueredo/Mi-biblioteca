-- Insertar autores conocidos en la tabla libros_autor
INSERT INTO libros_autor (nombre, nacionalidad)
VALUES 
('Gabriel García Márquez', 'Colombia'),
('Miguel de Cervantes', 'España'),
('J.K. Rowling', 'Reino Unido'),
('J.R.R. Tolkien', 'Reino Unido'),
('George Orwell', 'Reino Unido'),
('Jane Austen', 'Reino Unido'),
('Mark Twain', 'Estados Unidos'),
('Ernest Hemingway', 'Estados Unidos'),
('Isabel Allende', 'Chile'),
('Mario Vargas Llosa', 'Perú');

-- Insertar 100 libros famosos en la tabla libros_libro
INSERT INTO libros_libro (nombre, fecha_lanzamiento, genero_id, calificacion_id, autor_id)
VALUES 
-- Libros de Gabriel García Márquez
('Cien Años de Soledad', '1967-05-30', 'Realismo Mágico', 2, 1),
('El Amor en los Tiempos del Cólera', '1985-09-05', 'Romance', 1, 1),
('Crónica de una Muerte Anunciada', '1981-03-15', 'Drama', 2, 1),
('El Otoño del Patriarca', '1975-01-01', 'Ficción', 3, 1),
('Relato de un Náufrago', '1970-01-01', 'Aventura', 2, 1),

-- Libros de Miguel de Cervantes
('Don Quijote de la Mancha', '1605-01-16', 'Novela', 1, 2),
('La Galatea', '1585-01-01', 'Poesía', 3, 2),
('Novelas Ejemplares', '1613-01-01', 'Cuentos', 2, 2),
('Los Trabajos de Persiles y Sigismunda', '1617-01-01', 'Novela', 4, 2),
('El Coloquio de los Perros', '1613-01-01', 'Ficción', 2, 2),

-- Libros de J.K. Rowling
('Harry Potter y la Piedra Filosofal', '1997-06-26', 'Fantasía', 1, 3),
('Harry Potter y la Cámara Secreta', '1998-07-02', 'Fantasía', 1, 3),
('Harry Potter y el Prisionero de Azkaban', '1999-07-08', 'Fantasía', 1, 3),
('Harry Potter y el Cáliz de Fuego', '2000-07-08', 'Fantasía', 1, 3),
('Harry Potter y la Orden del Fénix', '2003-06-21', 'Fantasía', 1, 3),

-- Libros de J.R.R. Tolkien
('El Señor de los Anillos: La Comunidad del Anillo', '1954-07-29', 'Fantasía', 1, 4),
('El Señor de los Anillos: Las Dos Torres', '1954-11-11', 'Fantasía', 1, 4),
('El Señor de los Anillos: El Retorno del Rey', '1955-10-20', 'Fantasía', 1, 4),
('El Hobbit', '1937-09-21', 'Fantasía', 1, 4),
('El Silmarillion', '1977-09-15', 'Fantasía', 2, 4),

-- Libros de George Orwell
('1984', '1949-06-08', 'Distopía', 1, 5),
('Rebelión en la Granja', '1945-08-17', 'Fábula', 1, 5),
('Homenaje a Cataluña', '1938-01-01', 'Histórico', 2, 5),
('El Camino a Wigan Pier', '1937-01-01', 'Ensayo', 3, 5),
('Sin Blanca en París y Londres', '1933-01-01', 'Autobiografía', 2, 5),

-- Libros de Jane Austen
('Orgullo y Prejuicio', '1813-01-28', 'Romance', 1, 6),
('Sentido y Sensibilidad', '1811-01-01', 'Romance', 2, 6),
('Emma', '1815-01-01', 'Romance', 2, 6),
('Mansfield Park', '1814-01-01', 'Romance', 3, 6),
('Persuasión', '1817-01-01', 'Romance', 2, 6),

-- Libros de Mark Twain
('Las Aventuras de Tom Sawyer', '1876-06-01', 'Aventura', 1, 7),
('Las Aventuras de Huckleberry Finn', '1884-12-10', 'Aventura', 1, 7),
('El Príncipe y el Mendigo', '1881-01-01', 'Ficción', 2, 7),
('Un Yankee en la Corte del Rey Arturo', '1889-01-01', 'Fantasía', 3, 7),
('Vida en el Mississippi', '1883-01-01', 'Autobiografía', 2, 7),

-- Libros de Ernest Hemingway
('El Viejo y el Mar', '1952-09-01', 'Drama', 1, 8),
('Por Quién Doblan las Campanas', '1940-01-01', 'Drama', 2, 8),
('Adiós a las Armas', '1929-01-01', 'Drama', 2, 8),
('Fiesta', '1926-01-01', 'Drama', 3, 8),
('Las Nieves del Kilimanjaro', '1936-01-01', 'Cuentos', 2, 8),

-- Libros de Isabel Allende
('La Casa de los Espíritus', '1982-01-01', 'Drama', 1, 9),
('De Amor y de Sombra', '1984-01-01', 'Romance', 2, 9),
('Eva Luna', '1987-01-01', 'Ficción', 2, 9),
('Cuentos de Eva Luna', '1989-01-01', 'Cuentos', 3, 9),
('Paula', '1994-01-01', 'Autobiografía', 2, 9),

-- Libros de Mario Vargas Llosa
('La Ciudad y los Perros', '1963-01-01', 'Drama', 1, 10),
('La Casa Verde', '1966-01-01', 'Ficción', 2, 10),
('Conversación en la Catedral', '1969-01-01', 'Drama', 2, 10),
('Pantaleón y las Visitadoras', '1973-01-01', 'Comedia', 3, 10),
('La Fiesta del Chivo', '2000-01-01', 'Histórico', 1, 10);