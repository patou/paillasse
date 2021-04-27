-- phpMyAdmin SQL Dump
-- version OVH
-- https://www.phpmyadmin.net/
--
-- Hôte : mysql51-86.perso
-- Généré le :  Dim 07 mars 2021 à 13:20
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
-- Structure de la table `inventaire_sources`
--

CREATE TABLE `inventaire_sources` (
  `id` int(11) NOT NULL,
  `bibliographie` text,
  `discographie` text,
  `web_1_desc` varchar(255) DEFAULT NULL,
  `web_1_url` varchar(255) DEFAULT NULL,
  `web_2_desc` varchar(255) DEFAULT NULL,
  `web_2_url` varchar(255) DEFAULT NULL,
  `web_3_desc` varchar(255) DEFAULT NULL,
  `web_3_url` varchar(255) DEFAULT NULL,
  `web_4_desc` varchar(255) DEFAULT NULL,
  `web_4_url` varchar(255) DEFAULT NULL,
  `web_5_desc` varchar(255) DEFAULT NULL,
  `web_5_url` varchar(255) DEFAULT NULL,
  `renseignements` varchar(100) DEFAULT NULL,
  `date_maj` date DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `inventaire_sources`
--

INSERT INTO `inventaire_sources` (`id`, `bibliographie`, `discographie`, `web_1_desc`, `web_1_url`, `web_2_desc`, `web_2_url`, `web_3_desc`, `web_3_url`, `web_4_desc`, `web_4_url`, `web_5_desc`, `web_5_url`, `renseignements`, `date_maj`) VALUES
(1, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 97-100', NULL, 'Site de l\\\'association La Voix des Orgues', 'http://www.lavoixdesorgues.org', 'Page Facebook de l\\\'association', 'https://www.facebook.com/lavoixdesorgues', 'Chaîne YouTube de l\\\'association', 'http://www.youtube.com/user/lavoixdesorgues', NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'Le Grand Orgue de la Cathédrale de Nantes (du XVe siècle à nos jours) par Félix MOREAU (2005)\n\nPlaquette 81 pages + \\\"tableau comparatif des restaurations successives\\\" (juin 2005)', NULL, 'Association des Amis de l\\\'Orgue de Nantes et de Loire Atlantique', 'http://www.orgue-nantes.com/les-orgues/cathedrale-go/', 'Musique sacrée à la Cathédrale de Nantes', 'http://www.musiquesacree-nantes.cef.fr/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 195-197', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'Louis Delhommeau, Orgues et organistes de la cathédrale de Luçon, Luçon, 1966\nJean-Michel Dieuaide, Le Grand orgue de la cathédrale de Luçon, éditions Ouest-France, Rennes, 2001', 'Félix Moreau, Musique française à l´orgue de Luçon (Raison, Franck), Art et Musique, 1968\nFélix Moreau, César Franck, les trois chorals pour orgue, Art et Musique, 1969\nAndré Isoir, L\'orgue français après la Révolution (Boëly, Lefébure-Wely), Calliope CAL1918, 1974\nAndré Isoir, César Franck, l´oeuvre d´orgue, Calliope CAL1919/CAL1920/cal1921, 1974\nLionel Rogg, Johannes Brahms, intégrale de l´oeuvre pour orgue, Erato EDO259, 1974\nLothar Knappe, Charles-Marie Widor, Symphonie n°2, Musica Viva MV30-1082, 1980\nJean-Claude Mara et Jean Dahais, Mars, Mara SYP 80002, 1981\nJean-Pierre Leguay, Liszt-Mendelssohn, Art et Musique AM8401, 1984\nFrançois Clément, Johannes Brahms, Intégrale de l´oeuvre d´orgue, Art et Musique, AM/CD107/39503, 1995\nNicolas Gorenstein, Les organistes postclassiques parisiens (Benoist, Fessy), Syrius SYR141324', 'Site de l\\\'association Jeux d\\\'orgues à la cathédrale de Luçon', 'http://www.orguelucon.org/', 'Site Patrimoine des Pays de la Loire', 'http://www.patrimoine.paysdelaloire.fr/patrimoine/detail-notices/IM85000346/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(6, 'Louis Delhommeau, Orgues et organistes de la cathédrale de Luçon, Luçon, 1966', '', 'Site de l\\\'association Jeux d\\\'orgues à la cathédrale de Luçon', 'http://www.orguelucon.org/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(7, NULL, 'Hautbois et orgue, par Paul-Ronan Ladmirault et Florence Ladmirault (2005).', 'Site du facteur d\\\'orgues Denis Londe', 'https://orguesdenislonde.wordpress.com/2010/11/17/st-aignan-de-grand-lieu-loire-atlantique/#more-314', 'Site des amis de l\\\'Orgue de Nantes et de Loire Atlantique', 'http://www.orgue-nantes.com/les-orgues/st-aignan/', 'Site de la commune de Saint-Aignan-de-Grand-Lieu', 'http://www.saint-aignan-grandlieu.fr/Decouvrir-la-commune/Notre-patrimoine', NULL, NULL, NULL, NULL, NULL, NULL),
(8, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 199-202', NULL, 'Site du facteur d\\\'orgues', 'http://www.orguent.fr/fr/accueil.php?cat=orrens', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(9, NULL, NULL, 'Chaîne YouTube Henri-Franck Beaupérin', 'https://www.youtube.com/user/ACCJBD/featured', '', '', '', '', NULL, '', NULL, NULL, NULL, NULL),
(10, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(16, 'Dufourq N. (1964). Le grand orgue de la chapelle Saint-Louis du prytanée militaire de La Flèche. Ed. A. et J. Picard & Cie, Paris, 76 p.', 'Vernet O., Ensemble Jacques Moderne (Dir. J.-Y. Hameline). Messe solennelle à l\\\'usage des paroisses, Francois Couperin. Ed. Ligia Digital (2000), Lidi 0104089-00', 'Site de l\\\'association Orgues en Fléchois', 'http://orguesenflechois.com/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(11, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 217-219', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(12, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(13, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 139-174\nDuret D., Russon J.-B. (1954). La cathédrale de Nantes. Ed. Imprimerie de la Bretagne, Nantes, 92 p.', 'Jehan M.-T., Moreau F., avec la participation du choeur grégorien de Nantes (dir. M. Tillie). Oeuvres pour orgue, Félix Moreau. Ed. Solstice, SOCD 209\nJehan M.-T., Moreau F., avec choeur, solistes vocaux et instrumentaux (dir. J. Rehak). Oeuvres vocales et instrumentales, Félix Moreau. Ed. Solstice, SOCD 189\nMoreau F.,Jehan M.-T. Noël aux Grandes Orgues la Cathédrale de Nantes. Ed. Arts et musique, AM/CD 107/38302\nMoreau F. Musiques françaises d\\\'orgue du XVIIème et du XVIIIème siècle. Ed. Forlane, UCD 16716\nJehan M.-T. Intégrale de l\\\'oeuvre pour orgue, Augustin Barié. Ed. Solstice, SOCD 17', 'Association Musique Sacrée à la Cathédrale de Nantes', 'http://www.musiquesacree-nantes.cef.fr/les-orgues/les-instruments-de-la-cathedrale', 'Association Hymnal', 'http://www.hymnal-orgue.org/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(14, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 175-181', 'Jehan M.-T., Moreau F., avec la participation du choeur grégorien de Nantes (dir. M. Tillie). Oeuvres pour orgue, Félix Moreau. Ed. Solstice, SOCD 209\nJehan M.-T., Moreau F., avec choeur, solistes vocaux et instrumentaux (dir. J. Rehak). Oeuvres vocales et instrumentales, Félix Moreau. Ed. Solstice, SOCD 189\nJehan M.-T. Oeuvres choisies, René Vierne. Ed. Lade, L.CD.007', 'Association Musique Sacrée à la Cathédrale de Nantes', 'http://www.musiquesacree-nantes.cef.fr/les-orgues/les-instruments-de-la-cathedrale', 'Association Hymnal', 'http://www.hymnal-orgue.org/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(15, NULL, 'Chiron M., Metz J.-J., Les couleurs de l\\\'orgue romantique. Art et Musique AM/CD 107/39703, 1997\nChiron M., Ouvrard E., Touya A.-L., Le Choeur des Mauges (Dir. K. Blardone), Louis Vierne, oeuvres vocales avec orgue. Art et Musique AM/CD 107/30506, 2005', 'Association des amis de l\\\'orgue de Saint-Macaire-en-Mauges', 'http://www.orguesaintmacaire.org/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(17, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 21-24', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(18, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(19, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 183-188', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(20, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(21, NULL, NULL, 'Site de Dominique Oberthur', 'http://www.orgues-oberthur.org/tech/font.php?lang=eu', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(22, NULL, NULL, 'Page communauté des Carmes - Site du diocèse', 'http://catholique-angers.cef.fr/Les-Carmes-a-Angers', 'Page des Amis des orgues Doutre - Site du diocèse', 'http://catholique-angers.cef.fr/Les-Amis-des-Orgues-de-la-Doutre-Angers', NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(23, NULL, NULL, 'Page Web de l\\\'association sur le site du diocèse', 'http://catholique-angers.cef.fr/Les-Amis-des-Orgues-de-la-Doutre-Angers', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(24, NULL, '', 'http://catholique-angers.cef.fr/Les-Amis-des-Orgues-de-la-Doutre-Angers', 'Page Web de l\\\'association sur le site du diocèse d\\\'Angers', '', '', '', '', NULL, NULL, NULL, NULL, NULL, NULL),
(25, '', NULL, NULL, '', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(26, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(27, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(28, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(29, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 395-397', NULL, 'Association des Amis de l\\\'orgue', 'https://orguestphilbert.wordpress.com', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(30, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(31, NULL, '', 'Page web de l\\\'association sur le site du diocèse d\\\'Angers', 'http://catholique-angers.cef.fr/Les-Amis-des-Orgues-de-la-Doutre-Angers', NULL, '', NULL, NULL, NULL, NULL, NULL, '', NULL, NULL),
(47, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 225-238', NULL, 'Site des Amis de l\\\'Orgue de Nantes', 'http://www.orgue-nantes.com/les-orgues/st-nicolas/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(32, NULL, '', 'Page Web de l\\\'association sur le site du diocèse d\\\'Angers', 'http://catholique-angers.cef.fr/Les-Amis-des-Orgues-de-la-Doutre-Angers', NULL, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(33, NULL, NULL, 'Page Web de l\\\'association sur le site du diocèse d\\\'Angers', 'http://catholique-angers.cef.fr/Les-Amis-des-Orgues-de-la-Doutre-Angers', '', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(35, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 339-341', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(45, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(46, '', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(34, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 79-81', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(36, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(37, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(39, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(40, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(41, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(42, NULL, NULL, 'Association des Amis des Orgues', 'http://www.meniorgue.fr/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(43, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(44, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(48, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 289-292', NULL, 'Site du facteur d\\\'orgues', 'http://www.orguent.fr/fr/accueil.php?cat=orrena', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(49, NULL, NULL, 'Site du facteur d\\\'orgues', 'http://www.orgues-oberthur.org/tech/luc.php?lang=eu', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(50, NULL, NULL, 'Site du facteur d\\\'orgues', 'http://www.orguent.fr/fr/accueil.php?cat=orrecl', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(51, NULL, NULL, 'Site du facteur d\\\'orgues', 'http://orguent.fr/fr/accueil.php?cat=ornech', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(52, NULL, NULL, 'Site du facteur d\\\'orgues', 'http://orguent.fr/fr/accueil.php?cat=ornelp', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(53, NULL, NULL, 'Site du facteur d\\\'orgues', 'http://orguent.fr/fr/accueil.php?cat=ornemo', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(54, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 267-270', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(56, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(57, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(58, NULL, NULL, 'Site du facteur d\\\'orgues', 'http://www.orgues-oberthur.org/tech/bruf.php?lang=eu', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(59, NULL, NULL, 'Site des Amis de l\\\'Orgue', 'http://jp.blaineau.free.fr/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(60, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 207-210', NULL, 'Site de l\\\'association Jeux de mains jeux de pieds', 'https://orguestclement.wordpress.com/', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(61, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 41-42', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(62, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 413-415', '', 'Site de l\\\'association', 'https://orguethouare.wordpress.com/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(63, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 13-15', NULL, 'Site du facteur d\\\'orgues', 'http://www.orgues-oberthur.org/tech/ance.php?lang=eu', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(64, NULL, 'Le fabuleux destin de l\\\'orgue de Commequiers - Suite mélangées. Jean-Michel Dieuaide (2006). Editions Hortus, Hortus 521.', 'Site de l\\\'association', 'http://batcerise.no-ip.com/com.orgue/index.php?value=accueil&tool=desktop&n=20&menu=1&', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(65, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(67, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(69, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(70, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(71, NULL, 'Johann Ludwig Krebs : Clavierübung. Olivier Vernet et Ensemble \\\\\\\"in Ore mel\\\\\\\" CD Ligia 0104136-04, 2004\nManufacture d\\\'orgues Thomas. Olivier Vernet. Å’uvres de Johann Ludwig Krebs (CD I/15). CD Manufacture Thomas, 2008', 'Site du facteur d\\\'orgues', 'http://www.orgues-thomas.com/website/index.php?option=com_content&view=article&id=24%3Abazougers&catid=7%3Aorgue-neuf&Itemid=89&lang=fr', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(72, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 259-266', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(73, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 253-256', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(74, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 239-241', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(75, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 211-214', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(76, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 259-266', 'Marcel Dupré, œuvres pour orgue. Micheline Lagache et Philippe Lefebvre. Disque FR 811110, 1981', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(77, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 221-222', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(78, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(79, '- Dictionnaire historique Célestin Port, édition révisée Charles Combe 1965, page 740.\n- registre des délibérations du conseil de fabrique de Cheviré-le-Rouge.\n- Marcel Dupré. Marcel Dupré raconte... , Paris : Bornemann, 1972.\n- Graham Steed, The Organ Works of Marcel Dupré, Hillsdale, New York, Pendragon Press, 1999.\n- ARCAMC (1993). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 1 : Maine-et-Loire', NULL, 'Site web de l\\\'association des amis de l\\\'orgue de Cheviré-le-Rouge', 'http://chevire.org/', 'Blog de l\\\'association des amis de l\\\'orgue de Cheviré-le-Rouge', 'https://fr-fr.facebook.com/Orguedechevirelerouge', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(80, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(81, '', NULL, 'Association des Amis de Notre-Dame-de-Cunault', 'http://www.lesheuresmusicalesdecunault.fr/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(82, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(83, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(84, NULL, NULL, '', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(85, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(86, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(87, '', 'Louis Vierne, œuvres vocales avec orgue. Art et Musique AM/CD 107/30506, 2005', NULL, 'www.orguesaintmacaire.org', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(88, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(89, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 77-78', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(90, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 75-76', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(91, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(92, NULL, NULL, 'Site du facteur d\\\'orgues', 'http://www.orguescattiaux.org/Liste%20des%20instruments/Le%20Pouliguen/EC-Pouliguen.html', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(93, NULL, NULL, 'Les Amis de l\\\'orgue d\\\'Ancinnes', 'http://www.amis-orgue-ancinnes.com/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(94, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 373-374\nArticle Ouest-France :\nhttps://www.ouest-france.fr/pays-de-la-loire/ancenis-44150/une-resurrection-pour-lorgue-de-leglise-saint-medard-1188249\n', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(95, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 101-103', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(96, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 245-247', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(97, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 191-192', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(98, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(99, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(100, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(101, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(102, NULL, 'Syrius1413396(2005)Dandrieu,Clérambault,Séjan - Helga Schauerte-Maubouet', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(103, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(104, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(105, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(106, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 17-18', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(107, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(108, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(109, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(110, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(111, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(112, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(113, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(114, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(115, '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(116, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(117, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(118, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 31-33', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(119, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(120, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(121, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(122, '', 'Discographie :\nChiron M., Metz J.-J., Les couleurs de l\\\'orgue romantique. Art et Musique AM/CD 107/39703, 1997\nChiron M., Ouvrard E., Touya A.-L., Le Choeur des Mauges (Dir. K. Blardone), Louis Vierne, oeuvres vocales avec orgue. Art et Musique AM/CD 107/30506, 2005', NULL, 'www.orguesaintmacaire.org', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(123, NULL, NULL, '', 'http://orgue.pouzauges.free.fr/', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(124, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(125, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(126, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(127, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(128, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(130, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(131, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(132, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(133, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(134, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(135, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(136, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(137, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(138, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(139, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(140, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(141, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(142, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(143, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(144, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(145, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(146, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(147, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(148, 'ARCAMC (1995). Inventaire National des Orgues - Orgues en Pays de la Loire, Tome 2 : Loire-Atlantique, pp. 305-307', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(149, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(150, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(151, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(152, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `inventaire_sources`
--
ALTER TABLE `inventaire_sources`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `inventaire_sources`
--
ALTER TABLE `inventaire_sources`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=153;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
