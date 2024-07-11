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

### Fichier XML

Ces des fichiers historiques qui datent de 2018 à 2020. Ces fichiers  ne sont pas as autoporteurs. Il doivent être interprétés à l’aide de données référentielles qui permettent la caractérisation précise de la mesure : localisation de la station, typologie de la station et du point de prélèvement, méthode de mesure utilisée, dates de fonctionnement… Ces informations sont contenues dans deux fichiers annexes, également téléchargeables sur le site et nommés « dataset B » et « dataset D ».*

Pour lire et extraires les données à partir de ces fichiers en structure XML, nous avons utilisé un job talend.















