'''
Reference for the Welsh-Powell coloring algorithm:
https://www.geeksforgeeks.org/welsh-powell-graph-colouring-algorithm/
'''

graph = [
    [0, 90, 85, 90, 105, 110],
    [90, 0, 77, 111, 83, 64],
    [85, 77, 0, 120, 98, 125],
    [90, 111, 120, 0, 50, 63],
    [105, 83, 98, 50, 0, 150],
    [110, 64, 125, 63, 150, 0]
]

radius = 100

def make_unweighted(graph, radius):
    n = len(graph)
    unweighted_graph = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= radius and i != j:
                unweighted_graph[i][j] = 1
            else:
                unweighted_graph[i][j] = 0

    return unweighted_graph


def is_connected(graph, vertex_one, vertex_two):
    return graph[vertex_one][vertex_two]

# Function to color a graph using the Welsh-Powell algorithm
def color_welsh(graph):
    list_of_vertex = []

    # Find the degree of a vertex
    n = len(graph)
    for i in range(n):
        temp_deg = 0
        for j in range(n):
            temp_deg += graph[i][j]
        list_of_vertex.append([i, temp_deg, 0])

    # Sort the vertices based on their degree in decreasing order
    list_of_vertex.sort(key=lambda x: x[1], reverse=True)
    
    last_color = 1
    i = 0
    while i < n:
        current_vertex = list_of_vertex[i][0]
        list_of_vertex[i][2] = last_color
        for j in range(i+1,n):
            current_vertex_two = list_of_vertex[j]
            if (not is_connected(graph,current_vertex,current_vertex_two[0])) and current_vertex_two[2] == 0:
                list_of_vertex[j][2] = last_color
        
        k = i
        while k < n and list_of_vertex[k][2] != 0:
            k += 1

        i = k
        last_color += 1

    list_of_vertex.sort(key=lambda x:x[0])
    return list_of_vertex

def calculate_frequency(color):
    base_frequency = 85
    frequency_increment = 0.4
    return base_frequency + color*frequency_increment

def print_assigned_towers(colored_vertex_list):
    for x in colored_vertex_list:
        print(f"Tower {x[0] + 1}:\t{calculate_frequency(x[2])} Hz")

def main():
    unweighted_graph = make_unweighted(graph, radius)
    colored_vertex_list = color_welsh(unweighted_graph)
    print()
    print("--------------RADIO FREQUENCY ASSIGNMENT--------------")
    print()
    print("The assigned frequency for each tower is:")
    print_assigned_towers(colored_vertex_list)
    print()

if __name__ == "__main__":
    main()