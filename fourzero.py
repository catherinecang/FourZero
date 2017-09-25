def solve(init_pos, primitive, generate_moves, do_move):
	def tree(root, branches = []):
		return [root, branches]
	def root(t):
		return t[0]
	def branches(t):
		return t[1]
	def isleaf(t):
		return not branches(t)
	def shortestdistance(t):
		if isleaf(t):
			return 0
		else:
			return min([shortestdistance(b) for b in branches(t)]) + 1
	def createtree(n):
		if n < 0:
			return tree(False)
		elif primitive(n) == "Loss":
			return tree(False)
		else:
			branches = [createtree(n-1), createtree(n-2)]
			rt = True
			for b in branches:
				rt = rt and root(b)
			rt = not rt
			return tree(rt, branches)
	soln =  createtree(init_pos)
	return root(soln), shortestdistance(soln)
	


def generate_moves(pos):
	assert pos > 0
	if pos < 2:
		return [1]
	else:
		return [2,1]

def do_move(pos, action):
	return pos - action

def primitive(pos):
	if pos == 0:
		return "Loss"
	else:
		return "Undecided"

def main():
	n = 4
	if solve(4, primitive, generate_moves, do_move)[0]:
		ans = "Win"
	else:
		ans = "Loss"
	print ("The amount of moves left equals how many moves per person (as in each time someone takes sticks that counts as a move).")
	print(ans, solve(4, primitive, generate_moves, do_move)[1])


if __name__ == '__main__':
	main()