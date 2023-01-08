CREATE DATABASE IF NOT EXISTS proyectoNotas_python;
USE proyectoNotas_python;
-- Recordar que para esta pequeña implementacion con python y mysql estamos utilizando phpMyadmin.
-- El proyecto va a constar de dos tablas 1 de los usuario y 1 de las notas vinculada a cada usuario.
CREATE TABLE usuarios(
    id          int(25) auto_increment NOT NULL,
    nombre      varchar(100) NULL,
    apaellidos  varchar(255) NULL,
    mail        varchar(255) NOT NULL,
    password    varchar(255) NOT NULL,
    fecha       date NOT NULL,
    CONSTRAINT usuarios_pk PRIMARY KEY (id),
    CONSTRAINT email_uk UNIQUE (email)
)ENGINE=InnoDB; -- Esto significa que va a mantener la integridad referencial y todo tipo de relaciones entre tablas.

CREATE TABLE notas(
    id          int(25) auto_increment NOT NULL,
    usuario_id  int(25) NOT NULL,
    titulo      varchar(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    fecha       date NOT NULL,
    CONSTRAINT notas_pk PRIMARY KEY (id),
    CONSTRAINT notas_usuarios_fk FOREIGN KEY(usuario_id) REFERENCES usuarios(id) 
)ENGINE=InnoDB;