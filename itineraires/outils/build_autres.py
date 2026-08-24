#!/usr/bin/env python3
"""Génère alpes-et-artisanat.html et trois-villes.html."""
import pathlib, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from style import page, station, span

HERE = pathlib.Path(__file__).parent
DIR = HERE.parent

def carte(steps, excursions, flights):
    js = f"""
    const {{buildMap}}=require("./genmap.js");
    process.stdout.write(buildMap({steps}, {excursions}, {{flights:{flights}}}));
    """
    return subprocess.run(["node", "-e", js], cwd=HERE,
                          capture_output=True, text=True, check=True).stdout

CAPTION = ['<span class="li"><span class="dot" style="background:var(--m-stop)"></span> station, avec le nombre de nuits</span>',
           '<span class="li"><span class="sw" style="background:var(--m-route)"></span> le fil du voyage</span>',
           '<span class="li"><span class="sw" style="background:var(--m-air)"></span> arrivée et départ</span>']

FOOT = """Budget calculé sur les données du dépôt : prix d'hébergement par nuit en chambre à trois,
  trajets chiffrés sur le graphe des liaisons réelles, 40 € par jour et par personne de nourriture.
  Le prix du vol est une hypothèse de mi-mai fondée sur les relevés Finnair du 23 août 2026, tarif
  Economy Classic, deux bagages de 23 kg compris. Tous les montants sont des estimations à revérifier
  au moment de réserver, et l'hébergement en ryokan comme en gassho se réserve très en avance."""

COMPARE = """<section>
  <p class="eyebrow">Les trois propositions</p>
  <h2>Côte à <em>côte</em></h2>
  <div class="sheet"><table>
    <thead><tr><th>Itinéraire</th><th>Ce qu'il donne</th><th class="n">Stations</th><th class="n">Trajet</th><th class="n">Par pers.</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
</section>"""

def rows(hi):
    data = [("Des cascades et des ateliers","Kamikochi, la nuit en gassho, les vallées du Hida","5","7 h 35","2 972 €"),
            ("La porcelaine et la mémoire","Arita, Dejima, l'Aso — et une île entièrement neuve","4","2 h 35","2 497 €"),
            ("Trois villes, trois semaines","Le rythme le plus doux, deux trains, cinq nuits par base","3","4 h 45","2 537 €")]
    return "".join(
      f'<tr class="{"sum" if n==hi else ""}"><td><b>{n}</b></td><td>{d}</td>'
      f'<td class="n">{s}</td><td class="n">{t}</td><td class="n">{p}</td></tr>'
      for n,d,s,t,p in data)

