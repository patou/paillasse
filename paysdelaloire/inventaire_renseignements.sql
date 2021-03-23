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
-- Structure de la table `inventaire_renseignements`
--

CREATE TABLE `inventaire_renseignements` (
  `id` int(11) NOT NULL,
  `statut` int(1) DEFAULT NULL,
  `departement` varchar(50) DEFAULT NULL,
  `ville` varchar(100) DEFAULT NULL,
  `edifice` varchar(100) DEFAULT NULL,
  `instrument` varchar(100) DEFAULT NULL,
  `emplacement` varchar(255) DEFAULT NULL,
  `facteur1` varchar(100) DEFAULT NULL,
  `facteur2` varchar(100) DEFAULT NULL,
  `facteur3` varchar(100) DEFAULT NULL,
  `facteur4` varchar(100) DEFAULT NULL,
  `facteur5` varchar(100) DEFAULT NULL,
  `facteur6` varchar(100) DEFAULT NULL,
  `facteur7` varchar(100) DEFAULT NULL,
  `facteur8` varchar(100) DEFAULT NULL,
  `buffet` varchar(100) DEFAULT NULL,
  `diapason` varchar(50) DEFAULT NULL,
  `temperament` varchar(50) DEFAULT NULL,
  `contributeur` int(4) DEFAULT NULL,
  `nbr_jeux` int(3) DEFAULT NULL,
  `image` varchar(25) DEFAULT NULL,
  `credit` varchar(25) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `inventaire_renseignements`
--

INSERT INTO `inventaire_renseignements` (`id`, `statut`, `departement`, `ville`, `edifice`, `instrument`, `emplacement`, `facteur1`, `facteur2`, `facteur3`, `facteur4`, `facteur5`, `facteur6`, `facteur7`, `facteur8`, `buffet`, `diapason`, `temperament`, `contributeur`, `nbr_jeux`, `image`, `credit`) VALUES
(1, 3, 'Loire-Atlantique (44)', 'Guérande', 'Collégiale Saint-Aubin', 'Grand orgue', 'sol, au fond du choeur', 'Beuchet-Debierre (1955)', 'Renaud (1982)', '', '', '', '', '', '', '', '443', 'Égal', 1, 42, 'DN64MsCXM67lDiqi.jpg', 'Valentin Leroux'),
(2, 1, 'Loire-Atlantique (44)', 'Nantes', 'Cathédrale Saint-Pierre', 'Grand orgue', 'En tribune', 'Girardet (1619)', 'Clicquot (1784)', 'Merklin (1866)', 'Gloton (1933)', 'Beuchet-Debierre (1971)', '', '', '', '', '', NULL, 1, 74, 'UEZkgWl8WFHTVHG7.jpg', ''),
(3, 3, 'Sarthe (72)', 'La Ferté-Bernard', 'Église Notre-Dame-des-Marais', 'Grand orgue', 'Tribune, première travée de la nef côté nord', 'Baudot (1501)', 'Bert (1535)', 'Baldner (1894)', 'Beurtin (1938)', 'Renaud (1985)', '', '', '', 'Baudot (1501) et Chemin (1535)', NULL, NULL, 15, 19, 'j88hPnEvZRmluKws.jpg', NULL),
(4, 3, 'Loire-Atlantique (44)', 'Nantes', 'Église Notre-Dame-de-Toutes-Aides', 'Grand orgue', 'sol, au fond du chœur', 'Debierre (1885)', 'Gloton-Debierre (1945)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'égal', 12, 14, 'dKWXb5BUj2m0fReD.jpg', 'Philippe Humeau'),
(5, 3, 'Vendée (85)', 'Luçon', 'Cathédrale Notre-Dame-de-l´Assomption', 'Grand orgue', 'Tribune au fond de la nef', 'Cavaillé-Coll (1856)', 'Schwenkedel (1968)', '', NULL, NULL, NULL, NULL, NULL, '', '', 'égal', 13, 54, 'M9uEzmUQYUuvn8mm.jpg', 'Guillaume Marionneau'),
(6, 3, 'Vendée (85)', 'Luçon', 'Cathédrale Notre-Dame-de-l\'Assomption', 'Orgue de chœur', 'sol, première travée du chœur côté sud', 'Debierre (1882)', '', NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, 'égal', 13, 10, 't31hxmH6YjpxQS7O.jpg', 'Guillaume Marionneau'),
(7, 3, 'Loire-Atlantique (44)', 'Saint-Aignan-de-Grand-Lieu', 'Église Saint-Aignan', 'Grand orgue', 'Sol, première travée de la nef côté nord', 'Londe (2000)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Benoît Camozzi (polychromie Paul Poilpré)', '440', 'Inégal 1/6Â° de comma', 12, 15, '2bmJEEd6EnLoWMs6.jpg', ''),
(8, 3, 'Loire-Atlantique (44)', 'Nantes', 'Église Notre-Dame-de-Toutes-Joies', 'Grand orgue', 'sol, au fond du transept nord', 'Debierre (1863)', 'Gloton-Debierre (1937)', 'MBGO (2008)', NULL, NULL, NULL, NULL, NULL, 'Debierre 1863', NULL, 'égal', 14, 19, 'gIG3rlDKbRDFdiEV.jpg', 'Paroisse'),
(9, 3, 'Maine-et-Loire (49)', 'Angers', 'Cathédrale Saint-Maurice', 'Grand orgue', 'Tribune, fond de la nef', 'Cavaillé-Coll (1873)', 'Beuchet-Debierre (1959)', NULL, NULL, NULL, NULL, NULL, NULL, '', '435', 'égal', 15, 65, 'KPYj58DsHs6VxvtX.jpg', 'Inventaire national'),
(10, 3, 'Maine-et-Loire (49)', 'Beaufort-en-Vallée', 'Église Notre-Dame', 'Grand orgue', 'tribune en fond de nef', 'Bonn (1874)', 'Debierre (1884)', 'Gloton (1934)', 'MLGO (1994)', NULL, NULL, NULL, NULL, 'Moisseron 1874', '440', 'égal', 15, 37, 'Hbi0yLXAsziPYQwP.jpg', 'Henri-Franck Beaupérin'),
(11, 3, 'Loire-Atlantique (44)', 'Nantes', 'Église Saint-Félix', 'Grand orgue', 'sol, au fond de la nef', 'Beuchet-Debierre 1954', 'DLFO 2008', NULL, NULL, NULL, NULL, NULL, NULL, 'Beuchet-Debierre 1954', '440', 'Egal', 16, 31, '29LjqPvT0y4qk5O6.jpg', ''),
(12, 3, 'Maine-et-Loire (49)', 'Angers', 'Cathédrale Saint-Maurice', 'Orgue de chœur', 'sol au fond du chœur', 'Bonn (1856)', 'Beuchet-Debierre (1967)', NULL, NULL, NULL, NULL, NULL, NULL, 'Chapeau 1856', '', 'égal', 15, 17, 'vk4x0gq9eiyeXqKZ.jpg', ''),
(13, 3, 'Loire-Atlantique (44)', 'Nantes', 'Cathédrale Saint-Pierre-et-Saint-Paul', 'Grand orgue', 'Tribune au fond de la nef', 'Girardet (1619)', 'Clicquot (1784)', 'Merklin (1868)', 'Gloton-Debierre (1933)', 'Beuchet-Debierre (1971)', NULL, NULL, NULL, 'Girardet (1619), Lépine (1768)', NULL, 'égal', 15, 75, 'owurX4Dxk9PRcopc.jpg', ''),
(14, 3, 'Loire-Atlantique (44)', 'Nantes', 'Cathédrale Saint-Pierre-et-Saint-Paul', 'Orgue de chœur', 'sol, première travée du chœur côté nord', 'Debierre 1896', 'Gloton-Debierre 1946', 'Renaud 1993', 'MBGO 2013', NULL, NULL, NULL, NULL, NULL, NULL, 'égal', 15, 31, 'CKMmVVU3Oh4Cy41y.jpg', 'Inventaire national'),
(15, 3, 'Maine-et-Loire (49)', 'Saint-Macaire-en-Mauges', 'Église Saint-Macaire', 'Grand orgue', 'Tribune au fond de la nef', 'Gloton-Debierre (1925)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Gloton-Debierre (1925)', '440', 'Egal', 17, 22, '3aOrcTt0PrGQDriV.jpg', 'Etienne Ouvrard'),
(16, 3, 'Sarthe (72)', 'La Flèche', 'Chapelle Saint-Louis, prytanée militaire', 'Grand orgue', 'Tribune, fond de la nef', 'Levasseur (1640)', 'Benoist & Sarelot (1996)', NULL, NULL, NULL, NULL, NULL, NULL, 'Frileux, Cornet et Jousse (1640)', '392', 'inégal', 15, 35, 'lcbVObu8nsqcbdON.jpg', NULL),
(17, 3, 'Loire-Atlantique (44)', 'Batz-sur-Mer', 'Église Saint-Guénolé', 'Grand orgue', 'Tribune au fond de la nef', 'Brunel ? (fin XVIIe s.)', 'Gloton-Debierre (1926)', 'Renaud (1986)', NULL, NULL, NULL, NULL, NULL, NULL, '440', NULL, 15, 21, 'sekmoKy79P7a8QO4.jpg', 'Inventaire national'),
(18, 3, 'Sarthe (72)', 'Le Mans', 'Cathédrale Saint-Julien', 'Grand orgue', 'Tribune au fond du transept sud', 'Bert (1531)', 'De Héman (1651)', 'Claude Frères (1833)', 'Abbé Tronchet (1913)', 'Beuchet-Debierre & Danion-Gonzalez (1974)', 'Nonnet & Plet (2018)', NULL, NULL, 'Hayneufve (1531)', '440', 'égal', 15, 63, 'tMyUiDCpg5U1LUVM.jpg', NULL),
(19, 3, 'Loire-Atlantique (44)', 'Nantes', 'Église Notre-Dame-de-Bon-Port St-Louis', 'Grand orgue', 'Tribune au fond de la nef', 'Debierre (1891)', 'Gloton-Debierre (1929)', 'Renaud (1981)', NULL, NULL, NULL, NULL, NULL, 'Debierre (1891)', '', 'égal', 15, 40, 'Et6ZUt094qCfELws.jpg', 'Henri-Franck Beaupérin'),
(20, 3, 'Mayenne (53)', 'Craon', 'Église Saint-Nicolas', 'Grand orgue', 'Tribune au fond de la nef', 'Stoltz et Goyadin (1856)', 'Beuchet-Debierre (1964)', 'Boisseau (2003)', NULL, NULL, NULL, NULL, NULL, 'Stoltz et Goyadin (1856), Boisseau (2003)', NULL, 'égal', 15, 32, 'gTI8b0WN54WqMC9M.jpg', 'Henri-Franck Beaupérin'),
(21, 3, 'Vendée (85)', 'Fontenay-le-Comte', 'Église Notre-Dame', 'Grand orgue', 'Tribune au fond de la nef', 'Oberthur (1995)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Oberthur 1995', '440', 'égal', 1, 29, 'zCTSr2qops1DrdmA.jpg', NULL),
(22, 3, 'Maine-et-Loire (49)', 'Angers', 'Chapelle des Bénédictines du Calvaire', 'Orgue de chœur', 'Sol, côté gauche du chœur', 'Verschueren (1960)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'En chêne - 3 plates-faces. ', '440', NULL, 18, 6, 'YDQ0dnRR5VCPbbJE.JPG', 'Amis orgues de la Doutre'),
(23, 3, 'Maine-et-Loire (49)', 'Angers', 'Église Sainte-Marie de Belle-Beille', 'Orgue polyphone', 'Sol, côté droit de la nef', 'Louis Debierre', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Debierre', '440', 'égal', 18, 5, 'gLgelY0kQIJCLfVc.jpg', 'Amis orgues de la Doutre'),
(24, 3, 'Maine-et-Loire (49)', 'Angers', 'Chapelle du Bon-Pasteur', 'Grand orgue', 'Tribune au fond de la nef', 'Koenig (1972)', 'Kuhn (1992)', NULL, NULL, NULL, NULL, NULL, NULL, 'Koenig 1972', '440', '', 18, 20, 'iVsf4dyRXv4EKEvJ.jpg', 'Amis Orgues de la Doutre'),
(25, 3, 'Vendée (85)', 'Saint-Gilles-Croix-de-Vie', 'Église Sainte-Croix', 'Grand orgue', 'Tribune au fond de la nef', 'Emeriau (1983-1993)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Emeriau 1983', '440', 'Werkmeister', 15, 19, 'yW0Wudl4wdsmpFkf.jpg', 'Henri-Franck Beaupérin'),
(26, 3, 'Vendée (85)', 'La Roche-sur-Yon', 'Église Saint-Louis', 'Grand orgue', 'Tribune au fond de la nef', 'Yves Koenig (1989)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '443', 'égal', 15, 40, 'EOp6fQGumeAJiKx6.jpg', NULL),
(27, 3, 'Vendée (85)', 'Le Fenouiller', 'Église Saint-Laurent', 'Orgue de chœur', 'sol, angle sud du chœur', 'Guillemin (1982)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '445', 'Kirnberger III', 15, 8, '5eHqa5Dt21XCO2XD.jpg', 'Sébastien Avril'),
(28, 3, 'Maine-et-Loire (49)', 'Cholet', 'Église Notre-Dame', 'Grand orgue', 'sol, transept sud', 'Beuchet-Debierre (1969)', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 'égal', 15, 44, 'uvCCvayRWUBAZhXW.jpg', ''),
(29, 3, 'Loire-Atlantique (44)', 'Saint-Philbert-de-Grand-Lieu', 'Église Saint-Philibert', 'Grand orgue', 'Tribune au fond de la nef', 'Van Bever (1895)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 19, 19, '0cQWaNBY7XwSpQco.jpg', 'Samuel Delaunay'),
(30, 3, 'Sarthe (72)', 'Ecommoy', 'Église Saint-Martin', 'Grand orgue', 'Sol, transept nord', 'Damiens (1876)', 'Conan & Lemercier (2008)', NULL, NULL, NULL, NULL, NULL, NULL, 'Damiens 1876, Lemercier 2008', '440', 'Egal', 20, 16, 'IUMpdYw1nJ7FnCik.jpg', NULL),
(31, 3, 'Maine-et-Loire (49)', 'Angers', 'Église Sainte-Trinité', 'Grand orgue', 'Tribune au fond de la nef', 'Daublaine-Callinet (1840)', 'Debierre (1870)', 'Chéron (1950)', 'Sévère (1972)', NULL, NULL, NULL, NULL, 'Daublaine-Callinet 1840', '440', '', 18, 24, '3tjAnualEQsOXEeU.JPG', 'Amis Orgues de la Doutre'),
(32, 3, 'Maine-et-Loire (49)', 'Angers', 'Église Sainte-Thérèse', 'Grand orgue', 'Tribune au fond de la nef', 'Debierre (1903)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '440', 'égal', 18, 22, 'tSmTyegrz6mUIR8s.JPG', 'Amis Orgues de la Doutre'),
(33, 3, 'Maine-et-Loire (49)', 'Angers', 'Église Saint-Jacques', 'Grand orgue', 'Sol, dans le transept sud', 'Cavaillé-Coll-Convers (1926)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Convers', '440', 'égal', 18, 16, 'lItlPmnQO3fh9UZ6.JPG', 'Amis Orgues de la Doutre'),
(34, 3, 'Loire-Atlantique (44)', 'Le Croisic', 'Église Notre-Dame-de-Pitié', 'Grand orgue', 'Tribune au fond de la nef', 'Ducroquet (?)', 'Debierre (1895)', 'Renaud (1974)', NULL, NULL, NULL, NULL, NULL, 'Ducroquet (?)', NULL, 'égal', 15, 13, 'jPdqIvUstOtQ5xEy.jpg', NULL),
(35, 3, 'Loire-Atlantique (44)', 'Rezé', 'Église Saint-Paul', 'Grand orgue', 'sol, au fond du choeur', 'Facteur inconnu (?)', 'Cavaillé-Coll (1850)', 'Debierre (1911)', 'Renaud (1971)', 'Sévère (1997)', NULL, NULL, NULL, NULL, NULL, 'égal', 15, NULL, '9cPyv1XaNW5Y8Zzi.JPG', NULL),
(36, 3, 'Mayenne (53)', 'Lassay-les-Châteaux', 'Église Saint-Fraimbault', 'Orgue de chœur', 'sol, au fond du chœur', 'Daublaine-Callinet (1842)', 'Firmin (1946)', 'Conan et Lemercier (2007)', NULL, NULL, NULL, NULL, NULL, NULL, '440', 'Rameau', 21, 11, 'piGz3VYYLUzxg8n7.jpg', ''),
(45, 3, 'Mayenne (53)', 'Pontmain', 'Basilique Notre-Dame', 'Grand orgue', 'Tribune au fond de la nef', 'Gloton-Debierre (1931)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Gloton 1931', NULL, 'égal', 15, 34, 'i1PqbVEw7xas8VYJ.jpg', 'Henri-Franck Beaupérin'),
(37, 3, 'Sarthe (72)', 'Solesmes', 'Abbaye Saint-Pierre', 'Grand orgue', 'Tribune au fond de la nef', 'Schwenkedel (1967)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Georges Lhôte 1967', NULL, 'égal', 15, 38, 'm9yfgVOqLkoevKcS.jpg', NULL),
(38, 2, NULL, NULL, NULL, 'NOUVEL INSTRUMENT', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'FCNyVoE5yJiUPlN4.jpg', NULL),
(39, 3, 'Sarthe (72)', 'La Flèche', 'Église Saint-Thomas', 'Grand orgue', 'Tribune au fond de la nef', 'Merklin (1885)', 'Chéron (?)', 'Benoist & Sarélot (1976)', NULL, NULL, NULL, NULL, NULL, 'Merlkin 1885', '', 'égal', 23, 21, 'jVI3IlM619IBkyyJ.JPG', 'Gwilherm Poullennec'),
(40, 3, 'Maine-et-Loire (49)', 'Angers', 'Église Saint-Joseph', 'Grand orgue', 'Tribune au fond de la nef', 'Cavaillé-Coll (1879)', 'Sévère (1960)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'égal', 15, 27, 'R0ff30LRkuM0s7dV.jpg', NULL),
(41, 3, 'Vendée (85)', 'Challans', 'Église Notre-Dame', 'Grand orgue', 'Tribune dans le transept sud', 'Rémy Mahler (2003)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Mahler 2003', NULL, 'Kirnberger III', 15, 22, 'SryLNuW8rg79bf2u.jpg', 'Henri-Franck Beaupérin'),
(42, 3, 'Maine-et-Loire (49)', 'La Ménitré', 'Église Saint-Jean-Baptiste', 'Grand orgue', 'Tribune au fond de la nef', 'Hulbert (1842)', 'Bonn (1869)', 'Debierre (1898)', NULL, NULL, NULL, NULL, NULL, 'Bonn 1869', NULL, 'égal', 15, 14, 'PhI4yS8QDMTZdf2h.JPG', 'Henri-Franck Beaupérin'),
(43, 3, 'Mayenne (53)', 'Laval', 'Cathédrale Sainte-Trinité', 'Grand orgue', 'Tribune au fond de la nef', 'Cavaillé-Coll (1853)', '', NULL, NULL, NULL, NULL, NULL, NULL, 'Cavaillé-Coll 1853', '434', 'égal', 15, 28, 'JzE5SQX0dpKxYWxR.jpg', NULL),
(44, 3, 'Maine-et-Loire (49)', 'Noyant', 'Église Saint-Martin', 'Orgue de chœur', 'sol, au fond du chœur', 'Holdich (1850 ?)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Holdich 1850 ?', '440', 'Egal', 24, 8, NULL, 'Marc Inglebert'),
(46, 1, '', '', '', 'NOUVEL INSTRUMENT', '', '', NULL, NULL, NULL, NULL, NULL, NULL, '', '', NULL, NULL, 22, NULL, NULL, NULL),
(47, 3, 'Loire-Atlantique (44)', 'Nantes', 'Basilique Saint-Nicolas', 'Grand orgue', 'Tribune au fond de la nef', 'Beuchet-Debierre (1963)', 'Hurvy (2002)', NULL, NULL, NULL, NULL, NULL, NULL, 'Beuchet-Debierre 1963', NULL, 'égal', 15, 41, '404PKrTEZ1lOhzhD.jpg', 'Henri-Franck Beaupérin'),
(48, 3, 'Loire-Atlantique (44)', 'Nantes', 'Chapelle du collège Saint-Stanislas', 'Orgue de chœur', 'sol, transept sud', 'Cavaillé-Coll (1867)', 'Gloton-Debierre (1946)', NULL, NULL, NULL, NULL, NULL, NULL, '', '440', 'égal', 15, 13, 'q39PhyYPN8HGF65D.JPG', 'Henri-Franck Beaupérin'),
(49, 3, 'Vendée (85)', 'Les Lucs-sur-Boulogne', 'Église Saint-Pierre', 'Grand orgue', 'Sol, transept sud', 'Oberthur (1985)', '', NULL, NULL, NULL, NULL, NULL, NULL, 'Oberthur', NULL, 'égal', 15, 14, 'tYvkgF3BqbpYINSh.jpg', 'Hervé-Jacques Hylae'),
(50, 3, 'Loire-Atlantique (44)', 'Le Clion', 'Église Chaire-de-Saint-Pierre', 'Orgue de choeur', 'sol, au fond du choeur', 'Alizon (?)', 'MBGO (2007)', NULL, NULL, NULL, NULL, NULL, NULL, 'MBGO 2007', NULL, 'égal', 15, 8, 'VXCPgmZv3S7lhYQX.jpg', 'MBGO'),
(51, 3, 'Maine-et-Loire (49)', 'Chemillé', 'Église Notre-Dame', 'Grand orgue', 'sol, transept nord', 'Merklin (1914)', 'MBGO (1993)', NULL, NULL, NULL, NULL, NULL, NULL, 'Merklin 1914', NULL, '', 15, 16, 'VdIXJ9o0evjglziC.jpg', 'MBGO'),
(52, 3, 'Loire-Atlantique (44)', 'La Planche', 'Église Saint-Jacques', 'Grand orgue', 'Sol, au fond du choeur', 'MBGO (2003)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'MBGO 2003', NULL, 'égal', 15, 8, 'UYmwhTZYM19dhbNs.jpg', 'MBGO'),
(53, 3, 'Vendée (85)', 'Mouilleron-le-Captif', 'Église Saint-Martin', 'Grand orgue', NULL, 'MBGO (1996)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, NULL, NULL, NULL),
(54, 3, 'Loire-Atlantique (44)', 'Nantes', 'Église Sainte-Thérèse', 'Grand orgue', 'tribune au fond de la nef', 'Renaud-Bouvet (1964)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Renaud-Bouvet 1964', '440', 'égal', 15, 54, 'ksDpNC600qYYUoFE.jpg', 'Paroisse'),
(55, 3, 'Vendée (85)', 'Olonne-sur-Mer', 'Église Notre-Dame-de-l\'Assomption', 'Orgue de chœur', 'sol, côté sud du chœur', 'Delhumeau (2002)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, 25, 18, 'RWI3zsVMG57Aq0lB.jpg', NULL),
(56, 1, 'Vendée (85)', 'Les Sables d\\\'Olonne', 'Église Notre Dame de Bon Port', 'Orgue de choeur', 'Choeur', 'Jean Baptiste Lelogeais (1859)', 'Louis Debierre (1890)', 'Gloton (1939)', 'Joseph Beuchet (1972)', 'Manufacture d\\\'orgues ROBERT (2002)', NULL, NULL, NULL, NULL, NULL, NULL, 25, 23, NULL, NULL),
(57, 2, 'Vendée (85)', 'Les Sables-d\\\'Olonne', 'Église Saint-Pierre', 'Orgue de chœur', 'sol, au fond du chœur', 'Gloton-Debierre (1935)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 25, NULL, 'UW8mUsQSaV4HevWH.jpg', NULL),
(58, NULL, 'Vendée (85)', 'La Bruffière', 'Église Sainte-Radegonde', 'Grand orgue', 'sol, au fond du choeur', 'Oberthur (1980)', '', NULL, NULL, NULL, NULL, NULL, NULL, 'Oberthur', NULL, 'égal', 25, 21, 'Ui8w3XJhhbCa4rbg.jpg', 'Henri-Franck Beaupérin'),
(59, 3, 'Vendée (85)', 'Montaigu', 'Église Saint-Jean-Baptiste', 'Grand orgue', 'sol, au fond du chœur', 'Stoltz (1892)', 'Beuchet-Debierre (1958)', 'Renaud (1984)', '', NULL, NULL, NULL, NULL, 'Cavaillé-Coll', '437', 'inégal', 25, 27, 'hMOlwR8WkxpVgTt2.jpg', NULL),
(60, 3, 'Loire-Atlantique (44)', 'Nantes', 'Église Saint-Clément', 'Grand orgue', 'sol, entre les arcades du déambulatoire', 'Debierre (1893)', 'Beuchet-Debierre (1978)', 'Hurvy (1993)', 'Robert Frères (2012)', NULL, NULL, NULL, NULL, 'Debierre 1893', NULL, 'égal', 15, 28, 'ANhf71vE33djJiP2.jpg', 'Site de l\\\'association'),
(61, 3, 'Loire-Atlantique (44)', 'Bouguenais', 'Église Saint-Pierre', 'Grand orgue', 'Sol, au fond du chœur', 'Gloton-Debierre (1945)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'égal', 15, 13, 'gKtS5r9MRqa5JpQG.JPG', 'Henri-Franck Beaupérin'),
(62, 3, 'Loire-Atlantique (44)', 'Thouaré-sur-Loire', 'Église Saint-Vincent', 'Grand orgue', 'Tribune au fond de la nef', 'Debierre (1912)', 'Beuchet-Debierre (1960)', 'Hurvy (1994)', NULL, NULL, NULL, NULL, NULL, 'Hurvy 1994', NULL, 'égal', 15, 14, 'tc6QiA4tSgayGy5W.jpg', 'Site de l\\\'association'),
(63, 3, 'Loire-Atlantique (44)', 'Ancenis', 'Église Saint-Pierre', 'Grand orgue', 'Tribune au fond de la nef', 'Le Logeais (1851)', 'Debierre (1881)', 'Oberthur (1982)', NULL, NULL, NULL, NULL, NULL, 'Le Logeais 1851, Oberthur 1982', NULL, 'égal', 15, 18, '09DYPKzL8jjhRpzH.jpg', NULL),
(64, 3, 'Vendée (85)', 'Commequiers', 'Église Saint-Pierre', 'Grand orgue', 'sol, transept nord', 'Bénévoles (1979-2003)', 'Conan (2005)', NULL, NULL, NULL, NULL, NULL, NULL, 'Bénévoles', NULL, 'Rameau', 15, 30, 'E4kd11KeN6fr7UPS.jpg', 'Site de l\\\'association'),
(65, 3, 'Vendée (85)', 'Le Poiré-sur-Vie', 'Église Saint-Pierre', 'Grand orgue', 'Tribune au fond de la nef', 'Abbey (1896)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'égal', 15, 26, 'NE6a5wIRaF7XF7NB.jpg', 'Ville du Poiré-sur-Vie'),
(66, NULL, 'Vendée (85)', 'Fontenay-le-Comte', 'Église Notre-Dame', 'Ancien grand orgue (démonté)', 'tribune au fond de la nef', 'Lapeyre (1844)', 'Debierre (1890)', '', NULL, NULL, NULL, NULL, NULL, 'Debierre 1890', NULL, 'égal', 15, 22, 'Fr9ak6242wEqAenC.jpg', 'Ville de Fontenay-le-Comt'),
(67, 3, 'Vendée (85)', 'Chavagnes-en-Paillers', 'Église Saint-Pierre-et-Saint-Paul', 'Grand orgue', 'sol, côté nord de la nef', 'Guillemin (1989)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '443', 'Kirnberger II', 15, 22, 'Gcx9t43SUC0r2A3y.jpg', ''),
(68, 3, 'Maine-et-Loire (49)', 'Trémentines', 'Église Notre-Dame', 'Orgue de chœur', 'sol, bas côté gauche du chœur', 'Thomas (197..)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Thomas', NULL, '', 15, 9, 'hIvwEjNse7eL2BKY.jpg', 'Philippe Humeau'),
(69, 3, 'Maine-et-Loire (49)', 'Beaupréau', 'Collège Notre-Dame-de-Bonne-Nouvelle', 'Grand orgue', 'sol, transept nord', 'Gloton-Debierre (1930)', 'Alcouffe (1968-72)', 'Renaud (1973)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 15, 15, '8vGC12SiOSrAX2c6.jpg', 'Philippe Humeau'),
(70, 3, 'Mayenne (53)', 'Evron', 'Basilique Notre-Dame-de-l\'Epine', 'Grand orgue', 'tribune au fond de la nef', 'Goydadin (1877)', 'Roethinger (1964)', NULL, NULL, NULL, NULL, NULL, NULL, '1623', NULL, 'égal', 15, 20, 'UCH98a5pzUwPQWWR.jpg', 'Ville d\\\'Evron'),
(71, 3, 'Mayenne (53)', 'Bazougers', 'Prieuré de la Cotellerie', 'Grand orgue', 'tribune au fond de la nef', 'Thomas (2002)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Thomas 2002', '440', 'Meurice/Thomas', 15, 23, 'B8gy096wymC3UwWU.jpg', 'Manufacture Thomas'),
(72, 3, 'Loire-Atlantique (44)', 'Vertou', 'Institut Les Hauts-Thébaudières', 'Grand orgue', 'tribune en fond de scène', 'Debierre (1899)', 'Beuchet-Debierre (1976)', NULL, NULL, NULL, NULL, NULL, NULL, 'Beuchet-Debierre 1976', NULL, 'égal', 15, 40, 'KiFaSU7cjiqhBAjO.jpg', 'ARCAMC'),
(73, 3, 'Loire-Atlantique (44)', 'Nantes', 'Église Sainte-Croix', 'Grand orgue', 'Sol, au fond du chœur', 'Le Logeais (XIXe s.)', 'Gloton-Debierre (1925)', 'Renaud (1976)', NULL, NULL, NULL, NULL, NULL, 'Le Logeais - Gloton-Debierre', NULL, 'égal', 15, 21, 'NjPnOcqy49PEkNYD.jpg', 'Didier Berthelot'),
(74, 3, 'Loire-Atlantique (44)', 'Nantes', 'Basilique Saint-Nicolas', 'Orgue de chœur', 'sol, entre les arcades centrales du déambulatoire', 'Debierre (1880)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Debierre 1880', NULL, 'égal', 15, 13, 'jI3BbFbSxnyzy1tQ.jpg', 'Didier Berthelot'),
(75, 3, 'Loire-Atlantique (44)', 'Nantes', 'Basilique Saint-Donatien', 'Grand orgue', 'sol, transept sud', 'Debierre (1881)', 'Renaud (1971)', NULL, NULL, NULL, NULL, NULL, NULL, 'Renaud 1971', NULL, 'égal', 15, 23, 'dqnR6H5nVvepNah7.jpg', NULL),
(77, 3, 'Loire-Atlantique (44)', 'Nantes', 'Église Saint-Jacques', 'Orgue de chœur', 'sol, au fond du chœur', 'Debierre (1891)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'égal', 15, 6, 'YzhZrgj72yxaOgOQ.jpg', 'Henri-Franck Beaupérin'),
(76, 3, 'Loire-Atlantique (44)', 'Nantes', 'Église Sainte-Madeleine', 'Grand orgue', 'tribune au fond de la nef', 'Bouvet (1955)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Bouvet 1955', NULL, 'égal', 15, 35, 'NGAVqVQYQvj2lKNe.jpg', 'Henri-Franck Beaupérin'),
(78, NULL, 'Vendée (85)', 'Olonne-sur-mer', 'église Notre-Dame', 'Grand orgue', 'Choeur de l\\\'église', 'Delhumeau', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Type XVIIIème siècle allemand', '440', 'Valotti', 26, 14, 'Dyb0hKMRC0gRir2f.jpg', ''),
(79, 3, 'Maine-et-Loire (49)', 'Cheviré-le-Rouge', 'Église Saint-Médard', 'Orgue de chœur', 'Sol, au fond du chœur', 'Bonn (1865)', 'Debierre (1875)', 'Perroux (1953)', NULL, NULL, NULL, NULL, NULL, 'Bonn (1865)', NULL, 'égal', 27, 13, '5w6ffmF1e7h9I6Ku.jpg', 'Denis Épié'),
(86, 3, 'Maine-et-Loire (49)', 'Saumur', 'Église Notre-Dame-de-Nantilly', 'Grand orgue', 'Tribune, fond de la nef', 'Pierre Le Hellocq (1685-1690)', 'Louis Bonn (1847)', 'MBGO (2016)', NULL, NULL, NULL, NULL, NULL, NULL, '438', 'D\\\'Alembert-Rousseau', 12, 33, 'txPowYeUaZLIL7cR.jpg', 'Philippe Humeau'),
(80, 1, NULL, NULL, NULL, 'NOUVEL INSTRUMENT', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 26, NULL, NULL, NULL),
(81, 3, 'Maine-et-Loire (49)', 'Chênehutte-Trèves-Cunault', 'Prieurale Notre-Dame', 'Grand orgue', 'sol, transept sud', 'Boisseau (1977)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, 37, '4WqXv9Vq6uGH1R1z.jpg', 'Henri-Franck Beaupérin'),
(82, 3, 'Vendée (85)', 'La Bruffière', 'Église Saint-Radegonde', 'Grand orgue', 'Sol, au fond du chœur', 'Oberthur (1981)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'égal', 15, NULL, 'jSS0ON2vPb9P2iww.jpg', 'Henri-Franck Beaupérin'),
(83, 3, 'Vendée (85)', 'Mareuil-sur-Lay', 'Église Saint-Sauveur', 'Grand orgue', 'Sol, transept nord', 'Oberthur (1988)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Oberthur 1988', NULL, 'égal', 15, 12, 'FPWOHaI3kXnbLSkw.jpg', 'Oberthur'),
(84, 3, 'Loire-Atlantique (44)', 'Vertou', 'Église Saint-Martin', 'Orgue de nef', 'Sol, au fond du transept nord', 'Ménoret (1998)', '', '', NULL, NULL, NULL, NULL, NULL, 'Ménoret 1998', '', 'égal', 27, 13, 'WVwPQKEbkSVI9J7a.JPG', 'Pierre Queval'),
(92, 3, 'Loire-Atlantique (44)', 'Le Pouliguen', 'Église Saint-Nicolas', 'Grand orgue', 'sol, au fond du chœur', 'Cattiaux (2017)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, 32, 'nxRzclca5Gv1s0SI.jpg', 'Henri-Franck Beaupérin'),
(85, 1, 'Maine-et-Loire (49)', '', '', 'NOUVEL INSTRUMENT', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 27, NULL, NULL, NULL),
(87, 3, 'Maine-et-Loire (49)', 'Saint-Macaire-en-Mauges', 'Église Saint-Macaire', 'Orgue polyphone', 'sol, au fond du chœur', 'Debierre', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 30, 6, 'nxiE8v7e6HGzOxML.JPG', 'Etienne Ouvrard'),
(88, 3, 'Loire-Atlantique (44)', 'Le Loroux-Bottereau', 'Église Saint-Jean-Baptiste', 'Grand Orgue', 'Sol, au fond du chœur', 'Gloton-Debierre (1947)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 30, 26, 'rAUjIPAIar2jOXTy.jpg', ''),
(89, 3, 'Loire-Atlantique (44)', 'Clisson', 'Église de la Trinité', 'Orgue de chœur', 'sol, au fond du chœur', 'Debierre (1874)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Debierre (1874)', NULL, 'égal', 15, 7, 'gHWaovhF4IVXaTar.jpg', 'Pierre Queval'),
(90, 3, 'Loire-Atlantique (44)', 'Clisson', 'Église Notre-Dame', 'Orgue de chœur', 'sol, au fond du chœur', 'Debierre 1903', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Debierre (1903)', NULL, 'égal', 15, 8, 'vexFPrSazUrYEJSQ.JPG', 'Pierre Queval'),
(91, 3, 'Maine-et-Loire (49)', 'Andrezé', 'Église Saint-Pierre', 'Grand orgue', 'sol, au fond du choeur', 'inconnu (XIXe s.)', 'Renaud (1984-1990)', 'Léon (2006)', NULL, NULL, NULL, NULL, NULL, NULL, '440', '', 17, 8, 'pex5GnyghqsGZiXt.jpg', 'Etienne Ouvrard'),
(93, 3, 'Sarthe (72)', 'Ancinnes', 'Église St-Pierre-St-Paul', 'Grand orgue', 'tribune en fond de nef', 'Damiens Frères (1863)', 'Mounier (1985)', NULL, NULL, NULL, NULL, NULL, NULL, 'Damiens (1863)', '', 'égal', 15, 15, 'EreQsLUGe9XiUQES.jpg', ''),
(94, 3, 'Loire-Atlantique (44)', 'Saint-Mars-la-Jaille', 'Église Saint-Médard', 'Orgue de chœur', 'Sol, au fond du chœur', 'Bedel & Isambart (1937)', 'Manufacture dÂ´Orgues Robert Frères (2013)', NULL, NULL, NULL, NULL, NULL, NULL, 'artisans locaux 1937', NULL, 'égal', 15, 12, 'Djead9i3Ry7ClLVU.jpg', 'Pierre Queval'),
(95, 3, 'Loire-Atlantique (44)', 'Héric', 'Église Saint-Nicolas', 'Grand orgue', 'sol, au fond du chœur', 'Bouvet (1965)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Bouvet 1965', NULL, 'égal', 15, 23, 'eH4J8ptcjEkVRzJi.JPG', 'Henri-Franck Beaupérin'),
(96, 3, 'Loire-Atlantique (44)', 'Nantes', 'Église Saint-Similien', 'Orgue de chœur', 'Sol, première travée du chœur côté sud', 'Le Logeais (?)', 'Debierre (1886)', 'Debierre (1905)', 'Gloton-Debierre (1935)', 'Renaud (1991)', '', NULL, NULL, 'Le Logeais', NULL, 'égal', 15, 17, 'SW6xdzqo7CACPOHU.JPG', 'Pierre Queval'),
(97, 3, 'Loire-Atlantique (44)', 'Nantes', 'Église Notre-Dame-de-Lourdes', 'Orgue de chœur', 'Sol, au fond du chœur', 'Gloton-Debierre (1946)', 'Renaud (1990)', NULL, NULL, NULL, NULL, NULL, NULL, 'Gloton-Debierre 1946', NULL, 'égal', 15, 19, 'H1paHIcQw6DcOTXA.JPG', 'Pierre Queval'),
(98, 3, 'Maine-et-Loire (49)', 'Le Lion-d\'Angers', 'Église Saint-Martin-de-Vertou', 'Orgue de chœur', 'sol, au fond du chœur', 'Debierre (1893)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Moisseron & André 1893', NULL, 'égal', 15, 5, 'DsyOMhft4e1ygJvY.JPG', NULL),
(99, 3, 'Maine-et-Loire (49)', 'Angers', 'Église Notre-Dame-des-Victoires', 'Orgue de chœur', 'sol, deuxième travée du chœur côté sud', 'Cavaillé-Coll (1865)', 'Debierre (1903)', 'Beuchet-Debierre (1963)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'égal', 15, 14, 'xv3Ft9WERyseBO5C.jpg', 'Henri-Franck Beaupérin'),
(100, 3, 'Sarthe (72)', 'Sablé', 'Église Notre-Dame', 'Grand orgue', 'Tribune au fond de la nef', 'Ducroquet (1843)', 'Debierre (1873)', 'Gloton (1923)', 'Toussaint (1995)', NULL, NULL, NULL, NULL, 'Ducroquet', NULL, 'égal', 15, 23, 'X2XlnBRf8JQaTDlA.jpg', 'Michel Bourcier'),
(101, NULL, 'Loire-Atlantique (44)', 'Héric', 'Eglise Saint-Nicolas', 'Grand orgue', 'Sol, au fond du chœur', 'Bouvet', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, NULL, 'oY8W1srH0lJevRWQ.jpg', NULL),
(102, NULL, 'Sarthe (72)', 'Saint Calais', 'Eglise Notre Dame', 'Grand orgue', 'Tribune en fond de nef', 'Inconnu XVIIème siècle', 'Daublaine-Callinet (1845)', 'Benoist et Sarélot (1978)', NULL, NULL, NULL, NULL, NULL, 'à deux corps', '440', 'égal', 31, 32, NULL, 'voir feuillet Journées P'),
(103, NULL, NULL, NULL, NULL, 'NOUVEL INSTRUMENT', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 31, NULL, NULL, NULL),
(104, 3, 'Sarthe (72)', 'Saint-Calais', 'Église Notre-Dame', 'Grand orgue', 'Tribune au fond de la nef', 'Daublaine-Callinet (1846)', 'Benoist-Sarelot (1978)', NULL, NULL, NULL, NULL, NULL, NULL, 'XVIIe siècle', '', NULL, 15, 32, '6JyjOvLnsZJMZQEr.jpg', 'Philippe Humeau'),
(105, 2, 'Loire-Atlantique (44)', 'Bourgneuf en Retz', 'Eglise Notre Dame de Bon Port', 'Grand orgue', 'Choeur', 'Georges Gloton 1925', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', 'égal', 30, 10, NULL, 'Jean-François Ouvrard'),
(106, 3, 'Loire-Atlantique (44)', 'Arthon-en-Retz', 'Église Saint-Martin', 'Orgue de chœur', 'sol, au fond du chœur', 'Gloton-Debierre (1942)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Gloton-Debierre', NULL, 'égal', 30, 11, 'SHsxaoRht7Lh3PBB.jpg', 'Jean-François Ouvrard'),
(107, 3, 'Maine-et-Loire (49)', 'Cholet', 'Conservatoire à Rayonnement Départemental', 'Grand orgue', 'au sol', 'Birouste (1990-91)', 'Villard (2003)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 30, 8, 'HI8Nv4eYRrB8Pn37.jpg', 'Etienne Ouvrard'),
(108, 3, 'Maine-et-Loire (49)', 'Beaupréau', 'Église Notre-Dame', 'Grand Orgue', 'Tribune au fond de la nef', 'Esbin (1897)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', 'égal', 30, 12, 'dxCuGIoq9dYSyRIf.jpg', 'Etienne Ouvrard'),
(109, 3, 'Maine-et-Loire (49)', 'Cholet', 'Église Saint-Pierre', 'Orgue de chœur', 'sol, au fond du transept nord', 'Debierre (1878)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Debierre', '440', 'égal', 30, 10, 'kLr2itVlxV1hHK1s.jpg', 'Etienne Ouvrard'),
(110, 3, 'Loire-Atlantique (44)', 'Orvault', 'Église Saint-Léger', 'Grand orgue', 'Sol, au fond du transept sud', 'Tolbecque (XIXe s.)', '', NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, 'égal', 15, 13, '0eg8v5Az1gQXTydj.jpg', 'Florence Ladmirault'),
(111, 3, 'Loire-Atlantique (44)', 'Bourgneuf-en-Retz', 'Eglise Notre-Dame de Bon-Port', 'Orgue de chœur', 'sol, côté nord du chœur', 'Gloton-Debierre (1925)', NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, '440', 'égal', 30, 10, 'NtfBAhmsgznAqwBC.jpg', 'Roger Martin'),
(112, 3, 'Sarthe (72)', 'Mamers', 'Église Notre-Dame', 'Grand orgue', '', 'Van Bever (1901)', 'Chéron (1960)', NULL, NULL, NULL, NULL, NULL, NULL, 'Van Bever', NULL, 'égal', 15, 26, 'nXuOhYcyB7iFLeuW.jpg', 'Loïc Desauty'),
(113, 3, 'Sarthe (72)', 'Fresnay-sur-Sarthe', 'Église Notre-Dame-de-l´Assomption', 'Grand orgue', 'Tribune au fond de la nef', 'Gloton-Debierre (1932)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'égal', 15, 13, 'pmeDmCVwQ7JCmaAQ.jpg', NULL),
(114, 3, 'Sarthe (72)', 'La Chartre-sur-le-Loir', 'Eglise Saint-Vincent', 'Grand orgue', 'Tribune au fond de la nef', 'Thébault (1869)', 'Tronchet (1930)', 'Benoist-Sarelot (1977)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'égal', 15, 13, '82o1ipywZyOZlmLx.jpg', 'Ville de La Chartre'),
(115, 3, 'Sarthe (72)', 'Château-du-Loir', 'Eglise Saint-Guingalois', 'Grand orgue', 'Tribune au fond de la nef', 'Guillouard (1845)', 'Enault-Beauté (1914)', 'Renaud (1991)', NULL, NULL, NULL, NULL, NULL, 'XVIIe siècle', NULL, 'égal', 15, 16, 'zvYl1E6Bmc80RLNT.jpg', NULL),
(116, 3, 'Maine-et-Loire (49)', 'Baugé', 'Église Saint-Laurent', 'Grand orgue', 'Tribune au fond de la nef', 'Maillard (1642)', 'Bonn (1850)', 'Benoist-Sarelot (1975)', NULL, NULL, NULL, NULL, NULL, 'Maillard 1642', NULL, 'égal', 15, 20, 'cYobMB9AxOpLbRQI.jpg', 'Inventaire national'),
(117, 3, 'Vendée (85)', 'La Roche-sur-Yon', 'Conservatoire à Rayonnement Départemental', 'Orgue d\'étude', 'au sol, salle d\\\'orgue', 'Fouss (2018)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Fouss', '440', '', 15, 4, 'g7ID93bAevjjqB7y.jpg', 'CRD'),
(118, 3, 'Loire-Atlantique (44)', 'La Bernerie-en-Retz', 'Église Notre-Dame-de-Bon-Secours', 'Grand orgue', 'Tribune au fond de la nef', 'Debierre (1880)', 'Renaud (1989-98)', NULL, NULL, NULL, NULL, NULL, NULL, 'Debierre', NULL, 'égal', 15, 26, '3Ce2fxWORNSMbavj.jpg', 'Roger Martin'),
(119, 3, 'Loire-Atlantique (44)', 'La Chapelle-sur-Erdre', 'Église Sainte-Catherine ', 'Grand orgue', 'tribune dans le transpet sud', 'Walker (1967)', 'Hurvy (2011)', NULL, NULL, NULL, NULL, NULL, NULL, 'Walcker 1967', '440', '', 32, 24, 'BJgoDcqvmmpvbQna.jpg', 'J.-François Maisonneuve'),
(120, 3, 'Loire-Atlantique (44)', 'La Chapelle-sur-Erdre', 'Domicile privé', 'Orgue de salon', 'au sol', 'Koenig (1988)', 'Hurvy (2016)', NULL, NULL, NULL, NULL, NULL, NULL, 'Koenig 1988', '440', '', 32, 12, 'Dmo83NcXGps3RVQq.jpg', 'Jean-François Maisonneuve'),
(121, 3, 'Sarthe (72)', 'Le Lude', 'Eglise St-Vincent', 'Grand orgue', 'Tribune au fond de la nef', 'Debierre (1895)', 'Conan (1992)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'égal', 15, 12, 'YnvBjXK2LXHRtGYB.jpg', 'Gwillerm Poullennec'),
(122, 2, 'Maine-et-Loire (49)', 'Saint Macaire en Mauges (Sèvremoine)', 'Eglise Saint Macaire', 'Grand orgue', 'Tribune', 'Gloton-Debierre (1925)', 'Nicolas Toussaint MGBO (2019)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 30, 22, NULL, 'Etienne Ouvrard'),
(123, 3, 'Vendée (85)', 'Pouzauges', 'Eglise Saint-Jacques', 'Grand orgue', 'sol, bas-côté nord de la nef', 'Bonn (1856-1866)', 'Debierre (1909)', 'Gloton-Debierre (1935)', 'Chevron (2004)', NULL, NULL, NULL, NULL, NULL, '440', 'égal', 30, 18, 'dHlZcrbmi4gEAsIS.jpg', 'Etienne Ouvrard'),
(124, 3, 'Maine-et-Loire (49)', 'Saint-Georges-sur-Loire', 'Église Saint-Georges', 'Grand orgue', 'Tribune, fond de la nef', 'Cavaillé-Coll (1874)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 30, 7, 'b514DZX3odD3RgLK.jpg', 'Etienne Ouvrard'),
(125, 3, 'Vendée (85)', 'Saint-Laurent-sur-Sèvre', 'Basilique Saint Louis-Marie Grignion de Montfort', 'Grand orgue', 'sol, au fond du transept sud', 'Formentelli (1987-1998)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 30, 47, 'rRk5r2AZ2xkmOJSW.jpg', 'FFAO'),
(126, 3, 'Maine-et-Loire (49)', 'Torfou', 'Église Saint-Martin', 'Grand orgue', 'sol, transept sud', 'Debierre (1880)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 30, 13, 'XFvy0wiAxJx4NDAI.jpg', 'Etienne Ouvrard'),
(127, 3, 'Maine-et-Loire (49)', 'Saumur', 'Église Notre-Dame-des-Ardilliers', 'Orgue de chœur', 'Sol, deuxième travée de la nef côté sud', 'Bonn (1850)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 15, 7, 'QJCMuqTDl6oehSlM.jpg', 'Philippe Humeau'),
(128, 3, 'Loire-Atlantique (44)', 'Nantes', 'Domicile privé', 'Orgue de salon', 'salon, au sol', 'Birouste (1987)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '435', 'égal', 15, 2, '7D3t3d9jZ88ps7WY.jpg', 'Philippe Humeau'),
(129, 1, NULL, NULL, NULL, 'NOUVEL INSTRUMENT', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(130, 3, 'Maine-et-Loire (49)', 'Montreuil-Bellay', 'Collégiale Notre-Dame', 'Grand orgue', 'Tribune au fond de la nef', 'Bonn (1852 ?)', '', NULL, NULL, NULL, NULL, NULL, NULL, 'Bonn', NULL, 'égal', 15, 16, 'R2KxfU7tkPNSUCJG.jpg', ''),
(131, 3, 'Mayenne (53)', 'Laval', 'Église Saint-Vénérand', 'Grand orgue', 'Tribune au fond de la nef', 'Lefebvre (XVIIIe s.)', 'Debierre (1893)', NULL, NULL, NULL, NULL, NULL, NULL, 'Debierre (1893)', NULL, NULL, 15, 33, 'h1RwDUQdmNbZ2n58.jpg', NULL),
(132, 3, 'Mayenne (53)', 'Laval', 'Notre-Dame-d\'Avesnières', 'Ancien orgue', 'ancienne église de Torcé-Viviers', 'Lusson (1590)', '', NULL, NULL, NULL, NULL, NULL, NULL, 'Jean Dubois (1590)', NULL, NULL, 15, NULL, 'UybHWA77YTvsLohd.jpg', 'ARCAMC'),
(133, 3, 'Mayenne (53)', 'Laval', 'Notre-Dame-d\'Avesnières', 'Grand orgue', 'Tribune au fond de la nef', 'Debierre (1895)', 'Lambert (1965)', NULL, NULL, NULL, NULL, NULL, NULL, 'Debierre (1985)', '432', 'égal', 15, 25, 'MkQY53nNAkiNkNKw.jpg', NULL),
(134, 3, 'Loire-Atlantique (44)', 'Nantes', 'Domicile privé', 'Orgue de salon', 'au sol', 'Birouste (2018)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Birouste 2019', '440', 'égal', 16, 1, 'DhQKaQQPzW99Cqza.jpg', 'Martine Rochedreux'),
(135, 3, 'Maine-et-Loire (49)', 'Béhuard', 'Église Saint-Martin', 'Orgue polyphone', 'au sol, près de l\'autel', 'Debierre (1912)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 30, 5, 'px8LFnNSfrSL94ZX.jpg', 'Etienne Ouvrard'),
(136, 3, 'Maine-et-Loire (49)', 'Le May-sur-Evre', 'Eglise Saint Michel', 'Orgue polyphone', 'au sol, transept gauche', 'Beuchet-Debierre (1960)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 30, 7, '3s6giXznnKNHzyTu.jpg', 'Etienne Ouvrard'),
(137, 3, 'Maine-et-Loire (49)', 'Chemillé', 'Eglise Saint-Pierre', 'Orgue polyphone', 'au sol, dans le transept nord', 'Debierre (1912)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'egal', 30, 6, 'VvBietERqkZjzHcO.jpg', 'Etienne Ouvrard'),
(138, 3, 'Loire-Atlantique (44)', 'Pornichet', 'Église Notre-Dame-des-Dunes', 'Grand orgue', 'Au sol, transept gauche', 'Delhumeau (2013)', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'Vallotti', 1, 16, 'w5fJOBSZ7JaEG0ZT.jpg', 'Marie-Andrée Courjault'),
(139, 2, 'Loire-Atlantique (44)', 'Saint-Nazaire', 'Église de l\'Immaculée', 'Orgue de chœur', 'sol, au fond du transept nord', 'Mutin', 'Beuchet-Debierre (1961)', '', '', NULL, NULL, NULL, NULL, NULL, '440', 'égal', 1, 9, 'EwaXrS9B6jzTvO9X.jpg', 'Marie-Andrée Courjault'),
(140, 2, 'Loire-Atlantique (44)', 'Saint-André-des-Eaux', 'Eglise Saint-André', 'Orgue de chœur', 'sol, au fond du chœur', 'Lelogeais (1860)', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 1, 8, '8saPxVJqMSRmXZMV.jpg', 'Marie-Andrée Courjault'),
(141, 3, 'Loire-Atlantique (44)', 'Saint-Nazaire', 'Église Notre-Dame d\'Espérance', 'Grand orgue', 'Tribune au fond de la nef', 'Lacorre et Robert (2004)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Lacorre et Robert 2004', '440', 'égal', 1, 7, 'v4a9n5tHXYwIYtf4.jpg', 'Marie-Andrée Courjault'),
(142, 2, 'Loire-Atlantique (44)', 'Saint-Nazaire', 'Église Saint-Gohard', 'Grand orgue', 'au sol, au fond du chœur', 'Beuchet-Debierre (1955)', '', NULL, NULL, NULL, NULL, NULL, NULL, 'Beuchet-Debierre 1955', '440', 'égal', 1, 0, 'kDGEDCq3fHEXjfCt.jpg', 'Marie-Andrée Courjault'),
(143, 2, 'Loire-Atlantique (44)', 'Saint-Nazaire', 'Église Saint-Nazaire', 'Grand orgue', 'Au sol, transept nord', 'Beuchet (1956)', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 1, 19, 'mCp7lDL7Jmnv8WBg.', 'Marie-Andrée Courjault'),
(144, 2, 'Loire-Atlantique (44)', 'Saint-Nazaire', 'Église Sainte-Anne', 'Grand orgue', 'Tribune au fond de la nef', 'Bouvet (1960)', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 1, 20, 'lCYdkUd8dUtTslYx.jpg', 'Marie-Andrée Courjault'),
(145, 2, 'Loire-Atlantique (44)', 'Saint-Nazaire', 'Église Saint-Joseph-de-Méan', 'Orgue polyphone', 'au sol, dans le chœur', 'Debierre (1899)', '', '', NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 1, 6, NULL, NULL),
(146, 3, 'Loire-Atlantique (44)', 'Vallet', 'Église Notre-Dame', 'Grand orgue', 'sol, au fond du chœur', 'Le Logeais (1857)', 'Debierre (1875)', 'Renaud (1981-1994)', NULL, NULL, NULL, NULL, NULL, 'Renaud 1981', '440', 'égal', 15, 20, 'hLq8jUcIhNd3lOtP.jpg', 'Philippe Humeau'),
(147, 3, 'Sarthe (72)', 'Le Mans', 'Cathédrale St-Julien', 'Orgue de chœur', 'sol, première travée du chœur côté nord', 'Ducroquet (1854)', 'Abbé Tronchet (1912)', 'Chéron (1957)', 'Benoist-Sarélot (1973)', NULL, NULL, NULL, NULL, 'Ducroquet 1854', '440', 'égal', 15, 17, '3y99qKpJHeNeCsOG.jpg', NULL),
(148, 3, 'Loire-Atlantique (44)', 'Nort-sur-Erdre', 'Eglise Saint-Christophe', 'Orgue de chœur', 'sol, déambulatoire derrière l\'autel', 'Cavaillé-Coll (1884)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Cavaillé-Coll 1884', NULL, 'égal', 15, 14, 'icUhNftG3V3RqzoB.jpg', 'Les Amis de l\'Orgue'),
(149, 1, NULL, NULL, NULL, 'NOUVEL INSTRUMENT', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 34, NULL, NULL, NULL),
(150, 2, 'Maine-et-Loire (49)', 'Le Marillais', 'Sanctuaire Notre-Dame', 'Grand Orgue', 'Tribune', 'Schreder', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 30, 15, NULL, 'Hugo Guitierrez'),
(151, 3, 'Vendée (85)', 'Saint-Hilaire-de-Riez', 'Eglise St-Hilaire', 'Orgue de chœur', 'sol, transept sud', 'Birouste (2020)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Birouste 2020', '440', 'égal', 15, 3, '7SehPXQ3DqcwgRQH.jpg', 'Philippe Humeau'),
(152, 2, 'Maine-et-Loire (49)', 'Tillières', 'Eglise Saint Pierre', 'Orgue de choeur', 'Transept nord', 'Louis Debierre (1904)', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '440', 'égal', 30, 5, '26z7OKmYykG2Ctlx.jpg', 'François Chaillou');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `inventaire_renseignements`
--
ALTER TABLE `inventaire_renseignements`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `inventaire_renseignements`
--
ALTER TABLE `inventaire_renseignements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=153;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
