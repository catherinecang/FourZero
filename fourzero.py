def solve(init_pos, primitive, generate_moves, do_move):
	generate_moves = {1, 2}
	if init_pos % 3 == 0:
		return "Loss"
	else:
		return "Win"

def generate_moves(pos):
	assert pos > = 1
	if pos < 2:
		return [1]
	else:
		return [1,2]

def do_move(pos, action):
	return pos - action

def primitive(pos):
	if pos == 0:
		return "LOSS"
	elif pos == 1 or pos == 2:
		return "WIN"

def main(3, 5, 2, 1):
	solve(4, primitive, generate_moves(), do_move)
if __name__ == '__main__':
	main()