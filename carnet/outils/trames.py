#!/usr/bin/env python3
"""Les trois itinéraires, descendus au niveau de la journée.

Les coûts sont en yens et par personne, sauf mention. Ils servent au budget
indicatif de la journée — le budget global reste celui des postes, en euros.
"""

YEN = 165.0  # ¥ pour 1 €, relevé du 23/08/2026 — sert aux conversions d'affichage


def b(h, quoi, note="", cout=0, kind="see"):
    """Un moment de la journée. kind : move, see, eat, walk, rest, stay, note."""
    return {"h": h, "quoi": quoi, "note": note, "cout": cout, "kind": kind}


def j(n, etape, titre, blocs, note=""):
    return {"n": n, "etape": etape, "titre": titre, "blocs": blocs, "note": note}


def e(eid, nom, kanji, nuits, j0, j1, meteo, loge, nuitee, signe, teinte, table, resume):
    """Une étape. `nuitee` est le prix de la chambre à trois, par nuit, en euros."""
    return {"id": eid, "nom": nom, "kanji": kanji, "nuits": nuits, "j0": j0, "j1": j1,
            "meteo": meteo, "loge": loge, "nuitee": nuitee, "signe": signe,
            "teinte": teinte, "table": table, "resume": resume}


def r(quoi, quand, note, critique=False):
    return {"quoi": quoi, "quand": quand, "note": note, "critique": critique}


# ══════════════════════════════════════════════════════════════════════
#  1 · Des cascades et des ateliers — 18 nuits, 5 étapes, 2 972 €
# ══════════════════════════════════════════════════════════════════════

ALPES_ETAPES = [
 e("kyoto", "Kyoto", "京都", 5, 1, 6, "18–24 °C, sec — avant la saison des pluies",
   "Machiya ou hôtel vers Karasuma-Oike, à dix minutes à pied du métro", 98, "pagode", "soir",
   ["Kaiseki au comptoir, une fois — c'est le repas qui restera",
    "Tofu de Nanzen-ji, obanzai le soir, matcha à Uji",
    "Nishiki pour le déjeuner debout : tamago, anguille, tsukemono"],
   "Deux journées en ville, trois en périphérie, une sans rien prévoir."),

 e("takayama", "Takayama", "高山", 5, 6, 11, "14–22 °C en ville, 8–16 °C à Kamikochi",
   "Ryokan dans les ruelles de Sanmachi, chambre à trois avec futons", 145, "cascade", "aube",
   ["Bœuf de Hida grillé sur feuille de magnolia (hoba-miso)",
    "Mitarashi dango salés aux marchés du matin",
    "Sake de Hida : sept brasseries en ville, dégustation à la louche"],
   "Une ville de charpentiers, deux journées de montagne, une de repos."),

 e("shirakawago", "Shirakawa-go", "白川郷", 1, 11, 12, "12–21 °C, brume le matin sur les rizières",
   "Une gassho-zukuri qui reçoit des hôtes — demi-pension, futons au sol", 180, "gassho", "aube",
   ["Le dîner de la maison : truite de rivière, légumes de montagne, miso au foyer",
    "Doburoku, le saké non filtré du village"],
   "La seule étape d'une nuit, et elle se justifie : le village après 16 h."),

 e("kanazawa", "Kanazawa", "金沢", 4, 12, 16, "16–24 °C, averses possibles",
   "Hôtel près du marché Omicho, entre la gare et Higashi Chaya", 80, "torii", "jour",
   ["Kaisendon au marché Omicho, à 8 h, crabe et crevettes douces",
    "Jibuni — le canard mijoté local, épais et sucré",
    "Feuille d'or sur un thé ou une glace, au moins pour voir"],
   "Le cœur artisanal, et la base d'où l'on atteint la haute montagne."),

 e("tokyo", "Tokyo", "東京", 3, 16, 19, "19–26 °C, lourd en fin de séjour",
   "Yanaka ou Nezu — le vieux Tokyo, bas et calme, à vingt minutes de tout", 92, "tour", "soir",
   ["Tsukiji le matin, debout : oursin, omelette dashi, thé grillé",
    "Un izakaya de Yanaka, sans carte en anglais",
    "Les dépachika en sous-sol pour les cadeaux du retour"],
   "Trois nuits pour finir, dans le Tokyo d'avant plutôt qu'à Shinjuku."),
]

