
from __future__ import print_function
#!/usr/bin/python3

import numpy as np
import argparse

class move:
	def __init__(self,row,col):
		self.row=row
		self.col=col

player, opponent =1,-1
board=[]

class TicTacToe:
	def __init__(self, board=None, play = 1) -> None:
		if board is None:
			self.board = self.init_board()
		else:
			self.board = board
		
		self.play = play
		

	def init_board(self):
		return np.array([[0,0,0],[0,0,0],[0,0,0]])

	def print_board(self):
		print (self.board)
		
	def isMovesLeft(self):
		for i in range(3):
			for j in range(3):
				if (self.board[i][j]== 0):
					return True
		return False



	def eval_win(self):
		
		for row in range(3):
			if (self.board[row][0]==self.board[row][1] and self.board[row][1]==self.board[row][2]):
				if (self.board[row][0]== player):
					return +1
				elif (self.board[row][0]== opponent):
					return -1
		
		for col in range(3):
			if (self.board[0][col]==self.board[1][col] and self.board[1][col]==self.board[2][col]):
				if (self.board[0][col]== player):
					return +1
				elif (self.board[0][col]== opponent):
					return -1
		
		if (self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2]):
			if (self.board[0][0]== player):
				return 1
			elif (self.board[0][0]== opponent):
				return -1
	    
		if (self.board[0][2]==self.board[1][1] and self.board[1][1]==self.board[2][0]):
			if (self.board[0][2]== player):
				return 1
			elif (self.board[0][2]== opponent):
				return -1
	    
	    # Else if none of them have won then return 0
		return 0
	    


	def minimax(self,chance):		#initial after x places then chance of o goes
		board = self.board
		score=self.eval_win()
		
		if (score == 1) :
			return score + 1
		if (score == -1):			
			return score - 1
			
		if(self.isMovesLeft()==False):			#draw
			return 0 
			
		if(chance == player):
			bestp=-1000
			for i in range(3):
				for j in range(3):
					if (board[i][j] == 0):
						board[i][j]= player
						bestp=max(bestp,self.minimax(opponent))
						
						board[i][j]=0
			return bestp		
		else:
			besto=1000
			for i in range(3):
				for j in range(3):
					if (self.board[i][j] == 0):
						board[i][j]= opponent
						besto=min(besto,self.minimax(player))
						board[i][j]=0
			return besto	


	def findBestMoveplayer(self):
		board = self.board
		best=-1000
		bmove=move(-1,-1)
		for i in range(3):
			for j in range(3):
				if (board[i][j] == 0):
					board[i][j]= player
					
					temp=self.minimax(opponent)
					
					board[i][j]= 0
					if temp>best:
						
						bmove.row,bmove.col=i,j
						best=temp																				
		self.board[bmove.row][bmove.col]  = player
		
		return bmove
		
	def findBestMoveOpponent(self):
		board = self.board
		best= 1000
		bmove=move(-1,-1)
		for i in range(3):
			for j in range(3):
				if (board[i][j] == 0):
					board[i][j]= opponent
					
					temp=self.minimax(player)
					
					board[i][j]= 0
					if temp < best:
						
						bmove.row,bmove.col=i,j
						best=temp																				
		self.board[bmove.row][bmove.col]  = opponent
		
		return bmove

	def play_game(self):
		if(self.play == player):
			for i in range(3):
				for j in range(3):
					if (self.board[i][j] == 0):
						self.board[i][j]= player
						if (self.eval_win() == 1 ):
							self.board[i][j]= player
							return self.board, self.eval_win()
						else:
							self.board[i][j]= 0
							

							
			bestmove=self.findBestMoveplayer()
			
			if(self.eval_win() != 1 and self.eval_win() != -1 ) and (self.isMovesLeft() == True) :
				self.play = opponent
				self.play_game()
				
		elif(self.play == opponent):
			for i in range(3):
				for j in range(3):
					if (self.board[i][j] == 0):
						self.board[i][j]= opponent
						if (self.eval_win() == -1):
							self.board[i][j]= opponent
							return self.board, self.eval_win()
						else:
							self.board[i][j]= 0
			bestmove=self.findBestMoveOpponent()
			
			if(self.eval_win() != 1 and self.eval_win() != -1 ) and (self.isMovesLeft() == True) :
				self.play = player
				self.play_game()
			
		return self.board, self.eval_win()
		
def load_board( filename ):
	return np.loadtxt( filename)
	
def main():
	parser = argparse.ArgumentParser(description='Play tic tac toe')
	parser.add_argument('-f', '--file', default=None, type=str ,help='load board from file')
	parser.add_argument('-p', '--player', default=1, type=int, choices=[1,-1] ,help='player that playes first, 1 or -1')
	args = parser.parse_args()

	board = load_board(args.file) if args.file else None
	
	ttt = TicTacToe(board, 1)
	
	ttt.print_board()
	b,p = ttt.play_game()
	print("final board: \n{}".format(b))
	print("winner: player {}".format(p))

if __name__ == '__main__':
	main()
	

