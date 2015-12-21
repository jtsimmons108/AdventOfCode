import itertools
distances = open('AC_9_Start.txt').read().strip().split('\n')

distance_map = {}
cities = []
for line in distances:
    info = line.split()
    couple = (info[0], info[2])
    cities.extend(couple)
    distance_map.update({couple: int(info[4])})
    
cities = set(cities)
print cities
distances = []
for combo in itertools.permutations(cities):
    distance = 0
    valid_route = True
    for num in range(len(cities) - 1):
        travel = (combo[num], combo[num+1])
        travel2 = (combo[num + 1], combo[num])
        if travel in distance_map.keys():
            distance += distance_map[travel]
        elif travel2 in distance_map.keys():
            distance +=distance_map[travel2]
        else:
            valid_route = False
            
    if valid_route:
        distances += [distance]
        
print max(distances)