ALPES_JOURS = [
 j(1, "kyoto", "Arrivée", [
   b("06h20", "Départ Paris CDG", "Finnair AY1576. Enregistrement des deux valises la veille en ligne.", 0, "move"),
   b("14h05", "Escale à Helsinki", "2 h 40 de correspondance — large. Le terminal non-Schengen est petit, la porte est vite trouvée.", 0, "move"),
   b("16h45", "Vol Helsinki → Osaka Kansai", "13 h 05. Dormir dès le premier service : à l'arrivée il sera 9 h du matin dans votre tête.", 0, "move"),
   b("09h55", "Atterrissage au Kansai", "Immigration et bagages : compter une heure. Remplir <b>Visit Japan Web</b> dans l'avion fait gagner la file — QR code à présenter.", 0, "move"),
   b("11h30", "Haruka jusqu'à Kyoto", "75 minutes, direct. Acheter le billet au guichet JR du hall d'arrivée.", 3600, "move"),
   b("13h00", "Poser les valises", "Le check-in est souvent à 15 h, mais tous les hôtels gardent les bagages. Ressortir tout de suite.", 0, "stay"),
   b("14h00", "Marcher au bord du Kamo", "Ne rien planifier. Une heure de berge, un café, une supérette pour l'eau et les petits déjeuners. La lumière tient jusqu'à 19 h en mai.", 0, "walk"),
   b("18h30", "Premier dîner près de Pontocho", "Une ruelle d'un mètre de large entre la rivière et Kawaramachi. Ne pas viser haut ce soir : yakitori, bière, coucher tôt.", 2500, "eat"),
 ], note="Le décalage est de 7 h. Se coucher à 21 h coûte trois jours de réveils à 4 h — tenir jusqu'à 22 h."),

 j(2, "kyoto", "Le Kyoto qu'on croit connaître", [
   b("06h30", "Fushimi Inari, à l'ouverture de fait", "Le sanctuaire ne ferme jamais. Entre 6 h et 8 h, les milliers de torii sont à vous ; à 10 h, c'est une file. Deux heures pour monter au sommet et redescendre par les sentiers de derrière.", 0, "walk"),
   b("09h30", "Petit déjeuner à Inari", "Les échoppes ouvrent avec le premier train. Inari-zushi, thé.", 700, "eat"),
   b("11h00", "Kiyomizu-dera et la côte des potiers", "Monter par Gojo-zaka plutôt que par Sannenzaka : c'est la rue des ateliers de céramique, et personne ne la prend.", 500, "see"),
   b("13h00", "Déjeuner à Nishiki", "La halle couverte, quatre cents mètres de comptoirs. On mange debout, on goûte, on ne s'assied pas.", 1500, "eat"),
   b("15h30", "Retour à l'hôtel", "Sieste assumée. C'est le jour où le décalage frappe le plus fort.", 0, "rest"),
   b("18h00", "Gion à la tombée du jour", "Hanamikoji et les ruelles de Shirakawa. Regarder les maisons, pas les geiko — les photographier de près est mal vu et désormais interdit dans certaines rues.", 0, "walk"),
   b("19h30", "Obanzai", "La cuisine domestique de Kyoto, servie en petits plats. Moins cher et plus intéressant qu'un kaiseki de touristes.", 3500, "eat"),
 ]),

 j(3, "kyoto", "Nara", [
   b("08h15", "Kintetsu jusqu'à Nara", "45 minutes depuis Kyoto, un départ toutes les 30 minutes. La gare Kintetsu est à dix minutes du parc, la gare JR à vingt-cinq.", 760, "move"),
   b("09h30", "Todai-ji", "Le Bouddha de quinze mètres, sous la plus grande charpente de bois ancienne du monde — et l'actuelle ne fait que les deux tiers de l'originale.", 800, "see"),
   b("11h00", "Le parc et les daims", "Mille deux cents, en liberté, qui s'inclinent pour un biscuit. Ils mordent aussi les sacs plastique : garder la nourriture hors de vue.", 200, "walk"),
   b("12h30", "Déjeuner", "Nakatanidou pour le mochi pilé au marteau en public, puis un vrai déjeuner dans Sanjo-dori.", 1300, "eat"),
   b("14h00", "Kasuga-taisha", "Trois mille lanternes, de pierre le long de l'allée, de bronze sous les auvents. La forêt qui l'entoure n'a pas été coupée depuis mille ans.", 500, "see"),
   b("15h30", "Naramachi", "L'ancien quartier marchand, maisons basses et boutiques d'artisans. Beaucoup plus calme que le parc.", 0, "walk"),
   b("17h30", "Retour sur Kyoto", "", 760, "move"),
 ]),

 j(4, "kyoto", "Kurama et Kibune, à pied", [
   b("08h40", "Eizan Line jusqu'à Kurama", "30 minutes depuis Demachiyanagi, sur une ligne à voie unique qui monte dans la forêt. Les deux voitures panoramiques valent le coup.", 470, "move"),
   b("09h30", "Le sentier de Kurama à Kibune", "Deux heures entre deux villages, par un col à 400 m. Racines, marches de pierre, cèdres. Dénivelé modéré mais réel : de bonnes chaussures.", 500, "walk"),
   b("12h00", "Déjeuner à Kibune", "Dès juin, les restaurants montent des terrasses <i>kawadoko</i> au-dessus de la rivière. En mai, on mange à l'intérieur, au bord de l'eau quand même.", 3000, "eat"),
   b("14h00", "Kibune-jinja", "L'escalier aux lanternes rouges. Sanctuaire de l'eau, où l'on tire des oracles qui n'apparaissent qu'une fois trempés.", 0, "see"),
   b("15h30", "Bain à Kurama Onsen", "Un bain extérieur en pleine forêt, à dix minutes du terminus. Le meilleur usage possible de jambes fatiguées.", 1000, "rest"),
   b("18h00", "Retour à Kyoto", "", 470, "move"),
 ], note="Le sentier ferme par forte pluie. Vérifier la météo la veille et intervertir avec le jour 5 si besoin."),

 j(5, "kyoto", "Thé, puis les mains", [
   b("08h30", "Uji", "Vingt minutes en JR. La ville du thé depuis le XIIIᵉ siècle.", 240, "move"),
   b("09h30", "Byodo-in", "Le pavillon du Phénix, celui des pièces de dix yens. Reconstruit nulle part — c'est l'original de 1053.", 700, "see"),
   b("11h00", "Préparer son matcha", "Plusieurs maisons de thé font moudre la feuille à la meule de pierre puis fouetter soi-même. Trente minutes, et on comprend la différence de prix.", 1500, "see"),
   b("12h30", "Déjeuner soba au thé vert", "Spécialité locale, et les boutiques du bord de rivière font de bons bentos.", 1200, "eat"),
   b("15h00", "Fureaikan, musée de l'artisanat", "Sous le parc Okazaki. <b>Gratuit</b>, et c'est le meilleur endroit du voyage pour voir la laque, la teinture et la feuille d'or expliquées côte à côte, avec des artisans en démonstration.", 0, "see"),
   b("17h00", "Nishijin", "Le quartier des tisserands. Métiers Jacquard en marche au Nishijin Textile Center, et des ateliers de rue où l'on entend le battement avant de voir la porte.", 0, "see"),
   b("19h00", "Kaiseki, le vrai", "Le repas à ne pas économiser. Réserver depuis la France, en demandant à l'hôtel de téléphoner. Compter 8 000 à 15 000 ¥ par personne.", 10000, "eat"),
 ]),

 j(6, "takayama", "La ligne du Hida", [
   b("08h00", "Vider la chambre", "Petit déjeuner à la supérette, valises bouclées.", 0, "stay"),
   b("09h15", "Shinkansen jusqu'à Nagoya", "35 minutes. Réserver la veille, les Hikari sont pleins le matin.", 5900, "move"),
   b("10h48", "Limited express Hida jusqu'à Takayama", "2 h 20 en remontant la vallée de la Hida — <b>une des plus belles lignes du pays</b>. Se placer côté droit en montant : la rivière y est presque tout du long. Bento acheté à Nagoya.", 6300, "move"),
   b("13h10", "Arrivée, dépose des valises", "Le ryokan est à dix minutes à pied de la gare.", 0, "stay"),
   b("14h30", "Sanmachi", "Trois rues d'entrepôts et de maisons de marchands d'époque Edo, noircies par le temps. Les brasseries de saké se signalent par une boule de cèdre suspendue au-dessus de la porte — verte quand le nouveau saké est prêt, brune ensuite.", 0, "walk"),
   b("18h00", "Premier hoba-miso", "Du miso, des champignons et du bœuf de Hida grillés sur une feuille de magnolia, sur un réchaud individuel. Le plat de la ville.", 3000, "eat"),
 ]),

 j(7, "takayama", "Kamikochi", [
   b("06h50", "Premier bus pour Hirayu", "Depuis la gare routière, à côté de la gare. Un aller-retour se prend au guichet.", 2200, "move"),
   b("08h20", "Correspondance pour Kamikochi", "Les voitures privées sont interdites dans la vallée depuis 1975 — d'où le changement à Hirayu.", 1400, "move"),
   b("09h00", "Le pont Kappa et l'Azusa", "La rivière est d'un turquoise laiteux, laissé par la roche broyée. En face, les Hotaka à 3 190 m, souvent encore blancs en mai.", 0, "see"),
   b("09h30", "Vers l'étang Taisho, puis Myojin", "Trois heures de sentier <b>plat</b>, en boucle, le long de l'eau. C'est la marche que tes parents feront sans difficulté — et la plus belle du voyage.", 0, "walk"),
   b("12h30", "Déjeuner à Myojin", "Le petit refuge au bord de l'étang. Simple, chaud, et la terrasse donne sur le miroir d'eau.", 1200, "eat"),
   b("14h00", "Option : Dakesawa", "Pour les jambes qui en veulent, 600 m de dénivelé en deux heures vers un cirque glaciaire. Redescendre avant 16 h.", 0, "walk"),
   b("16h30", "Dernier bus", "Ne pas le manquer — il n'y a rien après. Vérifier l'horaire du jour au guichet le matin.", 3600, "move"),
   b("18h30", "Bain, puis dîner au ryokan", "", 0, "rest"),
 ], note="Kamikochi est fermé de mi-novembre à mi-avril. En mai, prévoir une polaire : il fait dix degrés de moins qu'en ville."),

 j(8, "takayama", "Comment on vivait ici", [
   b("07h00", "Marchés du matin", "Deux, tous les jours : Miyagawa le long de la rivière, Jinya-mae devant l'ancien bureau du gouvernement. Légumes de montagne, cornichons, dango salés grillés.", 500, "walk"),
   b("09h00", "Takayama Jinya", "<b>Le seul bureau de gouvernement d'époque Edo encore debout au Japon.</b> Salles d'audience, greniers à riz de l'impôt, et une salle d'interrogatoire où les instruments sont exposés sans commentaire.", 440, "see"),
   b("11h00", "Bus pour Hida no Sato", "Dix minutes.", 260, "move"),
   b("11h20", "Hida no Sato", "Une trentaine de fermes démontées dans les vallées voisines et remontées autour d'un étang. On entre, on voit les foyers noircis, les greniers à vers à soie, les outils. Compter deux bonnes heures.", 700, "see"),
   b("13h30", "Déjeuner sur place", "Soba de sarrasin de montagne, à la cabane du village.", 1000, "eat"),
   b("15h30", "Sculpture sur if", "L'<i>ichii ittobori</i> se taille d'un seul couteau, sans peinture, en jouant sur les deux teintes du bois de l'if. Ateliers ouverts dans les ruelles de Sanmachi.", 0, "see"),
   b("18h30", "Bœuf de Hida", "Moins connu que celui de Kobe, souvent meilleur, et deux fois moins cher ici qu'à Tokyo. Un restaurant de la vieille ville, réservé le matin même.", 6000, "eat"),
 ]),

 j(9, "takayama", "Eau chaude et cascade", [
   b("08h30", "Bus vers Hirayu", "Sur la route de Kamikochi.", 1600, "move"),
   b("09h40", "Hirayu Otaki", "Une chute de 64 m qu'on approche à quelques mètres. En mai, elle est au débit de la fonte — on la sent avant de la voir.", 0, "see"),
   b("11h00", "Les bains de Hirayu", "Une dizaine de sources, dont plusieurs bains extérieurs en forêt. Le plus grand, Hirayu no Mori, a seize bassins et accepte les visiteurs à la journée.", 700, "rest"),
   b("13h30", "Déjeuner au village", "", 1200, "eat"),
   b("16h00", "Retour à Takayama", "", 1600, "move"),
   b("17h30", "Rien", "Une fin d'après-midi sans programme, au milieu du voyage. C'est délibéré.", 0, "rest"),
 ], note="Journée de récupération, placée entre deux marches. La déplacer selon la météo — c'est le jour le plus souple de la trame."),

 j(10, "takayama", "Furukawa", [
   b("09h00", "Train pour Hida-Furukawa", "Quinze minutes vers le nord. Les cars ne s'y arrêtent pas.", 240, "move"),
   b("09h30", "Les canaux du Seto", "Un village de charpentiers, comme Takayama mais sans la foule : des canaux à carpes le long des entrepôts blancs. On en fait le tour en une heure, lentement.", 0, "walk"),
   b("11h00", "Musée des charpentiers", "Les assemblages du Japon en bois, à taille réelle, qu'on peut manipuler. Aucun clou nulle part.", 500, "see"),
   b("12h30", "Déjeuner à Furukawa", "", 1200, "eat"),
   b("15h00", "Retour, et les brasseries", "Sept maisons de saké à Takayama, la plupart ouvertes à la dégustation pour deux ou trois cents yens le verre. Le riz de Hida et l'eau de fonte donnent des sakés secs.", 800, "eat"),
   b("17h00", "Acheter, si on achète", "C'est ici qu'on trouve la sculpture sur if et la laque de Hida. Les ateliers expédient en France.", 0, "see"),
 ]),

 j(11, "shirakawago", "Le village après les cars", [
   b("08h30", "Laisser les grosses valises", "Consigne à la gare de Takayama, ou le ryokan les garde. Monter avec un sac pour une nuit — la gassho n'a pas d'ascenseur et les futons sont au sol.", 600, "stay"),
   b("10h50", "Bus Nohi pour Shirakawa-go", "50 minutes. <b>Réserver le siège</b> : le bus est souvent complet en saison.", 2600, "move"),
   b("12h00", "Déjeuner au village", "Truite grillée à la broche, soba, et le doburoku si l'occasion se présente.", 1500, "eat"),
   b("13h30", "Wada-ke", "La maison du chef de village, la plus grande ouverte à la visite. Monter dans les combles voir la charpente et les claies d'élevage des vers à soie.", 400, "see"),
   b("15h00", "Le Minkaen, sur l'autre rive", "Vingt-cinq maisons remontées, un musée de plein air nettement moins fréquenté que le village lui-même. Démonstrations de réfection de toiture certains jours.", 600, "see"),
   b("16h30", "Les cars repartent", "C'est l'heure qui justifie la nuit sur place. Entre 16 h et 10 h le lendemain, le village redevient un village.", 0, "note"),
   b("17h30", "Shiroyama au crépuscule", "Vingt minutes de montée jusqu'au belvédère. En mai-juin, les rizières en eau doublent le village en reflet, et la lumière rasante de 18 h vaut toutes les photos de midi.", 0, "walk"),
   b("19h00", "Dîner au foyer", "La demi-pension est la règle. Truite de rivière plantée autour du foyer central, légumes de montagne, miso. On mange avec les autres hôtes.", 0, "eat"),
 ], note="Premier hébergement à réserver du voyage — six mois à l'avance, avant même le vol."),

 j(12, "kanazawa", "Vers l'or", [
   b("06h30", "Le village vide", "Se lever tôt une dernière fois. La brume monte des rizières, il n'y a personne, et c'est pour cette heure-là qu'on a dormi ici.", 0, "walk"),
   b("08h00", "Petit déjeuner à la maison", "Riz, poisson grillé, œuf, soupe. Comme le dîner, autour du foyer.", 0, "eat"),
   b("10h45", "Bus Hokutetsu pour Kanazawa", "1 h 15. Réserver aussi celui-ci.", 2600, "move"),
   b("12h15", "Arrivée et dépose", "L'hôtel est près d'Omicho, entre la gare et la vieille ville.", 0, "stay"),
   b("14h00", "Higashi Chaya", "Le quartier des maisons de thé, aux façades de lattes de bois. Deux maisons se visitent à l'intérieur — Shima et Kaikaro — avec leurs salons à l'étage et la feuille d'or aux murs.", 750, "see"),
   b("16h00", "Poser la feuille d'or soi-même", "Plusieurs ateliers font décorer une boîte ou des baguettes. La feuille fait un dixième de micron : elle se déchire au moindre souffle, ce qui est tout l'intérêt.", 1500, "see"),
   b("19h00", "Jibuni", "Le canard mijoté de Kanazawa, lié à la fécule, avec du wasabi frais. Épais, sucré, très différent du reste du voyage.", 3000, "eat"),
 ]),

 j(13, "kanazawa", "La route alpine", [
   b("07h30", "Shinkansen jusqu'à Toyama", "23 minutes.", 3000, "move"),
   b("08h30", "Toyama → Murodo", "Train de montagne, funiculaire, puis car à travers le plateau. Trois correspondances, deux heures, et on passe de 200 à 2 450 m.", 9500, "move"),
   b("11h00", "Le mur de neige", "Un corridor taillé dans une congère de dix à quinze mètres, ouvert à la marche sur cinq cents mètres. Il tient jusqu'à mi-juin, en fondant.", 0, "walk"),
   b("12h30", "Déjeuner à Murodo", "Le restaurant de la station. Il n'y a rien d'autre là-haut, et c'est très bien ainsi.", 1500, "eat"),
   b("13h30", "L'étang Mikuri", "Une heure de tour, sur la neige en mai. Les crampons légers se louent sur place. Par temps clair, le Tateyama entier se reflète dedans.", 0, "walk"),
   b("15h00", "Redescente", "Par le même chemin, ou en traversée jusqu'au barrage de Kurobe si le temps le permet — mais alors on ne revient pas à Toyama le soir.", 0, "move"),
   b("18h30", "Retour à Kanazawa", "", 3000, "move"),
 ], note="Compter environ 90 € par personne pour la journée. La route ouvre mi-avril et ferme fin novembre — vérifier l'état d'ouverture, la neige décide."),

 j(14, "kanazawa", "Le marché, le jardin, les samouraïs", [
   b("07h00", "Kenrokuen avant l'heure", "<b>L'entrée est gratuite avant 7 h</b> (8 h l'hiver), et les allées sont vides. Un des trois grands jardins du Japon, dessiné sur deux siècles.", 0, "walk"),
   b("08h30", "Marché Omicho", "Trois cents ans de halle. Crabe des neiges, crevettes douces, oursins de la mer du Japon. Prendre un kaisendon — un bol de riz couvert de sashimi — au comptoir, pour le petit déjeuner.", 2500, "eat"),
   b("10h30", "Nagamachi", "Le quartier des samouraïs, avec ses murs de terre protégés l'hiver par des nattes de paille. La maison Nomura se visite, jardin compris.", 550, "see"),
   b("13h00", "Musée du XXIᵉ siècle", "Un disque de verre posé dans la ville, sans façade ni entrée principale. La piscine de Leandro Erlich s'y regarde par en dessous. Réserver le créneau en ligne.", 1200, "see"),
   b("15h30", "Musée de la feuille d'or", "<b>99 % de la feuille d'or japonaise vient d'ici.</b> Le musée Yasue montre le battage : quatre heures pour amener un gramme à un mètre carré.", 310, "see"),
   b("18h30", "Comptoir de sushi", "Kanazawa se dispute Kanazawa le meilleur poisson du pays. Un omakase de quartier, pas un comptoir à touristes.", 6000, "eat"),
 ]),

 j(15, "kanazawa", "La côte de Noto", [
   b("08h30", "Prendre la voiture", "Agence près de la gare. Environ 70 € la journée pour le groupe, plus l'essence. <b>Le permis international est obligatoire</b> — à demander en préfecture avant de partir, c'est gratuit et ça prend quelques semaines.", 0, "move"),
   b("10h30", "Senmaida", "Mille rizières en terrasses qui dévalent jusqu'à la mer. En mai elles sont en eau, donc en miroir. Un sentier descend entre elles jusqu'aux rochers.", 0, "see"),
   b("12h30", "Déjeuner à Wajima", "Poisson du port, dans une ville qui se relève encore du séisme de 2024. Y déjeuner est utile autant qu'agréable.", 1800, "eat"),
   b("14h00", "La laque de Wajima", "Cent couches, chacune poncée. Le musée montre les étapes, et plusieurs ateliers de la ville laissent entrer.", 630, "see"),
   b("16h00", "La route côtière du retour", "Par la côte ouest, avec les falaises et les rochers de Ganmon. Deux heures jusqu'à Kanazawa.", 0, "move"),
 ], note="Sans voiture : remplacer par le Myoryu-ji (le temple aux pièges, visite guidée sur réservation) et le musée D.T. Suzuki, deux salles et un bassin, le lieu le plus calme de la ville."),

 j(16, "tokyo", "Traversée", [
   b("09h00", "Kagayaki jusqu'à Tokyo", "2 h 30, direct, sans changement. Réserver la veille — c'est un train très emprunté. Côté droit après Nagano pour les montagnes.", 14000, "move"),
   b("12h00", "Poser les valises à Yanaka", "Le vieux Tokyo : ruelles basses, temples, un cimetière ombragé et des chats. Vingt minutes de Tokyo Station, infiniment plus calme le soir.", 0, "stay"),
   b("14h00", "Yanaka à pied", "Un des rares quartiers épargnés par le séisme de 1923 et par les bombardements de 1945. On y marche sans but.", 0, "walk"),
   b("16h00", "Yanaka Ginza", "Une rue commerçante d'après-guerre, en pente, où l'on grignote debout : croquettes, brochettes, dorayaki.", 800, "eat"),
   b("19h00", "Izakaya de quartier", "Sans carte en anglais, avec des habitués. Montrer du doigt fonctionne très bien.", 3000, "eat"),
 ]),

 j(17, "tokyo", "Mont Takao", [
   b("08h00", "Keio jusqu'à Takaosanguchi", "50 minutes depuis Shinjuku, pour 599 m de montagne — ce qui est absurde et formidable.", 430, "move"),
   b("09h00", "Le sentier 6", "Il remonte un ruisseau en forêt et passe la petite chute de Biwa. 1 h 30, quelques passages dans le lit du cours d'eau, de l'ombre tout du long. Le meilleur des huit sentiers, et le moins fréquenté.", 0, "walk"),
   b("10h45", "Yakuo-in", "À mi-pente, un temple de montagne aux statues de tengu — les créatures à long nez, gardiennes de la forêt.", 0, "see"),
   b("11h45", "Le sommet", "Par temps clair, le Fuji est au sud-ouest. Les échoppes du haut font des soba et de la bière.", 1000, "eat"),
   b("13h30", "Redescente par le téléphérique", "La pente est raide à la descente : le funiculaire, un des plus raides du pays, s'impose.", 490, "move"),
   b("15h00", "Bain à Takaosan Onsen", "Contre la gare, à la sortie du sentier. Bains extérieurs, et on repart propre.", 1100, "rest"),
   b("18h30", "Retour sur Tokyo", "", 430, "move"),
 ], note="À faire en semaine : le mont Takao est la montagne du dimanche des Tokyoïtes, et le week-end le sentier principal se fait à la queue leu leu."),

 j(18, "tokyo", "Maisons et couteaux", [
   b("09h00", "Musée en plein air de l'architecture Edo-Tokyo", "À Koganei, quarante minutes. Trente maisons et boutiques sauvées de la démolition et remontées : bains publics, taverne, échoppe de teinturier, villa moderniste des années 1940. Le pendant urbain de Hida no Sato, et presque personne n'y va.", 400, "see"),
   b("13h00", "Déjeuner sur place", "Le parc de Koganei autour, si le temps s'y prête.", 1000, "eat"),
   b("15h00", "Kappabashi", "La rue des fournisseurs de restaurants, entre Ueno et Asakusa. Couteaux forgés, moules à pâtisserie, vaisselle au kilo, et les répliques de plats en résine. C'est là qu'on achète un couteau qui durera trente ans, gravé à son nom devant soi.", 0, "see"),
   b("17h30", "Senso-ji en fin de journée", "À dix minutes à pied. La grande lanterne, et Nakamise vidée de ses cars.", 0, "walk"),
   b("19h00", "Dernier vrai dîner", "Le repas où l'on dépense sans compter, puisque c'est le dernier.", 6000, "eat"),
 ]),

 j(19, "tokyo", "Retour", [
   b("07h00", "Tsukiji, le marché extérieur", "Le marché aux poissons a déménagé à Toyosu, mais les échoppes de rue sont restées. Oursin, omelette dashi, thé grillé, debout, à sept heures du matin.", 2000, "eat"),
   b("10h00", "Dépachika", "Les sous-sols alimentaires des grands magasins de Ginza. C'est là qu'on prend les cadeaux : thés, sucreries, sauces, emballés comme des bijoux.", 0, "see"),
   b("13h00", "Récupérer les valises", "L'hôtel les garde après le check-out. Prévoir large : la pesée compte, avec deux fois 23 kg.", 0, "stay"),
   b("15h00", "Monorail jusqu'à Haneda", "30 minutes depuis Hamamatsucho. Être au comptoir 3 h avant.", 500, "move"),
   b("18h55", "Vol Haneda → Helsinki → Paris", "Environ 18 h avec l'escale. Départ en soirée, arrivée à Paris le lendemain matin.", 0, "move"),
 ]),
]

