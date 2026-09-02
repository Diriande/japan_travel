#!/usr/bin/env python3
"""Enveloppe de l'application : styles et gabarit."""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Petrona:ital,wght@0,400;0,600;0,700;1,400'
         '&family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" '
         'rel="stylesheet">')

CSS = """
:root{
  --washi:#EFEFEA; --sheet:#FAFAF7; --card:#FFFFFF;
  --sumi:#1A1D19; --encre:#3E4238; --pale:#767B6E; --trait:#DCDCD3;
  --bero:#1D3E63; --beni:#B23A2E; --clay:#8A6A3F; --moss:#4A6247; --ambre:#C6873C;
  --side:#191C18; --side-t:#E7E7DF; --side-p:#8D9186; --side-a:#2A2E27;
  --sc-a:#F0B978; --sc-b:#C4694A; --sc-c:#BFD4DF; --sc-d:#F1D9B0;
  --sc-e:#AFC9DE; --sc-f:#E4EDF2;
  --sc-l1:#8E6B57; --sc-l2:#6D5A50; --sc-l3:#463F3C; --sc-l4:#252523;
  --sc-sig:#1A1614; --sc-astre:#FBE9C8;
  --f-disp:"Petrona",Georgia,"Times New Roman",serif;
  --f-body:"Archivo","Helvetica Neue",Arial,sans-serif;
  --f-num:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,monospace;
  --r:14px; --sidew:270px;
  --m-sea:#E4E8E4; --m-land:#D3D6CE; --m-coast:#B7BCB0; --m-ink:#1A1D19; --m-muted:#7B8074;
  --m-route:var(--bero); --m-air:var(--beni); --m-exc:var(--clay);
  --m-stop:var(--bero); --m-onstop:#FFFFFF;
}
:root:not([data-theme="light"]){ @media (prefers-color-scheme:dark){
  --washi:#12140F; --sheet:#181B15; --card:#1E211B;
  --sumi:#E9EAE2; --encre:#C6C9BC; --pale:#8B9083; --trait:#2E322A;
  --bero:#7FA6CE; --beni:#DE8878; --clay:#BFA075; --moss:#8FAE88; --ambre:#D9A768;
  --side:#0C0E0A; --side-t:#E4E5DC; --side-p:#7E8377; --side-a:#1C2018;
  --sc-a:#8A5B3E; --sc-b:#4A2C2A; --sc-c:#3E566A; --sc-d:#8A7050;
  --sc-e:#3B546B; --sc-f:#6C8296;
  --sc-l1:#4E3B31; --sc-l2:#3B322C; --sc-l3:#2A2624; --sc-l4:#181817;
  --sc-sig:#0A0908; --sc-astre:#C4A57A;
  --m-sea:#0E1210; --m-land:#232821; --m-coast:#39402F; --m-ink:#E9EAE2; --m-muted:#8B9083;
  --m-route:#7FA6CE; --m-air:#DE8878; --m-exc:#BFA075; --m-stop:#7FA6CE; --m-onstop:#0E1720;
}}
:root[data-theme="dark"]{
  --washi:#12140F; --sheet:#181B15; --card:#1E211B;
  --sumi:#E9EAE2; --encre:#C6C9BC; --pale:#8B9083; --trait:#2E322A;
  --bero:#7FA6CE; --beni:#DE8878; --clay:#BFA075; --moss:#8FAE88; --ambre:#D9A768;
  --side:#0C0E0A; --side-t:#E4E5DC; --side-p:#7E8377; --side-a:#1C2018;
  --sc-a:#8A5B3E; --sc-b:#4A2C2A; --sc-c:#3E566A; --sc-d:#8A7050;
  --sc-e:#3B546B; --sc-f:#6C8296;
  --sc-l1:#4E3B31; --sc-l2:#3B322C; --sc-l3:#2A2624; --sc-l4:#181817;
  --sc-sig:#0A0908; --sc-astre:#C4A57A;
  --m-sea:#0E1210; --m-land:#232821; --m-coast:#39402F; --m-ink:#E9EAE2; --m-muted:#8B9083;
  --m-route:#7FA6CE; --m-air:#DE8878; --m-exc:#BFA075; --m-stop:#7FA6CE; --m-onstop:#0E1720;
}

*{box-sizing:border-box}
body{margin:0;background:var(--washi);color:var(--encre);
  font-family:var(--f-body);font-size:15px;line-height:1.62;-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:var(--f-disp);color:var(--sumi);margin:0;line-height:1.14;font-weight:600}
b,strong{color:var(--sumi);font-weight:600}
em{font-style:italic}
a{color:var(--bero)}
button{font:inherit;color:inherit}

/* ————————————————————————— charpente ————————————————————————— */
.wrap{display:grid;grid-template-columns:var(--sidew) minmax(0,1fr);min-height:100vh}

.side{background:var(--side);color:var(--side-t);position:sticky;top:0;height:100vh;
  display:flex;flex-direction:column;overflow-y:auto;overflow-x:hidden}
.brand{padding:22px 20px 16px;border-bottom:1px solid var(--side-a);display:flex;gap:13px;align-items:flex-start}
.brand .mk{font-family:var(--f-disp);font-size:27px;line-height:1;color:var(--beni);
  writing-mode:vertical-rl;letter-spacing:.14em;padding-top:2px}
.brand .bt{font-family:var(--f-disp);font-size:19px;color:var(--side-t);line-height:1.2}
.brand .bs{font-family:var(--f-num);font-size:10px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--side-p);margin-top:5px}

.pick{padding:14px 14px 4px}
.pick label{font-family:var(--f-num);font-size:9.5px;letter-spacing:.17em;text-transform:uppercase;
  color:var(--side-p);display:block;margin:0 6px 7px}
.pick select{width:100%;background:var(--side-a);color:var(--side-t);border:1px solid transparent;
  border-radius:9px;padding:9px 10px;font-size:13.5px;cursor:pointer}
.pick select:focus{outline:none;border-color:var(--beni)}

.nav{padding:12px 10px;flex:1}
.nav .grp{font-family:var(--f-num);font-size:9.5px;letter-spacing:.17em;text-transform:uppercase;
  color:var(--side-p);margin:14px 10px 6px}
.nav button{display:flex;align-items:center;gap:10px;width:100%;background:none;border:0;
  padding:8px 10px;border-radius:9px;cursor:pointer;color:var(--side-t);text-align:left;font-size:14px}
.nav button:hover{background:var(--side-a)}
.nav button[aria-current="true"]{background:var(--side-a);color:#fff;font-weight:600}
.nav button[aria-current="true"] .ic{color:var(--beni)}
.nav .ic{width:17px;height:17px;flex:none;color:var(--side-p)}
.nav .tag{margin-left:auto;font-family:var(--f-num);font-size:10.5px;color:var(--side-p)}
.nav .stp{padding-left:14px;font-size:13px;color:var(--side-p)}
.nav .stp:hover{color:var(--side-t)}
.nav .stp .no{font-family:var(--f-num);font-size:10.5px;width:15px;color:var(--beni)}

.tools{padding:12px 14px 18px;border-top:1px solid var(--side-a);display:flex;flex-wrap:wrap;gap:7px}
.tools button{background:var(--side-a);border:0;border-radius:8px;padding:7px 11px;
  font-size:12px;cursor:pointer;color:var(--side-p)}
.tools button:hover{color:var(--side-t)}

.main{min-width:0;padding:0 0 90px}
.view{display:none;animation:in .22s ease}
.view.on{display:block}
@keyframes in{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:none}}
.pad{padding:0 40px;max-width:1080px}

/* ————————————————————————— scènes ————————————————————————— */
.scene{display:block;width:100%;height:100%;position:absolute;inset:0}
.hero{position:relative;height:290px;overflow:hidden;display:flex;align-items:flex-end}
.hero .in{position:relative;padding:0 40px 26px;max-width:1080px;width:100%}
.hero h1{font-size:clamp(34px,4.6vw,54px);color:#FBFBF6;text-shadow:0 2px 22px rgba(0,0,0,.5)}
.hero h1 em{color:#F6D9A8}
.hero .deck{color:#EDE9DF;max-width:60ch;margin:11px 0 0;text-shadow:0 1px 14px rgba(0,0,0,.6);font-size:15.5px}
.hero .seal{display:inline-flex;align-items:center;gap:9px;font-family:var(--f-num);font-size:10.5px;
  letter-spacing:.19em;text-transform:uppercase;color:#F3E4CB;margin-bottom:13px;
  text-shadow:0 1px 10px rgba(0,0,0,.7)}
.hero .seal i{width:11px;height:11px;background:var(--beni);display:block;border-radius:2px}

/* ————————————————————————— blocs communs ————————————————————————— */
.eyebrow{font-family:var(--f-num);font-size:10.5px;letter-spacing:.19em;text-transform:uppercase;
  color:var(--beni);margin:0 0 9px}
h2{font-size:clamp(23px,2.5vw,31px);margin:0 0 6px}
h2 em{color:var(--bero)}
.lede{color:var(--pale);max-width:64ch;margin:0 0 20px}
section{padding:44px 0 4px}
.card{background:var(--card);border:1px solid var(--trait);border-radius:var(--r)}

.tally{display:grid;grid-template-columns:repeat(auto-fit,minmax(132px,1fr));gap:1px;
  background:var(--trait);border:1px solid var(--trait);border-radius:var(--r);overflow:hidden;margin:26px 0 0}
.tally .c{background:var(--card);padding:15px 17px}
.tally .k{font-family:var(--f-num);font-size:9.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--pale)}
.tally .v{font-family:var(--f-num);font-size:25px;color:var(--sumi);margin-top:3px;font-weight:500}
.tally .c.hi .v{color:var(--beni)}

.grid{display:grid;gap:18px}
.g2{grid-template-columns:repeat(auto-fit,minmax(330px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(238px,1fr))}

/* étapes en vitrine */
.stcard{overflow:hidden;display:flex;flex-direction:column}
.stcard .top{position:relative;height:132px}
.stcard .lab{position:absolute;left:16px;bottom:12px;color:#FBFBF6;text-shadow:0 2px 16px rgba(0,0,0,.6)}
.stcard .lab .n{display:block;font-family:var(--f-disp);font-size:25px;line-height:1.1}
.stcard .lab .k{display:block;font-family:var(--f-num);font-size:11px;letter-spacing:.14em;opacity:.86}
.stcard .no{position:absolute;right:14px;top:13px;width:29px;height:29px;border-radius:50%;
  background:rgba(12,12,10,.62);color:#fff;font-family:var(--f-num);font-size:13px;
  display:grid;place-items:center;backdrop-filter:blur(3px)}
.stcard .bd{padding:15px 17px 17px;flex:1;display:flex;flex-direction:column;gap:11px}
.stcard .meta{display:flex;flex-wrap:wrap;gap:6px}
.pill{font-family:var(--f-num);font-size:10.5px;letter-spacing:.05em;padding:3.5px 9px;border-radius:99px;
  background:color-mix(in srgb,var(--bero) 11%,transparent);color:var(--bero);white-space:nowrap}
.pill.w{background:color-mix(in srgb,var(--ambre) 15%,transparent);color:var(--clay)}
.pill.m{background:color-mix(in srgb,var(--moss) 14%,transparent);color:var(--moss)}
.pill.r{background:color-mix(in srgb,var(--beni) 12%,transparent);color:var(--beni)}
.stcard .why{color:var(--pale);font-size:14px;margin:0}
.stcard ul{margin:0;padding-left:17px;font-size:13.5px;color:var(--pale)}
.stcard li{margin:3px 0}

/* ————————————————————————— jour par jour ————————————————————————— */
.dayhead{display:flex;align-items:center;gap:14px;margin:34px 0 13px;padding-top:8px}
.dayhead .kj{font-family:var(--f-disp);font-size:20px;color:var(--beni)}
.dayhead h3{font-size:20px}
.dayhead .rule{flex:1;height:1px;background:var(--trait)}
.dayhead .cnt{font-family:var(--f-num);font-size:11px;color:var(--pale)}

.day{border:1px solid var(--trait);border-radius:var(--r);background:var(--card);margin-bottom:11px;overflow:hidden}
.day.done{opacity:.62}
.dh{display:flex;align-items:center;gap:14px;padding:14px 17px;cursor:pointer;user-select:none;width:100%;
  background:none;border:0;text-align:left}
.dh:hover{background:color-mix(in srgb,var(--bero) 4%,transparent)}
.dn{font-family:var(--f-num);font-size:12px;color:var(--card);background:var(--bero);
  width:36px;height:36px;border-radius:9px;display:grid;place-items:center;flex:none;font-weight:600}
.day.done .dn{background:var(--moss)}
.dt{flex:1;min-width:0}
.dt .t{display:block;font-family:var(--f-disp);font-size:17.5px;color:var(--sumi);line-height:1.25}
.dt .s{display:block;font-family:var(--f-num);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--pale);margin-top:2px}
.dh .chev{color:var(--pale);flex:none;transition:transform .2s}
.day.open .chev{transform:rotate(180deg)}
.dbody{display:none;padding:2px 17px 17px;border-top:1px solid var(--trait)}
.day.open .dbody{display:block}

.blk{display:grid;grid-template-columns:58px 22px 1fr auto;gap:12px;align-items:start;padding:11px 0;
  border-bottom:1px dashed var(--trait)}
.blk:last-of-type{border-bottom:0}
.blk .hh{font-family:var(--f-num);font-size:12px;color:var(--pale);padding-top:2px}
.blk .ic{width:19px;height:19px;color:var(--bero);margin-top:2px}
.blk.k-eat .ic{color:var(--beni)} .blk.k-move .ic{color:var(--pale)}
.blk.k-walk .ic{color:var(--moss)} .blk.k-rest .ic{color:var(--clay)}
.blk .q{display:block;color:var(--sumi);font-weight:600;font-size:14.5px}
.blk .nt{display:block;color:var(--pale);font-size:13.5px;margin-top:2px}
.blk .cc{font-family:var(--f-num);font-size:12px;color:var(--clay);white-space:nowrap;padding-top:2px}
.blk .cc small{color:var(--pale);display:block;font-size:10px;text-align:right}
.blk.tick{cursor:pointer}
.blk.tick:hover .q{color:var(--bero)}
.blk.off .q,.blk.off .nt{text-decoration:line-through;color:var(--pale)}

.dnote{margin-top:13px;padding:11px 13px;border-radius:10px;
  background:color-mix(in srgb,var(--ambre) 9%,transparent);
  border-left:3px solid var(--ambre);color:var(--encre);font-size:13.5px}
.dnote>b:first-child{display:block;font-family:var(--f-num);font-size:9.5px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--clay);margin-bottom:3px}
.dnote b{color:var(--sumi);font-weight:600}
.jot{width:100%;margin-top:11px;background:var(--sheet);border:1px solid var(--trait);border-radius:10px;
  padding:10px 12px;font:inherit;font-size:13.5px;color:var(--encre);resize:vertical;min-height:52px}
.jot:focus{outline:none;border-color:var(--bero)}
.dsum{display:flex;gap:16px;flex-wrap:wrap;margin-top:12px;padding-top:11px;border-top:1px solid var(--trait);
  font-family:var(--f-num);font-size:11.5px;color:var(--pale)}
.dsum b{color:var(--sumi)}

/* ————————————————————————— carte ————————————————————————— */
.mapbox{background:var(--sheet);border:1px solid var(--trait);border-radius:var(--r);overflow:hidden}
.mapbox svg{display:block;width:100%;height:auto}
.legend{display:flex;flex-wrap:wrap;gap:9px 20px;padding:14px 18px;border-top:1px solid var(--trait);
  font-family:var(--f-num);font-size:11px;color:var(--pale)}
.legend .li{display:flex;align-items:center;gap:7px}
.legend .dot{width:9px;height:9px;border-radius:50%;display:block}
.legend .sw{width:19px;height:2.5px;display:block;border-radius:2px}

/* ————————————————————————— budget ————————————————————————— */
.bar{height:9px;border-radius:99px;background:var(--trait);overflow:hidden;margin:9px 0 0}
.bar i{display:block;height:100%;background:var(--bero);border-radius:99px}
.bar.over i{background:var(--beni)}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{padding:10px 13px;text-align:left;border-bottom:1px solid var(--trait);vertical-align:top}
th{font-family:var(--f-num);font-size:9.5px;letter-spacing:.15em;text-transform:uppercase;
  color:var(--pale);font-weight:500}
td.n,th.n{text-align:right;font-family:var(--f-num);white-space:nowrap}
tr:last-child td{border-bottom:0}
tr.sum td{background:color-mix(in srgb,var(--bero) 6%,transparent);font-weight:600;color:var(--sumi)}
.sheet{border:1px solid var(--trait);border-radius:var(--r);overflow:hidden;background:var(--card)}
.scroll{overflow-x:auto}

.qadd{display:grid;grid-template-columns:repeat(auto-fill,minmax(112px,1fr));gap:9px}
.qadd button{background:var(--card);border:1px solid var(--trait);border-radius:11px;padding:11px 9px;
  cursor:pointer;text-align:center;transition:.14s}
.qadd button:hover{border-color:var(--bero);transform:translateY(-1px)}
.qadd .q{display:block;font-size:13px;color:var(--sumi);font-weight:500}
.qadd .p{display:block;font-family:var(--f-num);font-size:11.5px;color:var(--clay);margin-top:2px}

.form{display:flex;flex-wrap:wrap;gap:9px;align-items:center;margin:16px 0}
.form input,.form select{background:var(--card);border:1px solid var(--trait);border-radius:9px;
  padding:9px 11px;font:inherit;font-size:14px;color:var(--encre)}
.form input:focus,.form select:focus{outline:none;border-color:var(--bero)}
.form input[type=number]{width:104px;font-family:var(--f-num)}
.form .go{background:var(--bero);color:#fff;border:0;border-radius:9px;padding:10px 17px;cursor:pointer;font-weight:600}
.form .go:hover{filter:brightness(1.08)}

.ring{display:grid;place-items:center}
.ring svg{transform:rotate(-90deg)}
.ring .lbl{font-family:var(--f-num);font-size:11px;color:var(--pale);text-align:center;margin-top:7px}

.spend{list-style:none;margin:0;padding:0}
.spend li{display:flex;align-items:center;gap:12px;padding:9px 0;border-bottom:1px solid var(--trait);font-size:14px}
.spend li:last-child{border-bottom:0}
.spend .w{flex:1;min-width:0;color:var(--sumi)}
.spend .w small{display:block;color:var(--pale);font-family:var(--f-num);font-size:10.5px;letter-spacing:.06em}
.spend .a{font-family:var(--f-num);color:var(--clay);white-space:nowrap}
.spend .x{background:none;border:0;color:var(--pale);cursor:pointer;padding:3px 6px;border-radius:6px;line-height:1}
.spend .x:hover{color:var(--beni);background:color-mix(in srgb,var(--beni) 10%,transparent)}

/* ————————————————————————— listes à cocher ————————————————————————— */
.check{list-style:none;margin:0;padding:0}
.check li{display:flex;gap:12px;align-items:flex-start;padding:11px 0;border-bottom:1px solid var(--trait);cursor:pointer}
.check li:last-child{border-bottom:0}
.check .bx{width:19px;height:19px;border:1.6px solid var(--trait);border-radius:5px;flex:none;margin-top:2px;
  display:grid;place-items:center;transition:.14s}
.check li.on .bx{background:var(--moss);border-color:var(--moss);color:#fff}
.check li.on .w{text-decoration:line-through;color:var(--pale)}
.check .w{flex:1;color:var(--sumi)}
.check .w small{display:block;color:var(--pale);font-size:13px;font-weight:400;text-decoration:none}
.check .when{font-family:var(--f-num);font-size:10.5px;color:var(--pale);white-space:nowrap;padding-top:3px}
.check li.crit .when{color:var(--beni)}

.note{border-left:3px solid var(--beni);background:color-mix(in srgb,var(--beni) 7%,transparent);
  padding:14px 17px;border-radius:0 10px 10px 0;margin:18px 0}
.note b{display:block;margin-bottom:4px}
.note p{margin:0;font-size:14px;color:var(--pale)}

.modal{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:60;display:grid;
  place-items:center;padding:22px;overflow:auto}
.modal .box{background:var(--card);border:1px solid var(--trait);border-radius:var(--r);
  padding:24px 26px;max-width:620px;width:100%;box-shadow:0 18px 50px rgba(0,0,0,.3)}
.modal h3{font-size:22px}
.modal .form{flex-wrap:wrap}

footer{margin:56px 40px 0;padding:22px 0 0;border-top:1px solid var(--trait);
  font-size:12.5px;color:var(--pale);max-width:1000px}

/* ————————————————————————— étroit ————————————————————————— */
.burger{display:none;position:fixed;left:13px;top:13px;z-index:40;background:var(--side);color:var(--side-t);
  border:0;border-radius:10px;width:41px;height:41px;cursor:pointer;place-items:center;
  box-shadow:0 3px 14px rgba(0,0,0,.28)}
.veil{display:none;position:fixed;inset:0;background:rgba(0,0,0,.42);z-index:29}
.veil.on{display:block}

@media(max-width:900px){
  .wrap{grid-template-columns:1fr}
  .side{position:fixed;left:0;top:0;z-index:30;width:var(--sidew);
    transform:translateX(-100%);transition:transform .24s}
  .side.on{transform:none}
  .burger{display:grid}
  .main{padding-top:58px}
  .pad{padding:0 20px}
  .hero .in{padding:0 20px 22px}
  .hero{height:238px}
  footer{margin:44px 20px 0}
  .blk{grid-template-columns:52px 20px 1fr;gap:9px}
  .blk .cc{grid-column:3;text-align:left;padding-top:0}
  .blk .cc small{text-align:left;display:inline;margin-left:5px}
}
@media print{
  .side,.burger,.tools,.jot,.qadd,.form{display:none}
  .wrap{display:block} .view{display:block!important} .day .dbody{display:block!important}
}
"""


def page(titre, corps, script):
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titre}</title>
{FONTS}
<style>{CSS}</style>
</head><body>
{corps}
<script>{script}</script>
</body></html>"""
