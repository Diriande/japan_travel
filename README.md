# Voyage au Japon - Alpes japonaises, 2 à 3 semaines

Compilation de préparation pour un voyage au Japon, pour **2 ou 3 personnes**, avec un lit garanti pour chacun (chambres partagées ou individuelles). Itinéraire centré sur Tokyo, le Mont Fuji, Hakone et les Alpes japonaises (Gifu, Gero Onsen, Takayama, Kanazawa), en évitant le Kansai (Kyoto/Osaka/Nara) déjà visité.

## Hypothèses de départ

- **Durée** : 3 semaines par défaut (21 jours / 19 nuits sur place), avec une version condensée à 2 semaines (14 jours / 12 nuits) — les deux sont sélectionnables dans le dashboard
- **Voyageurs** : 2 ou 3 personnes (le dashboard permet de basculer entre les deux ; l'incertitude porte sur la participation d'un des deux parents)
- **Saison de référence** : mi-saison type avril (sakura) ou novembre (momiji) — haute saison, donc tarifs plutôt hauts. Hors de ces périodes, compter 15-25% de moins sur vols et hébergement.
- **Vols** : Finnair, Paris-Helsinki-Tokyo, 2x23kg en soute inclus, ~1000€ A/R par personne (hypothèse utilisateur)
- **Devise** : 1 EUR ≈ 160-165 JPY (à vérifier au moment de la réservation)

⚠️ Tous les tarifs sont des **estimations 2025/2026 à vérifier** avant réservation (prix des transports, musées et vols évoluent).

## Structure du repo

- `01_vols/` — vols internationaux Finnair + alternatives
- `02_transport/` — JR Pass vs billets à l'unité, IC card, trajets longue distance, option voiture de location
- `03_hebergement/` — hôtels/ryokans par étape, avec tarifs chambre individuelle / partagée
- `04_itineraire/` — programme jour par jour, découpé par étape géographique
- `05_activites/` — liste des activités et visites par ville, avec tarifs et alternatives sans vertige
- `06_budget/` — budgets totaux consolidés pour 2 et 3 personnes
- `07_pratique/` — visa, argent, eSIM, assurance, bagages
- `data/` — fichiers JSON sources (repris par le dashboard)
- `dashboard/index.html` — **dashboard interactif** : sélectionne la durée, le nombre de voyageurs, la formule d'hébergement, les activités par ville, et calcule le budget total en direct

## Utiliser le dashboard

Ouvrir `dashboard/index.html` dans un navigateur (aucune connexion internet requise, tout est autonome). Il permet de :
- choisir 2 ou 3 voyageurs
- choisir la durée (preset 2 ou 3 semaines, ou ajuster le nombre de nuits ville par ville)
- choisir la formule d'hébergement (chambre partagée ou individuelle)
- activer/désactiver l'option voiture de location (Takayama → Kanazawa, via Gokayama/Hida Furukawa)
- cocher/décocher les activités par ville pour ajuster le budget
- modifier les hypothèses de coût (nourriture, transport local, trajets longue distance, divers) dans la section dédiée
- voir le budget total et par personne se recalculer en direct, avec la répartition par poste

## Budget total indicatif (version 3 semaines, 19 nuits)

Hébergement visé en business hotel économique (type Toyoko Inn/R&B Hotel/APA Hotel), avec deux formules possibles :

| | 2 personnes | 3 personnes |
|---|---|---|
| **Chambre partagée** (type Riverside Shinjuku) — total | ~7078€ | ~10347€ |
| Chambre partagée — par personne | ~3539€ | ~3449€ |
| **Chambre individuelle** (type R&B Hotel Ueno-Hirokoji) — total | ~7794€ | ~11691€ |
| Chambre individuelle — par personne | ~3897€ | ~3897€ |

Détail dans `06_budget/`. Le dashboard recalcule ces montants en direct selon les choix faits (durée, activités, formule d'hébergement, voiture de location, prix du vol, hypothèses de coût).

## Itinéraire en un coup d'oeil

Tokyo (8 nuits, arrivée + retour) → Kamakura (excursion d'une journée) → Kawaguchiko/Fuji Five Lakes (2 nuits) → Hakone (1 nuit) → Nagoya & Gifu (2 nuits) → Gero Onsen (1 nuit) → Takayama & Shirakawa-go (2 nuits) → Kanazawa (3 nuits) → retour direct à Tokyo en Shinkansen

Détail complet dans `04_itineraire/`.

## Piste à explorer plus tard

Une variante plus économique centrée sur le Kansai (Osaka/Kyoto/Nara/Kobe/Wakayama) a été évoquée mais mise de côté pour l'instant au profit de cette version Alpes japonaises. À reprendre dans une itération séparée si besoin.
