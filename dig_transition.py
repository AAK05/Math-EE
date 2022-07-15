#Function to count the number of pattern occurrences in a sequence
def transition(data,depth=2):
    graph = {}
    for i in range(len(data)-(depth-1)):
        pattern = ""
        for n in range(depth):
            pattern += str(data[i+n]) + ":"
        pattern = pattern[:-1]
        graph[pattern] = graph.get(pattern,0) + 1
    return graph
    permutations = len(graph)
    modal = max(graph,key=graph.get)
    mode = graph[modal]
    total = len(data)
    expected = total/permutations
    error = ((mode-expected)/expected)*100
    #print(modal,mode,total,expected)
    return (modal, error)

def max_pattern(data,depth=2):
    graph = transition(data,depth)
    permutations = len(graph)
    modal = max(graph,key=graph.get)
    mode = graph[modal]
    total = len(data)
    expected = total/permutations
    error = ((mode-expected)/expected)*100
    print(modal,mode,total,expected)
    return (modal, error)

def min_pattern(data,depth=2):
    graph = transition(data,depth)
    permutations = len(graph)
    antimodal = min(graph,key=graph.get)
    mode = graph[antimodal]
    total = len(data)
    expected = total/permutations
    error = ((mode-expected)/expected)*100
    #print(modal,mode,total,expected)
    return (antimodal, error)