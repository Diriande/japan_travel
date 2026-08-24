# Génération des cartes

`genmap.js` produit une carte SVG statique cadrée sur les étapes d'un itinéraire, à partir du
fond de carte du planificateur (`dashboard/itineraire.html`).

- `mapdata.json` — trait de côte Natural Earth 10 m simplifié, lacs, rivières, et la projection.
  Extrait du planificateur, à régénérer si celui-ci change.
- `places-min.json` — coordonnées des lieux utilisés dans les itinéraires.

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
