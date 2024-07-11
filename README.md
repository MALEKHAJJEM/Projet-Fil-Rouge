# Projet-File-Rouge
Surveillance et Prédiction de la qualité de l’air dans la Région Auvergne-Rhône-Alpes​

Dans le cadre d'une formation aux métiers de « data analyst » sur une période de 3 mois, notre équipe a pris  en charge la réalisation du cas d’usage opérationnel des données. 
L'equipe est composée 3 stagaires, "Data Analysts juniors", disposant de compétences sur la gestion des bases de données, la création de dashboards (datavisualisation), et la conceptualisation des modèles de machine learning.

Pendant 8 semaines on s’est lancée dans une démarche pédagogique et expérimentale sur la réalisation d’un prototype de réutilisation de données présentes en open data.  
Cette démarche vise à présenter des leviers d’amélioration de la qualité de l’air avec  :

-Un dashboard sur la qualité de l’air en Auvergne Rhonalpes, entre 2018 et 2024.
-Un modèle de machine learning (Régression et classification).

## Source de données
### Fichier CSV
Les données ont été colléctés à partir de [https://www.data.gouv.fr/fr/datasets/donnees-temps-reel-de-mesure-des-concentrations-de-polluants-atmospheriques-reglementes-1/].

Un premier Script applé scraping_data sert à télécharger les fichier csv en local. Ces données CSV sont des données relatievement récents qui date de 2021 à 2024.
Ces données d’observation accessibles sur le site [http://data.gouv.fr] sont issues de la surveillance réglementaire de la qualité de l’air. Elles décrivent les concentrations moyennes horaires des polluants réglementés surveillés par des appareils de mesure automatiques installés sur des stations fixes.

Exemple de ficheirs CSV: 


```
Date de début;Date de fin;Organisme;code zas;Zas;code site;nom site;type d'implantation;Polluant;type d'influence;discriminant;Réglementaire;type d'évaluation;procédure de mesure;type de valeur;valeur;valeur brute;unité de mesure;taux de saisie;couverture temporelle;couverture de données;code qualité;validité
2021/10/22 00:00:00;2021/10/22 01:00:00;ATMO GRAND EST;FR44ZAG02;ZAG METZ;FR01011;Metz-Centre;Urbaine;NO;Fond;A;Oui;mesures fixes;Auto NO Conf meth CHIMILU;moyenne horaire validée;1.1;1.1;µg-m3;;;;A;1
2021/10/22 01:00:00;2021/10/22 02:00:00;ATMO GRAND EST;FR44ZAG02;ZAG METZ;FR01011;Metz-Centre;Urbaine;NO;Fond;A;Oui;mesures fixes;Auto NO Conf meth CHIMILU;moyenne horaire validée;0.8;0.8;µg-m3;;;;A;1
2021/10/22 02:00:00;2021/10/22 03:00:00;ATMO GRAND EST;FR44ZAG02;ZAG METZ;FR01011;Metz-Centre;Urbaine;NO;Fond;A;Oui;mesures fixes;Auto NO Conf meth CHIMILU;moyenne horaire validée;;;µg-m3;;;;N;-1
2021/10/22 03:00:00;2021/10/22 04:00:00;ATMO GRAND EST;FR44ZAG02;ZAG METZ;FR01011;Metz-Centre;Urbaine;NO;Fond;A;Oui;mesures fixes;Auto NO Conf meth CHIMILU;moyenne horaire validée;1.7;1.7;µg-m3;;;;A;1
2021/10/22 04:00:00;2021/10/22 05:00:00;ATMO GRAND EST;FR44ZAG02;ZAG METZ;FR01011;Metz-Centre;Urbaine;NO;Fond;A;Oui;mesures fixes;Auto NO Conf meth CHIMILU;moyenne horaire validée;2.7;2.725;µg-m3;;;;A;1
2021/10/22 05:00:00;2021/10/22 06:00:00;ATMO GRAND EST;FR44ZAG02;ZAG METZ;FR01011;Metz-Centre;Urbaine;NO;Fond;A;Oui;mesures fixes;Auto NO Conf meth CHIMILU;moyenne horaire validée;11.1;11.05;µg-m3;;;;A;1
2021/10/22 06:00:00;2021/10/22 07:00:00;ATMO GRAND EST;FR44ZAG02;ZAG METZ;FR01011;Metz-Centre;Urbaine;NO;Fond;A;Oui;mesures fixes;Auto NO Conf meth CHIMILU;moyenne horaire validée;7.9;7.9;µg-m3;;;;A;1
```



### Fichier XML

Ces des fichiers historiques qui datent de 2018 à 2020. Ces fichiers  ne sont pas as autoporteurs. Il doivent être interprétés à l’aide de données référentielles qui permettent la caractérisation précise de la mesure : localisation de la station, typologie de la station et du point de prélèvement, méthode de mesure utilisée, dates de fonctionnement… Ces informations sont contenues dans deux fichiers annexes, également téléchargeables sur le site et nommés « dataset B » et « dataset D ».*

Pour lire et extraires les données à partir de ces fichiers en structure XML, nous avons utilisé un job [talend parent](https://github.com/MALEKHAJJEM/Projet-File-Rouge/blob/main/image/Job%20parant.png).


Ce job commence par :


-  Récupérer la liste des fichiers : tfileFetch : le but est de télécharger la liste de tous les fichiers d'une année donnée à partir de [https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/old/].
*  Faire une pause le temps de faire une manipulation manuel pour enlever la balise "hr" qui bloque Talend.
+ Lecture 2020.xml ligne par ligne (chaque <a>) (les nom des fichier xml): TfileinputXML
- Stocker l'URL dans une variable à l'aide tjavaRow1( on garde que les fichier verifier)
- Télécharger les fichiers (tFileFetch) permet de télécharger fichier par fichier à partir des liste.


This site was built using [GitHub Pages](https://pages.github.com/).





