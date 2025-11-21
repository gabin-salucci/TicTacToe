import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#F1FAEE")
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.game_mode = None
        self.buttons = []
        self.wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.create_menu()
    
    def create_menu(self):
        for w in self.root.winfo_children():
            w.destroy()
        
        f = tk.Frame(self.root, bg="#F1FAEE")
        f.pack(expand=True, pady=50)
        
        tk.Label(f, text="TIC TAC TOE", font=('Arial', 36, 'bold'), 
                fg='#D4AF37', bg="#F1FAEE").pack(pady=20)
        
        tk.Button(f, text="2 Joueurs", font=('Arial', 16, 'bold'),
                 bg="#FFCA3A", fg='white', width=15, height=2,
                 command=lambda: self.start_game('pvp')).pack(pady=10)
        
        tk.Button(f, text="Contre IA", font=('Arial', 16, 'bold'),
                 bg="#52D1C0", fg='white', width=15, height=2,
                 command=lambda: self.start_game('pvia')).pack(pady=10)
    
    def start_game(self, mode):
        self.game_mode = mode
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.create_board()
    
    def create_board(self):
        for w in self.root.winfo_children():
            w.destroy()
        
        f = tk.Frame(self.root, bg="#F1FAEE")
        f.pack(expand=True)
        
        self.info = tk.Label(f, text=f"Tour: {self.current_player}",
                            font=('Arial', 18, 'bold'),
                            fg='#ecf0f1', bg="#F1FAEE")
        self.info.pack(pady=20)
        
        g = tk.Frame(f, bg="#1D3557")
        g.pack(pady=10)
        
        self.buttons = []
        for i in range(9):
            b = tk.Button(g, text='', font=('Arial', 32, 'bold'),
                         width=5, height=2, bg='#ecf0f1',
                         command=lambda x=i: self.move(x))
            b.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(b)
        
        tk.Button(f, text="Menu", font=('Arial', 12),
                 bg='#95a5a6', fg='white',
                 command=self.create_menu).pack(pady=20)
    
    def move(self, pos):
        if self.board[pos]:
            return
        
        self.board[pos] = self.current_player
        self.buttons[pos].config(text=self.current_player,
                                fg='#B300FF' if self.current_player == 'X' else '#FF1B1C')
        
        if self.check_win(self.current_player):
            self.end(f"Joueur {self.current_player} gagne!")
            return
        
        if '' not in self.board:
            self.end("Match nul!")
            return
        
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.info.config(text=f"Tour: {self.current_player}")
        
        if self.game_mode == 'pvia' and self.current_player == 'O':
            self.root.after(50, self.ia_move)
    
    def ia_move(self):
        m = ia(self.board, 'O')
        if m is not False:
            self.move(m)
    
    def check_win(self, p):
        return any(all(self.board[i] == p for i in w) for w in self.wins)
    
    def end(self, msg):
        messagebox.showinfo("Fin", msg)
        self.create_menu()


def ia(b, s):
    if len(b) != 9:
        return False
    
    o = 'X' if s == 'O' else 'O'
    w = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    # Gagner ou bloquer
    for p in (s, o):
        for c in w:
            v = [b[i] for i in c]
            if v.count(p) == 2 and v.count('') == 1:
                return c[v.index('')]
    
    # Centre
    if b[4] == '':
        return 4
    
    # Coins
    for i in (0, 2, 6, 8):
        if b[i] == '':
            return i 
    
    # Reste
    for i in range(9):
        if b[i] == '':
            return i
    
    return False


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x600")
    root.resizable(False, False)
    TicTacToe(root)
    root.mainloop()