/* Retire l'enveloppe HTML d'une page du dépôt pour la publier en Artifact.
   Les fichiers versionnés sont des documents complets, pour l'ouverture locale ;
   le publish d'Artifact fournit sa propre enveloppe. */
const fs = require("fs");
const src = process.argv[2], dst = process.argv[3];
if (!src || !dst) { console.error("usage: node strip.js <source> <destination>"); process.exit(1); }
let t = fs.readFileSync(src, "utf8");
t = t.replace(/^[\s\S]*?<head>\s*/i, "")
     .replace(/<meta[^>]*>\s*/gi, "")
     .replace(/<\/head>\s*<body>\s*/i, "\n")
     .replace(/\s*<\/body>\s*<\/html>\s*$/i, "\n");
fs.writeFileSync(dst, t);
console.log(dst, "->", (t.length / 1024).toFixed(0) + " Ko");
