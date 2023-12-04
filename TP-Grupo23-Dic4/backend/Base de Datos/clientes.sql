-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-12-2023 a las 12:05:11
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `clientes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mensajes`
--

CREATE TABLE `mensajes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `email` varchar(60) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `excursion` tinyint(5) NOT NULL,
  `fecha_viaje` date NOT NULL,
  `cant_personas` tinyint(20) NOT NULL,
  `comentario_cliente` varchar(500) NOT NULL,
  `fecha_envio` datetime NOT NULL,
  `leido` tinyint(1) NOT NULL DEFAULT 0,
  `gestion` varchar(500) DEFAULT NULL,
  `fecha_gestion` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mensajes`
--

INSERT INTO `mensajes` (`id`, `nombre`, `email`, `telefono`, `excursion`, `fecha_viaje`, `cant_personas`, `comentario_cliente`, `fecha_envio`, `leido`, `gestion`, `fecha_gestion`) VALUES
(1, 'Martin Lopez', 'mlopez@hotmail.com', '5432167890', 2, '2023-12-14', 3, 'Comentario de prueba del primer cliente que se creó', '2023-11-20 00:00:00', 1, 'Se confirmo la reserva del cliente', '2023-11-21 15:32:00'),
(2, 'Noelia Ramirez', 'noeramirez@hotmail.com', '1234567890', 1, '2024-02-25', 2, 'Comentario de prueba del segundo cliente que se creó', '2023-11-21 00:00:00', 1, 'Respondiendo a Noelia a traves de Python', '2023-12-01 19:40:44'),
(3, 'Matias Seminara', 'matias@gmail.com', '123456789', 1, '2024-01-26', 2, 'Esto es un mensaje de prueba que graba en la base de datos', '2023-11-29 08:03:49', 1, 'Respondiendo por primera vez usando UPDATE desde python', '2023-12-01 19:27:53'),
(4, 'Matias Seminara2', 'matias@gmail.com', '123456789', 1, '2024-01-26', 2, 'Esto es un mensaje de prueba que graba en la base de datos', '2023-12-01 12:05:16', 0, NULL, NULL),
(6, 'Matias Seminara5', 'matias@gmail.com', '123456789', 1, '2024-01-26', 2, 'Esto es un mensaje de prueba que graba en la base de datos', '2023-12-01 12:43:31', 1, 'Hemos contactado al cliente y cambio su reserva', '2023-12-01 22:11:22'),
(7, 'Ramiro Perotti', 'ramiro@gmail.com', '1243658792', 2, '2024-09-16', 7, 'Estoy buscando alojamiento para 7 personas', '2023-12-01 19:26:41', 1, 'El cliente se contacto con nosotros y lo pudo resolver.', '2023-12-03 18:10:13'),
(9, 'Juan Garcia', 'juan@gmail.com', '1124784575', 1, '2025-05-29', 5, 'Mensaje de prueba enviado desde Postman', '2023-12-03 18:51:25', 1, 'La gestion fue generada desde Postman', '2023-12-03 20:16:16'),
(10, 'Sebastian Martinez', 'sebastian@gmail.com', '1192447212', 1, '2024-01-18', 3, 'Comentario de prueba desde el formulario en HTML', '2023-12-03 20:52:42', 1, 'Modificando gestión desde admin.html', '2023-12-04 01:02:50'),
(12, 'Nahuel Smith', 'nahuel@gmail.com', '1122212212', 2, '2024-10-21', 2, 'Nueva prueba desde reservas.html', '2023-12-04 01:11:23', 1, 'Probando modificar desde admin.html', '2023-12-04 01:34:07');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `mensajes`
--
ALTER TABLE `mensajes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `mensajes`
--
ALTER TABLE `mensajes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