ALPES_RESA = [
 r("La maison gassho de Shirakawa-go", "6 mois avant", "Une quinzaine reçoivent des hôtes, et elles partent en quelques jours à l'ouverture des réservations. À bloquer <b>avant le vol</b>.", True),
 r("Le vol multi-destination Finnair", "4 à 6 mois avant", "Arrivée Osaka Kansai, départ Tokyo Haneda. Vérifier que Finnair dessert le Kansai aux dates visées — sinon inverser le sens du voyage.", True),
 r("Le ryokan de Takayama", "3 mois avant", "Cinq nuits en chambre à trois, c'est ce qui limite le choix. Confirmer que les futons sont pour trois."),
 r("La route alpine Tateyama-Kurobe", "1 mois avant", "Le billet combiné se prend en ligne. Ouverture mi-avril à fin novembre, mur de neige jusqu'à mi-juin."),
 r("Les bus Takayama → Shirakawa-go → Kanazawa", "1 mois avant", "Nohi et Hokutetsu, sièges numérotés, souvent complets en saison.", True),
 r("Le kaiseki de Kyoto", "1 mois avant", "Demander à l'hôtel de téléphoner — beaucoup n'ont pas de réservation en ligne."),
 r("La voiture pour Noto", "2 semaines avant", "Et le <b>permis international</b>, à demander en préfecture plusieurs semaines à l'avance."),
 r("Les Shinkansen", "la veille", "Kyoto → Nagoya, et Kanazawa → Tokyo. Se prennent aux bornes, mais les places assises partent le matin."),
]

ALPES_BUDGET = [
 ("Vol A/R", "Finnair, arrivée Osaka, départ Tokyo, 2 × 23 kg", 750),
 ("Hébergement", "18 nuits en chambre à trois, dont la gassho", 647),
 ("Transport", "220 € de trajets, 95 € d'excursions, 7 €/jour de local", 448),
 ("Nourriture", "40 € par jour et par personne", 760),
 ("Activités", "Entrées, ateliers, route alpine comprise", 50),
 ("Divers", "eSIM, assurance, souvenirs", 300),
]


def repris(jours, numeros, decale=0, etape=None):
    """Reprend des journées d'une autre trame en les renumérotant.

    Kyoto ouvre les trois itinéraires : autant n'écrire ces journées qu'une fois.
    """
    out = []
    for k in numeros:
        d = dict(next(x for x in jours if x["n"] == k))
        d["n"] = k + decale
        if etape:
            d["etape"] = etape
        out.append(d)
    return out


# ══════════════════════════════════════════════════════════════════════
#  2 · La porcelaine et la mémoire — 16 nuits, 4 étapes, 2 497 €
# ══════════════════════════════════════════════════════════════════════

