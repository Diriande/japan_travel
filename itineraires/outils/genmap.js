/* Génère une carte SVG statique, cadrée sur les étapes d'un itinéraire. */
const fs = require("fs");
const { PROJ, MAPPATHS, WATER } = JSON.parse(fs.readFileSync(__dirname + "/mapdata.json", "utf8"));
const PLACES = JSON.parse(fs.readFileSync(__dirname + "/places-min.json", "utf8"));

const AIRPORTS = {
  KIX: { n: "Kansai", code: "KIX", lon: 135.244, lat: 34.434 },
  FUK: { n: "Fukuoka", code: "FUK", lon: 130.451, lat: 33.585 },
  HND: { n: "Haneda", code: "HND", lon: 139.781, lat: 35.549 },
  NRT: { n: "Narita", code: "NRT", lon: 140.386, lat: 35.765 }
};

const proj = (lon, lat) => [(lon * PROJ.K - PROJ.x0) * PROJ.sc, (-lat - PROJ.y0) * PROJ.sc];

// steps : [{id, nights, label}], excursions : [{from, to}] pour les allers-retours
function buildMap(steps, excursions = [], opts = {}) {
  const air = opts.flights || {};                     // { in:"KIX", out:"FUK" }
  const pts = steps.map(s => proj(PLACES[s.id].lon, PLACES[s.id].lat));
  const excPts = excursions.map(e => [proj(PLACES[e.from].lon, PLACES[e.from].lat),
                                      proj(PLACES[e.to].lon, PLACES[e.to].lat)]);

  const airPts = ["in", "out"].filter(k => air[k]).map(k => {
    const a = AIRPORTS[air[k]];
    return { k, a, p: proj(a.lon, a.lat) };
  });

  // cadrage sur l'ensemble, ratio 4:3
  const all = [...pts, ...excPts.flat(), ...airPts.map(x => x.p)];
  const minX = Math.min(...all.map(p => p[0])), maxX = Math.max(...all.map(p => p[0]));
  const minY = Math.min(...all.map(p => p[1])), maxY = Math.max(...all.map(p => p[1]));
  const cx = (minX + maxX) / 2, cy = (minY + maxY) / 2;
  const RATIO = opts.ratio || 0.78;
  const w = Math.max((maxX - minX) * 1.55, ((maxY - minY) * 1.45) / RATIO, 150);
  const h = w * RATIO;
  const vb = [cx - w / 2, cy - h / 2, w, h];
  const k = w / PROJ.W;                                   // contre-échelle des repères
  const S = (v) => (v * k * 2.4).toFixed(2);              // taille apparente constante

  const arc = (a, b, bow) => {
    const [x1, y1] = a, [x2, y2] = b;
    const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
    const dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy) || 1;
    return `M${x1.toFixed(1)},${y1.toFixed(1)}Q${(mx - dy / len * bow).toFixed(1)},${(my + dx / len * bow).toFixed(1)} ${x2.toFixed(1)},${y2.toFixed(1)}`;
  };

  let main = "";
  for (let i = 0; i < pts.length - 1; i++) {
    const len = Math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) || 1;
    main += arc(pts[i], pts[i + 1], Math.min(len * 0.15, w * 0.05));
  }
  let exc = "";
  for (const [a, b] of excPts) {
    const len = Math.hypot(b[0] - a[0], b[1] - a[1]) || 1;
    const bow = Math.max(len * 0.22, w * 0.012);
    exc += arc(a, b, bow) + arc(b, a, bow);
  }

  const land = MAPPATHS.map(d => `<path d="${d}" fill="var(--m-land)" stroke="var(--m-coast)" stroke-width="1" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>`).join("");
  const water = WATER.rivers.map(d => `<path d="${d}" fill="none" stroke="var(--m-sea2)" stroke-width="1.2" vector-effect="non-scaling-stroke"/>`).join("")
    + WATER.lakes.map(d => `<path d="${d}" fill="var(--m-sea2)" stroke="var(--m-coast)" stroke-width=".6" vector-effect="non-scaling-stroke"/>`).join("");

  const excMarks = excursions.map(e => {
    const [x, y] = proj(PLACES[e.to].lon, PLACES[e.to].lat);
    return `<g transform="translate(${x.toFixed(1)},${y.toFixed(1)})">
      <circle r="${S(2.4)}" fill="var(--m-exc)" opacity=".9"/>
      <text y="${S(-4.2)}" text-anchor="middle" font-size="${S(4.4)}" fill="var(--m-exc)"
            stroke="var(--m-land)" stroke-width="${S(1.1)}" paint-order="stroke">${PLACES[e.to].n}</text>
    </g>`;
  }).join("");

  // vols : un trait qui sort du cadre, et l'aéroport
  const planes = airPts.map(({ k, a, p }) => {
    const [x, y] = p;
    const arriving = k === "in";
    const dir = arriving ? -1 : 1;                    // l'aller entre par la gauche, le retour sort par la droite
    const tail = [x + dir * w * 0.17, y - h * 0.1];
    return `<g>
      <path d="M${tail[0].toFixed(1)},${tail[1].toFixed(1)}Q${((x + tail[0]) / 2).toFixed(1)},${((y + tail[1]) / 2 - h * 0.045).toFixed(1)} ${x.toFixed(1)},${y.toFixed(1)}"
            fill="none" stroke="var(--m-air)" stroke-width="1.4" stroke-dasharray="3 4"
            stroke-linecap="round" vector-effect="non-scaling-stroke" opacity=".85"/>
      <g transform="translate(${x.toFixed(1)},${y.toFixed(1)})">
        <circle r="${S(3.2)}" fill="var(--m-land)" stroke="var(--m-air)" stroke-width="${S(0.7)}"/>
        <path d="M${S(-2)},${S(0.3)} L${S(2)},${S(0.3)} M${S(0)},${S(-2)} L${S(0)},${S(2)}"
              stroke="var(--m-air)" stroke-width="${S(0.75)}" stroke-linecap="round" fill="none"
              transform="rotate(${arriving ? -35 : 35})"/>
      </g>
      <text x="${(x + dir * Number(S(5))).toFixed(1)}" y="${(y - Number(S(5.6))).toFixed(1)}"
            text-anchor="${arriving ? "end" : "start"}" font-size="${S(4.2)}" font-weight="600"
            fill="var(--m-air)" stroke="var(--m-land)" stroke-width="${S(1.1)}" paint-order="stroke">${arriving ? "Arrivée" : "Départ"} · ${a.code}</text>
    </g>`;
  }).join("");

  const marks = steps.map((s, i) => {
    const [x, y] = proj(PLACES[s.id].lon, PLACES[s.id].lat);
    const anchor = s.anchor || "n";
    const lx = anchor === "w" ? S(-6.4) : anchor === "e" ? S(6.4) : 0;
    const ly = anchor === "s" ? S(8.4) : anchor === "n" ? S(-6.4) : S(1.6);
    const ta = anchor === "w" ? "end" : anchor === "e" ? "start" : "middle";
    return `<g transform="translate(${x.toFixed(1)},${y.toFixed(1)})">
      <circle r="${S(4.6)}" fill="var(--m-land)" opacity=".9"/>
      <circle r="${S(3.6)}" fill="var(--m-stop)"/>
      <text y="${S(1.3)}" text-anchor="middle" font-size="${S(4)}" font-weight="600" fill="var(--m-onstop)">${i + 1}</text>
      <text x="${lx}" y="${ly}" text-anchor="${ta}" font-size="${S(5.2)}" font-weight="600" fill="var(--m-ink)"
            stroke="var(--m-land)" stroke-width="${S(1.3)}" paint-order="stroke">${PLACES[s.id].n}</text>
      <text x="${lx}" y="${anchor === "s" ? S(13.4) : S(-1.4)}" text-anchor="${ta}" font-size="${S(3.9)}" fill="var(--m-muted)"
            stroke="var(--m-land)" stroke-width="${S(1.1)}" paint-order="stroke">${s.nights} nuit${s.nights > 1 ? "s" : ""}</text>
    </g>`;
  }).join("");

  return `<svg class="itinmap" viewBox="${vb.map(v => v.toFixed(1)).join(" ")}" role="img"
     aria-label="Carte de l'itinéraire : ${steps.map(s => PLACES[s.id].n).join(", ")}">
  <rect x="${(vb[0] - w).toFixed(1)}" y="${(vb[1] - h).toFixed(1)}" width="${(w * 3).toFixed(1)}" height="${(h * 3).toFixed(1)}" fill="var(--m-sea)"/>
  <g>${land}</g>
  <g opacity=".85">${water}</g>
  ${exc ? `<path d="${exc}" fill="none" stroke="var(--m-exc)" stroke-width="1.6" stroke-dasharray="4 4" stroke-linecap="round" vector-effect="non-scaling-stroke" opacity=".9"/>` : ""}
  <path d="${main}" fill="none" stroke="var(--m-route)" stroke-width="2.4" stroke-dasharray="7 6" stroke-linecap="round" vector-effect="non-scaling-stroke"/>
  ${planes}${excMarks}${marks}
</svg>`;
}

module.exports = { buildMap };

if (require.main === module) {
  const out = buildMap(
    [{ id: "kyoto", nights: 5 }, { id: "takayama", nights: 5 }, { id: "shirakawago", nights: 1, anchor: "w" },
     { id: "kanazawa", nights: 4 }, { id: "tokyo", nights: 3, anchor: "e" }],
    [{ from: "takayama", to: "kamikochi" }, { from: "kanazawa", to: "toyama" }]
  );
  console.log("SVG généré :", (out.length / 1024).toFixed(1), "Ko");
}
