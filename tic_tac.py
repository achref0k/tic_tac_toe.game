class Player:
    def __init__(self):
        self.name=""
        self.symbole=""
    def choose_name(self):
        while True:
         name=input("Enter your name Letters Only :")
         if name.isalpha():
            self.name=name
            break
         print("invalid name ,please use letters only :")
    def choose_symbole(self):
       while True :
          symbole=input("Enter your symbol :")
          if symbole.isalpha() and len(symbole)==1 :
             self.symbole=symbole.upper()
             break
          print("invalid symbole  enter a valid symbol :")
class Menu:

   def display_main_menu(self):
      print("*************welcome to my first X-O Game******************")
      print("1.Start Game")
      print("2.quit Game")
      choice=input("Enter you choice")
      return choice
   def display_endgame_menu(self):
      print("*************Game Over !****************")
      print("1.Restart Game")
      print("2.quit Game")
      choice=input("Enter you choice")
      return choice
class Board:
   def __init__(self):
      self.board=[str(i) for i in range(1,10)]  
   def display_board(self):
      for i in range (0,9,3):
         print("|".join(self.board[i:i+3]))
         if i<9:
            print("-"*5)

   def update_board(self,choice,symbole):
      if self.is_valid_move(choice):
         self.board[choice-1]=symbole
         return True
      return False
   def is_valid_move(self,choice):
      return self.board[choice-1].isdigit()
   def reset_board(self):
      self.board=[str(i) for i in range(1,10)] 
class Game:
   def __init__(self):
      self.players=[Player(),Player()]
      self.board=Board()
      self.menu=Menu()
      self.currebt_player_index=0

   def start_game (self):
      choice=self.menu.display_main_menu()
      if choice=="1":
         self.setup_players()
         self.play_game()
      else :
         self.quit_game()
   def setup_players(self):
      for number,player in enumerate (self.players,start=1):
         print(f"player{number} --> enter your details:")
         player.choose_name()
         player.choose_symbole()
         print("-"*20)
   def play_game(self):
      while True :
         self.play_turn()
         if self.check_win() :
            print(f"***************{self.players[self.currebt_player_index].name} is the loser ***************")
            choice=self.menu.display_endgame_menu()
            if choice=="1":
               self.restart_game()
            else:
               self.quit_game()
               break
         elif self.check_draw():
            print("******draw******")
            
   def restart_game(self):
      self.board.reset_board()
      self.currebt_player_index=0
      self.play_game()
   def check_win(self):
      
      win_combinations=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
      for combo in win_combinations:
         if (self.board.board[combo[0]]==self.board.board[combo[1]]==self.board.board[combo[2]]):
            return True
      return False
   def play_turn(self):
      player=self.players[self.currebt_player_index]
      self.board.display_board()
      
      print(f"{player.name}'s turn ({player.symbole} )")
      while True :
         try:
            cell_choice=int(input("give your choice   :"))
            if 1<= cell_choice<=9 and  self.board.update_board(cell_choice,player.symbole):
               break
            else :
               print("invalid move  ")
         except ValueError:
            print("please enter a number between 1 and 9.")
      self.switch_player()
   def switch_player(self):
      self.currebt_player_index= 1-self.currebt_player_index
   def check_draw(self):
      check=False
      l=0
      for i in self.board.board :
         if i.isalpha() :
            l+=1
      if l==9:
         check =True
      return check
   def quit_game(self):
      print("******************thank you for playing !*******************************")

game=Game()
game.start_game()