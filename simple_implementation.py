from collections import deque

def gale_shapley(men_prefs, women_prefs):
    
    # Préparer indices rapides et structures
    # Pour chaque femme, construire un dict de rang pour comparaison rapide
    women_rank = {
        w: {man: rank for rank, man in enumerate(pref_list)}
        for w, pref_list in women_prefs.items()
    }

    # File des hommes libres (proposants) avec pour chacun l'index de la prochaine femme à qui proposer
    free_men = deque(men_prefs.keys())
    next_proposal_index = {m: 0 for m in men_prefs}

    # Engagements: femme -> homme (None si libre)
    fiance_of_woman = {w: None for w in women_prefs}
    # Résultat ultimately: man -> woman
    fiance_of_man = {m: None for m in men_prefs}

    while free_men:
        man = free_men.popleft()
        prefs = men_prefs[man]
        if next_proposal_index[man] >= len(prefs):
            # Plus de femmes à proposer -> cet homme reste célibataire
            continue
        woman = prefs[next_proposal_index[man]]
        next_proposal_index[man] += 1

        current = fiance_of_woman.get(woman)
        if current is None:
            # femme libre -> s'engage avec cet homme
            fiance_of_woman[woman] = man
            fiance_of_man[man] = woman
        else:
            # femme compare l'ancien et le nouveau prétendant
            # plus petit rang = plus préféré
            if women_rank[woman].get(man, float('inf')) < women_rank[woman].get(current, float('inf')):
                # elle préfère le nouveau -> se fiance avec nouveau
                fiance_of_woman[woman] = man
                fiance_of_man[man] = woman
                # l'ancien redevient libre
                fiance_of_man[current] = None
                free_men.append(current)
            else:
                # elle rejette le nouvel homme -> celui-ci reste libre et proposera la prochaine
                free_men.append(man)

    return fiance_of_man

def is_stable(matching, men_prefs, women_prefs):
    """
    Vérifie la stabilité d'un matching donné.
    Retourne (True/False, list_of_blocking_pairs)
    Un blocking pair (m,w) est un couple non apparié qui se préfèrent mutuellement
    par rapport à leurs partenaires actuels.
    """
    # construire inverse: femme -> homme
    woman_of = {w: None for w in women_prefs}
    for m, w in matching.items():
        if w is not None:
            woman_of[w] = m

    # construire rangs
    men_rank = {m: {w: rank for rank, w in enumerate(pref)} for m, pref in men_prefs.items()}
    women_rank = {w: {m: rank for rank, m in enumerate(pref)} for w, pref in women_prefs.items()}

    blockers = []
    for m in men_prefs:
        current_w = matching.get(m)
        for w in men_prefs[m]:
            if w == current_w:
                # pas de blocage sur sa partenaire actuelle ni après (préférences ordonnées)
                break
            current_man_of_w = woman_of.get(w)
            # m préfère w à sa partenaire actuelle ?
            prefers = men_rank[m].get(w, float('inf')) < men_rank[m].get(current_w, float('inf')) if current_w is not None else True
            # w préfère m à son partenaire actuel ?
            w_prefers = women_rank[w].get(m, float('inf')) < women_rank[w].get(current_man_of_w, float('inf')) if current_man_of_w is not None else True
            if prefers and w_prefers:
                blockers.append((m, w))
    return (len(blockers) == 0, blockers)

def example():
    # Exemple simple
    men_prefs = {
        "A": ["X", "W", "Y", "Z"],
        "B": ["W", "X", "Y", "Z"],
        "C": ["W", "X", "Z", "Y"],
        "D": ["X", "Y", "W", "Z"]
    }

    women_prefs = {
        "W": ["B", "C", "A", "D"],
        "X": ["D", "A", "B", "C"],
        "Y": ["A", "B", "C", "D"],
        "Z": ["A", "B", "C", "D"]
    }

    matching = gale_shapley(men_prefs, women_prefs)
    print("Matching (homme -> femme):")
    for m in sorted(matching):
        print(f"  {m} -> {matching[m]}")

    stable, blockers = is_stable(matching, men_prefs, women_prefs)
    print("\nEst-ce stable ?", stable)
    if not stable:
        print("Paires bloquantes :", blockers)
    else:
        print("Aucune paire bloquante trouvée.")

if __name__ == "__main__":
    example()