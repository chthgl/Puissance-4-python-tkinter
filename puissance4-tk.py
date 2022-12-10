import tkinter as tk
from tkinter import messagebox
import random
# constantes pour la grille
ROWS = 6
COLS = 7

# constantes pour les joueurs
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

# couleurs pour les joueurs
PLAYER_1_COLOR = 'red'
PLAYER_2_COLOR = 'yellow'

class ConnectFour(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Connect Four')

        # créer une grille vide
        self.grid = []
        for i in range(ROWS):
            row = [EMPTY] * COLS
            self.grid.append(row)

        # créer la zone de jeu
        self.canvas = tk.Canvas(self, width=COLS*100, height=ROWS*100)
        self.canvas.grid(row=1, column=0, columnspan=COLS)

        # ajouter un événement pour détecter les clics de souris
        self.canvas.bind('<Button-1>', self.play_turn)

        self.current_player = PLAYER_1
        # dessiner les lignes de démarcation de la grille
        for i in range(1, ROWS):
            self.canvas.create_line(0, i*100, COLS*100, i*100, fill='black')
        for i in range(1, COLS):
            self.canvas.create_line(i*100, 0, i*100, ROWS*100, fill='black')
    def play_turn_robot(self):
        # utiliser la stratégie minimax pour trouver le meilleur coup pour le robot
        best_col = self.find_best_move_minimax()
  

    def find_best_move_minimax(self):
        best_col = None
        #best_eval = float('-inf')
        #best_eval = self.minimax(1, PLAYER_2)
        # Si toutes les colonnes sont pleines, choisit une colonne au hasard
        if best_col is None:
            best_col = random.randint(0, COLS-1)
            # trouver la première ligne vide dans la colonne sélectionnée
            for row in range(ROWS-1, -1, -1):
                if self.grid[row][best_col] == EMPTY:
                    break
            # placer le pion dans la case libre la plus basse de la colonne sélectionnée
            self.grid[row][best_col] = self.current_player
            # mettre à jour l'interface graphique pour afficher le pion
            color = PLAYER_1_COLOR if self.current_player == PLAYER_1 else PLAYER_2_COLOR
            self.canvas.create_oval(best_col*100+10, row*100+10, best_col*100+90, row*100+90, fill=color)
        # vérifier si le joueur courant a gagné
        if self.check_win(self.current_player):
            self.show_win_message()
        # changer de joueur
        if self.current_player == PLAYER_1:
            self.current_player = PLAYER_2
        else:
            self.current_player = PLAYER_1
        self.play_turn
        # retourner la colonne avec la meilleure évaluation
        #return best_col

    # jouer un coup dans la colonne spécifiée pour le joueur spécifié
    def play_turn(self, event):
        # calculer la colonne où le joueur a cliqué
        col = event.x // 100

        # si c'est au tour du joueur 2, utiliser la stratégie minimax pour déterminer le meilleur coup
        # et appeler la méthode play_turn_robot avec les coordonnées du coup calculé
        if self.current_player == PLAYER_2:
            self.play_turn_robot()
            return
        # calculer la colonne où le joueur a cliqué
        col = event.x // 100

        # trouver la première ligne vide dans la colonne spécifiée
        for row in range(ROWS-1, -1, -1):
            if self.grid[row][col] == EMPTY:
                self.grid[row][col] = self.current_player
                break

        # dessiner le pion du joueur courant
        color = PLAYER_1_COLOR if self.current_player == PLAYER_1 else PLAYER_2_COLOR
        self.canvas.create_oval(col*100+10, row*100+10, col*100+90, row*100+90, fill=color)

        # vérifier si le joueur courant a gagné
        if self.check_win(self.current_player):
            self.show_win_message()
        # changer de joueur
        if self.current_player == PLAYER_1:
            self.current_player = PLAYER_2
        else:
            self.current_player = PLAYER_1

    # vérifier si le joueur spécifié a gagné
    # vérifier si le joueur spécifié a gagné
    def check_win(self, player):
        # vérifier les lignes
        for row in range(ROWS):
            for col in range(COLS-3):
                if self.grid[row][col] == player and self.grid[row][col+1] == player and self.grid[row][col+2] == player and self.grid[row][col+3] == player:
                    return True

        # vérifier les colonnes
        for row in range(ROWS-3):
            for col in range(COLS):
                if self.grid[row][col] == player and self.grid[row+1][col] == player and self.grid[row+2][col] == player and self.grid[row+3][col] == player:
                    return True

        # vérifier les diagonales (\ et /)
        for row in range(ROWS-3):
            for col in range(COLS-3):
                if self.grid[row][col] == player and self.grid[row+1][col+1] == player and self.grid[row+2][col+2] == player and self.grid[row+3][col+3] == player:
                    return True
                if self.grid[row][col+3] == player and self.grid[row+1][col+2] == player and self.grid[row+2][col+1] == player and self.grid[row+3][col] == player:
                    return True

        # aucun joueur n'a gagné
        return False

    # afficher un message de victoire
    def show_win_message(self):
        messagebox.showinfo('Victoire', 'Le joueur {} a gagné !'.format(self.current_player))
        self.destroy()

    # jouer une partie de puissance 4
    def play_game(self):
        self.mainloop()

# créer et lancer une partie de puissance 4
game = ConnectFour()
game.play_game()
