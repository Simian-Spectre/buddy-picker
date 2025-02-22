import random

players = ["Aiden",
           "Bimi",
           "Bryce",
           "Lund",
           "Andrew",
           "Cupid",
           "Dustin",
           "Dane",
           "Daniel",
           "Elijah",
           "George",
           "Grant",
           "Grayson",
           "Henri",
        #    "Hilding",
           "Ian",
           "Isaiah",
           "Jackson",
           "Jake",
           "Joey",
           "Malcolm",
           "Max",
           "Reavy",
           "Oscar",
           "Rainor",
        #    "Duke",
           "Fridge",
           "Sawyer"]

def read_excluded_pairs(file_path):
    excluded_pairs = set()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            pair = line.split(':')

            # Add both directions to the set (name1:name2 and name2:name1)
            excluded_pairs.add((pair[0], pair[1]))
            excluded_pairs.add((pair[1], pair[0]))

            # Check for a throuple
            if(len(pair) == 3):
                excluded_pairs.add((pair[1], pair[2]))
                excluded_pairs.add((pair[2], pair[1]))
                excluded_pairs.add((pair[0], pair[2]))
                excluded_pairs.add((pair[2], pair[0]))

    return excluded_pairs

def generate_buddies(names, excluded_pairs):
    buddies = []

    # Shuffle names and create a list to edit
    random.shuffle(names)
    remaining_names = names

    # boolean for odd number of names
    needsThrouple = len(names) % 2 == 1

    if needsThrouple:
        for i in range(0, len(remaining_names)-3, 2):
            # Deal with throuple first
            if(i==0):
                pair1 = (remaining_names[0], remaining_names[1])
                pair2 = (remaining_names[1], remaining_names[2])
                pair3 = (remaining_names[2], remaining_names[0])
                throuple = (remaining_names[0], remaining_names[1], remaining_names[2])
                while pair1 in excluded_pairs or pair2 in excluded_pairs or pair3 in excluded_pairs:
                    random.shuffle(remaining_names)
                    throuple = (remaining_names[0], remaining_names[1], remaining_names[2])
                remaining_names = remaining_names[3:]
                buddies.append(throuple)

            # Deal with pairs
            pair = (remaining_names[0], remaining_names[1])

            # Check if this pair is in the excluded list
            while pair in excluded_pairs:
                # Check to see if it is 
                if(len(remaining_names)==2):
                    print("SHIT'S FUCKED, RERUN ME")
                    break #maybe recall methodf???
                random.shuffle(remaining_names)
                pair = (remaining_names[0], remaining_names[1])
            remaining_names = remaining_names[2:]
            buddies.append(pair)
    else:
        for i in range(0, len(remaining_names), 2):
            pair = (remaining_names[0], remaining_names[1])

            # Check if this pair is in the excluded list
            while pair in excluded_pairs:
                # Check to see if it is 
                if(len(remaining_names)==2):
                    print("SHIT'S FUCKED, RERUN ME")
                    break #maybe recall method?
                random.shuffle(remaining_names)
                pair = (remaining_names[0], remaining_names[1])

            remaining_names = remaining_names[2:]
            buddies.append(pair)
    
    return buddies

def print_list_of_tuples(list):
    for tuple in list:
        group = ''
        for i in range(len(tuple)-1):
            group += tuple[i] + ':'
        group += tuple[-1]
        print(group)


# Create list of aready exhausted buddies
exhausted = read_excluded_pairs('exhausted.txt')
buddies = generate_buddies(players, exhausted)

print_list_of_tuples(buddies)