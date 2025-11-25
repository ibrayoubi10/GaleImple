from src.core import GenerateurPreferences, AlgorithmeGaleShapley
from src.experiments import TesteurAlgorithme
from src.analysis import afficher_rapport_console
from src.visuals import Visuals


def main() -> None:
    testeur = TesteurAlgorithme()

    # liste des scénarios 
    scenarios = [
        (10, 10, 42, "Scenario 10x10"),
        (20, 20, 55, "Scenario 20x20"),
        (50,   50,    15, "Scenario 50x50"),
        (100, 100,    26, "Scenario 100x100"),
        (200, 200,    19, "Scenario 200x200"),
        (500, 500,    11, "Scenario 500x500"),
    ]

    for i, (n_etu, n_etab, seed, nom) in enumerate(scenarios):
        res = testeur.tester_configuration(
            n_etudiants=n_etu,
            n_etablissements=n_etab,
            seed=seed,
            nom=nom,
            verbose_algo=False,
        )

        # On affiche un rapport détaillé uniquement pour le premier
        if i == 0:
            afficher_rapport_console(res["rapport"])

    #visuals
    vis = Visuals(testeur)
    vis.dashboard()


if __name__ == "__main__":
    main()
