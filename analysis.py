"""
Analyse des performances de l'algorithme de Gale-Shapley.

Correspond à la question 3 du Projet Stable Marriage.
"""

from __future__ import annotations
from typing import Dict, List, Any
import numpy as np
from collections import Counter


class AnalyseurSatisfaction:

    def __init__(
        self,
        pref_etu: Dict[int, List[int]],
        pref_etab: Dict[int, List[int]],
        appariements: Dict[int, int],
    ) -> None:
        self.pref_etu = pref_etu
        self.pref_etab = pref_etab
        self.appariements = appariements

    def calculer_rangs_etudiants(self) -> List[int]:
        """Rang (0 = premier choix) de l'établissement obtenu par chaque étudiant."""
        rangs: List[int] = []
        for etudiant, etablissement in self.appariements.items():
            rang = self.pref_etu[etudiant].index(etablissement)
            rangs.append(rang)
        return rangs

    def calculer_rangs_etablissements(self) -> List[int]:
        """Rang (0 = premier choix) de l'étudiant obtenu par chaque établissement."""
        rangs: List[int] = []
        for etudiant, etablissement in self.appariements.items():
            rang = self.pref_etab[etablissement].index(etudiant)
            rangs.append(rang)
        return rangs

    # ---------- METRIQUES ----------

    def satisfaction_normalise(self, rangs: List[int], n_max: int) -> float:
        """
        Satisfaction normalisée entre 0 et 1.

        1 = tous ont leur premier choix (rang 0)
        0 = tous ont leur dernier choix (rang n_max - 1)
        """
        if not rangs:
            return 0.0
        if n_max <= 1:
            return 1.0
        return 1 - (float(np.mean(rangs)) / float(n_max - 1))

    def _distribution_rangs(self, rangs: List[int]) -> Dict[int, int]:
        """Retourne un dict rang -> nombre d'agents."""
        return dict(Counter(rangs))

    # ---------- RAPPORT COMPLET ----------

    def rapport_complet(self) -> Dict[str, Any]:
        """Génère un rapport complet de satisfaction (sans affichage)."""
        rangs_etu = self.calculer_rangs_etudiants()
        rangs_etab = self.calculer_rangs_etablissements()

        n_etab = len(self.pref_etab)
        n_etu = len(self.pref_etu)

        sat_etu = self.satisfaction_normalise(rangs_etu, n_etab)
        sat_etab = self.satisfaction_normalise(rangs_etab, n_etu)

        rapport: Dict[str, Any] = {
            "rangs_etudiants": rangs_etu,
            "rangs_etablissements": rangs_etab,
            "satisfaction_etudiants": sat_etu,
            "satisfaction_etablissements": sat_etab,
            "satisfaction_globale": (sat_etu + sat_etab) / 2.0,
            "premiers_choix_etudiants": sum(1 for r in rangs_etu if r == 0),
            "premiers_choix_etablissements": sum(1 for r in rangs_etab if r == 0),
            "cout_social": int(sum(rangs_etu) + sum(rangs_etab)),
            "rang_moyen_etudiants": float(np.mean(rangs_etu)) if rangs_etu else 0.0,
            "rang_moyen_etablissements": float(np.mean(rangs_etab)) if rangs_etab else 0.0,
            "rang_median_etudiants": float(np.median(rangs_etu)) if rangs_etu else 0.0,
            "rang_median_etablissements": float(np.median(rangs_etab)) if rangs_etab else 0.0,
            "distribution_rangs_etudiants": self._distribution_rangs(rangs_etu),
            "distribution_rangs_etablissements": self._distribution_rangs(rangs_etab),
            "nombre_etudiants": n_etu,
            "nombre_etablissements": n_etab,
        }

        return rapport


# ---------- AFFICHAGE CONSOLE SÉPARÉ ----------

def _afficher_distribution_console(distribution: Dict[int, int]) -> None:
    """Affiche un histogramme textuel à partir d'un dict rang -> count."""
    if not distribution:
        print("  (aucune donnée)")
        return

    max_rang = max(distribution.keys())
    max_affiche = min(max_rang, 9)  # 0 à 9, et 10+ regroupés

    for rang in range(0, max_affiche + 1):
        count = distribution.get(rang, 0)
        barre = "█" * count
        print(f"  Rang {rang:2d} : {barre} ({count})")

    if max_rang > 9:
        count_rest = sum(
            c for r, c in distribution.items() if r >= 10
        )
        print(f"  Rang 10+ : {'█' * count_rest} ({count_rest})")


def afficher_rapport_console(rapport: Dict[str, Any]) -> None:
    """Affiche joliment le rapport de satisfaction."""

    print("\n" + "=" * 80)
    print("RAPPORT DE SATISFACTION")
    print("=" * 80)

    print(f"\n📊 MÉTRIQUES PRINCIPALES")
    print("-" * 80)
    print(f"Satisfaction des étudiants       : {rapport['satisfaction_etudiants']:.2%} ⭐")
    print(f"Satisfaction des établissements  : {rapport['satisfaction_etablissements']:.2%}")
    print(f"Satisfaction globale             : {rapport['satisfaction_globale']:.2%}")

    print(f"\n🎯 PREMIERS CHOIX")
    print("-" * 80)
    n_etu = len(rapport["rangs_etudiants"])
    n_etab = len(rapport["rangs_etablissements"])
    print(
        f"Étudiants avec 1er choix         : {rapport['premiers_choix_etudiants']}/{n_etu} "
        f"({rapport['premiers_choix_etudiants'] / n_etu * 100:.1f}%)"
    )
    print(
        f"Établissements avec 1er choix    : {rapport['premiers_choix_etablissements']}/{n_etab} "
        f"({rapport['premiers_choix_etablissements'] / n_etab * 100:.1f}%)"
    )

    print(f"\n📈 STATISTIQUES DES RANGS")
    print("-" * 80)
    print(f"Rang moyen - Étudiants           : {rapport['rang_moyen_etudiants']:.2f}")
    print(f"Rang moyen - Établissements      : {rapport['rang_moyen_etablissements']:.2f}")
    print(f"Rang médian - Étudiants          : {rapport['rang_median_etudiants']:.1f}")
    print(f"Rang médian - Établissements     : {rapport['rang_median_etablissements']:.1f}")
    print(f"Coût social total                : {rapport['cout_social']}")

    print(f"\n📊 DISTRIBUTION DES RANGS - ÉTUDIANTS")
    print("-" * 80)
    _afficher_distribution_console(rapport["distribution_rangs_etudiants"])

    print(f"\n📊 DISTRIBUTION DES RANGS - ÉTABLISSEMENTS")
    print("-" * 80)
    _afficher_distribution_console(rapport["distribution_rangs_etablissements"])
