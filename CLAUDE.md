# Voyage Japon

Dossier de préparation d'un voyage à trois (moi + mes parents), mi-mai à mi-juin, 3 semaines.
Documents en français. Montants en €, toujours datés et sourcés.

## Contraintes du voyage

- 3 voyageurs, **un lit par personne** (un lit double pour deux, c'est bon) — chambre à trois OK
- Plafond **3 000 € par personne**, tout compris
- **Okinawa exclue**. Déjà vus : Tokyo, Kansai, Fuji, Matsumoto. Jamais vus : Kanazawa, Toyama,
  Shirakawa-go, Kyushu, Tohoku
- Thèmes : paysages (montagne, cascades), table, artisanat, vie d'autrefois
- Préférence pour **peu d'étapes, longtemps** — une base de 4-5 nuits vaut mieux que trois d'une nuit
- La montagne est une préférence, pas une obligation : elle coûte cher en hébergement

## Chiffrer un itinéraire

- Le graphe de liaisons est dans `dashboard/itineraire.html` (const `EDGES`, `route()`) : durées et
  prix réels par personne. Extraire le `<script>` et l'évaluer pour chiffrer une trame.
- Hypothèses : 40 €/jour/pers de nourriture, 7 €/jour de transport local, 300 €/pers de divers
- Hébergement : `lodge[2]` = chambre à trois. Montagne 145-210 €, ville 76-98 € — c'est là que se
  joue l'écart entre deux itinéraires

## Pages HTML

- Les pages du dépôt sont des **documents complets avec `<!doctype html>`** — sans quoi le navigateur
  les ouvre en mode quirks et le rendu casse en local
- Pour publier en Artifact : `node itineraires/outils/strip.js <src> <dst>` retire l'enveloppe
- Cartes : `node itineraires/outils/genmap.js`, voir son README
- Tokens de couleur en clair **et** sombre, définis sur `:root` nu

## Vérifier une information de voyage

- **Les franchises bagages des sites agrégateurs sont fausses.** Vérifier sur le tunnel de
  réservation ou la page officielle de la compagnie. Marquer vérifié / non vérifié dans les tableaux
- **Kiwi.com et les comparateurs vendent du billet d'agence** : 274 € d'écart constaté sur un même
  vol Finnair. Ils situent les saisons entre elles, pas les prix atteignables
- Ne jamais présenter deux données avec le même niveau de confiance si l'une est vérifiée et l'autre non

## Pièges rencontrés dans le planificateur

- `setPointerCapture` sur le `<svg>` détourne les clics de ses enfants : gérer le pan par des
  écouteurs sur `window`, sans capture
- Un conteneur en `display:flex` disloque le texte riche — chaque `<b>` devient un flex item
- Douglas-Peucker sur un anneau fermé dégénère (premier et dernier point identiques) : couper
  l'anneau en deux avant de simplifier

## Git

- Remote en **HTTPS** (`gh auth git-credential`), pas SSH : aucune clé n'est enregistrée sur le compte
- `main` est la branche par défaut : brancher avant de commiter, PR puis merge