KYUSHU_ETAPES = [
 e("kyoto", "Kyoto", "京都", 4, 1, 5, "18–24 °C, sec",
   "Machiya ou hôtel vers Karasuma-Oike", 98, "pagode", "soir",
   ["Kaiseki au comptoir, une fois", "Tofu de Nanzen-ji, obanzai le soir",
    "Nishiki pour le déjeuner debout"],
   "Quatre nuits d'ouverture, le temps de sortir du décalage."),

 e("fukuoka", "Fukuoka", "福岡", 5, 5, 10, "20–26 °C, humide, averses courtes",
   "Hôtel vers Nakasu ou Hakata, à dix minutes de la gare", 76, "torii", "jour",
   ["Les <b>yatai</b> — cent trente baraques de rue montées chaque soir sur les trottoirs",
    "Tonkotsu ramen, le bouillon d'os de porc, né ici",
    "Mentaiko, œufs de morue au piment, sur du riz blanc"],
   "La base la moins chère du voyage, et la porte de la porcelaine."),

 e("nagasaki", "Nagasaki", "長崎", 4, 10, 14, "19–25 °C, la mer tempère",
   "Hôtel sur les pentes, vers Glover ou Dejima", 78, "vague", "soir",
   ["Champon — nouilles, porc, fruits de mer, dans un bouillon laiteux",
    "Castella, le gâteau portugais devenu japonais en quatre siècles",
    "Shippoku : la table sino-portugaise, à partager"],
   "Une ville à flanc de baie, seule fenêtre du Japon fermé."),

 e("kumamoto", "Kumamoto", "熊本", 3, 14, 17, "20–27 °C sur la plaine, 14–20 °C sur l'Aso",
   "Hôtel dans le centre, près du tramway", 74, "volcan", "aube",
   ["Basashi — le sashimi de cheval, spécialité locale, à goûter ou non",
    "Karashi renkon, racine de lotus fourrée à la moutarde et frite",
    "Le ramen de Kumamoto, à l'ail noir"],
   "Le plus grand cirque volcanique du monde, à une heure."),
]

KYUSHU_JOURS = (
 repris(ALPES_JOURS, [1, 2, 3]) +
 repris(ALPES_JOURS, [5], decale=-1) + [

 j(5, "fukuoka", "Descendre vers le sud", [
   b("08h30", "Vider la chambre", "", 0, "stay"),
   b("09h47", "Shinkansen Sakura jusqu'à Hakata", "3 h via Shin-Osaka. Les Sakura ont des sièges en 2+2 au lieu de 2+3 — plus larges, même prix. Bento acheté à Kyoto.", 12200, "move"),
   b("12h50", "Arrivée à Hakata", "La gare est une ville : dix étages de boutiques et de restaurants au-dessus des quais.", 0, "stay"),
   b("14h30", "Kushida-jinja", "Le sanctuaire de la ville, où l'on garde toute l'année un char de festival de dix mètres — ceux que des équipes de quartier portent en courant chaque juillet.", 0, "see"),
   b("16h00", "Le parc Ohori", "Un ancien fossé de château devenu lac, avec des îlots reliés par des ponts. Le tour fait deux kilomètres, à plat, et c'est là que la ville se promène.", 0, "walk"),
   b("19h00", "Premiers yatai", "Cent trente baraques montées chaque soir sur les trottoirs de Nakasu et Tenjin, démontées à l'aube. Huit tabourets, un rideau, du ramen et du oden. <b>C'est la spécialité de Fukuoka, et elle n'existe plus qu'ici.</b>", 2500, "eat"),
 ], note="Fukuoka est la ville la moins chère du voyage, et la mieux placée : Arita, Nagasaki et Kumamoto sont toutes à moins de deux heures."),

 j(6, "fukuoka", "Arita et Imari", [
   b("08h20", "Limited express jusqu'à Arita", "1 h 20 vers l'ouest, à travers les collines de Saga.", 2800, "move"),
   b("09h45", "Arita, la ville de la porcelaine", "<b>La première porcelaine du Japon y a été cuite en 1616</b>, par des potiers coréens amenés de force après les campagnes de Hideyoshi. La ville n'a jamais fait autre chose depuis.", 0, "see"),
   b("10h30", "Le musée Kyushu Ceramic", "Quatre siècles de production, dont la collection Shibata — dix mille pièces d'Imari d'exportation. Gratuit.", 0, "see"),
   b("12h30", "Déjeuner à Arita", "Servi dans de la porcelaine locale, forcément.", 1300, "eat"),
   b("14h00", "Le quartier des fours", "Uchiyama, une rue de kilns et d'ateliers, avec les murs de tessons — les rebuts de quatre siècles, encastrés dans les clôtures.", 0, "walk"),
   b("15h30", "Peindre une pièce", "Plusieurs ateliers font décorer une tasse au pinceau, cuite ensuite et expédiée. Compter un mois pour la recevoir.", 2500, "see"),
   b("17h00", "Retour sur Fukuoka", "", 2800, "move"),
 ]),

 j(7, "fukuoka", "Dazaifu", [
   b("09h00", "Nishitetsu jusqu'à Dazaifu", "45 minutes depuis Tenjin. Certaines rames sont décorées par un designer de trains célèbre.", 420, "move"),
   b("10h00", "Tenman-gu", "Le sanctuaire des études, où viennent les lycéens avant les examens. Six mille pruniers, et un bœuf de bronze qu'on frotte à la tête.", 0, "see"),
   b("11h30", "Komyozen-ji", "À deux minutes, et presque personne : un jardin de mousse et de pierres qu'on regarde assis sur la véranda de bois. Deux cents yens dans une boîte.", 200, "rest"),
   b("12h30", "Déjeuner", "Umegae-mochi, la galette de riz grillée fourrée de haricot rouge, vendue tout le long de l'allée.", 1200, "eat"),
   b("14h00", "Musée national de Kyushu", "Un des quatre musées nationaux du pays, dans un bâtiment de verre courbe adossé à la colline. Il raconte le Japon par ses échanges avec le continent — ce qui est tout le sujet de cet itinéraire.", 700, "see"),
   b("17h00", "Retour", "", 420, "move"),
 ]),

 j(8, "fukuoka", "Les barques de Yanagawa", [
   b("09h00", "Nishitetsu jusqu'à Yanagawa", "50 minutes vers le sud.", 870, "move"),
   b("10h15", "Descendre les canaux en barque", "Quatre cents ans de douves transformées en canaux, parcourus à la perche sur des barques à fond plat. Une heure au fil de l'eau, sous les saules et les ponts bas — le batelier chante, et il faut se baisser.", 1900, "walk"),
   b("12h00", "Unagi no seiromushi", "L'anguille de Yanagawa, cuite à la vapeur sur son riz dans un panier laqué. C'est <b>le</b> plat de la ville, et il vaut le détour à lui seul.", 3500, "eat"),
   b("14h00", "La résidence Ohana", "Une maison de daimyo avec son jardin de pins et sa salle occidentale de 1910, curieux mélange.", 700, "see"),
   b("16h30", "Retour sur Fukuoka", "", 870, "move"),
 ], note="Variante : Mojiko et Shimonoseki, à une heure — un port rétro de brique rouge, le détroit et son tunnel piéton sous la mer."),

 j(9, "fukuoka", "La ville, sans rien forcer", [
   b("09h30", "Le musée d'Asie de Fukuoka", "Le seul musée au monde consacré à l'art contemporain de toute l'Asie. Petit, très bien fait.", 200, "see"),
   b("11h30", "Shofuku-ji", "<b>Le premier temple zen du Japon</b>, fondé en 1195 par le moine qui a rapporté le thé de Chine. On y entre librement, il n'y a rien à payer et presque personne.", 0, "see"),
   b("13h00", "Ramen au comptoir", "Le tonkotsu est né ici : un bouillon d'os de porc bouilli douze heures jusqu'à devenir blanc. On commande la fermeté des nouilles, et on peut redemander une portion sèche — <i>kaedama</i>.", 900, "eat"),
   b("15h00", "Faire ses courses à Tenjin", "Les grands magasins, les sous-sols alimentaires, et les rues couvertes autour de Daimyo pour les petites boutiques.", 0, "see"),
   b("18h30", "Dernier yatai", "Choisir une baraque avec des habitués plutôt qu'une carte en anglais.", 2500, "eat"),
 ]),

 j(10, "nagasaki", "La fenêtre du Japon fermé", [
   b("09h30", "Kamome et Shinkansen Nishi-Kyushu", "1 h 30 avec un changement à Takeo-Onsen. La ligne à grande vitesse est ouverte depuis 2022 et ne va nulle part ailleurs.", 6600, "move"),
   b("11h10", "Arrivée, dépose des valises", "La ville tient dans une baie étroite : tout se fait à pied ou en tramway, à 140 ¥ le trajet.", 0, "stay"),
   b("13h30", "Dejima", "<b>Pendant deux cent dix ans, cet îlot en éventail a été le seul point de contact entre le Japon et l'Occident.</b> Les Hollandais y étaient consignés, et tout ce qui est entré de science européenne est passé par là. Une quinzaine de bâtiments ont été reconstruits à l'identique.", 520, "see"),
   b("16h00", "Le quartier chinois et le pont aux lunettes", "Shinchi, un des trois quartiers chinois du Japon. Le Megane-bashi, de 1634, se reflète en deux cercles quand la rivière est calme.", 0, "walk"),
   b("19h00", "Champon", "Nouilles épaisses, porc, fruits de mer et légumes dans un bouillon blanc — inventé ici pour nourrir les étudiants chinois pauvres.", 1200, "eat"),
 ]),

 j(11, "nagasaki", "Ce qui s'est passé ici", [
   b("09h00", "Musée de la bombe atomique", "Le 9 août 1945 à 11 h 02. Le musée est chronologique, factuel et très dur — surtout la salle des objets. Prévoir de ne rien faire de lourd après.", 200, "see"),
   b("11h00", "L'hypocentre et le parc de la Paix", "Une colonne noire marque le point exact, à cinq cents mètres au-dessus duquel la bombe a explosé. Autour, les pans de la cathédrale Urakami laissés en place.", 0, "see"),
   b("12h30", "Déjeuner tranquille", "", 1200, "eat"),
   b("14h30", "Le sanctuaire au torii d'une jambe", "Sanno-jinja : le souffle en a emporté la moitié, et il tient debout ainsi depuis. À côté, deux camphriers calcinés qui ont refeuillé l'année suivante.", 0, "see"),
   b("16h00", "Une fin d'après-midi vide", "Volontairement. Un café, la chambre, la baie.", 0, "rest"),
 ], note="La journée la plus lourde du voyage. Elle est placée en début d'étape pour ne pas finir dessus."),

 j(12, "nagasaki", "Gunkanjima", [
   b("09h00", "Bateau pour Hashima", "Une île de deux cents mètres sur quatre cents, couverte d'immeubles de béton vides — <b>la plus forte densité humaine jamais atteinte</b> quand cinq mille mineurs y vivaient. Fermée en 1974, abandonnée telle quelle.", 4500, "move"),
   b("10h30", "Débarquement", "On ne visite qu'un couloir sécurisé au sud, le reste s'écroule. La sortie est annulée si la houle dépasse 50 cm — <b>compter un jour de repli</b>.", 310, "see"),
   b("13h00", "Déjeuner au retour", "Sur le port.", 1500, "eat"),
   b("15h00", "Glover Garden", "Les maisons des marchands occidentaux du XIXᵉ, sur la pente, avec vue sur la baie. Celle de Glover est la plus ancienne maison de style occidental du Japon.", 620, "see"),
   b("17h00", "Oura, et les chrétiens cachés", "La plus ancienne église du pays. En 1865, des paysans y ont avoué à un prêtre français que leurs familles pratiquaient en secret depuis <b>sept générations</b>, sans prêtre ni livre.", 1000, "see"),
   b("20h00", "Le mont Inasa", "Téléphérique jusqu'à 333 m. La baie en fer à cheval, illuminée — une des vues de nuit les plus réputées du pays.", 1250, "see"),
 ]),

 j(13, "nagasaki", "Unzen, ou la ville", [
   b("08h30", "Bus pour Unzen", "1 h 40 par la péninsule de Shimabara.", 1850, "move"),
   b("10h30", "Les Enfers d'Unzen", "Des fumerolles en plein village, avec des passerelles entre les évents. C'est là qu'on a exécuté des chrétiens en les ébouillantant au XVIIᵉ — le lieu porte les deux histoires.", 0, "walk"),
   b("12h30", "Déjeuner et bain", "Les auberges du village ouvrent leurs bains à la journée.", 2200, "rest"),
   b("15h00", "Retour sur Nagasaki", "", 1850, "move"),
   b("18h00", "Shippoku, si l'envie est là", "La table sino-portugaise de Nagasaki, servie à partager sur un plateau rond — ce qui, au Japon, ne se fait nulle part ailleurs. Se réserve à trois minimum, donc c'est jouable.", 5000, "eat"),
 ], note="Variante si la sortie à Gunkanjima a été annulée la veille : c'est le jour de repli."),

 j(14, "kumamoto", "Le château qui se relève", [
   b("10h00", "Shinkansen via Fukuoka", "1 h 55 avec un changement à Hakata.", 9100, "move"),
   b("12h30", "Arrivée, dépose", "Le tramway dessert tout depuis la gare.", 0, "stay"),
   b("14h00", "Le château", "Un des trois grands châteaux du Japon, et ses murs incurvés que l'on disait infranchissables. <b>Le séisme de 2016 en a jeté une partie à terre</b> ; la reconstruction pierre par pierre durera jusqu'en 2052. Une passerelle surélevée traverse le chantier — on voit les murs en cours de remontage, numérotés.", 800, "see"),
   b("16h30", "Le jardin Suizenji", "Un parcours du Tokaido miniature : chaque butte est une étape de la route, dont un mont Fuji en gazon. Dessiné au XVIIᵉ autour d'une source.", 400, "walk"),
   b("19h00", "Karashi renkon", "Racine de lotus fourrée à la moutarde puis frite. Et le basashi pour qui veut essayer — Kumamoto en est la capitale.", 3000, "eat"),
 ]),

 j(15, "kumamoto", "L'Aso", [
   b("08h00", "Train pour Aso", "1 h 20 par la ligne de Hohi, qui monte dans la caldeira.", 1130, "move"),
   b("09h30", "Entrer dans le cirque", "<b>Le plus grand cirque volcanique du monde</b> : 25 km sur 18, avec quarante mille personnes qui vivent dedans, des villages, des routes et des rizières. Le rebord se voit de partout.", 0, "see"),
   b("10h30", "Le Nakadake", "Le cratère actif, fumant, qu'on approche en car jusqu'au bord. <b>L'accès ferme sans préavis</b> selon les gaz — vérifier le matin même sur le site du parc.", 1200, "see"),
   b("12h30", "Déjeuner à Kusasenri", "La prairie d'altitude, avec des chevaux en liberté et un ancien cratère devenu étang.", 1400, "eat"),
   b("14h00", "Le Komezuka", "Une colline conique parfaite, un cône de scories de cent mètres, avec une entaille au sommet — la légende dit qu'un dieu y a puisé du riz pour les affamés.", 0, "walk"),
   b("16h00", "Retour", "", 1130, "move"),
 ], note="Alternative si le cratère est fermé : Takachiho et ses gorges, où l'on descend une barque entre des orgues basaltiques sous une cascade. Trois heures de route, donc journée pleine."),

 j(16, "kumamoto", "Kurokawa", [
   b("09h00", "Bus pour Kurokawa Onsen", "2 h 30 à travers l'Aso. Un village thermal qui a refusé les néons et les grands hôtels : bois, pierre, lanternes, et une rivière au milieu.", 3000, "move"),
   b("12h00", "Le passeport des bains", "Un jeton de bois donne accès à <b>trois bains extérieurs au choix</b> parmi vingt-quatre, répartis dans les auberges du village. On circule en yukata d'un bain à l'autre.", 1500, "rest"),
   b("13h30", "Déjeuner au village", "", 1800, "eat"),
   b("17h00", "Retour à Kumamoto", "", 3000, "move"),
   b("19h30", "Dernier dîner", "", 4000, "eat"),
 ]),

 j(17, "kumamoto", "Retour par Fukuoka", [
   b("08h00", "Petit déjeuner et valises", "", 0, "stay"),
   b("09h30", "Shinkansen Sakura jusqu'à Hakata", "35 minutes. <b>Repartir de Fukuoka plutôt que de remonter sur Tokyo économise une journée entière et environ 130 € par personne.</b>", 5800, "move"),
   b("10h15", "Deux heures à Hakata", "Les sous-sols alimentaires de la gare pour les cadeaux : mentaiko sous vide, gâteaux de Kyushu.", 0, "see"),
   b("12h30", "Métro jusqu'à l'aéroport", "<b>Onze minutes depuis la gare de Hakata</b> — Fukuoka a l'aéroport le mieux placé du pays.", 260, "move"),
   b("15h30", "Vol Fukuoka → Paris", "Avec escale. Compter 20 h de porte à porte.", 0, "move"),
 ]),
])

