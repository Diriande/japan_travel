# Voyage au Japon - 2 à 3 semaines, deux variantes

Compilation de préparation pour un voyage au Japon, pour **2 ou 3 personnes**, avec un lit garanti pour chacun (chambres partagées ou individuelles). Deux itinéraires complets sont disponibles, sélectionnables directement dans le dashboard :

| Variante | Dossiers | Esprit |
|---|---|---|
| **Alpes japonaises** (par défaut) | `01_vols/` à `07_pratique/` à la racine | Tokyo, Mont Fuji, Hakone, Nagoya/Gifu, Gero Onsen, Takayama/Shirakawa-go, Kanazawa - grand tour vers l'ouest, en évitant le Kansai (déjà visité) |
| **Kanto économique** | `variante_kanto_economique/` | Tokyo en base, excursions vers Kamakura/Enoshima, Yokohama, Kawaguchiko/Hakone, Chichibu, Chiba (Nokogiriyama) - priorité temples/randonnée/découverte/nourriture, nettement moins cher (pas de Shinkansen) |

`01_vols/` et `07_pratique/` (visa, argent, eSIM, assurance, bagages) sont communs aux deux variantes.

## Hypothèses de départ (communes aux deux variantes)

- **Durée** : 3 semaines par défaut (21 jours / 19 nuits sur place), avec une version condensée à 2 semaines (12 nuits) — sélectionnables dans le dashboard
- **Voyageurs** : 2 ou 3 personnes (l'incertitude porte sur la participation d'un des deux parents)
- **Saison de référence** : mi-saison type avril (sakura) ou novembre (momiji) — haute saison, donc tarifs plutôt hauts. Hors de ces périodes, compter 15-25% de moins sur vols et hébergement.
- **Vols** : Finnair, Paris-Helsinki-Tokyo, 2x23kg en soute inclus, ~1000€ A/R par personne (hypothèse utilisateur)
- **Devise** : 1 EUR ≈ 160-165 JPY (à vérifier au moment de la réservation)

⚠️ Tous les tarifs sont des **estimations 2025/2026 à vérifier** avant réservation.

## Structure du repo

- `01_vols/` — vols internationaux Finnair + alternatives (commun)
- `07_pratique/` — visa, argent, eSIM, assurance, bagages (commun)
- `02_transport/`, `03_hebergement/`, `04_itineraire/`, `05_activites/`, `06_budget/`, `data/` — contenu de la variante **Alpes japonaises**
- `variante_kanto_economique/` — contenu complet de la variante **Kanto économique** (même structure interne : hébergement, itinéraire, activités, budget, données)
- `dashboard/index.html` — **dashboard interactif unique** couvrant les deux variantes : sélecteur de variante, durée, voyageurs, hébergement, activités, budget en direct

## Utiliser le dashboard

Ouvrir `dashboard/index.html` dans un navigateur (aucune connexion internet requise, tout est autonome). Il permet de :
- choisir la **variante** (Alpes japonaises / Kanto économique)
- choisir 2 ou 3 voyageurs
- choisir la durée (preset 2 ou 3 semaines, ou ajuster le nombre de nuits ville par ville)
- choisir la formule d'hébergement (chambre partagée ou individuelle)
- activer/désactiver l'option voiture de location (variante Alpes uniquement : Takayama → Kanazawa, via Gokayama/Hida Furukawa)
- cocher/décocher les activités par ville pour ajuster le budget
- modifier les hypothèses de coût (nourriture, transport local, trajets longue distance, divers) dans la section dédiée
- voir le budget total et par personne se recalculer en direct, avec la répartition par poste

## Budget total indicatif (version 3 semaines, 19 nuits, formule partagée)

| | 2 personnes | 3 personnes |
|---|---|---|
| **Alpes japonaises** — total / par pers. | ~7078€ / ~3539€ | ~10347€ / ~3449€ |
| **Kanto économique** — total / par pers. | ~6608€ / ~3304€ | ~9647€ / ~3216€ |

La variante Kanto économise ~500-760€ au total, principalement grâce à l'absence de Shinkansen et à moins de nuits hors de Tokyo. Détail dans `06_budget/` et `variante_kanto_economique/06_budget/`.

## Itinéraires en un coup d'oeil

**Alpes japonaises** : Tokyo (8 nuits, arrivée + retour) → Kamakura (excursion) → Kawaguchiko/Fuji (2 nuits) → Hakone (1 nuit) → Nagoya & Gifu (2 nuits) → Gero Onsen (1 nuit) → Takayama & Shirakawa-go (2 nuits) → Kanazawa (3 nuits) → retour direct Tokyo en Shinkansen. Détail dans `04_itineraire/`.

**Kanto économique** : Tokyo (14 nuits, base) → Kamakura & Enoshima (2 nuits) → Yokohama (excursion) → Kawaguchiko/Fuji (1 nuit) → Hakone (1 nuit) → Chichibu (excursion) → Nokogiriyama/Chiba (excursion) → Narita (1 nuit, avant le vol). Détail dans `variante_kanto_economique/04_itineraire/`.

## Piste à explorer plus tard

Une variante encore plus économique centrée sur le Kansai (Osaka/Kyoto/Nara/Kobe/Wakayama) a été évoquée mais mise de côté pour l'instant. À reprendre dans une itération séparée si besoin.
