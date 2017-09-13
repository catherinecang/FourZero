def solve(init_pos, primitive, generate_moves, do_move):
	generate_moves = {1, 2}
	if init_pos % 3 == 0:
		return "Loss"
	else:
		return "Win"

def main(3, 5, 2, 1):
	solve()
if __name__ == '__main__':
	main()