KYUSHU_RESA = [
 r("Le vol multi-destination", "4 à 6 mois avant", "Arrivée Osaka Kansai, <b>retour depuis Fukuoka</b>. C'est ce qui rend l'itinéraire cohérent : pas de remontée sur Tokyo.", True),
 r("La sortie à Gunkanjima", "1 mois avant", "Deux compagnies, sièges limités. <b>Annulée si la houle dépasse 50 cm</b> — garder le jour 13 en repli.", True),
 r("L'atelier de porcelaine à Arita", "3 semaines avant", "La pièce est cuite après votre départ et expédiée : prévoir un mois de délai."),
 r("Le shippoku de Nagasaki", "2 semaines avant", "Se commande à l'avance et pour trois personnes minimum."),
 r("Les hôtels", "2 à 3 mois avant", "Kyushu est nettement moins tendu que le Kansai — mais la chambre à trois reste ce qui limite."),
 r("L'état du cratère de l'Aso", "le matin même", "Le site du parc national publie le niveau de gaz. L'accès ferme sans préavis."),
]

KYUSHU_BUDGET = [
 ("Vol A/R", "Arrivée Osaka, retour Fukuoka, 2 × 23 kg", 780),
 ("Hébergement", "16 nuits en chambre à trois, aucune nuit de montagne", 428),
 ("Transport", "265 € de trajets et d'excursions, 7 €/jour de local", 377),
 ("Nourriture", "40 € par jour et par personne", 680),
 ("Activités", "Entrées, Gunkanjima, atelier de porcelaine", 132),
 ("Divers", "eSIM, assurance, souvenirs", 100),
]


# ══════════════════════════════════════════════════════════════════════
#  3 · Trois villes, trois semaines — 15 nuits, 3 étapes, 2 537 €
# ══════════════════════════════════════════════════════════════════════

TROIS_ETAPES = [
 e("kyoto", "Kyoto", "京都", 5, 1, 6, "18–24 °C, sec",
   "Machiya ou hôtel vers Karasuma-Oike", 98, "pagode", "soir",
   ["Kaiseki au comptoir, une fois", "Tofu de Nanzen-ji, obanzai le soir",
    "Nishiki pour le déjeuner debout"],
   "Deux journées en ville, trois en excursion, toutes à moins d'une heure."),

 e("kanazawa", "Kanazawa", "金沢", 5, 6, 11, "16–24 °C, averses possibles",
   "Hôtel près du marché Omicho", 80, "torii", "jour",
   ["Kaisendon au marché Omicho, à 8 h", "Jibuni, le canard mijoté local",
    "Feuille d'or sur un thé, au moins pour voir"],
   "Le cœur du voyage, et la base d'où l'on atteint montagne et village."),

 e("tokyo", "Tokyo", "東京", 5, 11, 16, "19–26 °C",
   "Yanaka ou Nezu, le vieux Tokyo", 92, "tour", "soir",
   ["Tsukiji le matin, debout", "Un izakaya de Yanaka sans carte en anglais",
    "Les dépachika pour les cadeaux"],
   "Cinq nuits pour finir, deux journées en ville, deux en excursion."),
]

