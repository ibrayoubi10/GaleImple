"""
Module pour lancer des expériences sur l'algorithme de Gale-Shapley
"""

from __future__ import annotations
from typing import Dict, Any, List

from core import GenerateurPreferences, AlgorithmeGaleShapley
from analysis import AnalyseurSatisfaction


class TesteurAlgorithme:
    """
    Lance plusieurs expériences et stocke les résultats.
    """
    def __init__(self) -> None:
        self.resultats: List[Dict[str, Any]] = []

    def tester_configuration(
        self,
        n_etudiants: int,
        n_etablissements: int,
        seed: int,
        nom: str = "",
        verbose_algo: bool = False,
    ) -> Dict[str, Any]:
        generateur = GenerateurPreferences(n_etudiants, n_etablissements, seed)
        pref_etu, pref_etab = generateur.generer()

        algo = AlgorithmeGaleShapley(pref_etu, pref_etab)
        appariement_etu = algo.executer(verbose=verbose_algo)

        analyseur = AnalyseurSatisfaction(pref_etu, pref_etab, appariement_etu)
        rapport = analyseur.rapport_complet()

        result = {
            "nom": nom or f"{n_etudiants}x{n_etablissements}_seed{seed}",
            "config": {
                "n_etudiants": n_etudiants,
                "n_etablissements": n_etablissements,
                "seed": seed,
            },
            "rapport": rapport,
            "historique": algo.historique,
        }
        self.resultats.append(result)
        return result
