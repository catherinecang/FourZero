def solve(init_pos, primitive, generate_moves, do_move):
	if primitive(init_pos) == "Loss":
		return False
	a = 0
<<<<<<< HEAD
	for i in generate_moves(init_pos):
		b =solve(do_move(init_pos, i), primitive, generate_moves, do_move) 
		a = a or not b
	return a
=======
	count = 0 
	for i in generate_moves(init_pos):
		b = solve(do_move(init_pos, i), primitive, generate_moves, do_move) 
		a = a or not b
		count += 1
	if a:
		return "Win", count
	else:
		return "Loss", count
>>>>>>> 2

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
<<<<<<< HEAD
	if solve(4, primitive, generate_moves, do_move):
		print("Win!")
	else:
		print("Loss")
=======
	print ("The amount of moves left equals how many moves per person (as in each time someone takes sticks that counts as a move).")
	print(solve(4, primitive, generate_moves, do_move))

>>>>>>> 2

if __name__ == '__main__':
	main()