TROIS_JOURS = (
 repris(ALPES_JOURS, [1, 2, 3, 4, 5]) + [

 j(6, "kanazawa", "Vers la mer du Japon", [
   b("08h30", "Vider la chambre", "", 0, "stay"),
   b("09h42", "Thunderbird jusqu'à Tsuruga", "Puis Shinkansen Hokuriku. 2 h 15 en tout depuis 2024, avec un changement de quai simple.", 9100, "move"),
   b("12h00", "Arrivée, dépose des valises", "La gare est couverte d'un immense portique de bois, le Tsuzumi-mon, en forme de tambour de théâtre nô.", 0, "stay"),
   b("14h00", "Higashi Chaya", "Le quartier des maisons de thé, aux façades de lattes de bois. Shima et Kaikaro se visitent à l'intérieur, salons à l'étage et feuille d'or aux murs.", 750, "see"),
   b("16h00", "Poser la feuille d'or soi-même", "Un dixième de micron : elle se déchire au moindre souffle. On décore une boîte ou des baguettes, et on repart avec.", 1500, "see"),
   b("19h00", "Jibuni", "Le canard mijoté de Kanazawa, lié à la fécule, avec du wasabi frais.", 3000, "eat"),
 ]),

 j(7, "kanazawa", "La route alpine et la plus haute cascade", [
   b("07h30", "Shinkansen jusqu'à Toyama", "23 minutes.", 3000, "move"),
   b("08h30", "Toyama → Murodo", "Train de montagne, funiculaire, car. Deux heures, de 200 à 2 450 m.", 9500, "move"),
   b("11h00", "Le mur de neige", "Un corridor taillé dans une congère de dix à quinze mètres. Il tient jusqu'à mi-juin.", 0, "walk"),
   b("12h30", "Déjeuner à Murodo", "", 1500, "eat"),
   b("13h30", "L'étang Mikuri", "Une heure de tour, sur la neige en mai. Le Tateyama s'y reflète par temps clair.", 0, "walk"),
   b("15h30", "Shomyo-daki, au pied", "<b>La plus haute cascade du Japon</b> : 350 m en quatre paliers. Au printemps, la fonte lui adjoint la Hannoki, plus haute encore mais saisonnière — les deux tombent côte à côte.", 0, "see"),
   b("18h30", "Retour à Kanazawa", "", 3000, "move"),
 ], note="Environ 90 € par personne. Vérifier l'ouverture de la route — la neige décide."),

 j(8, "kanazawa", "Shirakawa-go à la journée", [
   b("08h10", "Premier bus Hokutetsu", "1 h 15. <b>Prendre le tout premier</b> : entre 8 h 30 et 10 h, avant les cars, le village est encore calme.", 2600, "move"),
   b("09h30", "Le village", "Les maisons à mains jointes, charpentées sans un seul clou, dont les combles abritaient l'élevage des vers à soie.", 0, "walk"),
   b("10h30", "Wada-ke", "La maison du chef de village, la plus grande ouverte à la visite. Monter dans les combles voir la charpente.", 400, "see"),
   b("12h00", "Déjeuner", "Truite grillée à la broche, soba, légumes de montagne.", 1500, "eat"),
   b("13h30", "Le Minkaen, sur l'autre rive", "Vingt-cinq maisons remontées, bien plus tranquille que le village. Démonstrations de réfection de toiture certains jours.", 600, "see"),
   b("15h30", "Shiroyama", "Vingt minutes de montée jusqu'au belvédère. En mai-juin, les rizières en eau doublent le village en reflet.", 0, "walk"),
   b("17h00", "Retour sur Kanazawa", "", 2600, "move"),
 ], note="C'est le compromis de cet itinéraire : on voit le village, on ne le voit pas vide. La nuit sur place coûte 180 € la chambre."),

 j(9, "kanazawa", "Le marché, le jardin, les samouraïs", [
   b("07h00", "Kenrokuen avant l'heure", "<b>Entrée gratuite avant 7 h.</b> Un des trois grands jardins du Japon, dessiné sur deux siècles, et vide à cette heure-là.", 0, "walk"),
   b("08h30", "Marché Omicho", "Crabe des neiges, crevettes douces, oursins. Un kaisendon au comptoir pour le petit déjeuner.", 2500, "eat"),
   b("10h30", "Nagamachi", "Le quartier des samouraïs, murs de terre protégés par des nattes de paille. La maison Nomura se visite, jardin compris.", 550, "see"),
   b("13h00", "Musée du XXIᵉ siècle", "Un disque de verre sans façade ni entrée principale. La piscine de Leandro Erlich se regarde par en dessous. Créneau à réserver en ligne.", 1200, "see"),
   b("15h30", "Musée de la feuille d'or", "Quatre heures de battage pour amener un gramme à un mètre carré.", 310, "see"),
   b("18h30", "Comptoir de sushi", "Un omakase de quartier, pas un comptoir à touristes.", 6000, "eat"),
 ]),

 j(10, "kanazawa", "La côte de Noto", [
   b("08h30", "Prendre la voiture", "Environ 70 € la journée pour le groupe. <b>Permis international obligatoire</b>, à demander en préfecture avant de partir.", 0, "move"),
   b("10h30", "Senmaida", "Mille rizières en terrasses qui dévalent jusqu'à la mer. En mai elles sont en eau, donc en miroir.", 0, "see"),
   b("12h30", "Déjeuner à Wajima", "Poisson du port, dans une ville qui se relève du séisme de 2024.", 1800, "eat"),
   b("14h00", "La laque de Wajima", "Cent couches, chacune poncée. Le musée montre les étapes, des ateliers laissent entrer.", 630, "see"),
   b("16h00", "La route côtière", "Falaises et rochers de Ganmon sur le retour. Deux heures.", 0, "move"),
 ], note="Sans voiture : le Myoryu-ji, le temple aux pièges, et le musée D.T. Suzuki — deux salles et un bassin, le lieu le plus calme de la ville."),

 j(11, "tokyo", "Traversée", [
   b("09h00", "Kagayaki jusqu'à Tokyo", "2 h 30, direct. Réserver la veille. Côté droit après Nagano pour les montagnes.", 14000, "move"),
   b("12h00", "Poser les valises à Yanaka", "Ruelles basses, temples, un cimetière ombragé et des chats.", 0, "stay"),
   b("14h00", "Yanaka à pied", "Épargné par le séisme de 1923 et par les bombardements. On y marche sans but.", 0, "walk"),
   b("16h00", "Yanaka Ginza", "Une rue commerçante en pente où l'on grignote debout.", 800, "eat"),
   b("19h00", "Izakaya de quartier", "Sans carte en anglais, avec des habitués.", 3000, "eat"),
 ]),

 j(12, "tokyo", "Mont Takao", [
   b("08h00", "Keio jusqu'à Takaosanguchi", "50 minutes depuis Shinjuku, pour 599 m de montagne.", 430, "move"),
   b("09h00", "Le sentier 6", "Il remonte un ruisseau en forêt et passe la chute de Biwa. 1 h 30, de l'ombre tout du long, et le moins fréquenté des huit sentiers.", 0, "walk"),
   b("10h45", "Yakuo-in", "Un temple de montagne aux statues de tengu, à mi-pente.", 0, "see"),
   b("11h45", "Le sommet", "Le Fuji au sud-ouest par temps clair. Soba et bière aux échoppes du haut.", 1000, "eat"),
   b("13h30", "Funiculaire", "Un des plus raides du pays, et bienvenu à la descente.", 490, "move"),
   b("15h00", "Bain à Takaosan Onsen", "Contre la gare, à la sortie du sentier.", 1100, "rest"),
   b("18h30", "Retour", "", 430, "move"),
 ], note="À faire en semaine — c'est la montagne du dimanche des Tokyoïtes."),

 j(13, "tokyo", "Nikko", [
   b("07h30", "Tobu depuis Asakusa", "1 h 50 en limited express. Le Nikko All Area Pass couvre le train et les bus sur place.", 2900, "move"),
   b("09h30", "Tosho-gu", "Le mausolée de Tokugawa Ieyasu, qui croule sous les sculptures polychromes — <b>tout l'inverse de la sobriété japonaise</b>, et c'est le sujet. Les trois singes et le chat endormi y sont.", 1600, "see"),
   b("11h30", "Bus vers le lac Chuzenji", "45 minutes par les vingt-huit lacets de l'Irohazaka, à sens unique.", 1250, "move"),
   b("12h30", "Les chutes de Kegon", "97 m d'un seul jet. Un ascenseur descend cent mètres dans la roche jusqu'à une plateforme au pied — c'est là qu'on les regarde.", 570, "see"),
   b("14h00", "Déjeuner au bord du lac", "Truite du lac, ou yuba, la peau de lait de soja dont Nikko a fait sa spécialité.", 1500, "eat"),
   b("15h00", "Le marais de Senjogahara", "Deux heures de caillebotis <b>parfaitement plats</b> à 1 400 m, à travers un ancien lac comblé. Bouleaux, ruisseaux, et le Nantai en fond.", 0, "walk"),
   b("18h30", "Retour sur Tokyo", "", 2900, "move"),
 ], note="Journée longue mais sans difficulté. C'est ce qui manquait à la version deux jours : ici Nikko a sa journée entière."),

 j(14, "tokyo", "Maisons et couteaux", [
   b("09h00", "Musée en plein air de l'architecture Edo-Tokyo", "À Koganei. Trente maisons et boutiques sauvées de la démolition : bains publics, taverne, échoppe de teinturier, villa moderniste. Le pendant urbain de Hida no Sato, et presque personne n'y va.", 400, "see"),
   b("13h00", "Déjeuner sur place", "", 1000, "eat"),
   b("15h00", "Kappabashi", "Couteaux forgés, moules à pâtisserie, vaisselle au kilo. Un couteau qui durera trente ans, gravé devant soi.", 0, "see"),
   b("17h30", "Senso-ji en fin de journée", "La grande lanterne, et Nakamise vidée de ses cars.", 0, "walk"),
   b("19h00", "Dernier vrai dîner", "", 6000, "eat"),
 ]),

 j(15, "tokyo", "Le jour sans programme", [
   b("07h00", "Tsukiji, le marché extérieur", "Oursin, omelette dashi, thé grillé, debout, à sept heures.", 2000, "eat"),
   b("10h00", "Ce qui a manqué", "Une journée volontairement vide, en fin de séjour, pour y mettre ce qu'on a raté ou ce qu'on veut refaire. C'est le luxe des cinq nuits par base.", 0, "rest"),
   b("15h00", "Dépachika", "Les sous-sols de Ginza pour les cadeaux : thés, sucreries, sauces, emballés comme des bijoux.", 0, "see"),
   b("19h00", "Dernier izakaya", "", 3500, "eat"),
 ]),

 j(16, "tokyo", "Retour", [
   b("09h00", "Boucler les valises", "Prévoir large : la pesée compte, avec deux fois 23 kg.", 0, "stay"),
   b("13h00", "Monorail jusqu'à Haneda", "30 minutes depuis Hamamatsucho. Au comptoir 3 h avant.", 500, "move"),
   b("18h55", "Vol Haneda → Helsinki → Paris", "Environ 18 h avec l'escale.", 0, "move"),
 ]),
])

TROIS_RESA = [
 r("Le vol multi-destination Finnair", "4 à 6 mois avant", "Arrivée Osaka Kansai, départ Tokyo Haneda.", True),
 r("Les hôtels, trois seulement", "3 mois avant", "L'avantage de la trame : trois réservations au lieu de cinq, cinq nuits chacune. La chambre à trois reste ce qui limite.", True),
 r("La route alpine Tateyama-Kurobe", "1 mois avant", "Billet combiné en ligne. Ouverture mi-avril à fin novembre."),
 r("Le bus pour Shirakawa-go", "1 mois avant", "Hokutetsu, sièges numérotés. Prendre le premier départ."),
 r("Le musée du XXIᵉ siècle", "2 semaines avant", "Créneau horaire à réserver en ligne pour les expositions payantes."),
 r("La voiture pour Noto", "2 semaines avant", "Et le permis international, plusieurs semaines à l'avance."),
 r("Les deux trains longs", "la veille", "Kyoto → Kanazawa, et Kanazawa → Tokyo. Ce sont les deux seuls du voyage."),
]

TROIS_BUDGET = [
 ("Vol A/R", "Finnair, arrivée Osaka, départ Tokyo, 2 × 23 kg", 750),
 ("Hébergement", "15 nuits en chambre à trois, aucune nuit de montagne", 450),
 ("Transport", "230 € de trajets et d'excursions, 7 €/jour de local", 342),
 ("Nourriture", "40 € par jour et par personne", 640),
 ("Activités", "Entrées, route alpine, Nikko compris", 155),
 ("Divers", "eSIM, assurance, souvenirs", 200),
]


# ══════════════════════════════════════════════════════════════════════

