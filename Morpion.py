class Morpion:
    def __init__(self):
        self.plateau = [[' ' for _ in range(3)] for _ in range(3)]
        self.joueur = 'X'

    def afficher(self):
        for ligne in self.plateau:
            print('|'.join(ligne))
            print('-' * 5)

    def jouer_coup(self, ligne, col):
        if self.plateau[ligne][col] == ' ':
            self.plateau[ligne][col] = self.joueur
            return True
        return False

    def changer_joueur(self):
        self.joueur = 'O' if self.joueur == 'X' else 'X'

    def verifier_victoire(self):
        # Implémenter la logique pour vérifier si un joueur a gagné
        pass

    def plateau_plein(self):
        return all(cell != ' ' for row in self.plateau for cell in row)
