#!/usr/bin/env python3
"""Génère itineraires/porcelaine-et-memoire.html."""
import pathlib, subprocess, sys, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from style import page, station, span

HERE = pathlib.Path(__file__).parent
OUT = HERE.parent / "porcelaine-et-memoire.html"

mapsvg = subprocess.run(
    ["node", "-e", """
    const {buildMap}=require("./genmap.js");
    process.stdout.write(buildMap(
      [{id:"kyoto",nights:4,anchor:"e"},{id:"fukuoka",nights:5,anchor:"n"},
       {id:"nagasaki",nights:4,anchor:"w"},{id:"kumamoto",nights:3,anchor:"e"}],
      [], {flights:{in:"KIX",out:"FUK"}}));
    """], cwd=HERE, capture_output=True, text=True, check=True).stdout

route = "".join([
 station("✈", "Paris CDG → Osaka Kansai", "J1 · dans l'avion",
   "19 h porte à porte, escale à Helsinki. Arrivée au Kansai en fin d'après-midi, "
   "75 minutes de train jusqu'à Kyoto — vous dormez sur place le soir même.", leg=True),

 station(1, "Kyoto", "J1 – J5 · 4 nuits",
   "Incontournable pour un premier voyage, et tu le connais — autant l'aborder par les marges. "
   "<strong>Quatre nuits</strong> : deux journées en ville en attaquant très tôt, deux en périphérie, "
   "là où les cars ne vont pas.",
   [("past","hall","Journée à Nara",
     "45 minutes de train. Le Todai-ji et son Bouddha de quinze mètres sous la plus grande charpente "
     "de bois ancienne du monde. Le parc aux daims, et derrière, les trois mille lanternes de pierre "
     "du Kasuga-taisha."),
    ("view","tree","Kurama à Kibune, à pied",
     "Deux heures de sentier forestier entre deux villages, par un col à 400 m. Racines, torii, cèdres. "
     "On finit les pieds dans la rivière à Kibune, où les terrasses s'installent au-dessus de l'eau dès juin."),
    ("make","pot","Gojo-zaka et le Fureaikan",
     "La côte des potiers vers Kiyomizu, ses fours et ses boutiques d'atelier. Puis le musée de "
     "l'artisanat sous le parc Okazaki — gratuit, avec démonstrations de laque, teinture et feuille d'or. "
     "La bonne mise en bouche avant Arita."),
    ("eat","bowl","Nishiki, puis un cours de cuisine",
     "La halle couverte le matin, puis deux heures d'atelier : dashi, tempura, sushis roulés. "
     "C'est ce que les parents racontent en rentrant.")],
   nights="4 nuits"),
 span("3 h 00", "Shinkansen Sakura via Shin-Osaka · 74 € par personne"),

 station(2, "Fukuoka", "J5 – J10 · 5 nuits",
   "La grande ville du sud, dont l'aéroport est à dix minutes du centre en métro. "
   "<strong>C'est la base des deux journées d'artisanat</strong>, et la ville où l'on mange le mieux "
   "du voyage pour le moins cher.",
   [("make","pot","Arita et Imari",
     "Une heure de train. En 1616, un potier coréen déporté après les guerres de Hideyoshi trouve du "
     "kaolin dans la montagne d'Izumiyama : c'est l'acte de naissance de la porcelaine japonaise. "
     "Quatre siècles plus tard, la ville entière vit encore de ses fours. Ateliers ouverts, musée du "
     "Kyushu Ceramic, et le sanctuaire Tozan dont les torii sont en porcelaine."),
    ("past","boat","Yanagawa en barque",
     "Une heure au sud. Les douves d'une ancienne ville de château, devenues canaux, que l'on descend "
     "à la perche pendant une heure — le batelier chante. À l'arrivée, l'anguille cuite à la vapeur "
     "sur son riz, spécialité locale depuis trois siècles."),
    ("eat","bowl","Les yatai de Nakasu",
     "Une centaine de stands montés chaque soir sur les trottoirs et démontés à l'aube. Huit tabourets, "
     "un rideau, du ramen tonkotsu et des brochettes. C'est la dernière ville du Japon où la tradition "
     "survit vraiment."),
    ("past","gate","Dazaifu",
     "Trente minutes. Le sanctuaire des lettrés, son allée de six mille pruniers, et le Musée national "
     "de Kyushu — celui qui raconte les échanges avec le continent.")],
   nights="5 nuits"),
 span("1 h 30", "Limited express Kamome et Shinkansen Nishi-Kyushu · 40 € par personne"),

 station(3, "Nagasaki", "J10 – J14 · 4 nuits",
   "Une ville en amphithéâtre autour de sa baie, escarpée, avec des escaliers partout. "
   "<strong>Le seul port ouvert à l'Occident pendant les deux siècles où le Japon s'était fermé</strong> "
   "— ce qui en fait la ville la plus métissée du pays, et la plus étrange.",
   [("past","roof","Dejima",
     "Un îlot artificiel en éventail, construit pour y confiner les marchands hollandais de 1641 à 1859. "
     "Ils n'avaient pas le droit d'en sortir, les Japonais pas celui d'y entrer sans autorisation, et "
     "tout ce que le Japon a su de l'Occident pendant deux siècles est passé par ce mouchoir de poche. "
     "Reconstitué bâtiment par bâtiment."),
    ("eat","bowl","Le quartier chinois et Glover Garden",
     "Le plus vieux quartier chinois du Japon, où l'on mange le champon — nouilles au bouillon de porc "
     "et fruits de mer, inventé ici pour nourrir les étudiants chinois pauvres. Et les maisons de bois "
     "des marchands occidentaux, accrochées à la pente au-dessus du port."),
    ("view","boat","Gunkanjima",
     "Trois heures en bateau. Une île-cuirassé de 500 m où cinq mille mineurs vivaient entassés jusqu'à "
     "la fermeture du charbon en 1974, abandonnée du jour au lendemain. Béton nu, immeubles éventrés, "
     "classée à l'UNESCO. Sorties annulées par gros temps : prévoir une date de repli."),
    ("past","hall","Le parc de la paix",
     "Le second et dernier bombardement atomique, le 9 août 1945. Le musée est plus intime que celui "
     "d'Hiroshima, et la colonne noire qui marque l'hypocentre, plantée dans un parc ordinaire, dit "
     "peut-être davantage."),
    ("view","view","Mont Inasa au crépuscule",
     "Téléphérique jusqu'à 333 m. La baie, les grues du chantier naval et la ville qui s'allume dans "
     "son cirque de collines — l'une des trois grandes vues nocturnes du Japon.")],
   nights="4 nuits"),
 span("1 h 55", "Shinkansen via Fukuoka · 55 € par personne"),

 station(4, "Kumamoto", "J14 – J17 · 3 nuits",
   "La base volcanique, et la réponse à la montagne. <strong>L'Aso n'est pas un sommet mais un trou</strong> : "
   "une caldeira de 25 km de diamètre, avec des villages, des routes et des rizières au fond, et cinq "
   "cônes au milieu dont un fume en permanence.",
   [("view","view","Mont Aso",
     "Une heure trente de train à travers la caldeira. Le cratère du Nakadake quand l'activité permet "
     "d'approcher, les prairies de Kusasenri où paissent des chevaux, et le point de vue de Daikanbo sur "
     "l'ensemble du cirque. Marche facile à modérée, dénivelé au choix."),
    ("view","fall","Takachiho",
     "Deux heures et demie de bus. Une gorge de basalte en orgues verticales que l'on remonte à la rame, "
     "sous une cascade de 17 m qui tombe droit dans la barque. Le soir, le <i>kagura</i> — des danses "
     "masquées qui racontent la mythologie fondatrice, jouées par les villageois depuis des siècles."),
    ("past","roof","Château de Kumamoto",
     "L'un des trois plus imposants du Japon, avec ses murs en courbe conçus pour être inescaladables. "
     "Endommagé par le séisme de 2016 et en restauration depuis : on visite un chantier de charpente "
     "traditionnelle, ce qui est presque plus intéressant."),
    ("eat","bath","Kurokawa Onsen",
     "Un village thermal de vingt auberges dans une gorge boisée, qui a interdit les néons et les "
     "immeubles. Un laissez-passer donne accès à trois bains en plein air au choix. À la journée depuis "
     "Kumamoto, ou en nuit supplémentaire si la marge le permet.")],
   nights="3 nuits"),
 span("35 min", "Shinkansen Sakura jusqu'à Fukuoka · 35 € par personne"),

 station("✈", "Fukuoka → Paris CDG", "dernier jour",
   "28 h avec une escale à Kuala Lumpur ou Hanoï, dès 356 € l'aller simple. L'aéroport est à dix "
   "minutes du centre en métro.", leg=True),
])