# ——————————————————————————————— Alpes ———————————————————————————————
alpes_route = "".join([
 station("✈","Paris CDG → Osaka Kansai","J1 · dans l'avion",
   "19 h porte à porte, escale à Helsinki. Arrivée au Kansai en fin d'après-midi, 75 minutes de train "
   "jusqu'à Kyoto — vous dormez sur place le soir même.", leg=True),
 station(1,"Kyoto","J1 – J6 · 5 nuits",
   "Incontournable pour un premier voyage. <strong>Cinq nuits</strong> : deux journées en ville en "
   "attaquant très tôt, trois en périphérie — et une sans rien prévoir, ce qui n'est pas du luxe après "
   "le décalage.",
   [("past","hall","Journée à Nara","45 minutes de train. Le Todai-ji et son Bouddha de quinze mètres sous la plus grande charpente de bois ancienne du monde, le parc aux daims, les trois mille lanternes du Kasuga-taisha."),
    ("view","tree","Kurama à Kibune, à pied","Deux heures de sentier forestier entre deux villages, par un col à 400 m. On finit les pieds dans la rivière à Kibune, où les terrasses s'installent au-dessus de l'eau dès juin."),
    ("eat","bowl","Uji, la ville du thé","Vingt minutes. Maisons de thé où l'on apprend à préparer le matcha, le Byodo-in qui figure sur les pièces de dix yens, et une rivière bordée de saules."),
    ("make","loom","Nishijin, Gojo-zaka, Fureaikan","Le quartier des tisserands avec ses métiers en marche, la côte des potiers vers Kiyomizu, et le musée de l'artisanat sous le parc Okazaki — gratuit, avec démonstrations."),
    ("eat","bowl","Nishiki et un cours de cuisine","La halle couverte le matin, puis deux heures d'atelier : dashi, tempura, sushis roulés."),
    ("view","gate","Fushimi Inari à 7 h","Le seul créneau où les milliers de torii sont à vous. Deux heures pour monter au sommet et redescendre par les sentiers de derrière.")],
   nights="5 nuits"),
 span("3 h 00","Shinkansen jusqu'à Nagoya, puis limited express Hida · 80 € par personne"),
 station(2,"Takayama","J6 – J11 · 5 nuits",
   "Le Hida remonte la vallée depuis Nagoya, <strong>une des plus belles lignes du pays</strong> — côté "
   "droit en montant. Takayama est une ville de charpentiers : ses artisans étaient réquisitionnés par "
   "la cour impériale en guise d'impôt.",
   [("view","view","Journée à Kamikochi","1 h 30 de bus. Une vallée d'altitude fermée aux voitures, au pied des Alpes du Nord. Trois heures de sentier plat le long de l'Azusa, rivière d'un turquoise laiteux. Pour les jambes, Dakesawa monte 600 m en deux heures vers un cirque glaciaire."),
    ("view","fall","Hirayu Otaki et les onsen de la vallée","Sur la route de Kamikochi, une chute de 64 m qu'on approche à quelques mètres, et les bains de Hirayu, à ciel ouvert dans la forêt. La bonne journée de récupération entre deux marches."),
    ("past","roof","Hida no Sato","Une trentaine de fermes démontées dans les vallées voisines et remontées autour d'un étang. On entre, on voit les foyers noircis, les greniers à vers à soie. Le meilleur endroit du voyage pour comprendre comment on vivait ici."),
    ("past","hall","Takayama Jinya et Hida-Furukawa","Le seul bureau de gouvernement d'époque Edo encore debout — salles d'audience, greniers à riz de l'impôt, salle d'interrogatoire. Puis quinze minutes de train jusqu'à Furukawa, village de canaux à carpes que les cars ignorent."),
    ("make","pot","Sculpture sur if et laque de Hida","L'ichii ittobori se taille d'un seul couteau, sans peinture, en jouant sur les deux teintes du bois. Ateliers ouverts dans les ruelles de Sanmachi."),
    ("eat","bowl","Marchés du matin et bœuf de Hida","Deux marchés dès 7 h, l'un le long de la rivière, l'autre devant le Jinya. Le soir, le bœuf de Hida — moins connu que celui de Kobe, souvent meilleur, et bien moins cher ici qu'à Tokyo.")],
   nights="5 nuits"),
 span("50 min","Bus Nohi · 15 € par personne"),
 station(3,"Shirakawa-go","J11 – J12 · 1 nuit",
   "La seule étape d'une nuit, et elle se justifie : <strong>les cars arrivent à 10 h et repartent à "
   "16 h</strong>. Entre 16 h et 10 h le lendemain, le village est à vous. Laissez les grosses valises "
   "en consigne à Takayama, montez avec un sac.",
   [("past","roof","Nuit en gassho-zukuri","Les maisons à mains jointes, charpentées sans un seul clou, dont les combles abritaient l'élevage des vers à soie. Une quinzaine reçoivent des hôtes : c'est le premier hébergement à réserver, six mois à l'avance."),
    ("view","view","Shiroyama au crépuscule","Vingt minutes de montée. En mai-juin, les rizières en eau doublent le village en reflet, et la lumière rasante de 18 h vaut toutes les photos de midi."),
    ("past","hall","Wada-ke et le Minkaen","La maison du chef de village, et le musée de plein air sur l'autre rive, moins fréquenté, avec des démonstrations de réfection de toiture.")],
   nights="1 nuit"),
 span("1 h 15","Bus Hokutetsu · 15 € par personne"),
 station(4,"Kanazawa","J12 – J16 · 4 nuits",
   "Le cœur artisanal du voyage, et une ville que tu ne connais pas. Épargnée par les bombardements, "
   "elle a gardé ses quartiers entiers. <strong>99 % de la feuille d'or japonaise vient d'ici.</strong>",
   [("view","view","Journée route alpine Tateyama-Kurobe","23 minutes de Shinkansen jusqu'à Toyama, puis téléphérique, funiculaire et car jusqu'à Murodo, à 2 450 m. Le mur de neige — un corridor taillé dans dix à quinze mètres de congère — tient jusqu'à mi-juin. Environ 90 € par personne."),
    ("view","fall","Shomyo-daki, sur la même journée","Au pied de la route alpine, <b>la plus haute cascade du Japon</b> : 350 m en quatre paliers, doublée au printemps par la Hannoki qui n'existe que le temps de la fonte. Mai-juin est exactement sa saison de plus fort débit."),
    ("make","pot","Poser la feuille d'or soi-même","Plusieurs ateliers font décorer une boîte ou des baguettes. La feuille fait un dixième de micron : elle se déchire au moindre souffle, ce qui rend l'exercice inoubliable."),
    ("make","pot","Journée sur la côte de Noto","En voiture de location : les mille rizières en terrasses de Senmaida dévalant jusqu'à la mer, et les ateliers de laque de Wajima, montée en cent couches. Un paysage que presque aucun visiteur étranger ne voit."),
    ("past","roof","Higashi Chaya et Nagamachi","Le quartier des maisons de thé, dont on visite l'intérieur, et celui des samouraïs avec ses murs de terre protégés par des nattes de paille."),
    ("eat","bowl","Marché Omicho et Kenrokuen à 7 h","Crabe, crevettes douces, oursins de la mer du Japon ; les kaisendon du premier étage dès 9 h. Et le jardin à l'ouverture, quand l'entrée est gratuite et les allées désertes.")],
   nights="4 nuits"),
 span("2 h 30","Shinkansen Hokuriku Kagayaki, direct · 110 € par personne"),
 station(5,"Tokyo","J16 – J19 · 3 nuits",
   "Trois nuits pour finir, <strong>à Yanaka ou Nezu plutôt qu'à Shinjuku</strong> : le vieux Tokyo, "
   "ruelles basses, temples et cimetière ombragé, à vingt minutes de tout et infiniment plus calme le soir.",
   [("view","view","Mont Takao","50 minutes de Shinjuku pour 599 m de montagne, ce qui est absurde et formidable. Prenez le <b>sentier 6</b>, qui remonte un ruisseau en forêt et passe la petite chute de Biwa — 1 h 30, quelques passages dans le lit du cours d'eau. À mi-pente, le Yakuo-in et ses statues de tengu ; au sommet, le Fuji par temps clair. À faire en semaine."),
    ("past","roof","Musée en plein air de l'architecture Edo-Tokyo","À Koganei, trente maisons et boutiques sauvées de la démolition et remontées : bains publics, taverne, échoppe de teinturier, villa moderniste. Le pendant urbain de Hida no Sato, et presque personne n'y va."),
    ("past","gate","Yanaka à pied","Un des rares quartiers épargnés par le séisme de 1923 et les bombardements. Ruelles, artisans, chats, et Yanaka Ginza pour le goûter."),
    ("make","loom","Kappabashi","La rue des fournisseurs de restaurants : couteaux forgés, moules à pâtisserie, vaisselle au kilo. C'est là qu'on achète un couteau qui durera trente ans, gravé devant soi."),
    ("eat","bowl","Tsukiji le matin, dépachika le soir","Le marché aux poissons a déménagé mais les échoppes de rue sont restées : oursin, omelette dashi, thé grillé debout. Et les sous-sols alimentaires des grands magasins pour les cadeaux."),
    ("view","fall","Nikko, si l'envie revient","1 h 50 depuis Asakusa, faisable à la journée. Les chutes de Kegon, le marais de Senjogahara sur caillebotis, et le mausolée de Tokugawa. Ce n'est plus dans la trame, mais une journée libre peut y aller — 40 € par personne, décidé la veille selon la météo.")],
   nights="3 nuits"),
 station("✈","Tokyo Haneda → Paris CDG","dernier jour",
   "Finnair, 18 h avec l'escale. Le retour part de Tokyo en soirée et arrive à Paris le matin.", leg=True),
])

