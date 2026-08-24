# Carnet du Japon

Un document HTML unique qui tient les trois itinéraires : à lire avant de partir,
à remplir pendant. Il s'ouvre en double-cliquant `index.html`, ne demande aucun
réseau une fois les fontes en cache, et garde tout dans le navigateur.

## Ce qu'il contient

| Vue | À quoi elle sert |
|---|---|
| Le voyage | Les chiffres, les réservations qui restent, les étapes en vitrine, la carte, le budget prévu |
| Jour par jour | Les 52 journées des trois trames, dépliables, avec horaires, coûts et notes |
| Carte | Le tracé, les excursions, les vols d'arrivée et de départ |
| Budget | Prévu contre saisi, par poste et par étape, avec saisie rapide |
| Réservations | Dans l'ordre où il faut s'en occuper, les bloquantes en rouge |
| Valise | Une liste pensée pour trois semaines en mai-juin, ville et montagne |
| Carnet | Un bloc libre, plus le rappel des notes de chaque journée |

## Reconstruire

```
python3 carnet/outils/build.py
```

Il faut `node` sur le chemin : les cartes sont produites par
`itineraires/outils/genmap.js`, appelé en sous-processus.

## Les fichiers

- `outils/trames.py` — **le contenu**. Les trois itinéraires, journée par journée,
  avec leurs étapes, leurs réservations et leurs postes de budget. C'est ici qu'on
  écrit. Les coûts sont en yens et par personne.
- `outils/scenes.py` — les bandeaux de paysage, en aplats générés. Pas de
  photographie : des crêtes tirées d'un générateur à graine fixe, une silhouette
  par étape (torii, gassho, pagode, vague, volcan, tour, cascade) et un ciel
  dégradé. Même graine, même dessin d'un build à l'autre.
- `outils/shell.py` — les styles et le gabarit du document.
- `outils/app.js` — le moteur : rendu des vues, état, sauvegarde.
- `outils/build.py` — assemble le tout, plus la liste de valise et les dépenses
  rapides.

## Ce qu'il faut savoir

- **Le total du budget se calcule**, il ne se saisit pas. `par_pers` est la somme
  des postes : les deux ne peuvent plus diverger, ce qui était le cas avant
  (2 972 € annoncés pour 2 955 € de postes).
- **La sauvegarde a deux voies.** Le bouton propose un téléchargement *et* le
  texte à copier, parce qu'une page publiée en Artifact voit ses téléchargements
  bloqués par le bac à sable. Le même bouton recharge, par fichier ou par texte.
- **Les journées de Kyoto sont écrites une fois** et reprises par les trois
  trames via `repris()`, avec renumérotation. Corriger Nara les corrige toutes.
- Les couleurs de carte (`--m-*`) doivent rester définies dans les trois blocs de
  thème de `shell.py`, sinon les tracés d'excursion redeviennent invisibles.
