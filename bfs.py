class Node:
	def __init__(self, key):  # Node.__init__(root)
		self.data = key
		self.left = None
		self.right = None


def printLevelOrder(root,key):
	if root is None:
		return

	queue = []
	visited = []

	queue.append(root)

	while(len(queue) > 0):

		node = queue.pop(0)
		if node.data == key:
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
			
	print("Goal node not found")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

        
goal_node = int(input("Enter your goal node "))
printLevelOrder(root,goal_node)