BODY = f"""<section>
  <p class="eyebrow">Le parti pris</p>
  <h2>Pourquoi Kyushu <em>change la donne</em></h2>
  <p class="lede">Les deux autres propositions te faisaient revoir des régions que tu connais, Kanazawa
    mise à part. <strong>Kyushu est entièrement neuf pour toi</strong>, et c'est l'île la plus forte du
    Japon sur trois de tes quatre thèmes.</p>
  <div class="sheet"><table>
    <thead><tr><th>Thème</th><th>Ce que Kyushu apporte</th></tr></thead>
    <tbody>
      <tr><td><b>Artisanat</b></td><td>Arita, où la porcelaine japonaise est née en 1616 et se fabrique
        sans interruption depuis. Rien d'équivalent ailleurs.</td></tr>
      <tr><td><b>Vie d'autrefois</b></td><td>Dejima, l'îlot où les Hollandais furent confinés deux
        siècles durant, seule fenêtre du Japon fermé sur le monde.</td></tr>
      <tr><td><b>Table</b></td><td>Le ramen tonkotsu est né à Fukuoka, le champon à Nagasaki. Et les
        <i>yatai</i> n'existent plus vraiment qu'ici.</td></tr>
      <tr><td><b>Paysage</b></td><td>Moins alpin, mais volcanique : l'Aso et sa caldeira de 25 km, les
        gorges de Takachiho, les fumerolles de Beppu.</td></tr>
    </tbody></table></div>
  <p class="lede" style="margin-top:22px">Et l'hébergement y coûte <strong>76 à 80 € la chambre à
    trois</strong>, contre 145 à 210 € dans les vallées du Hida. C'est ce qui permet seize nuits sous
    les 2 500 €.</p>
</section>

<section>
  <p class="eyebrow">Quatre stations, trois trains</p>
  <h2>La route</h2>
  <p class="lede">On garde Kyoto pour tes parents — ils ne peuvent pas faire leur premier voyage sans —
    puis on descend vers le sud et on ne remonte plus.</p>
  <div class="route">{route}</div>
</section>

<section>
  <p class="eyebrow">Ce que ça coûte</p>
  <h2>Le budget</h2>
  <div class="sheet"><table>
    <thead><tr><th>Poste</th><th>Détail</th><th class="n">Par personne</th><th class="n">À trois</th></tr></thead>
    <tbody>
      <tr><td>Vol</td><td>Multi-destination : Paris-Osaka, puis Fukuoka-Paris</td><td class="n">750 €</td><td class="n">2 250 €</td></tr>
      <tr><td>Hébergement</td><td>16 nuits en ville, chambre à trois</td><td class="n">449 €</td><td class="n">1 348 €</td></tr>
      <tr><td>Transport</td><td>204 € de trains + 60 € d'excursions + 7 €/jour de local</td><td class="n">383 €</td><td class="n">1 149 €</td></tr>
      <tr><td>Nourriture</td><td>40 € par jour et par personne</td><td class="n">680 €</td><td class="n">2 040 €</td></tr>
      <tr><td>Activités</td><td>Entrées, Gunkanjima, ateliers</td><td class="n">45 €</td><td class="n">135 €</td></tr>
      <tr><td>Divers</td><td>eSIM, assurance, souvenirs</td><td class="n">300 €</td><td class="n">900 €</td></tr>
      <tr class="sum"><td>Total</td><td>503 € de marge sous le plafond</td><td class="n">2 497 €</td><td class="n">7 491 €</td></tr>
    </tbody></table></div>
  <div class="note">
    <b>Repartir de Fukuoka, et non d'Osaka</b>
    <p>C'était le point faible de la première version : 3 h 15 de Shinkansen et 130 € par personne le
      jour du vol. <strong>Vérification faite, Fukuoka-Paris existe en aller simple à partir de
      356 €</strong> — Malaysia Airlines via Kuala Lumpur, ou Vietnam Airlines via Hanoï autour de
      430 €. Le trajet du dernier jour tombe à 35 minutes et 35 €.</p>
    <p>Deux réserves : ces vols font 28 h avec une escale en Asie du Sud-Est, contre 19 h par Helsinki.
      Et <strong>ni Malaysia ni Vietnam Airlines n'ouvrent droit à l'indemnisation européenne</strong>
      au départ du Japon, contrairement à Finnair.</p>
  </div>
  <p class="lede" style="margin-top:24px">Avec 503 € de marge, deux dépenses valent le coup :
    <strong>une nuit à Takachiho</strong> pour voir le kagura sans surveiller le dernier bus, et
    <strong>une nuit à Kurokawa Onsen</strong>, environ 90 € par personne en ryokan avec les repas.</p>
</section>

<section>
  <p class="eyebrow">Les trois propositions</p>
  <h2>Côte à <em>côte</em></h2>
  <div class="sheet"><table>
    <thead><tr><th>Itinéraire</th><th>Ce qu'il donne</th><th class="n">Stations</th><th class="n">Trajet</th><th class="n">Par pers.</th></tr></thead>
    <tbody>
      <tr><td><b>Des cascades et des ateliers</b></td><td>Kamikochi, la nuit en gassho, les vallées du Hida</td><td class="n">5</td><td class="n">7 h 35</td><td class="n">2 955 €</td></tr>
      <tr class="sum"><td><b>La porcelaine et la mémoire</b></td><td>Arita, Dejima, l'Aso — et une île entièrement neuve</td><td class="n">4</td><td class="n">2 h 35</td><td class="n">2 497 €</td></tr>
      <tr><td><b>Trois villes, trois semaines</b></td><td>Le rythme le plus doux, deux trains, cinq nuits par base</td><td class="n">3</td><td class="n">4 h 45</td><td class="n">2 537 €</td></tr>
    </tbody></table></div>
  <div class="pair">
    <div><b>Celui-ci, si découvrir prime</b><p>Le seul des trois qui aille quelque part d'inconnu, et le
      meilleur rapport contenu-prix. 475 € de moins que la version alpine.</p></div>
    <div><b>Ce qu'il ne donne pas</b><p>Pas de Fuji, pas de village aux toits de chaume. Moins d'images
      attendues pour des parents qui découvrent le Japon — et c'est le vrai arbitrage, il n'est pas
      budgétaire.</p></div>
  </div>
</section>

<footer>
  Budget calculé sur les données du dépôt : prix d'hébergement par nuit en chambre à trois, trajets
  chiffrés sur le graphe des liaisons réelles, 40 € par jour et par personne de nourriture. Arita,
  Yanagawa, Takachiho et Kurokawa Onsen sont traités en excursions et chiffrés forfaitairement. Le prix
  du vol est une hypothèse de mi-mai fondée sur les relevés Finnair du 23 août 2026 et les allers simples
  Fukuoka-Paris relevés le même jour. Tous les montants sont des estimations à revérifier au moment de
  réserver.
</footer>"""

OUT.write_text(page(
  title="La porcelaine et la mémoire",
  seal="Quatre stations · mi-mai à mi-juin · trois voyageurs",
  h1="La porcelaine<br>et la <em>mémoire</em>",
  deck="Quatre siècles de fours à Arita, une ville qui a regardé l'Occident quand tout le pays s'était "
       "fermé, et la plus grande caldeira du monde. La seule grande île que tu ne connais pas.",
  tally=[("Par personne","2 497 €",True), ("À trois","7 491 €",False),
         ("Nuits","16",False), ("Trajet","2 h 35",False)],
  mapsvg=mapsvg,
  caption=['<span class="li"><span class="dot" style="background:var(--m-stop)"></span> station, avec le nombre de nuits</span>',
           '<span class="li"><span class="sw" style="background:var(--m-route)"></span> le fil du voyage</span>',
           '<span class="li"><span class="sw" style="background:var(--m-air)"></span> arrivée et départ</span>',
           "<span class=\"li\">Arita, Yanagawa, l'Aso et Takachiho se font depuis les stations</span>"],
  body=BODY))
print(f"{OUT} — {OUT.stat().st_size // 1024} Ko")
