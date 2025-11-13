from experiments import TesteurAlgorithme
from analysis import afficher_rapport_console
from visuals import creer_visualisations, tracer_satisfaction


def main() -> None:
    testeur = TesteurAlgorithme()

    # liste des scénarios 
    scenarios = [
        (10, 10, 42, "Scenario 10x10"),
        (20, 20, 1, "Scenario 20x20"),
        (50,   50,    2, "Scenario 50x50"),
        (100, 100,    3, "Scenario 100x100"),
        (200, 200,    4, "Scenario 200x200"),
        (500, 500,    5, "Scenario 500x500"),
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
    print("\nGénération des histogrammes de rangs pour les petits scénarios...")
    creer_visualisations(testeur)

    print("\nGénération du graphique de satisfaction globale...")
    tracer_satisfaction(testeur)


if __name__ == "__main__":
    main()
