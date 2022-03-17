class Node:
	def __init__(self, key, hv):  # Node.__init__(root)
		self.data = [key, hv]
		self.left = None
		self.right = None

def bubbleSort(array):

	for i in range(len(array)):
		for j in range(0, len(array) - i - 1):
			if array[j].data[1] > array[j + 1].data[1]:
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp

def printLevelOrder(root, key):
	if root is None:
		return

	queue = []
	visited = []
	element = []

	queue.append(root)

	while(len(queue) > 0):

		node = queue.pop(0)
		if node.data[0] == key:
			print("goal node found")
			visited.append(node.data)
			print(visited)
			return
		else:
			visited.append(node.data)

		if node.left is not None:
			queue.append(node.left)

		if node.right is not None:
			queue.append(node.right)

		bubbleSort(queue)

	print("Goal node not found")

	


root = Node(1,3)
root.left = Node(2,4)
root.right = Node(3,5)
root.left.left = Node(4,3)
root.left.right = Node(5,2)
root.right.left = Node(6,6)
root.right.right = Node(7,7)


goal_node = int(input("Enter your goal node "))
printLevelOrder(root, goal_node)
