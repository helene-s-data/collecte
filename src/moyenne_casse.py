def calculer_moyenne(notes):
    total = 0
    for note in notes:
        # ici j'ai supprimé [:-1] qui voulait dire de prendre toutes les notes sauf la dernière : 14
        total += note
    return total / len(notes)


notes_etudiants = [15, 12, 18, 9, 14]
moyenne = calculer_moyenne(notes_etudiants)
print(f"La moyenne des notes est : {moyenne}")