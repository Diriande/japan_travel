# Voyage au Japon - 3 semaines (21 jours)

Compilation de préparation pour un voyage au Japon de 3 semaines, pour **2 ou 3 personnes**, avec un lit garanti pour chacun (chambres twin/triple ou lits d'appoint).

## Hypothèses de départ

- **Durée** : 21 jours / 19 nuits sur place (J1 et J21 = jours de vol)
- **Voyageurs** : 2 ou 3 personnes (le dashboard permet de basculer entre les deux)
- **Saison de référence** : mi-saison type avril (sakura) ou novembre (momiji) — haute saison, donc tarifs plutôt hauts. Hors de ces périodes, compter 15-25% de moins sur vols et hébergement.
- **Vols** : Finnair, Paris-Helsinki-Tokyo, 2x23kg en soute inclus, ~1000€ A/R par personne (hypothèse utilisateur)
- **Devise** : 1 EUR ≈ 160-165 JPY (à vérifier au moment de la réservation)

⚠️ Tous les tarifs sont des **estimations 2025/2026 à vérifier** avant réservation (prix des transports, musées et vols évoluent).

## Structure du repo

- `01_vols/` — vols internationaux Finnair + alternatives
- `02_transport/` — JR Pass vs billets à l'unité, IC card, trajets Shinkansen
- `03_hebergement/` — hôtels/ryokans par étape, avec tarifs chambre 2 pers / 3 pers
- `04_itineraire/` — programme jour par jour, découpé par étape géographique
- `05_activites/` — liste des activités et visites par ville, avec tarifs
- `06_budget/` — budgets totaux consolidés pour 2 et 3 personnes
- `07_pratique/` — visa, argent, eSIM, assurance, bagages
- `data/` — fichiers JSON sources (repris par le dashboard)
- `dashboard/index.html` — **dashboard interactif** : sélectionne le nombre de voyageurs, les hébergements, les activités par ville, et calcule le budget total en direct

## Utiliser le dashboard

Ouvrir `dashboard/index.html` dans un navigateur (aucune connexion internet requise, tout est autonome). Il permet de :
- choisir 2 ou 3 voyageurs
- cocher/décocher les activités par ville pour ajuster le budget
- changer le tarif du vol (par défaut 1000€/pers)
- voir le budget total et par personne se recalculer en direct
- visualiser la répartition du budget par poste (vols, hébergement, transport, activités, nourriture, divers)

## Budget total indicatif

Hébergement visé en business hotel économique (type Toyoko Inn/R&B Hotel/APA Hotel), avec deux formules possibles :

| | 2 personnes | 3 personnes |
|---|---|---|
| **Chambre partagée** (type Riverside Shinjuku) — total | ~7155€ | ~10469€ |
| Chambre partagée — par personne | ~3578€ | ~3490€ |
| **Chambre individuelle** (type R&B Hotel Ueno-Hirokoji) — total | ~7872€ | ~11808€ |
| Chambre individuelle — par personne | ~3936€ | ~3936€ |

Détail dans `06_budget/`. Le dashboard recalcule ces montants en direct selon les choix faits (activités, formule d'hébergement, voiture de location, prix du vol).

## Itinéraire en un coup d'oeil

Tokyo (5 nuits) → Hakone (1 nuit) → Kyoto (5 nuits, excursions Nara + Osaka) → Hiroshima (2 nuits, excursion Miyajima) → Kanazawa (2 nuits) → Takayama (1 nuit, excursion Shirakawa-go) → Tokyo (3 nuits) → retour

Détail complet dans `04_itineraire/`.
