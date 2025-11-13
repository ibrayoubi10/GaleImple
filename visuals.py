# visuals.py
from __future__ import annotations
from typing import Any

import matplotlib.pyplot as plt
import numpy as np


def creer_visualisations(testeur: Any) -> None:
    """
    Exemple : histogrammes des rangs étudiants pour chaque scénario.
    'testeur' est une instance de TesteurAlgorithme ou tout objet
    ayant un attribut .resultats de la bonne forme.
    """
    for res in testeur.resultats:
        nom = res["nom"]
        rangs = res["rapport"]["rangs_etudiants"]

        if not rangs:
            continue

        plt.figure()
        plt.hist(rangs, bins=range(1, max(rangs) + 2), align="left", rwidth=0.8)
        plt.xlabel("Rang de l'établissement (1 = meilleur choix)")
        plt.ylabel("Nombre d'étudiants")
        plt.title(f"Distribution des rangs côté étudiants\nScénario : {nom}")
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def tracer_satisfaction(testeur: Any) -> None:
    """
    Trace un graphique comparant, pour chaque scénario, la satisfaction
    (en %) des étudiants et des établissements.
    On suppose que chaque élément de testeur.resultats contient :
      - "nom" : nom du scénario
      - "rapport" : dict avec clés
          * "satisfaction_etudiants"
          * "satisfaction_etablissements"
    """
    noms: list[str] = []
    sat_etu: list[float] = []
    sat_etab: list[float] = []

    for res in testeur.resultats:
        rapport = res["rapport"]
        noms.append(res["nom"])
        sat_etu.append(rapport["satisfaction_etudiants"] * 100.0)
        sat_etab.append(rapport["satisfaction_etablissements"] * 100.0)

    if not noms:
        print("Aucun résultat dans le testeur, rien à tracer.")
        return

    x = np.arange(len(noms))          # positions des scénarios
    largeur = 0.35                    # largeur des barres

    plt.figure()
    plt.bar(x - largeur/2, sat_etu, width=largeur, label="Étudiants")
    plt.bar(x + largeur/2, sat_etab, width=largeur, label="Établissements")

    plt.xticks(x, noms, rotation=20, ha="right")
    plt.ylabel("Satisfaction (%)")
    plt.ylim(0, 100)
    plt.title("Satisfaction par scénario\n(Étudiants vs Établissements)")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()
