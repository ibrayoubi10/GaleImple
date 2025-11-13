# main.py
from experiments import TesteurAlgorithme
from analysis import afficher_rapport_console
from visuals import creer_visualisations


def main() -> None:
    testeur = TesteurAlgorithme()

    res1 = testeur.tester_configuration(
        n_etudiants=10,
        n_etablissements=10,
        seed=42,
        nom="Scenario 10x10",
        verbose_algo=False,
    )

    afficher_rapport_console(res1["rapport"])

    # Autres scénarios
    testeur.tester_configuration(20, 20, seed=1, nom="Scenario 20x20")
    testeur.tester_configuration(50, 50, seed=2, nom="Scenario 50x50")
    testeur.tester_configuration(100, 100, seed=2, nom="Scenario 100x100")
    testeur.tester_configuration(200, 200, seed=2, nom="Scenario 200x200")
    testeur.tester_configuration(500, 500, seed=2, nom="Scenario 500x500")

    # Visualisations
    creer_visualisations(testeur)


if __name__ == "__main__":
    main()
