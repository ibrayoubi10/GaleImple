from __future__ import annotations
from typing import Any
import matplotlib.pyplot as plt
import numpy as np


class Visuals:

    def __init__(self, testeur: Any):
        self.testeur = testeur

        self.c1 = "#4C72B0"   # bleu
        self.c2 = "#DD8452"   # orange
        self.c3 = "#55A868"   # vert
        self.c4 = "#C44E52"   # rouge / rose profond
        self.c5 = "#8172B3"   # violet
        self.cgray = "#999999"

        plt.style.use("ggplot")

    def dashboard(self) -> None:
        for res in self.testeur.resultats:
            nom = res["nom"]
            rapport = res["rapport"]

            rangs_etu = rapport["rangs_etudiants"]
            rangs_etab = rapport["rangs_etablissements"]

            sat_etu = rapport["satisfaction_etudiants"] * 100
            sat_etab = rapport["satisfaction_etablissements"] * 100
            sat_glob = rapport["satisfaction_globale"] * 100

            fig, axes = plt.subplots(3, 2, figsize=(14, 12))
            fig.suptitle(f"Dashboard – {nom}", fontsize=18, fontweight="bold")

            ax = axes[0, 0]
            if rangs_etu:
                ax.hist(rangs_etu, bins=range(0, max(rangs_etu)+2),
                        align="left", rwidth=0.8, color=self.c1)
            ax.set_title("Histogramme rangs étudiants")
            ax.set_xlabel("Rang")
            ax.set_ylabel("Nombre")

            ax = axes[0, 1]
            if rangs_etab:
                ax.hist(rangs_etab, bins=range(0, max(rangs_etab)+2),
                        align="left", rwidth=0.8, color=self.c2)
            ax.set_title("Histogramme rangs établissements")
            ax.set_xlabel("Rang")
            ax.set_ylabel("Nombre")

            ax = axes[1, 0]
            ax.bar(["Étudiants", "Établissements"],
                   [sat_etu, sat_etab],
                   color=[self.c3, self.c4])
            ax.set_title("Satisfaction (%)")
            ax.set_ylim(0, 100)

            ax = axes[1, 1]
            ax.bar(["Globale"], [sat_glob], color=self.c5)
            ax.set_title("Satisfaction globale (%)")
            ax.set_ylim(0, 100)

            ax = axes[2, 0]
            if rangs_etu:
                ax.boxplot([rangs_etu],
                           labels=["Étudiants"],
                           patch_artist=True,
                           boxprops=dict(facecolor=self.c1, color=self.cgray),
                           medianprops=dict(color="black"))
            ax.set_title("Boxplot rangs étudiants")
            ax.set_ylabel("Rang")

            ax = axes[2, 1]
            ax.axis("off")
            ax.text(0.5, 0.5, "Espace libre\n(pour heatmap)",
                    ha="center", va="center", fontsize=12, color=self.cgray)

            plt.tight_layout(rect=[0, 0, 1, 0.95])
            plt.show()