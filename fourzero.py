def solve(init_pos, primitive, generate_moves, do_move):
	if primitive(init_pos) == "Loss":
		return False
	a = 0
	for i in generate_moves(init_pos):
		b =solve(do_move(init_pos, i), primitive, generate_moves, do_move) 
		a = a or not b
	return a

def generate_moves(pos):
	assert pos > 0
	if pos < 2:
		return [1]
	else:
		return [1,2]

def do_move(pos, action):
	return pos - action

def primitive(pos):
	if pos == 0:
		return "Loss"
	else:
		return "Undecided"

def main():
	if solve(4, primitive, generate_moves, do_move):
		print("Win!")
	else:
		print("Loss")

if __name__ == '__main__':
	main()