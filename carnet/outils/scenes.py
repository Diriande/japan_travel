#!/usr/bin/env python3
"""Bandeaux de paysage en aplats, un par étape.

Pas de photographie : des couches de collines générées, une silhouette signature
et un ciel dégradé. C'est déterministe — même graine, même dessin — donc une
étape garde son paysage d'une génération à l'autre.
"""
import math

W, H = 1500, 380


class Rng:
    """Générateur congruentiel, pour que le dessin ne bouge pas entre deux builds."""
    def __init__(self, seed):
        self.s = seed & 0x7FFFFFFF or 1

    def next(self):
        self.s = (self.s * 1103515245 + 12345) & 0x7FFFFFFF
        return self.s / 0x7FFFFFFF

    def between(self, a, b):
        return a + (b - a) * self.next()


def graine(txt):
    h = 2166136261
    for c in txt:
        h = ((h ^ ord(c)) * 16777619) & 0xFFFFFFFF
    return h


def crete(rng, base, ampleur, dents, aigu=0.0):
    """Une ligne de crête : somme de sinusoïdes, plus des pics si aigu > 0."""
    pts, n = [], 60
    phases = [rng.between(0, 6.28) for _ in range(3)]
    for i in range(n + 1):
        t = i / n
        y = base
        for k, ph in enumerate(phases):
            y -= ampleur * (0.6 / (k + 1)) * math.sin(t * dents * (k + 1) * 3.14159 + ph)
        if aigu:
            y -= aigu * ampleur * math.exp(-((t - 0.5) ** 2) / 0.02)
        pts.append((t * W, y))
    d = f"M0,{H} L{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for x, y in pts[1:]:
        d += f" L{x:.1f},{y:.1f}"
    return d + f" L{W},{H} Z"


# ————————————————————— silhouettes signature —————————————————————

def torii(x, y, s, fill):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="{fill}">'
            f'<path d="M-46,-4 L46,-4 L44,4 L-44,4 Z"/>'
            f'<path d="M-52,-14 Q0,-22 52,-14 L50,-6 Q0,-13 -50,-6 Z"/>'
            f'<rect x="-30" y="4" width="7" height="46"/><rect x="23" y="4" width="7" height="46"/>'
            f'<rect x="-26" y="14" width="52" height="5"/></g>')


def gassho(x, y, s, fill):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="{fill}">'
            f'<path d="M0,-40 L34,26 L-34,26 Z"/>'
            f'<rect x="-26" y="26" width="52" height="12"/></g>')


def pagode(x, y, s, fill):
    t = ""
    for i in range(4):
        w, yy = 40 - i * 8, -i * 21
        t += (f'<path d="M{-w},{yy} L{w},{yy} L{w-9},{yy-9} L{-w+9},{yy-9} Z"/>'
              f'<rect x="{-w+13}" y="{yy-22}" width="{2*(w-13)}" height="13"/>')
    t += '<rect x="-3" y="-104" width="6" height="20"/>'
    return f'<g transform="translate({x},{y}) scale({s})" fill="{fill}">{t}</g>'


def vague(x, y, s, fill):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="{fill}">'
            f'<path d="M-90,10 Q-50,-30 -10,-6 Q20,12 34,-14 Q48,-38 82,-20 '
            f'Q62,-40 34,-30 Q6,-20 -10,-16 Q-46,-46 -90,10 Z"/>'
            f'<path d="M-70,16 Q-30,-8 6,6 Q34,17 58,2" fill="none" stroke="{fill}" stroke-width="4"/></g>')


def volcan(x, y, s, fill):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="{fill}">'
            f'<path d="M-78,30 L-20,-34 Q0,-46 20,-34 L78,30 Z"/>'
            f'<path d="M-22,-32 Q-8,-56 -14,-72 Q2,-58 6,-74 Q16,-56 8,-34 Z" opacity=".55"/></g>')


def tour(x, y, s, fill):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="{fill}">'
            f'<path d="M-30,44 L-11,-30 L11,-30 L30,44 Z"/>'
            f'<rect x="-15" y="-16" width="30" height="6"/>'
            f'<rect x="-3" y="-58" width="6" height="28"/></g>')


def cascade(x, y, s, fill):
    return (f'<g transform="translate({x},{y}) scale({s})" fill="{fill}">'
            f'<path d="M-40,-56 L40,-56 L28,44 L-28,44 Z" opacity=".35"/>'
            f'<path d="M-16,-56 L16,-56 L11,40 L-11,40 Z" opacity=".55"/></g>')


SIGNES = {"torii": torii, "gassho": gassho, "pagode": pagode,
          "vague": vague, "volcan": volcan, "tour": tour, "cascade": cascade}


def scene(cid, signe="torii", teinte="soir"):
    """Un bandeau SVG autonome, dont les couleurs suivent les tokens de la page."""
    rng = Rng(graine(cid))
    ciel = {"soir": ("var(--sc-a)", "var(--sc-b)"),
            "aube": ("var(--sc-c)", "var(--sc-d)"),
            "jour": ("var(--sc-e)", "var(--sc-f)")}[teinte]
    g = f"sk{abs(graine(cid)) % 99999}"

    couches = ""
    for i in range(4):
        base = 178 + i * 46 + rng.between(-10, 10)
        d = crete(rng, base, 34 - i * 5, 1.4 + i * 0.7, aigu=(0.9 if i == 0 and signe == "volcan" else 0))
        couches += f'<path d="{d}" fill="var(--sc-l{i+1})"/>'

    sx = rng.between(W * 0.62, W * 0.80)
    sig = SIGNES[signe](sx, 258, 1.0, "var(--sc-sig)")

    astre = (f'<circle cx="{rng.between(W*0.40, W*0.55):.0f}" cy="{rng.between(78, 118):.0f}" '
             f'r="{rng.between(30, 42):.0f}" fill="var(--sc-astre)"/>')

    return (f'<svg class="scene" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" '
            f'role="presentation" aria-hidden="true">'
            f'<defs><linearGradient id="{g}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{ciel[0]}"/><stop offset="1" stop-color="{ciel[1]}"/>'
            f'</linearGradient></defs>'
            f'<rect width="{W}" height="{H}" fill="url(#{g})"/>{astre}{couches}{sig}</svg>')
