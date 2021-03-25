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
-- Structure de la table `inventaire_contributeurs`
--

CREATE TABLE `inventaire_contributeurs` (
  `id` int(11) NOT NULL,
  `contributeur_random` varchar(16) DEFAULT NULL,
  `contributeur_nom` varchar(255) DEFAULT NULL,
  `contributeur_mail` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `inventaire_contributeurs`
--

INSERT INTO `inventaire_contributeurs` (`id`, `contributeur_random`, `contributeur_nom`, `contributeur_mail`) VALUES
(1, 'Nd0I5t2u1gXoDj4s', 'Leroux Valentin', 'valentinleroux@9online.fr'),
(15, 'Tn9Ls6AKGyOMi42R', 'Henri-Franck Beaupérin', 'henri-franck.beauperin@wanadoo.fr'),
(14, 'Bmnyd8Ce6KZ2L2eI', 'CHAPLAIS Olivier', 'adriaque@me.com'),
(13, 'dPHpE6mp2p5gZKdJ', 'Marionneau Guillaume', 'guillaumemarionneau@orange.fr'),
(12, 'g6Oei73tl1ibLl6d', 'Humeau Philippe', 'p.humeau@gmail.com'),
(11, NULL, 'Valentin Le Héros', 'valentin@lavoixdesorgues.org'),
(16, 'wJkqBYDLFrW3MAKY', 'ROCHEDREUX Martine', 'martine.rochedreux@laposte.net'),
(17, '2LZjJlpx6Xv3YRs7', 'O', 'etienneouvrard@yahoo.fr'),
(18, 'm6HuX6jkwGU4spn3', 'Dumez Jean', 'lesamisdesorguesdeladoutre@gmail.com'),
(19, 'Zw4eMFs9nakWGiPX', 'Delaunay Samuel', 'delaunay.samuel@free.fr'),
(20, 'Q6DkeAIogsA4lAzp', 'GEORGE Sylviane', 's.georgeco@sfr.fr'),
(21, 'kUKbNcJVfHdCWplx', 'Rossignol Marc', 'marc-rossignol@orange.fr'),
(22, 'c7VF8UJUZRdtYPLi', '', ''),
(23, 'YOklYGdz99fM1w1N', 'Gwilherm POULLENNEC', 'gwilherm.poullennec@gmail.com'),
(24, '8SN4HUx9z71Zfjpf', 'Inglebert Marc', 'marc.inglebert@laposte.net'),
(25, 'xC2twFyZg7PfbKjg', 'BELAUD Valentin', 'valentin.belaud@orange.fr'),
(26, 'qEAtsbGdWsAdcXVs', 'Alain FRANCOIS', 'alafran@free.fr'),
(27, '8EE6DONbiunDZtkL', 'EPIE Denis', 'denis.epie@free.fr'),
(28, NULL, '', 'hodsqfhufdqhofuihfuioqh@tot'),
(29, NULL, 'Dabreteau Jacques', 'dabreteau.jacques@numericable.fr'),
(30, 'MXcqEpmH0RcBEvxv', 'gloton georges', 'anneouvrard@orange.fr'),
(31, 'tGNhO3opw4FIZ8jG', 'Iratçabal Michel', 'michel.iratcabal@hotmail.fr'),
(32, 'HwufelWbakFQt5HP', 'MAISONNEUVE JEAN-FRANCOIS', 'j-f.maisonneuve@orange.fr'),
(33, NULL, 'LESELLIER Jean -Noël', 'jean-noel.lesellier@wanadoo.fr'),
(34, 'xrqxzZxoyyGkswQk', 'Rousseau Yves', 'orgueetmusiqueavouvant@orange.fr');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `inventaire_contributeurs`
--
ALTER TABLE `inventaire_contributeurs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `inventaire_contributeurs`
--
ALTER TABLE `inventaire_contributeurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
