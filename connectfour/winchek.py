import numpy as np
def check(board):
	for i in range(6):
		for j in range(7):
			if board[i, j] == 1:
				if j+3 <= 6:
					right = 0
					for n in range(4):
						right += board[i, j+n]
					if right == 4: 
						print(f'right from {i, j}')
				if j-3 >= 0:
					left = 0
					for n in range(4):
						left += board[i, j-n]
					if left == 4:
						print(f'left from {i, j}')
				if i-3 >= 0:
					up = 0
					for n in range(4):
						up += board[i-n, j]
					if up == 4:
						print(f'up from {i, j}')
				if i+3 <= 5:
					down = board[i, j] + board[i+1, j] + board[i+2, j] + board[i+3, j]
					if down == 4:
						print(f'down from {i, j}')
				if (i-3 >= 0) and (j-3 >= 0):
					diag_up_left = 0
					for n in range(4):
						diag_up_left += board[i-n, j-n]
					if diag_up_left == 4:
						print(f'diag up left from {i, j}')
				if (i-3 >= 0) and (j+3 <= 6):
					diag_up_right = 0
					for n in range(4):
						diag_up_right += board[i-n, j+n]
					if diag_up_right == 4:
						print(f'diag up right from {i, j}')
				if (i+3 <=5) and (j-3 >= 0):
					diag_down_left = 0
					for n in range(4):
						diag_down_left += board[i+n, j-n]
					if diag_down_left == 4:
						print(f'diag down left from {i, j}')
				if (i+3 <= 5) and (j+3 <= 6):
					diag_down_right = 0
					for n in range(4):
						diag_down_right += board[i+n, j+n]
					if diag_down_right == 4:
						print(f'diag down right from {i, j}')
				


board = np.zeros((6, 7))
pattern = np.ones((1,4))
board[0, 0] = 1
board[1,1] = 1
board[2,2] = 1
board[0, 3:] = 1
board[1,3] = 1
board[2, 3] = 1
board[3, 1] = 1
board[3, 2] = 1
board[3, 3] = 1
board[3, 4] = 1

board[4, 4] = 1


print(board)
check(board)
