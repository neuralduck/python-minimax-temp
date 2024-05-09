import os
player1 = 1
player2 = -1
symbol1 = '\N{WHITE CIRCLE}'
symbol2 = '\N{BLACK CIRCLE}'

board = [[0 for _ in range(7)] for _ in range(6)] # 7 x 6 board
board[2][3] = 1
board[3][3] = 1
def move(column, mark):
	for cell in list(range(6))[::-1]:
		if board[0][column] != 0:
			print('Column full')
			break
		if board[cell][column] == 0:
			board[cell][column] = mark
			break

def available_moves():
	count = 6*7
	for i in range(6):
		for j in range(7):
			if board[i][j] in (1, -1):
				count -= 1
	return count
def print_board():
	print(*list(f'  {i}' for i in [0, 1, 2, 3, 4, 5, 6]))
	get_symbol = lambda x: f'{symbol1} |' if x == 1 else f'{symbol2} |' if x == -1 else '  |'
	dash1 = '\N{Three-Em Dash}'
	dash2 = '\N{Horizontal Bar}'
	dash3 = '\N{Two-Em Dash}'
	print(dash2*29)
	for row in board:
		row = list(map(get_symbol, row))
		print('|', *row)
		print(dash2*29)
def check(board):
	for i in range(6):
		for j in range(7):
			if board[i][j] in (1, -1):
				if j+3 <= 6:
					right = 0
					for n in range(4):
						right += board[i][j+n]
					if right == 4: 
						print(f'right from {i, j}')
						return 1
					if right == -4: 
						print(f'right from {i, j}')
						return -1
				if j-3 >= 0:
					left = 0
					for n in range(4):
						left += board[i][j-n]
					if left == 4:
						print(f'left from {i, j}')
						return 1
					if left == -4:
						print(f'left from {i, j}')
						return -1
				if i-3 >= 0:
					up = 0
					for n in range(4):
						up += board[i-n][j]
					if up == 4:
						print(f'up from {i, j}')
						return 1
					if up == -4:
						print(f'up from {i, j}')
						return -1

				if i+3 <= 5:
					down = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
					if down == 4:
						print(f'down from {i, j}')
						return 1
					if down == -4:
						print(f'down from {i, j}')
						return -1

				if (i-3 >= 0) and (j-3 >= 0):
					diag_up_left = 0
					for n in range(4):
						diag_up_left += board[i-n][j-n]
					if diag_up_left == 4:
						print(f'diag up left from {i, j}')
						return 1
					if diag_up_left == -4:
						print(f'diag up left from {i, j}')
						return -1
				if (i-3 >= 0) and (j+3 <= 6):
					diag_up_right = 0
					for n in range(4):
						diag_up_right += board[i-n][j+n]
					if diag_up_right == 4:
						print(f'diag up right from {i, j}')
						return 1
					if diag_up_right == -4:
						print(f'diag up right from {i, j}')
						return -1
				if (i+3 <=5) and (j-3 >= 0):
					diag_down_left = 0
					for n in range(4):
						diag_down_left += board[i+n][j-n]
					if diag_down_left == 4:
						print(f'diag down left from {i, j}')
						return 1
					if diag_down_left == -4:
						print(f'diag down left from {i, j}')
						return -1
				if (i+3 <= 5) and (j+3 <= 6):
					diag_down_right = 0
					for n in range(4):
						diag_down_right += board[i+n][j+n]
					if diag_down_right == 4:
						print(f'diag down right from {i, j}')
						return 1
					if diag_down_right == -4:
						print(f'diag down right from {i, j}')
						return -1
	return 0
turn = 1
n_moves = {i: 0 for i in range(7)}
'''while True:
	os.system('clear')
	print(available_moves())
	print(n_moves)
	print_board()

	if turn:
		choice = int(input(f"{symbol1}'s choice: "))
		if choice not in range(7):
			print('pick a choice within range')
			continue
	else:
		choice = int(input(f"{symbol2}'s choice: "))
		if choice not in range(7):
			print('pick a choice within range')
			continue
	n_moves[choice] += 1
	if turn:
		move(choice, player1)
	else:
		move(choice, player2)
	turn = int(not(turn))
	result = check(board)
	if result == 1:
		os.system('clear')
		print_board()
		print(f'{symbol1} wins')
		break
	elif result == -1:
		os.system('clear')
		print_board()
		print(f'{symbol2} wins')
		break'''

print_board()

	
