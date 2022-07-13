#Function to count the number of pattern occurrences in a sequence
def transition(data,depth=2):
    transitions = {}
    for i in range(len(data)-(depth-1)):
        pattern = ""
        for n in range(depth):
            pattern += str(data[i+n])
        transitions[pattern] = transitions.get(pattern,0) + 1
    permutations = len(transitions)
    modal = max(transitions,key=transitions.get)
    mode = transitions[modal]
    total = len(data)
    expected = total/permutations
    error = ((mode-expected)/expected)*100
    #print(modal,mode,total,expected)
    return error