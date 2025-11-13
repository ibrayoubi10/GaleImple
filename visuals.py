# visuals.py
from __future__ import annotations
from typing import Any

import matplotlib.pyplot as plt

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
        plt.show()
