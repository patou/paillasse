-- phpMyAdmin SQL Dump
-- version OVH
-- https://www.phpmyadmin.net/
--
-- Hôte : mysql51-86.perso
-- Généré le :  Dim 07 mars 2021 à 13:19
-- Version du serveur :  5.6.50-log
-- Version de PHP :  7.0.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `orguepay`
--

-- --------------------------------------------------------

--
-- Structure de la table `inventaire_mecanique`
--

CREATE TABLE `inventaire_mecanique` (
  `id` int(11) NOT NULL,
  `traction_notes` varchar(50) DEFAULT NULL,
  `traction_jeux` varchar(50) DEFAULT NULL,
  `console` varchar(100) DEFAULT NULL,
  `sommiers_type` varchar(100) DEFAULT NULL,
  `sommiers_spec` varchar(255) DEFAULT NULL,
  `soufflerie_type` varchar(100) DEFAULT NULL,
  `soufflerie_spec` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `inventaire_mecanique`
--

INSERT INTO `inventaire_mecanique` (`id`, `traction_notes`, `traction_jeux`, `console`, `sommiers_type`, `sommiers_spec`, `soufflerie_type`, `soufflerie_spec`) VALUES
(1, 'Électropneumatique', 'Électropneumatique', 'Intégrée au soubassement', '', '', 'À plis parallèles', ''),
(2, '', '', '', '', '', '', NULL),
(3, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Cunéiforme', NULL),
(4, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', 'sommier diatonique', 'À plis parallèles', NULL),
(5, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', '', 'À plis parallèles', ''),
(6, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', '', 'À plis parallèles', NULL),
(7, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(8, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(9, 'Électropneumatique', 'Électropneumatique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(10, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(11, 'Électropneumatique', 'Électropneumatique', 'Retournée', 'À membranes', NULL, 'À plis parallèles', NULL),
(12, 'Électropneumatique', 'Mécanique', 'Indépendante vers l\\\'orgue', 'À registres', NULL, 'À plis parallèles', NULL),
(13, 'Électropneumatique', 'Électropneumatique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(14, 'Électropneumatique', 'Électropneumatique', 'Mobile', 'À registres', NULL, 'À plis parallèles', NULL),
(15, 'Tubulaire', 'Tubulaire', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(16, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, NULL, NULL),
(17, 'Mécanique', 'Électropneumatique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(18, 'Mécanique', 'Électropneumatique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(19, 'Électropneumatique', 'Tubulaire', 'Indépendante vers l\\\'orgue', 'À registres', NULL, 'À plis parallèles', NULL),
(20, 'Mécanique', 'Électropneumatique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(21, 'Mécanique', 'Électrique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(22, 'Électrique', 'Électrique', 'Intégrée au soubassement', '', NULL, '', NULL),
(23, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(24, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Cunéiforme', NULL),
(25, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', 'à gravures alternées', NULL, NULL),
(26, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Cunéiforme', NULL),
(27, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Cunéiforme', NULL),
(28, 'Électropneumatique', 'Électropneumatique', 'Retournée', 'À registres', '', 'À plis parallèles', NULL),
(29, 'Mécanique', 'Mécanique', 'Indépendante vers l\\\'orgue', 'À registres', '', 'À plis parallèles', NULL),
(30, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(31, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', ''),
(32, 'Électrique', 'Électropneumatique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(33, 'Électropneumatique', 'Électropneumatique', 'Indépendante vers l\\\'orgue', '', NULL, 'À plis parallèles', NULL),
(34, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(35, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Alimentation directe', NULL),
(36, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(37, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(39, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(40, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(41, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Cunéiforme', NULL),
(42, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(43, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(44, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(45, 'Électropneumatique', '', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(46, '', '', '', NULL, NULL, NULL, NULL),
(47, 'Électropneumatique', 'Électropneumatique', 'Indépendante vers l\\\'orgue', 'À membranes', NULL, 'À plis parallèles', NULL),
(48, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(49, 'Mécanique', 'Électrique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(50, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(51, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(52, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(53, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(54, 'Électropneumatique', 'Électropneumatique', 'Indépendante vers l\\\\\\\\\\\\\\\'orgue', 'À registres', NULL, 'À plis parallèles', NULL),
(55, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Alimentation directe', NULL),
(56, '', 'Électropneumatique', 'Indépendante vers l\\\'orgue', NULL, NULL, NULL, NULL),
(57, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(58, 'Mécanique', 'Électropneumatique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(59, 'Mécanique', 'Électropneumatique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(60, 'Électropneumatique', 'Électropneumatique', 'Indépendante vers l\\\'orgue', 'À registres', NULL, 'À plis parallèles', NULL),
(61, 'Électropneumatique', 'Électropneumatique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(62, 'Mécanique', 'Mécanique', 'Latérale, intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(63, 'Mécanique', 'Électrique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(64, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(65, 'Pneumatique Barker', 'Pneumatique Barker', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(66, 'Électropneumatique', 'Électropneumatique', '', 'À registres', NULL, 'À plis parallèles', NULL),
(67, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(68, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Alimentation directe', NULL),
(69, 'Électropneumatique', 'Électropneumatique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(70, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(71, 'Mécanique', 'Mécanique', 'Arrière, intégrée au soubassement', 'À registres', NULL, 'Cunéiforme', NULL),
(72, 'Électropneumatique', 'Pneumatique Barker', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(73, 'Électropneumatique', 'Électropneumatique', 'Indépendante vers l\\\'orgue', 'À registres', NULL, 'À plis parallèles', NULL),
(74, 'Mécanique', 'Mécanique', 'Indépendante vers l\\\'orgue', 'À registres', NULL, 'À plis parallèles', NULL),
(75, 'Mécanique', 'Électropneumatique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(76, 'Électropneumatique', 'Électropneumatique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(77, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(78, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Alimentation directe', NULL),
(79, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(80, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(81, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(82, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Alimentation directe', NULL),
(83, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(84, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(85, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(86, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(87, 'Mécanique', 'Mécanique', NULL, 'À registres', NULL, 'À plis parallèles', NULL),
(88, 'Électrique', 'Électrique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(89, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(90, 'Mécanique', 'Tubulaire', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(91, 'Mécanique', 'Mécanique', 'Latérale, intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(92, 'Mécanique', 'Électrique', 'Intégrée au soubassement', 'À registres', NULL, NULL, NULL),
(93, 'Mécanique', 'Mécanique', 'Arrière, intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(94, 'Électropneumatique', 'Électropneumatique', 'Retournée', 'À membranes', NULL, 'À plis parallèles', NULL),
(95, 'Électropneumatique', 'Électropneumatique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(96, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(97, 'Électropneumatique', 'Électropneumatique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(98, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(99, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(100, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(101, 'Électropneumatique', 'Électropneumatique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(102, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', '', 'À plis parallèles', ' '),
(103, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(104, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, NULL, NULL),
(105, 'Électrique', 'Électrique', '', 'À registres', NULL, 'À plis parallèles', NULL),
(106, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(107, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, '', NULL),
(108, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(109, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(110, 'Mécanique', 'Mécanique', 'Latérale, intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(111, 'Électrique', 'Électrique', 'Indépendante vers l\\\'orgue', 'À registres', NULL, 'À plis parallèles', NULL),
(112, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(113, 'Tubulaire', 'Tubulaire', 'Latérale, intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(114, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(115, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(116, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Alimentation directe', NULL),
(117, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, NULL, NULL),
(118, 'Mécanique', 'Électrique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(119, 'Mécanique', 'Électrique', 'Latérale retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(120, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, '', NULL),
(121, 'Mécanique', 'Mécanique', 'Indépendante vers l\\\'orgue', 'À registres', NULL, 'À plis parallèles', NULL),
(122, 'Tubulaire', 'Tubulaire', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(123, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(124, 'Mécanique', 'Mécanique', 'Latérale, intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(125, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, '', NULL),
(126, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(127, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(128, 'Mécanique', NULL, 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(130, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(131, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(132, NULL, NULL, '', NULL, NULL, NULL, NULL),
(133, 'Électropneumatique', 'Électropneumatique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(134, 'Informatique', 'Informatique', 'Intégrée au soubassement', '', NULL, 'Alimentation directe', NULL),
(135, 'Mécanique', 'Mécanique', '', 'À registres', NULL, 'À plis parallèles', NULL),
(136, 'Mécanique', 'Mécanique', NULL, 'À registres', NULL, 'À plis parallèles', NULL),
(137, 'Mécanique', 'Mécanique', '', 'À registres', NULL, 'À plis parallèles', NULL),
(138, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, 'Cunéiforme', '2 réservoirs'),
(139, 'Mécanique', 'Mécanique', 'Latérale, intégrée au soubassement', 'À registres', '', 'À plis parallèles', ''),
(140, 'Mécanique', 'Mécanique', 'Intégrée au soubassement', 'À registres', NULL, '', 'Pompe à pied conservée'),
(141, 'Électrique', 'Électrique', 'Latérale, intégrée au soubassement', '', NULL, 'À plis parallèles', NULL),
(142, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(143, 'Électrique', 'Électrique', 'Retournée', 'À membranes', '', 'À plis parallèles', ''),
(144, 'Électrique', 'Électropneumatique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(145, 'Mécanique', 'Mécanique', '', NULL, NULL, '', 'Ventilateur électrique'),
(146, 'Mécanique', 'Électrique', 'Intégrée au soubassement', 'À registres', NULL, 'À plis parallèles', NULL),
(147, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(148, 'Mécanique', 'Mécanique', 'Retournée', 'À registres', NULL, 'À plis parallèles', NULL),
(149, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(150, 'Électropneumatique', '', 'Mobile', NULL, NULL, '', NULL),
(151, 'Informatique', 'Informatique', '', '', NULL, '', NULL),
(152, 'Mécanique', 'Mécanique', '', 'À registres', NULL, 'À plis parallèles', NULL);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `inventaire_mecanique`
--
ALTER TABLE `inventaire_mecanique`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `inventaire_mecanique`
--
ALTER TABLE `inventaire_mecanique`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=153;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
