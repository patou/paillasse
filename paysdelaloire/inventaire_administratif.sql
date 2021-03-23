-- phpMyAdmin SQL Dump
-- version OVH
-- https://www.phpmyadmin.net/
--
-- Hôte : mysql51-86.perso
-- Généré le :  Dim 07 mars 2021 à 13:15
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
-- Structure de la table `inventaire_administratif`
--

CREATE TABLE `inventaire_administratif` (
  `id` int(11) NOT NULL,
  `proprietaire` varchar(100) DEFAULT NULL,
  `affectataire` varchar(100) DEFAULT NULL,
  `titulaire` varchar(100) DEFAULT NULL,
  `entretien` varchar(100) DEFAULT NULL,
  `etat` varchar(50) DEFAULT NULL,
  `mh_1` varchar(100) DEFAULT NULL,
  `mh_2` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `inventaire_administratif`
--

INSERT INTO `inventaire_administratif` (`id`, `proprietaire`, `affectataire`, `titulaire`, `entretien`, `etat`, `mh_1`, `mh_2`) VALUES
(1, 'Ville', 'Paroisse', 'Christophe Gauche', 'Robert Frères', 'Bon', 'Non', ''),
(2, NULL, NULL, 'Mickaël Durand, Michel Bourcier, Marie-Thérèse Jehan', NULL, 'Bon', NULL, ''),
(3, 'Ville', 'Paroisse', NULL, NULL, NULL, 'Classé', 'Buffet'),
(4, 'Ville de Nantes', 'Paroisse', 'Denis Cotinat', 'MBGO', 'Bon', 'Non', NULL),
(5, 'État', 'Paroisse', 'Guillaume Marionneau', 'MBGO', 'Bon', 'Classé', 'Orgue entier'),
(6, 'État', 'Recteur de la cathédrale', 'Guillaume Marionneau', 'Nicolas Toussaint', 'Excellent', 'Classé', 'Orgue entier'),
(7, 'Ville', 'Paroisse', 'Olivier Brisson, Philippe Humeau, Marie Rocheteau', 'Denis Londe', 'Excellent', 'Non', ''),
(16, 'Etat', NULL, 'Clément Couturier', 'Jean-Pierre Conan', 'Excellent', 'Classé', 'Orgue entier'),
(8, 'Ville', 'Paroisse', 'Frédéric Labarre, Emmanuel Bonnet', 'MBGO', 'Excellent', 'Classé', 'Orgue entier'),
(9, 'Etat', 'Paroisse', 'Thomas Pellerin, Régis Prud\\\'Homme', 'DLFO', 'Bon', 'Classé', 'Buffet'),
(10, 'Ville', 'Paroisse', 'Henri-Franck Beaupérin (conservateur municipal)', 'Jean-Pierre Conan', 'Bon', 'Classé', 'Orgue entier'),
(11, 'Ville', 'Paroisse', 'Martine Rochedreux, Maurice N\\\'Gom', 'DLFO', 'Excellent', 'Non', ''),
(12, 'Etat', 'Paroisse', NULL, NULL, 'Moyen', 'Non', ''),
(13, 'Etat', 'Paroisse', 'Michel Bourcier, Mickaël Durand, Marie-Thérèse Jehan', 'MBGO', 'Injouable', 'Non', NULL),
(14, 'Etat', 'Paroisse', 'Michel Bourcier, Mickaël Durand, Marie-Thérèse Jehan', 'MBGO', 'Excellent', 'Classé', 'Partie instrumentale'),
(15, 'Paroisse', 'Paroisse', 'Etienne Ouvrard', 'MBGO', 'Excellent', 'Non', ''),
(17, 'Ville', 'Paroisse', NULL, '', 'Excellent', 'Classé', 'Buffet'),
(18, 'Etat', 'Paroisse', 'Marie-José Chasseguet', NULL, 'Excellent', 'Classé', 'Orgue entier'),
(19, 'Ville', 'Paroisse', 'Damien Rahier', 'Robert Frères', 'Bon', 'Classé', 'Partie instrumentale'),
(20, 'Ville', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL),
(21, 'Ville', 'Paroisse', NULL, NULL, '', 'Non', NULL),
(22, 'Communauté des Carmes', '', NULL, NULL, 'Bon', 'Non', ''),
(23, 'Paroisse', 'Paroisse', 'Amand Besnard', 'Philippe Emeriau', 'Bon', 'Non', ''),
(24, 'Congrégation', 'Congrégation', NULL, 'MBGO', 'Excellent', 'Non', NULL),
(25, 'Ville', 'Paroisse', 'Paul Jauffrit', '', 'Excellent', 'Non', ''),
(26, 'Ville', 'Paroisse', '', '', '', 'Non', NULL),
(27, 'Ville', 'Paroisse', NULL, '', 'Excellent', 'Non', NULL),
(28, 'Ville', 'Paroisse', 'Mado Neau', NULL, 'Moyen', 'Non', NULL),
(29, 'Ville', 'Paroisse', 'Christian Bertret', 'Bernard Hurvy', 'Bon', 'Non', ''),
(30, 'Ville', 'Paroisse', 'D. Chauchet', 'J.-P. Conan', 'Excellent', 'Non', ''),
(31, 'Ville', 'Paroisse', 'Jean Dumez', 'Philippe Emeriau', 'Moyen', 'Classé', 'Partie instrumentale'),
(32, 'Ville', 'Paroisse', 'Jean Dumez', 'Philippe Emeriau', 'Mauvais', 'Inscrit', 'Buffet'),
(33, 'Paroisse', 'Paroisse', 'Bruno Laurent', 'Philippe Emeriau', 'Moyen', 'Non', NULL),
(45, '', NULL, 'Alain Guérinel', 'Robert Frères', 'Excellent', 'Non', NULL),
(34, 'Ville', 'Paroisse', 'Irène Pincemaille', 'MBGO', 'Bon', 'Non', NULL),
(35, 'Ville', 'Paroisse', 'Michel Robin', '', 'Excellent', 'Non', NULL),
(36, 'Ville', 'Paroisse', 'Marc Rossignol', 'Jean-Pierre Conan', 'Excellent', 'Non', ''),
(37, '', NULL, NULL, NULL, 'Excellent', 'Non', NULL),
(39, 'Ville', 'Paroisse', '', '', 'Injouable', 'Non', ''),
(40, 'Ville', 'Paroisse', NULL, 'Thierry Lemercier', 'Moyen', 'Classé', 'Partie instrumentale'),
(41, 'Ville', 'Paroisse', 'Paul Craipeau', '', 'Mauvais', 'Non', NULL),
(42, 'Ville', 'Paroisse', NULL, 'MBGO', 'Excellent', 'Non', NULL),
(43, 'Etat', 'Paroisse', 'Emmanuel Hocdé', NULL, 'Bon', 'Non', NULL),
(44, 'AOCN', 'Paroisse', NULL, NULL, 'Moyen', 'Non', NULL),
(112, 'Ville', 'Paroisse', 'Loïc Desauty', NULL, 'Bon', 'Non', NULL),
(47, 'Ville', 'Paroisse', 'Florence Ladmirault', 'Hurvy', 'Bon', 'Non', NULL),
(48, 'Collège', 'Collège', '', 'MBGO', 'Bon', 'Classé', 'Partie instrumentale'),
(49, '', 'Paroisse', '', '', 'Bon', 'Non', ''),
(50, 'Ville', 'Paroisse', NULL, 'MBGO', 'Excellent', 'Non', NULL),
(51, 'Paroisse', 'Paroisse', 'Gérard Lefebvre', 'MBGO', 'Bon', 'Non', NULL),
(52, 'Ville', 'Paroisse', NULL, 'MBGO', 'Excellent', 'Non', NULL),
(53, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(54, 'Diocèse', 'Paroisse', 'Olivier Chaplais', '', 'Mauvais', 'Non', NULL),
(55, 'Ville', 'Paroisse', NULL, 'Delhumeau', 'Excellent', 'Non', ''),
(56, 'Ville des Sables d\\\'Olonne', 'Paroisse', 'Yves Poupeau', NULL, 'Bon', '', NULL),
(59, 'Ville', 'Paroisse', NULL, NULL, 'Mauvais', 'Non', NULL),
(60, 'Ville', 'Paroisse', 'Nicolas Daviaud, Henri Menanteau', 'Robert Frères', 'Bon', 'Non', NULL),
(61, 'Ville', 'Paroisse', 'Bertrand Duchesne', '', 'Moyen', 'Non', NULL),
(62, 'Ville', 'Paroisse', NULL, 'Hurvy', 'Bon', 'Non', NULL),
(63, 'Ville', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL),
(64, 'Ville', 'Paroisse', 'Fernand Briaud', 'Bernard Hurvy', 'Excellent', 'Non', NULL),
(65, 'Ville', 'Paroisse', '', NULL, 'Excellent', 'Classé', 'Partie instrumentale'),
(66, 'Ville', NULL, NULL, NULL, 'Injouable', 'Non', NULL),
(67, 'Ville', 'Paroisse', 'Jean-Marie Boissinot', '', 'Excellent', 'Non', NULL),
(68, 'Paroisse', 'Paroisse', NULL, NULL, 'Moyen', 'Non', NULL),
(69, 'Collège', 'Collège', NULL, NULL, 'Moyen', 'Non', NULL),
(70, 'Ville', 'Paroisse', NULL, NULL, '', 'Classé', 'Orgue entier'),
(71, 'Prieuré', 'Prieuré', 'Frère Claude', 'Thomas', 'Excellent', 'Non', NULL),
(72, 'Institut', 'Institut', NULL, NULL, 'Mauvais', 'Non', NULL),
(73, 'Ville', 'Paroisse', 'Pascal Petit', 'Toussaint', 'Bon', 'Non', NULL),
(74, 'Ville', 'Paroisse', 'Florence Ladmirault', NULL, 'Moyen', 'Non', NULL),
(75, 'Ville', 'Paroisse', 'Bruno Winkel', '', 'Injouable', 'Non', NULL),
(76, 'Ville', 'Paroisse', '', '', 'Injouable', 'Non', NULL),
(77, 'Ville', 'Paroisse', NULL, '', 'Bon', NULL, NULL),
(78, 'VILLE D\\\'OLONNE-SUR-MER', 'PAROISSE DES SABLES D OLONNE', 'aucun', 'DELHUMEAU', 'Excellent', 'Non', ''),
(79, 'Ville', 'Paroise', 'Denis Epié', '', 'Mauvais', 'Non', ''),
(86, 'Ville', 'Paroisse', 'Serge Schoenowsky', 'MBGO', 'Excellent', 'Classé', 'Orgue entier'),
(81, 'Association', 'Paroisse', 'Damien Hérisset', NULL, 'Excellent', 'Non', NULL),
(82, 'Paroisse', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL),
(83, NULL, 'Paroisse', NULL, '', 'Excellent', 'Non', NULL),
(84, 'Ville', 'Paroisse', '', '', 'Bon', 'Non', NULL),
(87, 'Paroisse', 'Paroisse', 'Etienne Ouvrard', 'DLFO', 'Bon', 'Non', ''),
(88, 'Paroisse', 'Paroisse', NULL, NULL, 'Bon', NULL, NULL),
(89, 'Ville', 'Paroisse', '', '', '', 'Non', NULL),
(90, 'Ville', 'Paroisse', NULL, NULL, NULL, 'Non', NULL),
(91, 'Ville', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL),
(92, 'Ville', 'Paroisse', 'Annie Monneraie', 'Cattiaux', 'Excellent', 'Non', ''),
(93, 'Ville', 'Paroisse', NULL, '', 'Excellent', 'Non', NULL),
(94, 'Paroisse', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL),
(95, 'Paroisse', 'Paroisse', '', 'Hurvy', 'Bon', 'Non', NULL),
(96, 'Ville', 'Paroisse', 'Emmanuel Lodé', '', 'Bon', 'Non', NULL),
(97, 'Paroisse', 'Paroisse', '', '', 'Bon', 'Non', NULL),
(98, 'Ville', 'Paroisse', NULL, NULL, 'Moyen', 'Non', NULL),
(99, 'Ville', 'Paroisse', NULL, NULL, 'Moyen', 'Non', NULL),
(100, 'Ville', 'Paroisse', NULL, 'MBGO', 'Bon', 'Non', NULL),
(111, 'Paroisse', 'Paroisse', NULL, NULL, 'Excellent', 'Non', ''),
(102, 'Mairie', 'Paroisse', NULL, 'Jean-Pierre Conan', 'Bon', 'Classé', 'Orgue entier'),
(104, 'Ville', 'Paroisse', '', 'Jean-Pierre Conan', 'Excellent', 'Classé', 'Orgue entier'),
(106, 'Paroisse', 'Paroisse', NULL, NULL, NULL, 'Non', NULL),
(107, 'Commune', NULL, 'Le professeur de la classe d\\\'orgue', NULL, 'Excellent', 'Non', NULL),
(108, 'Ville', 'Paroisse', NULL, NULL, 'Mauvais', 'Non', NULL),
(109, 'Ville', 'Paroisse', NULL, NULL, 'Bon', NULL, NULL),
(110, '', 'Paroisse', NULL, 'MBGO', 'Excellent', 'Non', NULL),
(113, 'Diocèse', 'Paroisse', NULL, NULL, NULL, 'Non', NULL),
(114, 'Ville', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL),
(115, 'Ville', 'Paroisse', NULL, NULL, 'Bon', 'Classé', 'Buffet'),
(116, 'Ville', 'Paroisse', NULL, 'Le Blé', 'Excellent', 'Classé', 'Buffet'),
(117, 'Ville', '', 'Le professeur de la classe d\\\'orgue', 'Fouss', 'Excellent', 'Non', NULL),
(118, 'Ville', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL),
(119, 'Paroisse', 'Paroisse', 'Jean-François Maisonneuve', 'Bernard Hurvy', 'Excellent', 'Non', NULL),
(120, 'privé', NULL, NULL, 'Bernard Hurvy', 'Excellent', 'Non', NULL),
(121, 'Ville', 'Paroisse', NULL, '', 'Excellent', 'Non', NULL),
(122, 'Commune de Sèvremoine', 'Paroisse', 'Etienne Ouvrard', 'MGBO (Nicolas Toussaint)', 'Excellent', 'Non', NULL),
(123, 'Ville', 'Paroisse', NULL, NULL, 'Excellent', 'Non', ''),
(124, 'Ville', 'Paroisse', NULL, 'Robert Frères', 'Bon', 'Non', NULL),
(125, 'Paroisse', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL),
(126, 'Ville', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL),
(127, 'Ville', 'Paroisse', '', 'Conan', 'Excellent', 'Non', NULL),
(128, 'Privé', NULL, NULL, 'MBGO', 'Excellent', 'Non', NULL),
(130, 'Ville', 'Paroisse', NULL, NULL, 'Mauvais', 'Non', NULL),
(131, 'Diocèse', 'Paroisse', NULL, NULL, 'Injouable', NULL, NULL),
(132, 'Ville', '', NULL, NULL, 'Injouable', 'Classé', 'Buffet'),
(133, 'Ville', 'Paroisse', NULL, NULL, NULL, 'Non', NULL),
(134, NULL, NULL, NULL, 'Birouste', 'Excellent', NULL, NULL),
(135, 'Paroisse', 'Paroisse', NULL, NULL, '', 'Non', NULL),
(136, 'Paroisse', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL),
(137, 'Paroisse', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL),
(138, 'Paroisse', 'Paroisse', '', 'Delhumeau', 'Excellent', 'Non', ''),
(139, 'Paroisse', 'Paroisse', 'Marie-Andrée Courjault', 'MBGO', 'Excellent', 'Non', NULL),
(140, 'Ville', 'Paroisse', '', 'Robert Frères', 'Bon', 'Non', NULL),
(141, 'Paroisse', 'Paroisse', '', 'Robert Frères', 'Bon', 'Non', NULL),
(142, 'Ville de Saint-Nazaire', 'Paroisse', 'Marcel Courjault', '', 'Mauvais', 'Non', NULL),
(143, 'Paroisse', 'Paroisse', 'Marcel Courjault', '', 'Moyen', 'Non', NULL),
(144, 'Paroisse', 'Paroisse', 'Marcel Courjault', 'MBGO', 'Bon', 'Non', NULL),
(145, 'Paroisse', 'Paroisse', '', 'MBGO', 'Bon', 'Non', NULL),
(148, 'Ville', 'Paroisse', 'Patrick Branchereau', 'MBGO', 'Excellent', '', NULL),
(146, 'Ville', 'Paroisse', 'Jacques Huteau', NULL, 'Bon', 'Non', NULL),
(147, 'Etat', 'Paroisse', 'Elisabeth Wilson', NULL, 'Bon', 'Non', NULL),
(149, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(150, NULL, NULL, NULL, 'Olivier et Stéphane Robert', 'Bon', 'Non', NULL),
(151, 'Ville', 'Paroisse', NULL, 'Birouste', 'Excellent', 'Non', NULL),
(152, 'Paroisse', 'Paroisse', NULL, NULL, 'Bon', 'Non', NULL);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `inventaire_administratif`
--
ALTER TABLE `inventaire_administratif`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `inventaire_administratif`
--
ALTER TABLE `inventaire_administratif`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=153;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