ALPES = f"""<section>
  <p class="eyebrow">La saison décide</p>
  <h2>Mai-juin, et pas <em>l'hiver</em></h2>
  <p class="lede">Tu hésitais entre mai-juin et l'hiver. Cet itinéraire tranche, et ce n'est pas qu'une
    question de prix.</p>
  <div class="note">
    <b>Deux pièces maîtresses ferment en hiver</b>
    <p><strong>Kamikochi</strong> est fermé de mi-novembre à mi-avril : la vallée n'est pas déneigée et
      les hôtels sont clos. La <strong>route alpine Tateyama-Kurobe</strong> n'ouvre que de mi-avril à
      fin novembre. Ce sont précisément les deux morceaux de montagne du voyage. En mai-juin, la route
      alpine offre en plus son <strong>mur de neige</strong> — un corridor taillé dans une congère de
      dix à quinze mètres.</p>
  </div>
  <p class="lede" style="margin-top:24px">Mai-juin apporte le reste : cascades au débit de la fonte,
    rizières en eau, montagne accessible sans crampons, et l'affluence qui retombe après la Golden Week
    — la première semaine de mai, à éviter absolument. <strong>Viser du 15 mai au 15 juin</strong>.</p>
</section>

<section>
  <p class="eyebrow">Cinq stations</p>
  <h2>La route</h2>
  <p class="lede">Elle descend d'ouest en est sans jamais revenir sur ses pas : arrivée au Kansai,
    traversée des Alpes, remontée sur Tokyo.</p>
  <div class="route">{alpes_route}</div>
</section>

<section>
  <p class="eyebrow">Ce que ça coûte</p>
  <h2>Le budget</h2>
  <div class="sheet"><table>
    <thead><tr><th>Poste</th><th>Détail</th><th class="n">Par personne</th><th class="n">À trois</th></tr></thead>
    <tbody>
      <tr><td>Vol A/R</td><td>Finnair, arrivée Osaka, départ Tokyo, 2 × 23 kg</td><td class="n">750 €</td><td class="n">2 250 €</td></tr>
      <tr><td>Hébergement</td><td>18 nuits, chambre à trois, dont la gassho de Shirakawa-go</td><td class="n">647 €</td><td class="n">1 941 €</td></tr>
      <tr><td>Transport</td><td>220 € de trajets + 95 € d'excursions + 7 €/jour de local</td><td class="n">448 €</td><td class="n">1 344 €</td></tr>
      <tr><td>Nourriture</td><td>40 € par jour et par personne</td><td class="n">760 €</td><td class="n">2 280 €</td></tr>
      <tr><td>Activités</td><td>Entrées, ateliers, route alpine incluse</td><td class="n">50 €</td><td class="n">150 €</td></tr>
      <tr><td>Divers</td><td>eSIM, assurance, souvenirs</td><td class="n">300 €</td><td class="n">900 €</td></tr>
      <tr class="sum"><td>Total</td><td>28 € de marge</td><td class="n">2 972 €</td><td class="n">8 916 €</td></tr>
    </tbody></table></div>
  <p class="lede" style="margin-top:24px">Si le vol dépasse 800 €, retirer une nuit à Takayama rend
    environ 95 € par personne sans rien sacrifier — il resterait quatre nuits, donc les deux journées de
    montagne. À l'inverse, un vol à 650 € libère 300 € par personne.</p>
</section>

{COMPARE.format(rows=rows("Des cascades et des ateliers"))}

<section>
  <p class="eyebrow">À trancher</p>
  <h2>Cinq décisions</h2>
  <div class="pair">
    <div><b>La gassho de Shirakawa-go</b><p>Une quinzaine de maisons reçoivent des hôtes, et elles se
      réservent six mois à l'avance. C'est le premier hébergement à bloquer, avant même le vol.</p></div>
    <div><b>La voiture pour Noto</b><p>Une journée de location depuis Kanazawa ouvre Senmaida et les
      ateliers de laque de Wajima. 70 € la journée pour le groupe, plus le permis international.</p></div>
    <div><b>Kamikochi à la journée ou la nuit</b><p>En partant de Takayama à 7 h, vous êtes dans la
      vallée à 8 h 30, avant les bus. Pour l'aube sur l'Azusa, gardez la chambre de Takayama et montez
      avec un sac.</p></div>
    <div><b>L'ordre du vol</b><p>Arrivée Osaka, départ Tokyo : un billet multi-destination. Vérifie que
      Finnair dessert le Kansai à tes dates — sinon on inverse le sens.</p></div>
    <div><b>La Golden Week</b><p>Du 29 avril au 5 mai, tout le Japon est en congés : trains pleins,
      hôtels doublés. Si tu vises mai, pars après le 10.</p></div>
  </div>
</section>

<footer>{FOOT}</footer>"""

