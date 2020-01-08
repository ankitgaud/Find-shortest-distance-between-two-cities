from collections import defaultdict

class Graph():
	def __init__(self):
		self.edges = defaultdict(list)
		self.weights = {}

	def add_edge(self, from_node, to_node, weight):
		self.edges[from_node].append(to_node)
		self.edges[to_node].append(from_node)
		self.weights[(from_node, to_node)] = weight
		self.weights[(to_node, from_node)] = weight




def dijsktra(graph, initial, end):
	shortest_paths = {initial: (None, 0)}
	current_node = initial
	visited = set()

	while current_node != end:
		visited.add(current_node)
		destinations = graph.edges[current_node]
		weight_to_current_node = shortest_paths[current_node][1]

		for next_node in destinations:
			weight = graph.weights[(current_node, next_node)] + weight_to_current_node
			#print(weight)
			if next_node not in shortest_paths:
				shortest_paths[next_node] = (current_node, weight)

			else:
				current_shortest_weight = shortest_paths[next_node][1]
				if current_shortest_weight > weight:
					shortest_paths[next_node] = (current_node, weight)




		next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}

		if not next_destinations:
			return "Route Not Possible"

		current_node = min(next_destinations, key=lambda k: next_destinations[k][1])


	path = []
	distance_sort = []
	while current_node is not None:
		path.append(current_node)
		next_node = shortest_paths[current_node][0]
		distance_sort.append(shortest_paths[current_node][1])
		current_node = next_node

	# Reverse path
	path = path[::-1]
	return path, distance_sort[0]

graph = Graph()


data_txt = open("input.txt", "r")

edges = []
for data in data_txt:
	try:
		data = data.split()
		edges.append((data[0].lower(), data[2].lower(), int(data[4])))
	except:
		print()

for edge in edges:
	graph.add_edge(*edge)

input1 = input("Start point: ")
input2 = input("Desinations point: ")
output, output1 = dijsktra(graph, input1.lower(), input2.lower())


for i in output:
	print(i, end=" --> ")
print(output1)
#print(output[0]," --> ", output[1], " --> ", output[2], "-->", output1)