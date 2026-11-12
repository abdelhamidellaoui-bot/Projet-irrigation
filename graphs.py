"""Génère les graphiques du README à partir de la base SQLite.

Adapter DB_PATH au nom réel de ta base (ex. "irrigation.db").
"""
import os
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd
DB_PATH = "agri.db"   
OUT_DIR = "graphs"
os.makedirs(OUT_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM parcelles", conn)
conn.close()

df["statut"] = df["irrigue"].map({1: "Irriguée", 0: "Non irriguée"})
COLORS = {"Irriguée": "#2a7fbf", "Non irriguée": "#d9822b"}

# --- Figure 2 : rendement moyen par culture ---
g = (df.groupby("culture")["rendement_t_ha"].mean()
       .sort_values(ascending=False).round(1))
fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.bar(g.index, g.values, color="#4c9a5f")
ax.bar_label(bars, fmt="%.1f")
ax.set_ylabel("Rendement moyen (t/ha)")
ax.set_title("Rendement moyen par culture")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(f"{OUT_DIR}/rendement_par_culture.png", dpi=200)
plt.close(fig)

# --- Figure 3 : surface irriguée vs non irriguée ---
s = df.groupby("statut")["surface_ha"].sum()
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(s.values, labels=s.index, autopct=lambda p: f"{p:.0f} %\n({p * s.sum() / 100:.0f} ha)",
       colors=[COLORS[k] for k in s.index], startangle=90,
       wedgeprops={"edgecolor": "white"})
ax.set_title("Répartition des surfaces selon l'irrigation")
fig.tight_layout()
fig.savefig(f"{OUT_DIR}/surface_irrigation.png", dpi=200)
plt.close(fig)

# --- Figure 4 : rendement moyen irrigué vs non irrigué ---
r = df.groupby("statut")["rendement_t_ha"].mean().round(1)
fig, ax = plt.subplots(figsize=(5, 4))
bars = ax.bar(r.index, r.values, color=[COLORS[k] for k in r.index])
ax.bar_label(bars, fmt="%.1f")
ax.set_ylabel("Rendement moyen (t/ha)")
ax.set_title("Rendement selon le statut d'irrigation")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(f"{OUT_DIR}/rendement_irrigation.png", dpi=200)
plt.close(fig)

print("Graphiques enregistrés dans", OUT_DIR)
