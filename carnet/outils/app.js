/* Carnet de voyage — moteur de rendu.
   Les données sont injectées au build dans DATA ; tout le reste vit ici.
   L'état tient dans localStorage, et s'exporte en un fichier JSON. */
(function () {
"use strict";

var CLE = "voyage-japon-carnet-v1";
var YEN = DATA.yen;

// ————————————————————————————— icônes —————————————————————————————
function ic(d, extra) {
  return '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" ' +
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + d + (extra || "") + '</svg>';
}
var I = {
  voyage: ic('<path d="M3 20V7l6-3 6 3 6-3v13l-6 3-6-3-6 3z"/><path d="M9 4v13M15 7v13"/>'),
  jours:  ic('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'),
  carte:  ic('<path d="M12 21s7-5.7 7-11a7 7 0 1 0-14 0c0 5.3 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>'),
  budget: ic('<path d="M12 2v20"/><path d="M17 6.5C17 4.6 14.8 4 12 4S7 4.9 7 7s2.4 2.8 5 3.4c2.6.6 5 1.3 5 3.6 0 2.1-2.2 3-5 3s-5-.8-5-2.8"/>'),
  valise: ic('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 12h18"/>'),
  resa:   ic('<path d="M9 11l2.5 2.5L16 8"/><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M8 2v4M16 2v4"/>'),
  carnet: ic('<path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H19v18H6.5A2.5 2.5 0 0 0 4 22z"/><path d="M4 17.5h15"/>'),
  move:   ic('<rect x="5" y="3" width="14" height="13" rx="3"/><path d="M5 10h14M8 20l-2 2M16 20l2 2"/><circle cx="8.5" cy="13" r=".6" fill="currentColor"/><circle cx="15.5" cy="13" r=".6" fill="currentColor"/>'),
  see:    ic('<path d="M2 12s3.6-6.5 10-6.5S22 12 22 12s-3.6 6.5-10 6.5S2 12 2 12z"/><circle cx="12" cy="12" r="2.7"/>'),
  eat:    ic('<path d="M3 11h18a8 8 0 0 1-8 8h-2a8 8 0 0 1-8-8z"/><path d="M6 7c0-1.5 1-2 1-3M10 7c0-1.5 1-2 1-3M14 7c0-1.5 1-2 1-3"/>'),
  walk:   ic('<circle cx="13" cy="4.5" r="1.8"/><path d="M11 21l1.5-6-2.5-2.2V8.5L13 7l3 2.5 2.5 1M9.5 12L7 15l-1 6"/>'),
  rest:   ic('<path d="M4 21h16M6 21v-4a6 6 0 0 1 12 0v4"/><path d="M9 6c0-1.2 1-1.6 1-2.6M13 6c0-1.2 1-1.6 1-2.6"/>'),
  stay:   ic('<path d="M3 21V9l9-6 9 6v12"/><path d="M9 21v-7h6v7"/>'),
  note:   ic('<circle cx="12" cy="12" r="9"/><path d="M12 8.2v4.4M12 16.2h.01"/>'),
  chev:   '<svg class="chev" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>',
  tick:   '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5l5.5 5.5L20 7"/></svg>'
};
var KLAB = { move:"trajet", see:"visite", eat:"table", walk:"marche", rest:"pause", stay:"logement", note:"à savoir" };

// ————————————————————————————— état —————————————————————————————
var S = { trame:"alpes", vue:"voyage", faits:{}, notes:{}, depenses:[], valise:{}, resa:{}, carnet:"", ouverts:{} };
try {
  var brut = localStorage.getItem(CLE);
  if (brut) { var o = JSON.parse(brut); for (var k in o) if (o[k] != null) S[k] = o[k]; }
} catch (e) { /* navigation privée, ou stockage bloqué : on tourne sans mémoire */ }

var minuteur = null;
function save() {
  clearTimeout(minuteur);
  minuteur = setTimeout(function () {
    try { localStorage.setItem(CLE, JSON.stringify(S)); } catch (e) {}
  }, 220);
}

function T() { return DATA.trames.filter(function (t) { return t.id === S.trame; })[0]; }
function etape(t, id) { return t.etapes.filter(function (e) { return e.id === id; })[0]; }
function esc(s) { return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
function eur(n) { return Math.round(n).toLocaleString("fr-FR") + " €"; }
function yen(n) { return "¥" + Math.round(n).toLocaleString("fr-FR"); }

// ————————————————————————————— vue : le voyage —————————————————————————————
function vVoyage() {
  var t = T();
  var e0 = t.etapes[0];
  var h = '<div class="hero">' + DATA.scenes[t.id + ":" + e0.id] +
    '<div class="in"><span class="seal"><i></i>' + t.etapes.length + ' stations · ' + t.nuits +
    ' nuits · mi-mai à mi-juin</span><h1>' + t.titre + '</h1><p class="deck">' + t.deck + '</p></div></div>';

  h += '<div class="pad">';
  var prevu = t.budget.reduce(function (a, b) { return a + b[2]; }, 0);
  var reel = S.depenses.reduce(function (a, d) { return a + d.eur; }, 0);
  h += '<div class="tally">' +
    cell("Par personne", eur(t.par_pers), true) +
    cell("À trois", eur(t.par_pers * 3)) +
    cell("Nuits", String(t.nuits)) +
    cell("Trajet", t.trajet) +
    cell("Sous le plafond", eur(3000 - t.par_pers)) + '</div>';

  // ce qu'il reste à réserver
  var reste = t.resa.filter(function (r, i) { return !S.resa[t.id + ":" + i]; });
  if (reste.length) {
    h += '<section><p class="eyebrow">À ne pas rater</p><h2>Prochaines <em>réservations</em></h2>' +
      '<p class="lede">' + reste.length + ' sur ' + t.resa.length + ' restent à faire. Les critiques sont en rouge.</p>' +
      '<div class="sheet" style="padding:4px 18px"><ul class="check">' +
      reste.slice(0, 4).map(function (r) {
        var i = t.resa.indexOf(r);
        return liResa(t, r, i);
      }).join("") + '</ul></div></section>';
  }

  h += '<section><p class="eyebrow">Les étapes</p><h2>Où l\'on <em>dort</em></h2>' +
    '<p class="lede">' + t.resume + '</p><div class="grid g3">';
  t.etapes.forEach(function (e, i) {
    h += '<article class="card stcard"><div class="top">' + DATA.scenes[t.id + ":" + e.id] +
      '<span class="no">' + (i + 1) + '</span>' +
      '<span class="lab"><span class="n">' + e.nom + '</span><br><span class="k">' + e.kanji +
      ' · J' + e.j0 + '–J' + e.j1 + '</span></span></div>' +
      '<div class="bd"><div class="meta">' +
        '<span class="pill">' + e.nuits + (e.nuits > 1 ? ' nuits' : ' nuit') + '</span>' +
        '<span class="pill w">' + e.nuitee + ' € la chambre</span></div>' +
      '<p class="why">' + e.resume + '</p>' +
      '<div class="meta"><span class="pill m">' + e.meteo + '</span></div>' +
      '<ul>' + e.table.map(function (x) { return '<li>' + x + '</li>'; }).join("") + '</ul>' +
      '<p class="why" style="font-size:13px"><b>Se loger :</b> ' + e.loge + '</p></div></article>';
  });
  h += '</div></section>';

  h += '<section><p class="eyebrow">Le tracé</p><h2>La <em>route</em></h2>' +
    '<div class="mapbox">' + DATA.cartes[t.id] + '<div class="legend">' +
    '<span class="li"><span class="dot" style="background:var(--m-stop)"></span> station, avec le nombre de nuits</span>' +
    '<span class="li"><span class="sw" style="background:var(--m-route)"></span> le fil du voyage</span>' +
    '<span class="li"><span class="sw" style="background:var(--m-exc)"></span> excursion depuis la base</span>' +
    '<span class="li"><span class="sw" style="background:var(--m-air)"></span> arrivée et départ</span>' +
    '</div></div></section>';

  h += '<section><p class="eyebrow">Ce que ça coûte</p><h2>Le <em>budget</em></h2>' +
    '<div class="sheet scroll"><table><thead><tr><th>Poste</th><th>Détail</th>' +
    '<th class="n">Par personne</th><th class="n">À trois</th></tr></thead><tbody>' +
    t.budget.map(function (b) {
      return '<tr><td><b>' + b[0] + '</b></td><td>' + b[1] + '</td><td class="n">' + eur(b[2]) +
             '</td><td class="n">' + eur(b[2] * 3) + '</td></tr>';
    }).join("") +
    '<tr class="sum"><td>Total</td><td>' + eur(3000 - prevu) + ' de marge sous le plafond</td><td class="n">' +
    eur(prevu) + '</td><td class="n">' + eur(prevu * 3) + '</td></tr></tbody></table></div>';
  if (reel > 0) h += '<p class="lede" style="margin-top:14px">Déjà dépensé et saisi : <b>' + eur(reel) +
    '</b>, soit ' + Math.round(reel / prevu * 100) + ' % du prévu.</p>';
  h += '</section>';

  return h + '</div>' + pied();
}
function cell(k, v, hi) {
  return '<div class="c' + (hi ? ' hi' : '') + '"><div class="k">' + k + '</div><div class="v">' + v + '</div></div>';
}

// ————————————————————————————— vue : jour par jour —————————————————————————————
function vJours() {
  var t = T();
  var h = '<div class="pad"><section><p class="eyebrow">Le déroulé</p><h2>Jour par <em>jour</em></h2>' +
    '<p class="lede">Les horaires sont indicatifs, les prix par personne et en yens. ' +
    'Cliquer un moment le barre — c\'est fait, ou c\'est abandonné. Chaque journée a un bloc de notes.</p>';

  var cur = null;
  t.jours.forEach(function (d) {
    if (d.etape !== cur) {
      cur = d.etape;
      var e = etape(t, cur);
      var dedans = t.jours.filter(function (x) { return x.etape === cur; });
      h += '<div class="dayhead"><span class="kj">' + e.kanji + '</span><h3>' + e.nom + '</h3>' +
        '<span class="rule"></span><span class="cnt">' + dedans.length + ' jours · ' +
        e.nuits + (e.nuits > 1 ? ' nuits' : ' nuit') + '</span></div>';
    }
    h += bloc(t, d);
  });
  return h + '</section></div>' + pied();
}

function bloc(t, d) {
  var cles = d.blocs.map(function (_, i) { return t.id + ":" + d.n + ":" + i; });
  var barres = cles.filter(function (c) { return S.faits[c]; }).length;
  var fini = barres === d.blocs.length;
  var ouv = S.ouverts[t.id + ":" + d.n];
  var cout = d.blocs.reduce(function (a, b, i) { return a + (S.faits[cles[i]] ? 0 : b.cout); }, 0);
  var e = etape(t, d.etape);

  var h = '<article class="day' + (ouv ? ' open' : '') + (fini ? ' done' : '') + '" data-day="' + d.n + '">' +
    '<button class="dh" data-open="' + d.n + '" aria-expanded="' + (ouv ? "true" : "false") + '">' +
    '<span class="dn">J' + d.n + '</span><span class="dt"><span class="t">' + d.titre + '</span>' +
    '<span class="s">' + e.nom + ' · ' + d.blocs.length + ' moments' +
    (cout ? ' · ' + yen(cout) : '') + (barres ? ' · ' + barres + ' barré' + (barres > 1 ? 's' : '') : '') +
    '</span></span>' + I.chev + '</button><div class="dbody">';

  d.blocs.forEach(function (b, i) {
    var c = cles[i], off = S.faits[c];
    h += '<div class="blk tick k-' + b.kind + (off ? ' off' : '') + '" data-tick="' + c + '">' +
      '<span class="hh">' + b.h + '</span>' + (I[b.kind] || I.see) +
      '<span><span class="q">' + b.quoi + '</span>' + (b.note ? '<span class="nt">' + b.note + '</span>' : '') + '</span>' +
      (b.cout ? '<span class="cc">' + yen(b.cout) + '<small>' + Math.round(b.cout / YEN) + ' €</small></span>' : '<span></span>') +
      '</div>';
  });

  if (d.note) h += '<div class="dnote"><b>À savoir</b>' + d.note + '</div>';
  h += '<div class="dsum"><span>Coût restant, par personne <b>' + yen(cout) + '</b> — soit ' +
       Math.round(cout / YEN) + ' €</span><span>À trois <b>' + yen(cout * 3) + '</b></span></div>';
  h += '<textarea class="jot" aria-label="Notes du jour ' + d.n + '" data-note="' + t.id + ":" + d.n + '" placeholder="Notes du jour ' + d.n +
       ' — réservations, adresses, ce qu\'on a aimé…">' + esc(S.notes[t.id + ":" + d.n] || "") + '</textarea>';
  return h + '</div></article>';
}

// ————————————————————————————— vue : carte —————————————————————————————
function vCarte() {
  var t = T();
  var h = '<div class="pad"><section><p class="eyebrow">Le tracé</p><h2>La <em>carte</em></h2>' +
    '<p class="lede">Les distances sont réelles, les temps de trajet aussi — ils viennent du graphe ' +
    'de liaisons du dépôt, pas d\'une estimation.</p>' +
    '<div class="mapbox">' + DATA.cartes[t.id] + '<div class="legend">' +
    '<span class="li"><span class="dot" style="background:var(--m-stop)"></span> station, avec le nombre de nuits</span>' +
    '<span class="li"><span class="sw" style="background:var(--m-route)"></span> le fil du voyage</span>' +
    '<span class="li"><span class="sw" style="background:var(--m-exc)"></span> excursion depuis la base</span>' +
    '<span class="li"><span class="sw" style="background:var(--m-air)"></span> arrivée et départ</span>' +
    '</div></div>';

  h += '<div class="grid g2" style="margin-top:26px">';
  t.etapes.forEach(function (e, i) {
    var js = t.jours.filter(function (d) { return d.etape === e.id; });
    h += '<article class="card" style="padding:17px 19px"><div class="meta" style="display:flex;gap:9px;align-items:baseline">' +
      '<span class="pill">' + (i + 1) + '</span><h3 style="font-size:19px">' + e.nom + '</h3>' +
      '<span class="pill w" style="margin-left:auto">' + e.kanji + '</span></div>' +
      '<p class="why" style="color:var(--pale);margin:9px 0 0;font-size:14px">' + e.resume + '</p>' +
      '<div class="dsum" style="border-top:1px solid var(--trait);margin-top:12px">' +
      '<span>J' + e.j0 + ' → J' + e.j1 + '</span><span><b>' + js.length + '</b> journées</span>' +
      '<span><b>' + e.nuitee + ' €</b> la chambre</span></div></article>';
  });
  return h + '</div></section></div>' + pied();
}

// ————————————————————————————— vue : budget —————————————————————————————
function vBudget() {
  var t = T();
  var prevu = t.budget.reduce(function (a, b) { return a + b[2]; }, 0);
  var reel = S.depenses.reduce(function (a, d) { return a + d.eur; }, 0);
  var pct = prevu ? Math.min(100, reel / prevu * 100) : 0;

  var h = '<div class="pad"><section><p class="eyebrow">Ce que ça coûte</p><h2>Le <em>budget</em></h2>' +
    '<p class="lede">À gauche le prévu, calculé sur les données du dépôt. À droite ce que vous saisissez ' +
    'pendant le voyage. Les montants sont par personne.</p>';

  h += '<div class="tally">' + cell("Prévu", eur(prevu), true) + cell("Saisi", eur(reel)) +
    cell("Reste", eur(Math.max(0, prevu - reel))) +
    cell("Plafond", eur(3000)) + '</div>' +
    '<div class="bar' + (reel > prevu ? ' over' : '') + '"><i style="width:' + pct.toFixed(1) + '%"></i></div>';

  // par poste
  var parPoste = {};
  S.depenses.forEach(function (d) { parPoste[d.poste] = (parPoste[d.poste] || 0) + d.eur; });
  h += '<div class="grid g2" style="margin-top:30px">';
  h += '<div class="sheet scroll"><table><thead><tr><th>Poste</th><th class="n">Prévu</th>' +
    '<th class="n">Saisi</th><th class="n">Écart</th></tr></thead><tbody>' +
    t.budget.map(function (b) {
      var r = parPoste[b[0]] || 0, d = b[2] - r;
      return '<tr><td><b>' + b[0] + '</b></td><td class="n">' + eur(b[2]) + '</td><td class="n">' +
        (r ? eur(r) : '—') + '</td><td class="n" style="color:' +
        (d < 0 ? 'var(--beni)' : 'var(--moss)') + '">' + eur(d) + '</td></tr>';
    }).join("") +
    '<tr class="sum"><td>Total</td><td class="n">' + eur(prevu) + '</td><td class="n">' + eur(reel) +
    '</td><td class="n">' + eur(prevu - reel) + '</td></tr>' +
    '</tbody></table></div>';

  // par étape
  var parEtape = {};
  S.depenses.forEach(function (d) { if (d.etape) parEtape[d.etape] = (parEtape[d.etape] || 0) + d.eur; });
  var maxE = Math.max.apply(null, [1].concat(Object.keys(parEtape).map(function (k) { return parEtape[k]; })));
  h += '<div class="card" style="padding:19px"><h3 style="font-size:17px;margin-bottom:13px">Par étape</h3>';
  t.etapes.forEach(function (e) {
    var v = parEtape[e.id] || 0;
    h += '<div style="margin-bottom:13px"><div style="display:flex;justify-content:space-between;font-size:13.5px">' +
      '<span>' + e.nom + '</span><span style="font-family:var(--f-num);color:var(--clay)">' +
      (v ? eur(v) : '—') + '</span></div>' +
      '<div class="bar"><i style="width:' + (v / maxE * 100).toFixed(1) + '%"></i></div></div>';
  });
  h += '</div></div>';

  // saisie
  h += '<section><p class="eyebrow">Enregistrer</p><h2>Une <em>dépense</em></h2>' +
    '<p class="lede">Un geste pour les dépenses courantes, le formulaire pour le reste. ' +
    'Tout est converti au taux de ' + YEN + ' ¥ pour 1 €.</p>' +
    '<div class="qadd">' + DATA.rapides.map(function (q, i) {
      return '<button data-quick="' + i + '"><span class="q">' + q[0] + '</span>' +
             '<span class="p">' + yen(q[1]) + '</span></button>';
    }).join("") + '</div>';

  h += '<div class="form"><input id="fq" type="text" placeholder="Quoi ?" aria-label="Libellé de la dépense" style="flex:1;min-width:150px">' +
    '<input id="fm" type="number" min="0" step="1" placeholder="Montant" aria-label="Montant">' +
    '<select id="fd" aria-label="Devise"><option value="yen">¥</option><option value="eur">€</option></select>' +
    '<select id="fp" aria-label="Poste de budget">' + t.budget.map(function (b) { return '<option>' + b[0] + '</option>'; }).join("") + '</select>' +
    '<select id="fe" aria-label="Étape"><option value="">— étape —</option>' +
    t.etapes.map(function (e) { return '<option value="' + e.id + '">' + e.nom + '</option>'; }).join("") +
    '</select><button class="go" id="fgo">Ajouter</button></div>';

  if (S.depenses.length) {
    h += '<div class="sheet" style="padding:6px 18px"><ul class="spend">' +
      S.depenses.slice().reverse().map(function (d) {
        var e = etape(t, d.etape);
        return '<li><span class="w">' + esc(d.quoi) + '<small>' + d.poste +
          (e ? ' · ' + e.nom : '') + ' · ' + d.date + '</small></span>' +
          '<span class="a">' + eur(d.eur) + '</span>' +
          '<button class="x" data-del="' + d.id + '" title="Supprimer">✕</button></li>';
      }).join("") + '</ul></div>';
  } else {
    h += '<p class="lede">Rien de saisi pour l\'instant.</p>';
  }
  return h + '</section></div>' + pied();
}

// ————————————————————————————— vues : listes —————————————————————————————
function vValise() {
  var h = '<div class="pad"><section><p class="eyebrow">Avant de partir</p><h2>La <em>valise</em></h2>' +
    '<p class="lede">Deux fois 23 kg par personne en soute, plus 8 kg en cabine. ' +
    'La liste est commune aux trois itinéraires.</p>';
  DATA.valise.forEach(function (grp) {
    h += '<h3 style="font-size:18px;margin:26px 0 4px">' + grp.nom + '</h3>' +
      '<div class="sheet" style="padding:4px 18px"><ul class="check">' +
      grp.items.map(function (it, i) {
        var c = "v:" + grp.nom + ":" + i, on = S.valise[c];
        return '<li class="' + (on ? 'on' : '') + '" data-check="valise" data-key="' + c + '">' +
          '<span class="bx">' + (on ? I.tick : '') + '</span><span class="w">' + it[0] +
          (it[1] ? '<small>' + it[1] + '</small>' : '') + '</span></li>';
      }).join("") + '</ul></div>';
  });
  return h + '</section></div>' + pied();
}

function liResa(t, r, i) {
  var c = t.id + ":" + i, on = S.resa[c];
  return '<li class="' + (on ? 'on ' : '') + (r.critique ? 'crit' : '') + '" data-check="resa" data-key="' + c + '">' +
    '<span class="bx">' + (on ? I.tick : '') + '</span>' +
    '<span class="w">' + r.quoi + '<small>' + r.note + '</small></span>' +
    '<span class="when">' + r.quand + '</span></li>';
}

function vResa() {
  var t = T();
  var faits = t.resa.filter(function (_, i) { return S.resa[t.id + ":" + i]; }).length;
  var h = '<div class="pad"><section><p class="eyebrow">Avant de partir</p><h2>Les <em>réservations</em></h2>' +
    '<p class="lede">Dans l\'ordre où il faut s\'en occuper. ' + faits + ' sur ' + t.resa.length + ' de faites.</p>' +
    '<div class="bar"><i style="width:' + (faits / t.resa.length * 100).toFixed(1) + '%"></i></div>' +
    '<div class="sheet" style="padding:4px 18px;margin-top:22px"><ul class="check">' +
    t.resa.map(function (r, i) { return liResa(t, r, i); }).join("") + '</ul></div>' +
    '<div class="note"><b>Ce qui bloque tout le reste</b><p>Les lignes en rouge conditionnent les autres : ' +
    'un hébergement complet ou un vol indisponible fait bouger toute la trame. Les traiter en premier.</p></div>';
  return h + '</section></div>' + pied();
}

function vCarnet() {
  var h = '<div class="pad"><section><p class="eyebrow">Sur place</p><h2>Le <em>carnet</em></h2>' +
    '<p class="lede">Un bloc libre, gardé dans le navigateur et repris dans l\'export. ' +
    'Les notes rattachées à une journée sont dans « Jour par jour ».</p>' +
    '<textarea class="jot" id="carnet" aria-label="Carnet libre" style="min-height:340px;font-size:15px" ' +
    'placeholder="Adresses, numéros de réservation, ce qu\'on a mangé, ce qu\'il faudra refaire…">' +
    esc(S.carnet) + '</textarea>';

  var t = T();
  var avec = t.jours.filter(function (d) { return (S.notes[t.id + ":" + d.n] || "").trim(); });
  if (avec.length) {
    h += '<h3 style="font-size:19px;margin:34px 0 12px">Notes des journées</h3><div class="sheet" style="padding:6px 18px">';
    h += '<ul class="spend">' + avec.map(function (d) {
      return '<li><span class="w">J' + d.n + ' · ' + d.titre +
        '<small>' + esc(S.notes[t.id + ":" + d.n]).slice(0, 160) + '</small></span></li>';
    }).join("") + '</ul></div>';
  }
  return h + '</section></div>' + pied();
}

function pied() {
  return '<footer>Les montants sont des estimations à revérifier au moment de réserver. ' +
    'Le prix du vol suit les relevés Finnair du 23 août 2026, tarif Economy Classic, deux bagages de 23 kg — ' +
    'la seule ligne vérifiée sur un tunnel de réservation. Hébergement en chambre à trois, ' +
    'trajets chiffrés sur le graphe des liaisons réelles, 40 € par jour et par personne de nourriture. ' +
    'Tout ce que vous saisissez reste dans ce navigateur : pensez à exporter.</footer>';
}

// ————————————————————————————— rendu —————————————————————————————
var VUES = { voyage:vVoyage, jours:vJours, carte:vCarte, budget:vBudget, valise:vValise, resa:vResa, carnet:vCarnet };
var NOMS = { voyage:"Le voyage", jours:"Jour par jour", carte:"Carte", budget:"Budget",
             valise:"Valise", resa:"Réservations", carnet:"Carnet" };

function nav() {
  var t = T();
  var reste = t.resa.filter(function (_, i) { return !S.resa[t.id + ":" + i]; }).length;
  var h = '<div class="brand"><span class="mk">旅</span><div><div class="bt">Carnet du Japon</div>' +
    '<div class="bs">trois voyageurs</div></div></div>';

  h += '<div class="pick"><label>Itinéraire</label><select id="pick" aria-label="Choisir un itinéraire">' +
    DATA.trames.map(function (x) {
      return '<option value="' + x.id + '"' + (x.id === S.trame ? ' selected' : '') + '>' +
        x.court + ' — ' + eur(x.par_pers) + '</option>';
    }).join("") + '</select></div>';

  h += '<nav class="nav">';
  ["voyage", "jours", "carte", "budget"].forEach(function (v) {
    h += '<button data-vue="' + v + '"' + (S.vue === v ? ' aria-current="true"' : '') + '>' +
      I[v] + NOMS[v] + '</button>';
  });
  h += '<div class="grp">Avant de partir</div>';
  ["resa", "valise"].forEach(function (v) {
    h += '<button data-vue="' + v + '"' + (S.vue === v ? ' aria-current="true"' : '') + '>' +
      I[v] + NOMS[v] + (v === "resa" && reste ? '<span class="tag">' + reste + '</span>' : '') + '</button>';
  });
  h += '<div class="grp">Sur place</div>' +
    '<button data-vue="carnet"' + (S.vue === "carnet" ? ' aria-current="true"' : '') + '>' +
    I.carnet + NOMS.carnet + '</button>';

  h += '<div class="grp">Les étapes</div>';
  t.etapes.forEach(function (e, i) {
    h += '<button class="stp" data-etape="' + e.id + '"><span class="no">' + (i + 1) + '</span>' +
      e.nom + '<span class="tag">J' + e.j0 + '</span></button>';
  });
  h += '</nav><div class="tools">' +
    '<button id="sav">Sauvegarde</button>' +
    '<button id="thm">Thème</button><button id="prt">Imprimer</button></div>';
  return h;
}

function render() {
  document.querySelector(".side").innerHTML = nav();
  var m = document.querySelector(".main");
  m.innerHTML = '<div class="view on">' + VUES[S.vue]() + '</div>';
  m.scrollTop = 0;
  save();
}

// ————————————————————————————— interactions —————————————————————————————
document.addEventListener("click", function (ev) {
  var el;

  if ((el = ev.target.closest("[data-vue]"))) {
    S.vue = el.dataset.vue; fermeSide(); render(); window.scrollTo(0, 0); return;
  }
  if ((el = ev.target.closest("[data-etape]"))) {
    var t = T(), id = el.dataset.etape;
    S.vue = "jours";
    t.jours.forEach(function (d) { if (d.etape === id) S.ouverts[t.id + ":" + d.n] = true; });
    fermeSide(); render();
    var cible = document.querySelectorAll(".dayhead")[t.etapes.map(function (e) { return e.id; }).indexOf(id)];
    if (cible) cible.scrollIntoView({ behavior: "smooth", block: "start" });
    return;
  }
  if ((el = ev.target.closest("[data-open]"))) {
    var k = T().id + ":" + el.dataset.open;
    S.ouverts[k] = !S.ouverts[k];
    var art = el.closest(".day");
    art.classList.toggle("open", !!S.ouverts[k]);
    el.setAttribute("aria-expanded", S.ouverts[k] ? "true" : "false");
    save(); return;
  }
  if ((el = ev.target.closest("[data-tick]"))) {
    var c = el.dataset.tick;
    if (S.faits[c]) delete S.faits[c]; else S.faits[c] = true;
    var jour = el.closest(".day");
    var t2 = T(), n = +jour.dataset.day;
    jour.outerHTML = bloc(t2, t2.jours.filter(function (d) { return d.n === n; })[0]);
    save(); return;
  }
  if ((el = ev.target.closest("[data-check]"))) {
    var quoi = el.dataset.check, cle = el.dataset.key, store = quoi === "valise" ? S.valise : S.resa;
    if (store[cle]) delete store[cle]; else store[cle] = true;
    render(); return;
  }
  if ((el = ev.target.closest("[data-quick]"))) {
    var q = DATA.rapides[+el.dataset.quick];
    ajoute(q[0], q[1] / YEN, q[2], "");
    return;
  }
  if ((el = ev.target.closest("[data-del]"))) {
    var id2 = el.dataset.del;
    S.depenses = S.depenses.filter(function (d) { return d.id !== id2; });
    render(); return;
  }
  if (ev.target.closest("#fgo")) {
    var quoi2 = document.getElementById("fq").value.trim() || "Dépense";
    var m2 = parseFloat(document.getElementById("fm").value);
    if (!(m2 > 0)) return;
    var dev = document.getElementById("fd").value;
    ajoute(quoi2, dev === "yen" ? m2 / YEN : m2,
           document.getElementById("fp").value, document.getElementById("fe").value);
    return;
  }
  if (ev.target.closest("#sav")) { sauvegarde(); return; }
  if (ev.target.closest("#prt")) { window.print(); return; }
  if (ev.target.closest("#thm")) { basculeTheme(); return; }
  if (ev.target.closest(".burger")) { ouvreSide(); return; }
  if (ev.target.closest(".veil")) { fermeSide(); return; }
});

document.addEventListener("change", function (ev) {
  if (ev.target.id === "pick") { S.trame = ev.target.value; render(); window.scrollTo(0, 0); }
});

document.addEventListener("input", function (ev) {
  if (ev.target.classList.contains("jot")) {
    if (ev.target.id === "carnet") S.carnet = ev.target.value;
    else S.notes[ev.target.dataset.note] = ev.target.value;
    save();
  }
});

function ajoute(quoi, montantEur, poste, etp) {
  S.depenses.push({
    id: String(S.depenses.length) + "-" + quoi.slice(0, 8) + "-" + Math.round(montantEur * 100),
    quoi: quoi, eur: montantEur, poste: poste, etape: etp,
    date: new Date().toLocaleDateString("fr-FR", { day: "2-digit", month: "short" })
  });
  render();
}

// ————————————————————————————— outils —————————————————————————————
function sauvegarde() {
  // En local le téléchargement part ; dans une page publiée le bac à sable le bloque,
  // d'où le texte à copier, qui marche partout.
  var json = JSON.stringify(S, null, 2);
  var d = document.createElement("div");
  d.className = "modal";
  d.innerHTML = '<div class="box"><h3>Sauvegarde</h3>' +
    '<p class="lede" style="margin:8px 0 12px">Tout ce que vous avez coché, noté et dépensé. ' +
    'Téléchargez le fichier, ou copiez le texte — les deux se rechargent par le même bouton.</p>' +
    '<textarea class="jot" id="mj" spellcheck="false" aria-label="Contenu de la sauvegarde" style="min-height:190px;font-family:var(--f-num);font-size:11.5px"></textarea>' +
    '<div class="form" style="margin:12px 0 0"><button class="go" id="mdl">Télécharger</button>' +
    '<button class="go" id="mld" style="background:var(--moss)">Charger ce texte</button>' +
    '<button class="go" id="mfl" style="background:var(--trait);color:var(--encre)">Depuis un fichier</button>' +
    '<button id="mx" style="background:none;border:0;color:var(--pale);cursor:pointer;margin-left:auto">Fermer</button>' +
    '</div><p id="mmsg" class="lede" style="margin:10px 0 0;min-height:20px"></p></div>';
  document.body.appendChild(d);
  d.querySelector("#mj").value = json;

  function dit(m) { d.querySelector("#mmsg").textContent = m; }

  d.querySelector("#mdl").onclick = function () {
    var txt = d.querySelector("#mj").value;
    dit("…");
    // Publiée en Artifact, la page n'a pas le droit de déclencher un téléchargement
    // elle-même : elle passe par l'hôte, qui demande au lecteur. En local, lien blob.
    hote().then(function (dl) {
      if (dl) {
        return dl.save({ filename: "carnet-japon.json", data: txt })
          .then(function () { dit("Sauvegarde enregistrée."); })
          .catch(function (e) {
            dit(e && e.code === "declined" ? "Téléchargement refusé — le texte ci-dessus reste copiable."
                                          : "Téléchargement impossible — copiez le texte ci-dessus.");
          });
      }
      var blob = new Blob([txt], { type: "application/json" });
      var u = URL.createObjectURL(blob), a = document.createElement("a");
      a.href = u; a.download = "carnet-japon.json";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(u); }, 1000);
      dit("Si rien ne s'est téléchargé, copiez le texte ci-dessus.");
    });
  };

  d.querySelector("#mld").onclick = function () {
    if (charge(d.querySelector("#mj").value)) { d.remove(); render(); }
    else dit("Ce texte n'est pas une sauvegarde valide.");
  };

  d.querySelector("#mfl").onclick = function () {
    var i = document.createElement("input");
    i.type = "file"; i.accept = "application/json,.json";
    i.onchange = function () {
      var f = i.files && i.files[0];
      if (!f) return;
      var fr = new FileReader();
      fr.onload = function () {
        if (charge(fr.result)) { d.remove(); render(); }
        else dit("Fichier illisible.");
      };
      fr.readAsText(f);
    };
    i.click();
  };

  d.querySelector("#mx").onclick = function () { d.remove(); };
  d.onclick = function (ev) { if (ev.target === d) d.remove(); };
}

function hote() {
  try {
    if (typeof claude !== "undefined" && claude && typeof claude.use === "function") {
      return Promise.resolve(claude.use("downloads")).catch(function () { return null; });
    }
  } catch (e) {}
  return Promise.resolve(null);
}

function charge(txt) {
  try {
    var o = JSON.parse(txt);
    if (!o || typeof o !== "object" || !o.trame) return false;
    for (var k in S) if (o[k] != null) S[k] = o[k];
    return true;
  } catch (e) { return false; }
}

function basculeTheme() {
  var r = document.documentElement;
  var a = r.getAttribute("data-theme");
  var sombre = a ? a === "dark"
    : window.matchMedia("(prefers-color-scheme: dark)").matches;
  r.setAttribute("data-theme", sombre ? "light" : "dark");
  try { localStorage.setItem(CLE + ":theme", r.getAttribute("data-theme")); } catch (e) {}
}
try {
  var th = localStorage.getItem(CLE + ":theme");
  if (th) document.documentElement.setAttribute("data-theme", th);
} catch (e) {}

function ouvreSide() {
  document.querySelector(".side").classList.add("on");
  document.querySelector(".veil").classList.add("on");
}
function fermeSide() {
  document.querySelector(".side").classList.remove("on");
  document.querySelector(".veil").classList.remove("on");
}

render();
})();