TRAMES = [
 {"id": "alpes", "nom": "Des cascades et des ateliers", "kanji": "山",
  "deck": "Construit sur ce que tu n'as pas encore vu — Kanazawa, Shirakawa-go, la haute montagne — "
          "et sur ce qui compte pour tes parents : l'eau et le relief, la table, les mains qui fabriquent.",
  "nuits": 18, "trajet": "7 h 35", "par_pers": 2972,
  "vol": {"in": "KIX", "out": "HND"},
  "etapes": ALPES_ETAPES, "jours": ALPES_JOURS, "resa": ALPES_RESA, "budget": ALPES_BUDGET,
  "carte": ('[{id:"kyoto",nights:5},{id:"takayama",nights:5},{id:"shirakawago",nights:1,anchor:"w"},'
            '{id:"kanazawa",nights:4,anchor:"w"},{id:"tokyo",nights:3,anchor:"e"}]',
            '[{from:"takayama",to:"kamikochi",anchor:"s"},{from:"kanazawa",to:"toyama",anchor:"e"}]',
            '{in:"KIX",out:"HND"}')},

 {"id": "kyushu", "nom": "La porcelaine et la mémoire", "kanji": "焼",
  "deck": "Une île entièrement neuve pour vous trois, la seule fenêtre du Japon fermé, le plus grand "
          "cirque volcanique du monde — et le retour depuis Fukuoka, qui évite de remonter sur Tokyo.",
  "nuits": 16, "trajet": "2 h 35", "par_pers": 2497,
  "vol": {"in": "KIX", "out": "FUK"},
  "etapes": KYUSHU_ETAPES, "jours": KYUSHU_JOURS, "resa": KYUSHU_RESA, "budget": KYUSHU_BUDGET,
  "carte": ('[{id:"kyoto",nights:4},{id:"fukuoka",nights:5,anchor:"n"},'
            '{id:"nagasaki",nights:4,anchor:"w"},{id:"kumamoto",nights:3,anchor:"e"}]',
            '[{from:"fukuoka",to:"arita",anchor:"n"},{from:"kumamoto",to:"aso",anchor:"e"}]',
            '{in:"KIX",out:"FUK"}')},

 {"id": "trois", "nom": "Trois villes, trois semaines", "kanji": "三",
  "deck": "Le rythme le plus doux : trois bases, cinq nuits chacune, deux trains dans tout le voyage. "
          "On dort dans les villes les moins chères et on va voir la montagne à la journée.",
  "nuits": 15, "trajet": "4 h 45", "par_pers": 2537,
  "vol": {"in": "KIX", "out": "HND"},
  "etapes": TROIS_ETAPES, "jours": TROIS_JOURS, "resa": TROIS_RESA, "budget": TROIS_BUDGET,
  "carte": ('[{id:"kyoto",nights:5},{id:"kanazawa",nights:5,anchor:"w"},{id:"tokyo",nights:5,anchor:"e"}]',
            '[{from:"kanazawa",to:"shirakawago",anchor:"w"},{from:"tokyo",to:"nikko",anchor:"e"}]',
            '{in:"KIX",out:"HND"}')},
]


def note_sur(jour, texte):
    """Une copie d'une journée reprise, avec sa note remplacée — l'hiver change les consignes."""
    d = dict(jour)
    d["note"] = texte
    return d


# ══════════════════════════════════════════════════════════════════════
#  4 · Tokyo et Kyushu — 18 nuits, 4 étapes, fin février à mi-mars
#      Bâti sur la promotion ANA TOKYO+ : les deux vols intérieurs sont
#      compris dans le billet international.
# ══════════════════════════════════════════════════════════════════════

TK_ETAPES = [
 e("tokyo", "Tokyo", "東京", 6, 1, 7, "6–13 °C, sec et lumineux — le Fuji se voit",
   "Yanaka ou Nezu, le vieux Tokyo, bas et calme", 92, "tour", "aube",
   ["Tsukiji le matin, debout : oursin, omelette dashi, thé grillé",
    "Un izakaya de Yanaka, sans carte en anglais",
    "Monjayaki, la version tokyoïte de l'okonomiyaki, qu'on cuit soi-même"],
   "Six nuits, dont trois journées entières hors de la ville."),

 e("fukuoka", "Fukuoka", "福岡", 5, 7, 12, "9–15 °C, doux pour la saison",
   "Vers Nakasu ou Hakata, à dix minutes de la gare", 76, "torii", "jour",
   ["Les <b>yatai</b> — cent trente baraques de rue montées chaque soir",
    "Tonkotsu ramen, le bouillon d'os de porc, né ici",
    "Mentaiko, œufs de morue au piment, sur du riz blanc"],
   "La base la moins chère, et la porte de la porcelaine."),

 e("nagasaki", "Nagasaki", "長崎", 4, 12, 16, "8–14 °C, la mer tempère",
   "Sur les pentes, vers Glover ou Dejima", 78, "vague", "soir",
   ["Champon — nouilles, porc, fruits de mer, bouillon laiteux",
    "Castella, le gâteau portugais devenu japonais en quatre siècles",
    "Shippoku : la table sino-portugaise, à partager"],
   "Une ville à flanc de baie, seule fenêtre du Japon fermé."),

 e("kumamoto", "Kumamoto", "熊本", 3, 16, 19, "8–15 °C en ville, 0–8 °C sur l'Aso",
   "Dans le centre, près du tramway", 74, "volcan", "aube",
   ["Basashi — le sashimi de cheval, spécialité locale",
    "Karashi renkon, racine de lotus à la moutarde, frite",
    "Le ramen de Kumamoto, à l'ail noir"],
   "Le plus grand cirque volcanique du monde, à une heure."),
]

