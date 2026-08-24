"""Identité visuelle des pages d'itinéraire : « stations de relais ».

Palette et vocabulaire empruntés aux estampes de voyage d'Hiroshige — papier washi,
encre sumi, bleu de Prusse (bero-ai), rouge carthame (beni). Chaque étape est une
station, avec un cartouche vertical portant son rang et son nom.
"""

CSS = """
:root {
  --washi:#E9EBE6; --washi-2:#E0E3DC; --sheet:#F4F5F2;
  --sumi:#1C1F1B; --sumi-soft:#5A6159; --rule:#C9CEC4; --rule-2:#D8DCD3;
  --bero:#1D3E63; --bero-2:#2C5687; --bero-pale:#DDE4EC;
  --beni:#B23A2E; --beni-pale:#F2E2DE;
  --indigo:#5C7A93; --moss:#4A6B4E; --clay:#8A6A3F;
  --f-disp:"Petrona",Georgia,serif;
  --f-body:"Archivo","Helvetica Neue",Arial,sans-serif;
  --f-num:"IBM Plex Mono",ui-monospace,Menlo,monospace;
  --m-sea:var(--bero-pale); --m-sea2:#C7D4E1; --m-land:var(--sheet); --m-coast:#9AA9B5;
  --m-route:var(--bero); --m-air:var(--beni); --m-exc:var(--clay);
  --m-stop:var(--bero); --m-onstop:#F4F5F2;
  --m-ink:var(--sumi); --m-muted:var(--sumi-soft);
}
@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
  --washi:#15181A; --washi-2:#101315; --sheet:#1D2124;
  --sumi:#E6E9E3; --sumi-soft:#98A099; --rule:#2E343A; --rule-2:#242A2F;
  --bero:#7FA6CE; --bero-2:#9BBBDC; --bero-pale:#1A2836;
  --beni:#DE8878; --beni-pale:#2E1D19;
  --indigo:#7B96AC; --moss:#7FA383; --clay:#BFA075;
  --m-sea:#0E1720; --m-sea2:#15242F; --m-land:#232A2F; --m-coast:#4B5A66;
  --m-route:#7FA6CE; --m-air:#DE8878; --m-exc:#BFA075; --m-stop:#7FA6CE; --m-onstop:#0E1720;
  --m-ink:#E6E9E3; --m-muted:#98A099;
}}
:root[data-theme="dark"]{
  --washi:#15181A; --washi-2:#101315; --sheet:#1D2124;
  --sumi:#E6E9E3; --sumi-soft:#98A099; --rule:#2E343A; --rule-2:#242A2F;
  --bero:#7FA6CE; --bero-2:#9BBBDC; --bero-pale:#1A2836;
  --beni:#DE8878; --beni-pale:#2E1D19;
  --indigo:#7B96AC; --moss:#7FA383; --clay:#BFA075;
  --m-sea:#0E1720; --m-sea2:#15242F; --m-land:#232A2F; --m-coast:#4B5A66;
  --m-route:#7FA6CE; --m-air:#DE8878; --m-exc:#BFA075; --m-stop:#7FA6CE; --m-onstop:#0E1720;
  --m-ink:#E6E9E3; --m-muted:#98A099;
}
*{box-sizing:border-box}
body{background:var(--washi);color:var(--sumi);font-family:var(--f-body);font-size:16.5px;
  line-height:1.6;margin:0;-webkit-font-smoothing:antialiased;font-weight:350}
.wrap{max-width:1000px;margin:0 auto;padding:0 24px}

/* cartouche de titre */
.plate{border-bottom:1px solid var(--rule);background:var(--sheet)}
.plate .wrap{display:grid;grid-template-columns:1fr auto;gap:40px;align-items:end;
  padding-top:64px;padding-bottom:34px}
.seal{font-family:var(--f-num);font-size:10px;letter-spacing:.22em;text-transform:uppercase;
  color:var(--beni);display:flex;align-items:center;gap:11px;margin:0 0 20px}
.seal::before{content:"";width:18px;height:18px;flex:none;background:var(--beni);border-radius:2px;
  opacity:.92}
h1{font-family:var(--f-disp);font-weight:500;font-size:clamp(38px,6.4vw,70px);line-height:1.02;
  letter-spacing:-.02em;margin:0;text-wrap:balance}
h1 em{font-style:italic;color:var(--bero)}
.deck{font-family:var(--f-disp);font-size:clamp(16.5px,2vw,19.5px);line-height:1.5;
  color:var(--sumi-soft);max-width:52ch;margin:20px 0 0;font-weight:400}
.tally{display:flex;flex-direction:column;border-left:1px solid var(--rule)}
.tally div{padding:10px 0 10px 22px;border-bottom:1px solid var(--rule-2)}
.tally div:last-child{border-bottom:0}
.tally .k{font-family:var(--f-num);font-size:9.5px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--sumi-soft);display:block}
.tally .v{font-family:var(--f-disp);font-size:27px;font-weight:500;line-height:1.1;
  font-variant-numeric:tabular-nums;display:block;margin-top:2px}
.tally .v.hi{color:var(--bero)}

/* carte */
figure.chart{margin:0;background:var(--m-sea);overflow:hidden;border-bottom:1px solid var(--rule)}
figure.chart svg.itinmap{display:block;width:100%;max-width:1080px;height:auto;margin:0 auto}
figcaption{display:flex;flex-wrap:wrap;gap:9px 26px;padding:14px 24px;background:var(--sheet);
  border-bottom:1px solid var(--rule);font-size:13px;color:var(--sumi-soft);
  max-width:1000px;margin:0 auto}
figcaption .li{display:flex;align-items:center;gap:8px}
figcaption .sw{width:18px;height:3px;flex:none}
figcaption .dot{width:10px;height:10px;border-radius:50%;flex:none}

section{padding:64px 0 0}
h2{font-family:var(--f-disp);font-weight:500;font-size:clamp(26px,3.7vw,38px);line-height:1.08;
  letter-spacing:-.015em;margin:0 0 12px;text-wrap:balance}
h2 em{font-style:italic;color:var(--bero)}
.eyebrow{font-family:var(--f-num);font-size:10px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--beni);margin:0 0 12px}
p.lede{color:var(--sumi-soft);max-width:62ch;margin:0 0 20px;font-size:16.5px;line-height:1.65}
p.lede strong{color:var(--sumi);font-weight:600}
p.lede:last-child{margin-bottom:0}

/* stations */
.route{display:flex;flex-direction:column;margin-top:34px;border-top:1px solid var(--rule)}
.station{display:grid;grid-template-columns:92px 1fr;border-bottom:1px solid var(--rule);
  background:var(--sheet)}
.mon{background:var(--bero);color:var(--sheet);display:flex;flex-direction:column;
  align-items:center;gap:14px;padding:22px 0 26px}
.mon .no{font-family:var(--f-disp);font-size:32px;font-weight:500;line-height:1}
.mon .vname{writing-mode:vertical-rl;text-orientation:mixed;font-family:var(--f-disp);
  font-size:20px;font-weight:500;letter-spacing:.06em;line-height:1}
.mon .nn{font-family:var(--f-num);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;
  writing-mode:vertical-rl;opacity:.72}
.station.leg .mon{background:var(--washi-2);color:var(--sumi-soft)}
.station.leg .mon .no{font-size:20px;line-height:1.4}
.pane{padding:26px 30px 30px}
.pane h3{font-family:var(--f-disp);font-weight:500;font-size:27px;letter-spacing:-.01em;
  margin:0 0 3px;line-height:1.1}
.station.leg .pane h3{font-size:20px}
.when{font-family:var(--f-num);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--sumi-soft);margin:0 0 16px}
.why{margin:0 0 20px;color:var(--sumi-soft);max-width:64ch;line-height:1.6}
.why strong{color:var(--sumi);font-weight:600}
.station.leg .why{margin-bottom:0}
.doings{display:flex;flex-direction:column}
.doing{display:grid;grid-template-columns:24px 1fr;gap:15px;padding:14px 0;
  border-top:1px solid var(--rule-2);align-items:start}
.doing:first-child{border-top:1px solid var(--rule)}
.doing .ico{width:24px;height:24px}
.doing .ico svg{width:100%;height:100%;display:block;fill:none;stroke:currentColor;
  stroke-width:1.4;stroke-linecap:round}
.doing b{font-weight:600;display:block;font-size:16px}
.doing .kind{font-family:var(--f-num);font-size:9px;letter-spacing:.14em;text-transform:uppercase;
  margin-left:9px;vertical-align:2px;font-weight:400}
.doing .n{display:block;font-size:14.5px;color:var(--sumi-soft);margin-top:4px;
  max-width:60ch;line-height:1.55}
.k-view{color:var(--moss)} .k-eat{color:var(--clay)}
.k-make{color:var(--beni)} .k-past{color:var(--bero)}
.span{display:grid;grid-template-columns:92px 1fr;border-bottom:1px solid var(--rule);
  background:var(--washi-2)}
.span .rule{border-right:1px solid var(--rule-2)}
.span .txt{padding:13px 30px;display:flex;flex-wrap:wrap;gap:6px 16px;align-items:baseline}
.span .dur{font-family:var(--f-disp);font-size:19px;font-weight:500;color:var(--bero)}
.span .via{font-size:14px;color:var(--sumi-soft)}

.sheet{overflow-x:auto;border:1px solid var(--rule);background:var(--sheet);margin-top:24px}
table{border-collapse:collapse;width:100%;font-size:15px}
thead th{text-align:left;font-family:var(--f-num);font-size:9.5px;font-weight:500;
  letter-spacing:.14em;text-transform:uppercase;color:var(--sumi-soft);padding:14px 20px;
  border-bottom:1px solid var(--rule);white-space:nowrap}
tbody td{padding:13px 20px;border-bottom:1px solid var(--rule-2)}
tbody tr:last-child td{border-bottom:0}
tbody tr.sum td{background:var(--bero-pale);font-weight:600;color:var(--bero)}
td.n,th.n{font-family:var(--f-num);font-variant-numeric:tabular-nums;text-align:right;
  white-space:nowrap}

.note{border-left:2px solid var(--beni);background:var(--beni-pale);padding:22px 26px;
  margin-top:26px;display:flex;flex-direction:column;gap:11px}
.note b{font-family:var(--f-disp);font-size:19px;font-weight:500;color:var(--beni)}
.note p{margin:0;font-size:15.5px;line-height:1.6}
.pair{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1px;
  background:var(--rule);border:1px solid var(--rule);margin-top:24px}
.pair > div{background:var(--sheet);padding:22px 24px;display:flex;flex-direction:column;gap:6px}
.pair b{font-family:var(--f-disp);font-size:20px;font-weight:500;line-height:1.15}
.pair p{margin:0;font-size:15px;color:var(--sumi-soft);line-height:1.55}

footer{border-top:1px solid var(--rule);margin-top:70px;padding:24px 0 76px;font-size:13px;
  color:var(--sumi-soft);line-height:1.65;max-width:74ch}
a{color:var(--bero)}
a:focus-visible,button:focus-visible{outline:2px solid var(--beni);outline-offset:2px}

@media (max-width:760px){
  .plate .wrap{grid-template-columns:1fr;gap:26px;padding-top:40px}
  .tally{border-left:0;border-top:1px solid var(--rule);display:grid;grid-template-columns:1fr 1fr}
  .tally div{padding-left:0;padding-right:14px}
  .station,.span{grid-template-columns:60px 1fr}
  .mon .vname{font-size:16px}
  .pane{padding:20px 20px 24px}
  .span .txt{padding:12px 20px}
  section{padding-top:46px}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
 'family=Petrona:ital,wght@0,400;0,500;0,600;1,400;1,500&'
 'family=Archivo:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">')

ICONS = {
 "view": '<path d="M1 17 8 5l4 6.5L14.5 8 21 17H1Z" stroke-linejoin="round"/>',
 "fall": '<path d="M4 2h3c0 4-2 5-2 9s2 4 2 7H4c0-3 2-3 2-7S4 6 4 2Zm5.5 0h3c0 4-2 5-2 9s2 4 2 7h-3c0-3 2-3 2-7s-2-5-2-9Zm5.5 0h3c0 4-2 5-2 9s2 4 2 7h-3c0-3 2-3 2-7s-2-5-2-9Z"/>',
 "gate": '<path d="M2 5h18M3 8h16M6 5v13M16 5v13M2 5c2-1.5 16-1.5 18 0"/>',
 "roof": '<path d="M11 2 2 11h3v8h12v-8h3L11 2Z" stroke-linejoin="round"/><path d="M8 19v-5h6v5"/>',
 "pot":  '<path d="M7 3h8l-1 3c2 1.5 3 4 3 6.5 0 4-3 6.5-6 6.5s-6-2.5-6-6.5C5 10 6 7.5 8 6L7 3Z" stroke-linejoin="round"/>',
 "loom": '<path d="M2 6h18v10H2zM2 9h18M2 13h18M7 6v10M13 6v10"/>',
 "bowl": '<path d="M2 10h18c0 5-4 8-9 8s-9-3-9-8Z" stroke-linejoin="round"/><path d="M7 7c0-2 2-2 2-4M12 7c0-2 2-2 2-4"/>',
 "boat": '<path d="M2 15h18l-2 4H4l-2-4Z" stroke-linejoin="round"/><path d="M11 15V3l6 8-6 4"/>',
 "tree": '<path d="M11 19v-6M11 13c0-4 3-6 6-6 0 4-2 6-6 6Zm0 0c0-4-3-6-6-6 0 4 2 6 6 6Z" stroke-linejoin="round"/>',
 "hall": '<path d="M2 8 11 3l9 5M4 8v9M8 8v9M14 8v9M18 8v9M2 19h18" stroke-linejoin="round"/>',
 "bath": '<path d="M3 14h16c0 3-3 5-8 5s-8-2-8-5Z" stroke-linejoin="round"/><path d="M7 11c0-2 1.5-2 1.5-4S7 5 7 3M11 11c0-2 1.5-2 1.5-4S11 5 11 3M15 11c0-2 1.5-2 1.5-4S15 5 15 3"/>',
}
KIND = {"view":("k-view","Paysage"), "eat":("k-eat","Table"),
        "make":("k-make","Artisanat"), "past":("k-past","Autrefois")}


def doing(kind, icon, title, note):
    cls, label = KIND[kind]
    return (f'<div class="doing"><span class="ico {cls}">'
            f'<svg viewBox="0 0 22 22" aria-hidden="true">{ICONS[icon]}</svg></span>'
            f'<span><b>{title}<span class="kind {cls}">{label}</span></b>'
            f'<span class="n">{note}</span></span></div>')


def station(no, name, when, why, doings=(), nights=None, leg=False):
    cls = "station leg" if leg else "station"
    mon = f'<div class="mon"><span class="no">{no}</span>'
    if not leg:
        mon += f'<span class="vname">{name}</span>'
        if nights:
            mon += f'<span class="nn">{nights}</span>'
    mon += "</div>"
    body = f'<div class="pane"><h3>{name}</h3><p class="when">{when}</p><p class="why">{why}</p>'
    if doings:
        body += '<div class="doings">' + "".join(doing(*d) for d in doings) + "</div>"
    body += "</div>"
    return f'<div class="{cls}">{mon}{body}</div>'


def span(dur, via):
    return (f'<div class="span"><div class="rule"></div><div class="txt">'
            f'<span class="dur">{dur}</span><span class="via">{via}</span></div></div>')


def page(title, seal, h1, deck, tally, mapsvg, caption, body):
    """Assemble un document complet, prêt pour l'ouverture locale."""
    tal = "".join(f'<div><span class="k">{k}</span>'
                  f'<span class="v{" hi" if hi else ""}">{v}</span></div>'
                  for k, v, hi in tally)
    cap = "".join(caption)
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
{FONTS}
<style>{CSS}</style>
</head>
<body>
<div class="plate"><div class="wrap">
  <div>
    <p class="seal">{seal}</p>
    <h1>{h1}</h1>
    <p class="deck">{deck}</p>
  </div>
  <div class="tally">{tal}</div>
</div></div>

<figure class="chart">
{mapsvg}
<figcaption>{cap}</figcaption>
</figure>

<div class="wrap">
{body}
</div>
</body>
</html>
"""