(DIR/"alpes-et-artisanat.html").write_text(page(
  title="Des cascades et des ateliers",
  seal="Cinq stations · mi-mai à mi-juin · trois voyageurs",
  h1="Des cascades<br>et des <em>ateliers</em>",
  deck="Construit sur ce que tu n'as pas encore vu — Kanazawa, Shirakawa-go, la haute montagne — et sur "
       "ce qui compte pour tes parents : l'eau et le relief, la table, les mains qui fabriquent.",
  tally=[("Par personne","2 972 €",True),("À trois","8 916 €",False),
         ("Nuits","18",False),("Trajet","7 h 35",False)],
  mapsvg=carte('[{id:"kyoto",nights:5},{id:"takayama",nights:5},{id:"shirakawago",nights:1,anchor:"w"},'
               '{id:"kanazawa",nights:4,anchor:"w"},{id:"tokyo",nights:3,anchor:"e"}]',
               '[{from:"takayama",to:"kamikochi",anchor:"s"},{from:"kanazawa",to:"toyama",anchor:"e"}]',
               '{in:"KIX",out:"HND"}'),
  caption=CAPTION + ['<span class="li">Kamikochi et la route alpine se font depuis leur station</span>'],
  body=ALPES))
print("alpes-et-artisanat.html")

# ————————————————————————— Trois villes —————————————————————————
tv_route = "".join([
 station("✈","Paris CDG → Osaka Kansai","J1 · dans l'avion",
   "19 h porte à porte, escale à Helsinki. 75 minutes de train depuis le Kansai : vous dormez à Kyoto "
   "le soir de l'arrivée.", leg=True),
 station(1,"Kyoto","J1 – J6 · 5 nuits",
   "<strong>Deux journées en ville, trois en excursion</strong>, toutes à moins d'une heure. Cinq nuits "
   "par base : le temps de trouver sa boulangerie et son itinéraire jusqu'à la gare.",
   [("past","hall","Nara, 45 minutes","Le Todai-ji et son Bouddha de quinze mètres sous la plus grande charpente de bois ancienne du monde. Le parc aux daims, les trois mille lanternes du Kasuga-taisha."),
    ("view","tree","Kurama à Kibune, à pied","Deux heures de sentier forestier entre deux villages, par un col à 400 m. On finit les pieds dans la rivière à Kibune, où les terrasses montent au-dessus de l'eau dès juin."),
    ("eat","bowl","Uji, la ville du thé","Vingt minutes. Maisons de thé où l'on apprend à préparer le matcha, le Byodo-in qui figure sur les pièces de dix yens, et une rivière bordée de saules."),
    ("make","loom","Nishijin, Gojo-zaka, Fureaikan","Le quartier des tisserands avec ses métiers en marche, la côte des potiers vers Kiyomizu, et le musée de l'artisanat sous le parc Okazaki — gratuit, démonstrations de laque, teinture et feuille d'or."),
    ("eat","bowl","Nishiki et un cours de cuisine","La halle couverte le matin, puis deux heures d'atelier : dashi, tempura, sushis roulés."),
    ("view","gate","Fushimi Inari à 7 h","Le seul créneau où les milliers de torii sont à vous.")],
   nights="5 nuits"),
 span("2 h 15","Thunderbird via Tsuruga · 55 € par personne"),
 station(2,"Kanazawa","J6 – J11 · 5 nuits",
   "Le cœur du voyage, et la ville que tu ne connais pas. Épargnée par les bombardements, elle a gardé "
   "ses quartiers entiers. <strong>99 % de la feuille d'or japonaise vient d'ici.</strong> Deux journées "
   "en ville, trois en excursion — c'est d'ici qu'on atteint la montagne et le village aux toits de chaume.",
   [("view","view","Route alpine et Shomyo-daki","23 minutes de Shinkansen jusqu'à Toyama, puis téléphérique, funiculaire et car jusqu'à Murodo, à 2 450 m — le mur de neige tient jusqu'à mi-juin. Au pied, <b>la plus haute cascade du Japon</b> : 350 m en quatre paliers, doublée au printemps par la Hannoki. Environ 90 € par personne."),
    ("past","roof","Shirakawa-go à la journée","1 h 15 de bus. Les maisons à mains jointes, charpentées sans un clou. Partez au premier bus : entre 8 h 30 et 10 h, avant les cars, le village est encore calme. Le musée de plein air sur l'autre rive reste tranquille toute la journée."),
    ("make","pot","Poser la feuille d'or soi-même","Plusieurs ateliers font décorer une boîte ou des baguettes. La feuille fait un dixième de micron : elle se déchire au moindre souffle."),
    ("make","pot","Journée sur la côte de Noto","En voiture : les mille rizières en terrasses de Senmaida dévalant jusqu'à la mer, et les ateliers de laque de Wajima, montée en cent couches."),
    ("past","roof","Higashi Chaya et Nagamachi","Le quartier des maisons de thé, dont on visite l'intérieur, et celui des samouraïs avec ses murs de terre protégés par des nattes de paille."),
    ("eat","bowl","Marché Omicho et Kenrokuen à 7 h","Crabe, crevettes douces, oursins de la mer du Japon. Et le jardin à l'ouverture, quand l'entrée est gratuite et les allées désertes.")],
   nights="5 nuits"),
 span("2 h 30","Shinkansen Hokuriku Kagayaki, direct · 110 € par personne"),
 station(3,"Tokyo","J11 – J16 · 5 nuits",
   "Cinq nuits pour finir, <strong>à Yanaka ou Nezu plutôt qu'à Shinjuku</strong> : le vieux Tokyo, "
   "ruelles basses, temples et cimetière ombragé. Deux journées en ville, deux en excursion, une "
   "demi-journée d'achats.",
   [("view","view","Mont Takao","50 minutes de Shinjuku pour 599 m de montagne. Prenez le <b>sentier 6</b>, qui remonte un ruisseau en forêt et passe la petite chute de Biwa — 1 h 30, quelques passages dans le lit du cours d'eau. Le Yakuo-in et ses tengu à mi-pente, le Fuji au sommet par temps clair. À faire en semaine."),
    ("view","fall","Nikko à la journée","1 h 50 depuis Asakusa. Les chutes de Kegon, 97 m d'un seul jet avec un ascenseur qui descend au pied dans la gorge, et le marais de Senjogahara — deux heures de caillebotis plats à 1 400 m. Le mausolée de Tokugawa croule sous les sculptures polychromes."),
    ("past","roof","Musée en plein air de l'architecture Edo-Tokyo","À Koganei, trente maisons et boutiques sauvées de la démolition et remontées : bains publics, taverne, échoppe de teinturier. Presque personne n'y va."),
    ("past","gate","Yanaka à pied","Un des rares quartiers épargnés par le séisme de 1923 et les bombardements. Ruelles, artisans, chats, et Yanaka Ginza pour le goûter."),
    ("make","loom","Kappabashi","La rue des fournisseurs de restaurants : couteaux forgés, moules à pâtisserie, vaisselle au kilo. Un couteau qui durera trente ans, gravé devant soi."),
    ("eat","bowl","Tsukiji le matin, dépachika le soir","Oursin, omelette dashi, thé grillé debout. Et les sous-sols alimentaires des grands magasins pour les cadeaux.")],
   nights="5 nuits"),
 station("✈","Tokyo Haneda → Paris CDG","dernier jour",
   "Finnair, 18 h avec l'escale.", leg=True),
])

