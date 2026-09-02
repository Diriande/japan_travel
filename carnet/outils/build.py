#!/usr/bin/env python3
"""Assemble le carnet : un document unique, ouvrable en local, sans réseau.

    python3 carnet/outils/build.py
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))

import scenes                     # noqa: E402
import trames as TR               # noqa: E402
from shell import page            # noqa: E402

RACINE = HERE.parent.parent
GENMAP = RACINE / "itineraires" / "outils"

TITRES = {
    "alpes":  ("Des cascades<br>et des <em>ateliers</em>", "Des cascades et des ateliers",
               "Cinq stations, d'ouest en est, sans jamais revenir sur ses pas."),
    "kyushu": ("La porcelaine<br>et la <em>mémoire</em>", "La porcelaine et la mémoire",
               "Quatre stations, dont trois sur une île qu'aucun de vous trois ne connaît."),
    "trois":  ("Trois villes,<br>trois <em>semaines</em>", "Trois villes, trois semaines",
               "Trois bases seulement, cinq nuits chacune, et deux trains dans tout le voyage."),
    "tokyo-kyushu": ("Tokyo<br>et <em>Kyushu</em>", "Tokyo et Kyushu",
               "Quatre stations, du Kanto au sud, reliées par deux vols compris dans le billet."),
}

# Dépenses courantes, enregistrées d'un geste. (libellé, yens, poste)
RAPIDES = [
    ("Ramen", 900, "Nourriture"),
    ("Konbini", 600, "Nourriture"),
    ("Café", 450, "Nourriture"),
    ("Bière", 500, "Nourriture"),
    ("Déjeuner", 1200, "Nourriture"),
    ("Dîner", 3000, "Nourriture"),
    ("Métro", 250, "Transport"),
    ("Bus", 400, "Transport"),
    ("Entrée", 600, "Activités"),
    ("Onsen", 800, "Activités"),
    ("Souvenir", 2000, "Divers"),
    ("Consigne", 600, "Divers"),
]

VALISE = [
    {"nom": "Papiers", "items": [
        ["Passeports, valides 6 mois après le retour", "Pour les trois. Photocopier et garder une copie séparée."],
        ["Visit Japan Web", "Immigration et douane remplies en ligne avant le vol : un QR code, et on évite la file."],
        ["Attestation d'assurance", "Les soins sont chers au Japon et se paient d'avance."],
        ["Permis de conduire international", "Seulement si vous louez à Kanazawa. Gratuit, en préfecture, plusieurs semaines de délai."],
        ["Confirmations d'hébergement imprimées", "Les petites auberges ne lisent pas toujours l'anglais à l'écran."],
    ]},
    {"nom": "Argent", "items": [
        ["Espèces en yens", "Le Japon reste très liquide : marchés, bus, petits restaurants, temples."],
        ["Une carte sans frais à l'étranger", "Les distributeurs 7-Eleven et des bureaux de poste acceptent les cartes étrangères, pas tous les autres."],
        ["Carte IC (Suica ou Icoca)", "Se recharge en espèces, sert dans tous les transports urbains et les supérettes."],
    ]},
    {"nom": "Vêtements", "items": [
        ["De quoi superposer", "18 à 26 °C en ville, 8 à 16 °C à Kamikochi et sur la route alpine. Tout se joue en couches."],
        ["Une polaire ou une doudoune fine", "Indispensable en altitude, même en juin."],
        ["Veste imperméable", "Mi-juin, la saison des pluies commence par le sud."],
        ["Chaussures de marche déjà rodées", "Kurama, le sentier 6 du Takao, Kamikochi. Ne pas partir avec des neuves."],
        ["Chaussures faciles à retirer", "On se déchausse dans les temples, les ryokans et certains restaurants."],
        ["Chaussettes sans trou", "Corollaire du point précédent, et pas une plaisanterie."],
    ]},
    {"nom": "Santé", "items": [
        ["Ordonnances traduites", "Pour tout traitement suivi."],
        ["Vérifier les molécules interdites", "La pseudoéphédrine et la codéine sont prohibées à l'entrée — beaucoup de médicaments contre le rhume en contiennent."],
        ["Anti-moustiques", "À partir de juin, surtout en forêt et près des rizières."],
        ["Pansements pour ampoules", "Trois semaines de marche."],
    ]},
    {"nom": "Technique", "items": [
        ["eSIM ou routeur de poche", "Une eSIM data pour trois semaines coûte 15 à 25 €. Vérifier que le téléphone est compatible."],
        ["Adaptateur type A", "Le Japon est en 100 V, fiches plates à deux broches. Les chargeurs récents supportent, les appareils chauffants non."],
        ["Batterie externe", "Les journées d'excursion durent douze heures."],
        ["Application de traduction hors ligne", "Télécharger le japonais avant de partir, avec la traduction par photo."],
    ]},
    {"nom": "Le petit matériel qui change tout", "items": [
        ["Une petite serviette", "Les toilettes publiques n'ont ni essuie-mains ni sèche-mains. Tout le monde en a une."],
        ["Un sac plastique pour les déchets", "Il n'y a presque aucune poubelle dans la rue : on rapporte ses déchets."],
        ["Un sac pliable", "Pour les achats, et pour la journée à Shirakawa-go où l'on laisse les valises."],
        ["Serviette de bain fine pour les onsen", "Beaucoup de bains publics la font payer."],
        ["De la place dans la valise", "Deux fois 23 kg à l'aller, et Kappabashi, Arita et Wajima à la fin."],
    ]},
]


def carte(steps, excursions, flights):
    js = (f'const {{buildMap}}=require("./genmap.js");'
          f'process.stdout.write(buildMap({steps}, {excursions}, {{flights:{flights}}}));')
    return subprocess.run(["node", "-e", js], cwd=GENMAP,
                          capture_output=True, text=True, check=True).stdout


def main():
    scenes_out, cartes_out, trames_out = {}, {}, []

    for t in TR.TRAMES:
        titre, court, resume = TITRES[t["id"]]
        for e in t["etapes"]:
            scenes_out[f'{t["id"]}:{e["id"]}'] = scenes.scene(
                f'{t["id"]}-{e["id"]}', e["signe"], e["teinte"])
        cartes_out[t["id"]] = carte(*t["carte"])
        trames_out.append({
            "id": t["id"], "titre": titre, "court": court, "resume": resume, "deck": t["deck"],
            "nuits": t["nuits"], "trajet": t["trajet"],
            "par_pers": sum(b[2] for b in t["budget"]),
            "vols": t.get("vols", False),
            "etapes": t["etapes"], "jours": t["jours"], "resa": t["resa"],
            "budget": t["budget"],
        })

    data = {"yen": TR.YEN, "trames": trames_out, "scenes": scenes_out,
            "cartes": cartes_out, "rapides": RAPIDES, "valise": VALISE}

    corps = ('<button class="burger" aria-label="Menu">'
             '<svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
             '</button><div class="veil"></div>'
             '<div class="wrap"><aside class="side"></aside><main class="main"></main></div>')

    script = ("const DATA=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n"
              + (HERE / "app.js").read_text())

    out = RACINE / "carnet" / "index.html"
    out.write_text(page("Carnet du Japon", corps, script))
    ko = out.stat().st_size / 1024
    print(f"{out.relative_to(RACINE)} — {ko:.0f} Ko, "
          f"{len(trames_out)} itinéraires, {sum(len(x['jours']) for x in trames_out)} journées, "
          f"{len(scenes_out)} scènes")


if __name__ == "__main__":
    main()
