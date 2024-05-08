import os
player1 = 'X'
player2 = 'O'
player1 = '\N{WHITE CIRCLE}'
player2 = '\N{BLACK CIRCLE}'

board = [['_' for _ in range(7)] for _ in range(6)] # 7 x 6 board
def move(column, mark):
	for cell in list(range(6))[::-1]:
		if board[0][column] != '_':
			print('Column full')
			break
		if board[cell][column] == '_':
			board[cell][column] = mark
			break

def print_board():
	print(*[0, 1, 2, 3, 4, 5, 6])
	for row in board:
		print(*row)
def check():
	for row in range(6):
		for col in range(6):
			u = 0
			d = 0
			r = 0
			l = 0
			ur = 0
			ul = 0
			dr = 0
			dl = 0
turn = 1
while True:
	os.system('clear')
	print_board()
	choice = int(input('your choice: '))
	assert choice in range(7)
	if turn:
		move(choice, player1)
	else:
		move(choice, player2)
	turn = int(not(turn))
	
