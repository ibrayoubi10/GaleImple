"""
Module pour générer des préférences aléatoires complètes
et une implémentation de l'algorithme de Gale-Shapley.

Correspond à la question 1 et 2 du Projet Stable Marriage.
"""

# core.py
from __future__ import annotations
from typing import Dict, List, Tuple, Any
import random
import numpy as np


class GenerateurPreferences:
    """
    Génère des préférences aléatoires pour étudiants et établissements.
    """
    def __init__(self, n_etudiants: int, n_etablissements: int, seed: int | None = None) -> None:
        self.n_etudiants = n_etudiants
        self.n_etablissements = n_etablissements
        self.seed = seed

        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)

    def generer(self) -> Tuple[Dict[int, List[int]], Dict[int, List[int]]]:
        """
        Retourne:
            - pref_etudiants: {etu -> [etab triés par préférence]}
            - pref_etablissements: {etab -> [etu triés par préférence]}
        """
        etudiants = list(range(self.n_etudiants))
        etablissements = list(range(self.n_etablissements))

        pref_etudiants: Dict[int, List[int]] = {}
        for e in etudiants:
            prefs = etablissements.copy()
            random.shuffle(prefs)
            pref_etudiants[e] = prefs

        pref_etablissements: Dict[int, List[int]] = {}
        for a in etablissements:
            prefs = etudiants.copy()
            random.shuffle(prefs)
            pref_etablissements[a] = prefs

        return pref_etudiants, pref_etablissements


class AlgorithmeGaleShapley:
    """
    Implémentation de l'algorithme de Gale–Shapley (version étudiants qui proposent).
    """
    def __init__(
        self,
        pref_etudiants: Dict[int, List[int]],
        pref_etablissements: Dict[int, List[int]],
    ) -> None:
        self.pref_etudiants = pref_etudiants
        self.pref_etablissements = pref_etablissements

        self.n_etudiants = len(pref_etudiants)
        self.n_etablissements = len(pref_etablissements)

        # Historique des étapes si tu veux analyser ou visualiser
        self.historique: List[Dict[str, Any]] = []

    def _score_etablissement(self, etab: int) -> Dict[int, int]:
        """
        Retourne un dict: étudiant -> rang dans la préférence de l'établissement.
        Plus petit = plus préféré.
        """
        ordre = self.pref_etablissements[etab]
        return {etu: rang for rang, etu in enumerate(ordre)}

    def executer(self, verbose: bool = False) -> Dict[int, int]:
        """
        Retourne un dictionnaire: {etudiant -> etablissement}
        """
        libres = set(self.pref_etudiants.keys())
        index_proposition: Dict[int, int] = {etu: 0 for etu in self.pref_etudiants}
        appariement_etab: Dict[int, int] = {}

        scores_etab: Dict[int, Dict[int, int]] = {
            etab: self._score_etablissement(etab) for etab in self.pref_etablissements
        }

        while libres:
            etu = libres.pop()
            prefs = self.pref_etudiants[etu]

            if index_proposition[etu] >= len(prefs):
                if verbose:
                    print(f"[WARN] Étudiant {etu} n'a plus d'établissement à proposer.")
                continue

            etab = prefs[index_proposition[etu]]
            index_proposition[etu] += 1

            self._enregistrer_etape(etu, etab, appariement_etab)

            if etab not in appariement_etab:
                appariement_etab[etab] = etu
                if verbose:
                    print(f"Étudiant {etu} est accepté par l'établissement {etab}.")
            else:
                etu_actuel = appariement_etab[etab]
                if scores_etab[etab][etu] < scores_etab[etab][etu_actuel]:
                    appariement_etab[etab] = etu
                    libres.add(etu_actuel)
                    if verbose:
                        print(
                            f"Étudiant {etu} remplace l'étudiant {etu_actuel} "
                            f"à l'établissement {etab}."
                        )
                else:
                    libres.add(etu)
                    if verbose:
                        print(
                            f"Étudiant {etu} est rejeté par l'établissement {etab} "
                            f"(garde {etu_actuel})."
                        )

        appariement_etu: Dict[int, int] = {}
        for etab, etu in appariement_etab.items():
            appariement_etu[etu] = etab

        return appariement_etu

    def _enregistrer_etape(self, etu: int, etab: int, appariement_etab: Dict[int, int]) -> None:
        self.historique.append({
            "etudiant": etu,
            "etablissement_demande": etab,
            "appariement_actuel": dict(appariement_etab),
        })


# ==========================
#  Bloc de test local
# ==========================

if __name__ == "__main__":

    n_etudiants = 15
    n_etablissements = 15
    seed = 42

    print(f"Test de génération avec {n_etudiants} étudiants, "
          f"{n_etablissements} établissements, seed={seed}\n")

    generateur = GenerateurPreferences(n_etudiants, n_etablissements, seed)
    pref_etu, pref_etab = generateur.generer()

    print("Préférences des étudiants :")
    for e, prefs in pref_etu.items():
        print(f"  Étudiant {e} : {prefs}")

    print("\nPréférences des établissements :")
    for a, prefs in pref_etab.items():
        print(f"  Établissement {a} : {prefs}")

    print("\nLancement de l'algorithme de Gale–Shapley...\n")
    algo = AlgorithmeGaleShapley(pref_etu, pref_etab)
    appariement_etu = algo.executer(verbose=True)

    print("\nAppariement final (étudiant -> établissement) :")
    for etu, etab in appariement_etu.items():
        print(f"  Étudiant {etu} → Établissement {etab}")
