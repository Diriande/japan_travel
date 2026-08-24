# Génération des cartes

`genmap.js` produit une carte SVG statique cadrée sur les étapes d'un itinéraire, à partir du
fond de carte du planificateur (`dashboard/itineraire.html`).

- `mapdata.json` — trait de côte Natural Earth 10 m simplifié, lacs, rivières, et la projection.
  Extrait du planificateur, à régénérer si celui-ci change.
- `places-min.json` — coordonnées des lieux utilisés dans les itinéraires.

## Vols

`buildMap(steps, excursions, { flights: { in: "KIX", out: "FUK" } })` place les aéroports d'arrivée et
de départ, avec un trait qui sort du cadre. Codes disponibles : KIX, FUK, HND, NRT.

## Enveloppe HTML

Les pages du dépôt sont des documents complets, avec `<!doctype html>` — sans quoi le navigateur les
ouvre en mode quirks et le rendu casse en local. Le publish d'Artifact fournissant sa propre enveloppe,
`strip.js` produit la version publiable :

```
node itineraires/outils/strip.js itineraires/trois-villes.html /tmp/pub.html
```

## Usage

```js
const { buildMap } = require("./genmap.js");
const svg = buildMap(
  [{ id: "kyoto", nights: 5 }, { id: "kanazawa", nights: 5, anchor: "w" }],
  [{ from: "kanazawa", to: "shirakawago" }]     // excursions, tracées en boucle
);
```

`anchor` place l'étiquette (`n`, `s`, `e`, `w`) quand deux villes se chevauchent. Le cadrage et la
taille des repères s'adaptent automatiquement à l'emprise des étapes.

Les couleurs viennent de tokens `--m-*` que la page hôte doit définir, en clair et en sombre.