TV = f"""<section>
  <p class="eyebrow">Le parti pris</p>
  <h2>Pourquoi c'est <em>moins cher</em></h2>
  <p class="lede">Ce n'est pas une question de confort mais de géographie. <strong>Les trois nuits chères
    du voyage alpin — Takayama à 145 €, Shirakawa-go à 180 €, Kamikochi à 210 € — sont des hébergements
    de montagne en demi-pension.</strong> Ici, on dort dans les trois villes les moins chères du parcours
    et on va voir la montagne à la journée.</p>
  <div class="sheet"><table>
    <thead><tr><th>Poste</th><th>Version alpine</th><th>Cette version</th><th class="n">Écart</th></tr></thead>
    <tbody>
      <tr><td>Hébergement</td><td>18 nuits, dont 6 en ryokan de montagne</td><td>15 nuits en ville</td><td class="n">−296 €</td></tr>
      <tr><td>Transport</td><td>5 étapes, 7 h 35 de trajet</td><td>2 trains, 4 h 45</td><td class="n">−125 €</td></tr>
      <tr><td>Nourriture</td><td>19 jours</td><td>16 jours</td><td class="n">−120 €</td></tr>
      <tr class="sum"><td>Par personne</td><td>2 972 €</td><td>2 537 €</td><td class="n">−435 €</td></tr>
    </tbody></table></div>
  <p class="lede" style="margin-top:22px">La contrepartie est réelle et il faut la nommer : <strong>vous
    ne dormez plus en gassho à Shirakawa-go</strong>, donc vous voyez le village entre 10 h et 16 h, avec
    les cars. Et vous ne verrez pas l'aube sur l'Azusa à Kamikochi. Tout le reste est là.</p>
</section>

<section>
  <p class="eyebrow">Trois stations, deux trains</p>
  <h2>La route</h2>
  <p class="lede">Cinq nuits par base : le rythme le plus doux possible pour un voyage à trois avec des
    parents qui découvrent.</p>
  <div class="route">{tv_route}</div>
</section>

<section>
  <p class="eyebrow">Ce que ça coûte</p>
  <h2>Le budget</h2>
  <div class="sheet"><table>
    <thead><tr><th>Poste</th><th>Détail</th><th class="n">Par personne</th><th class="n">À trois</th></tr></thead>
    <tbody>
      <tr><td>Vol A/R</td><td>Finnair, arrivée Osaka, départ Tokyo, 2 × 23 kg</td><td class="n">750 €</td><td class="n">2 250 €</td></tr>
      <tr><td>Hébergement</td><td>15 nuits en ville, chambre à trois</td><td class="n">450 €</td><td class="n">1 350 €</td></tr>
      <tr><td>Transport</td><td>165 € de trains + 75 € d'excursions + 7 €/jour de local</td><td class="n">352 €</td><td class="n">1 056 €</td></tr>
      <tr><td>Nourriture</td><td>40 € par jour et par personne</td><td class="n">640 €</td><td class="n">1 920 €</td></tr>
      <tr><td>Activités</td><td>Entrées, ateliers, route alpine incluse</td><td class="n">45 €</td><td class="n">135 €</td></tr>
      <tr><td>Divers</td><td>eSIM, assurance, souvenirs</td><td class="n">300 €</td><td class="n">900 €</td></tr>
      <tr class="sum"><td>Total</td><td>463 € de marge sous le plafond</td><td class="n">2 537 €</td><td class="n">7 611 €</td></tr>
    </tbody></table></div>
  <div class="note">
    <b>Si la marge sert à quelque chose</b>
    <p>Avec 463 € par personne de réserve, la meilleure dépense serait <strong>une nuit à Shirakawa-go en
      gassho</strong> — 60 € par personne, et vous retrouvez le village au crépuscule et à l'aube, ce que
      la version à la journée ne donne pas. C'est le seul vrai manque de cet itinéraire, et il se comble
      pour le prix d'un bon repas.</p>
  </div>
</section>

{COMPARE.format(rows=rows("Trois villes, trois semaines"))}

<footer>{FOOT}</footer>"""

(DIR/"trois-villes.html").write_text(page(
  title="Trois villes, trois semaines",
  seal="Trois stations · mi-mai à mi-juin · trois voyageurs",
  h1="Trois villes,<br>trois <em>semaines</em>",
  deck="Kyoto, Kanazawa, Tokyo. On défait les valises trois fois en seize jours, on prend deux trains, "
       "et tout le reste se fait en excursions. Moins fourni sur le papier, plus reposant en vrai.",
  tally=[("Par personne","2 537 €",True),("À trois","7 611 €",False),
         ("Nuits","15",False),("Trajet","4 h 45",False)],
  mapsvg=carte('[{id:"kyoto",nights:5},{id:"kanazawa",nights:5,anchor:"w"},{id:"tokyo",nights:5,anchor:"e"}]',
               '[{from:"kanazawa",to:"shirakawago",anchor:"w"},{from:"tokyo",to:"nikko",anchor:"e"}]',
               '{in:"KIX",out:"HND"}'),
  caption=CAPTION + ['<span class="li">Shirakawa-go et Nikko se font depuis leur station</span>'],
  body=TV))
print("trois-villes.html")