TK_JOURS = sorted(
 [
 j(1, "tokyo", "Arrivée", [
   b("11h35", "Départ Paris CDG", "ANA, vol direct. Douze heures, sans escale — c'est ce qu'on achète avec ce billet.", 0, "move"),
   b("07h05", "Atterrissage à Haneda", "Le lendemain matin, heure de Tokyo. Immigration et bagages : une heure. <b>Visit Japan Web</b> rempli dans l'avion fait gagner la file.", 0, "move"),
   b("08h45", "Monorail puis Yamanote", "40 minutes jusqu'à Nippori. Prendre une carte Suica au distributeur de la gare : elle sert dans tous les transports et dans les supérettes.", 800, "move"),
   b("10h00", "Déposer les valises", "Le check-in est à 15 h, mais tous les hôtels gardent les bagages. Ressortir tout de suite : c'est ce qui règle le décalage.", 0, "stay"),
   b("11h00", "Yanaka, sans but", "Un des rares quartiers épargnés par le séisme de 1923 et par les bombardements de 1945. Ruelles basses, temples, un cimetière planté de cerisiers, et des chats.", 0, "walk"),
   b("13h00", "Yanaka Ginza", "Une rue commerçante d'après-guerre, en pente, où l'on grignote debout : croquettes, brochettes, dorayaki tièdes.", 900, "eat"),
   b("16h00", "Tenir jusqu'à 21 h", "Le décalage est de 8 h en hiver. Se coucher à 19 h coûte trois jours de réveils à 3 h du matin.", 0, "rest"),
   b("18h30", "Premier izakaya", "Sans carte en anglais, avec des habitués. Montrer du doigt fonctionne très bien.", 3000, "eat"),
 ], note="En février, la nuit tombe vers 17 h 30 et le jour se lève à 6 h 20. Les journées d'excursion partent tôt."),

 j(2, "tokyo", "Le vieux Tokyo", [
   b("06h30", "Tsukiji, le marché extérieur", "Le marché aux poissons a déménagé à Toyosu, mais les échoppes de rue sont restées. Oursin, omelette dashi, thé grillé, debout, au petit matin. C'est l'heure où le décalage vous réveille de toute façon.", 2000, "eat"),
   b("09h00", "Hama-rikyu", "Un jardin de daimyo coincé entre les tours, avec un bassin qui monte et descend avec la marée — le seul du pays. En février, les pruniers y sont en fleurs et la maison de thé sur l'île sert le matcha.", 500, "walk"),
   b("11h30", "Senso-ji et Nakamise", "Le plus vieux temple de Tokyo, et la rue d'échoppes qui y mène. En semaine et hors saison, c'est encore respirable.", 0, "see"),
   b("14h00", "Kappabashi", "La rue des fournisseurs de restaurants, à dix minutes à pied. Couteaux forgés, moules à pâtisserie, vaisselle au kilo, répliques de plats en résine. <b>C'est là qu'on achète un couteau qui durera trente ans</b>, gravé à son nom devant soi. Y aller maintenant : on repassera le dernier jour si l'envie tient.", 0, "see"),
   b("17h00", "Bain public de quartier", "Un sento de Yanaka, à 550 ¥. Ce n'est pas un onsen de luxe, c'est le bain du coin — et c'est exactement l'intérêt.", 550, "rest"),
 ]),

 j(3, "tokyo", "Nikko", [
   b("07h30", "Tobu depuis Asakusa", "1 h 50 en limited express. Le Nikko All Area Pass couvre le train et les bus sur place.", 2900, "move"),
   b("09h30", "Tosho-gu sous la neige", "Le mausolée de Tokugawa Ieyasu, qui croule sous les sculptures polychromes — <b>tout l'inverse de la sobriété japonaise</b>, et c'est le sujet. Les trois singes, le chat endormi. En hiver, la neige sur les toits de bronze et l'absence de cars valent le froid.", 1600, "see"),
   b("11h30", "Bus vers le lac Chuzenji", "45 minutes par les vingt-huit lacets de l'Irohazaka. <b>Vérifier l'état de la route la veille</b> : elle ferme par forte neige, et les bus montent alors avec des chaînes.", 1250, "move"),
   b("12h30", "Les chutes de Kegon", "97 m d'un seul jet, et un ascenseur qui descend cent mètres dans la roche jusqu'à une plateforme au pied. <b>En février, les embruns gèlent sur les parois</b> et les cascades secondaires du cirque se figent en colonnes de glace — c'est la meilleure saison pour les voir.", 570, "see"),
   b("14h00", "Déjeuner au bord du lac", "Truite du lac, ou yuba — la peau de lait de soja dont Nikko a fait sa spécialité, servie brûlante.", 1500, "eat"),
   b("15h30", "Redescente", "Le marais de Senjogahara est sous la neige : ses caillebotis ne se marchent qu'en raquettes de décembre à mars. On le laisse pour une autre saison.", 1250, "move"),
   b("18h30", "Retour sur Tokyo", "", 2900, "move"),
 ], note="Journée longue et froide : 0 à 6 °C au lac, plusieurs degrés de moins qu'à Tokyo. Prévoir gants et bonnet, et vérifier la météo la veille."),

 j(4, "tokyo", "Kamakura", [
   b("08h40", "Ligne JR Yokosuka", "55 minutes depuis Tokyo. L'ancienne capitale militaire du Japon, de 1185 à 1333, coincée entre les collines et la mer.", 950, "move"),
   b("10h00", "Le Grand Bouddha", "Onze mètres de bronze, en plein air depuis qu'un raz-de-marée a emporté son pavillon en 1498. On entre à l'intérieur pour vingt yens.", 320, "see"),
   b("11h00", "Hase-dera", "À dix minutes. Une Kannon de bois de neuf mètres, un jardin en terrasses qui descend vers la baie, et une grotte de divinités taillées dans la roche. En février, les pruniers du jardin sont en fleurs.", 400, "see"),
   b("12h30", "Déjeuner", "Shirasu-don : les alevins de sardine de la baie, crus ou bouillis, sur du riz. On les pêche ici.", 1400, "eat"),
   b("14h00", "Le sentier de Daibutsu", "Une heure et demie de crête boisée entre les temples, par les collines qui protégeaient la ville. Dénivelé modéré, racines et marches, et des vues sur la baie.", 0, "walk"),
   b("16h00", "Hokoku-ji", "La bambouseraie, plus petite que celle d'Arashiyama et infiniment plus calme. On boit un matcha assis face aux bambous, compris dans l'entrée.", 900, "rest"),
   b("18h00", "Retour", "", 950, "move"),
 ]),

 j(5, "tokyo", "Mont Takao", [
   b("08h00", "Keio jusqu'à Takaosanguchi", "50 minutes depuis Shinjuku, pour 599 m de montagne — ce qui est absurde et formidable.", 430, "move"),
   b("09h00", "Le sentier 6", "Il remonte un ruisseau en forêt et passe la petite chute de Biwa. 1 h 30, quelques passages dans le lit du cours d'eau. <b>En février, vérifier qu'il est ouvert</b> : il ferme parfois pour verglas, et le sentier 1, bitumé, prend le relais.", 0, "walk"),
   b("10h45", "Yakuo-in", "À mi-pente, un temple de montagne aux statues de tengu — les créatures à long nez, gardiennes de la forêt.", 0, "see"),
   b("11h45", "Le sommet, et le Fuji", "<b>L'hiver est la meilleure saison pour le voir</b> : l'air sec de février le rend net presque un jour sur deux, contre un sur cinq en été. Il est au sud-ouest, enneigé jusqu'à mi-hauteur.", 1000, "eat"),
   b("13h30", "Funiculaire", "Un des plus raides du pays, et bienvenu à la descente.", 490, "move"),
   b("14h30", "Les pruniers de la vallée", "Entre Takaosanguchi et Ume-no-sato, <b>dix mille pruniers</b> le long de la rivière et de la vieille route. Fin février, ils sont ouverts — c'est la première floraison de l'année, un mois avant les cerisiers, et personne ne se déplace pour elle.", 0, "walk"),
   b("16h30", "Bain à Takaosan Onsen", "Contre la gare, à la sortie du sentier. Bains extérieurs, et on repart propre.", 1100, "rest"),
 ], note="À faire en semaine : le Takao est la montagne du dimanche des Tokyoïtes."),

 j(6, "tokyo", "Comment on vivait ici", [
   b("09h00", "Musée en plein air de l'architecture Edo-Tokyo", "À Koganei, quarante minutes. Trente maisons et boutiques sauvées de la démolition et remontées : bains publics, taverne, échoppe de teinturier, villa moderniste de 1942. <b>C'est le meilleur endroit du voyage pour comprendre comment on vivait ici</b>, et presque personne n'y va.", 400, "see"),
   b("12h30", "Déjeuner sur place", "La cantine du musée, dans une ancienne maison de thé.", 1000, "eat"),
   b("14h30", "Nezu-jinja", "Retour vers Yanaka. Un sanctuaire de 1705 épargné par les bombes, avec un tunnel de petits torii rouges — celui de Fushimi Inari en miniature, sans la file.", 0, "see"),
   b("16h00", "Ce qu'on a repéré", "Fin d'après-midi libre : Kappabashi si le couteau a mûri, un dépachika de Ginza pour les premiers cadeaux, ou rien du tout.", 0, "rest"),
   b("19h00", "Monjayaki", "La version tokyoïte de l'okonomiyaki : une pâte plus liquide qu'on cuit soi-même sur la plaque et qu'on racle avec de petites spatules. On en met partout, c'est prévu.", 2500, "eat"),
 ]),

 j(7, "fukuoka", "Le premier vol offert", [
   b("08h30", "Vider la chambre", "", 0, "stay"),
   b("09h30", "Monorail jusqu'à Haneda", "30 minutes depuis Hamamatsucho. Terminal intérieur, pas international.", 500, "move"),
   b("11h30", "Vol Haneda → Fukuoka", "1 h 50. <b>Compris dans le billet international</b> — c'est tout l'intérêt de cette trame. Les règles bagages de l'international s'appliquent au segment intérieur.", 0, "move"),
   b("13h20", "Arrivée à Fukuoka", "<b>Onze minutes de métro entre l'aéroport et la gare de Hakata</b> : Fukuoka a l'aéroport le mieux placé du pays.", 260, "move"),
   b("14h30", "Kushida-jinja", "Le sanctuaire de la ville, où l'on garde toute l'année un char de festival de dix mètres — ceux que des équipes de quartier portent en courant chaque juillet.", 0, "see"),
   b("16h00", "Le parc Ohori", "Un ancien fossé de château devenu lac, avec des îlots reliés par des ponts. Deux kilomètres à plat, et c'est là que la ville se promène.", 0, "walk"),
   b("19h00", "Premiers yatai", "Cent trente baraques montées chaque soir sur les trottoirs de Nakasu et Tenjin, démontées à l'aube. Huit tabourets, un rideau, du ramen et du oden. <b>Ça n'existe plus qu'ici.</b>", 2500, "eat"),
 ], note="Deux heures de porte à porte contre cinq heures de Shinkansen — et le vol ne coûte rien. C'est ce que la promotion achète."),
 ]
 + [note_sur(x, "Fin février, les six mille pruniers du sanctuaire sont en fleurs. C'est la raison de placer Dazaifu tôt dans l'étape : la floraison ne dure pas.")
    if x["n"] == 8 else x
    for x in repris(KYUSHU_JOURS, [7], decale=1)]
 + repris(KYUSHU_JOURS, [6], decale=3)
 + [note_sur(x, "Les <b>sagemon</b> — des mobiles de poupées et d'ornements cousus, suspendus dans les maisons de marchands — s'exposent de mi-février à début avril pour le Hinamatsuri. À confirmer sur le site de la ville, les dates bougent d'une année sur l'autre.")
    if x["n"] == 10 else x
    for x in repris(KYUSHU_JOURS, [8], decale=2)]
 + repris(KYUSHU_JOURS, [9, 10, 11, 12, 13, 14], decale=2)
 + [note_sur(x, "En mars, la caldeira est verte et le sommet parfois blanc. <b>La route du cratère ferme sans préavis</b> selon les gaz, et par neige : vérifier le matin même sur le site du parc national.")
    if x["n"] == 17 else x
    for x in repris(KYUSHU_JOURS, [15], decale=2)]
 + [note_sur(x, "De décembre à mars, le village allume chaque soir les <b>yuakari</b> : des lanternes de bambou tressé posées le long de la rivière. C'est la saison où Kurokawa est le plus beau — et la plus froide, donc la meilleure pour les bains extérieurs. Dates à confirmer auprès du syndicat d'initiative.")
    if x["n"] == 18 else x
    for x in repris(KYUSHU_JOURS, [16], decale=2)]
 + [
 j(19, "kumamoto", "Retour par le second vol offert", [
   b("07h00", "Petit déjeuner et valises", "Prévoir large à la pesée : Kappabashi, Arita et les dépachika laissent des traces.", 0, "stay"),
   b("08h30", "Aéroport de Kumamoto", "50 minutes de bus depuis le centre.", 1000, "move"),
   b("10h20", "Vol Kumamoto → Haneda", "1 h 50, <b>compris dans le billet</b>. Même réservation que l'international : en cas de retard, ANA réachemine — c'est l'avantage du billet unique sur deux billets séparés.", 0, "move"),
   b("12h10", "Correspondance à Haneda", "Passage du terminal intérieur à l'international par navette, quinze minutes. Compter trois heures entre les deux vols.", 0, "move"),
   b("15h05", "Vol Haneda → Paris CDG", "Douze heures, direct. Départ en début d'après-midi, arrivée à Paris en fin d'après-midi le même jour.", 0, "move"),
 ], note="Le voyage doit être terminé avant le 15 mars 2027 : ce retour est le dernier utilisable."),
 ],
 key=lambda x: x["n"])

TK_RESA = [
 r("Le billet ANA avec la promotion TOKYO+", "<b>avant le 30 septembre 2026</b>",
   "La mise en vente ne dure qu'un mois. <b>Vérifier sur le tunnel la franchise bagages pour trois passagers</b> — le tableau officiel du passage de 2 à 1 pièce ne couvre que les départs du Japon, pas de Paris — et la durée de séjour maximale du tarif.", True),
 r("Les deux vols intérieurs", "à la réservation du billet",
   "Haneda → Fukuoka et Kumamoto → Haneda, à demander <b>dans la même réservation</b>. Les aéroports d'entrée et de sortie peuvent différer : c'est ce qui rend cette trame possible.", True),
 r("La sortie à Gunkanjima", "2 mois avant",
   "Deux compagnies, sièges limités. <b>Annulée si la houle dépasse 50 cm</b>, et l'hiver est la saison la plus agitée — garder le jour 15 en repli.", True),
 r("Les hôtels", "3 mois avant", "Quatre réservations seulement. La chambre à trois reste ce qui limite le choix, à Tokyo surtout."),
 r("L'atelier de porcelaine à Arita", "3 semaines avant", "La pièce est cuite après votre départ et expédiée : compter un mois."),
 r("Le shippoku de Nagasaki", "2 semaines avant", "Se commande à l'avance, et pour trois personnes minimum — ce qui tombe bien."),
 r("Le Nikko All Area Pass", "la veille", "Couvre le train Tobu et les bus du lac. Se prend au guichet d'Asakusa."),
 r("L'état de la route de l'Irohazaka et du cratère de l'Aso", "le matin même", "Les deux ferment sans préavis, l'une par neige, l'autre par les gaz."),
]

TK_BUDGET = [
 ("Vol A/R", "ANA direct CDG–Haneda, <b>deux vols intérieurs compris</b>", 893),
 ("Hébergement", "18 nuits en chambre à trois, aucune nuit de montagne", 489),
 ("Transport", "95 € entre les étapes, 164 € d'excursions, 7 €/jour de local", 392),
 ("Nourriture", "40 € par jour et par personne", 760),
 ("Activités", "Entrées, Gunkanjima, atelier de porcelaine", 145),
 ("Divers", "eSIM, assurance, souvenirs", 200),
]

TRAMES.append({
 "id": "tokyo-kyushu", "nom": "Tokyo et Kyushu", "kanji": "翼",
 "deck": "Bâti sur la promotion ANA TOKYO+ : les deux vols intérieurs sont compris dans le billet. "
         "Tokyo et ses alentours pour commencer, puis Kyushu d'un bout à l'autre — et le retour par "
         "Kumamoto, sans jamais refaire un trajet en sens inverse.",
 "nuits": 18, "trajet": "7 h 05", "par_pers": sum(x[2] for x in TK_BUDGET),
 "vol": {"in": "HND", "out": "HND"}, "vols": True,
 "etapes": TK_ETAPES, "jours": TK_JOURS, "resa": TK_RESA, "budget": TK_BUDGET,
 "carte": ('[{id:"tokyo",nights:6,anchor:"e"},{id:"fukuoka",nights:5,air:true,anchor:"n"},'
           '{id:"nagasaki",nights:4,anchor:"w"},{id:"kumamoto",nights:3,anchor:"s"}]',
           '[{from:"tokyo",to:"nikko",anchor:"e"},{from:"tokyo",to:"kamakura",anchor:"s"},'
           '{from:"fukuoka",to:"arita",anchor:"n"},{from:"kumamoto",to:"aso",anchor:"e"}]',
           '{in:"HND",out:"HND"}')})
