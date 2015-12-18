

class Reindeer(object):
    
    def __init__(self, speed, time, rest):
        self.speed = speed
        self.time = time
        self.rest = rest
        
    def distance_travelled(self, duration):
        distance = 0
        while duration > 0:
            for i in range(self.time):
                if duration > 0:
                    duration -= 1
                    distance += self.speed
                
            duration -=  self.rest
            
        return distance

reindeer_list = open('AC_13_Start.txt').read().strip().split('\n')
reindeers = {}
for reindeer in reindeer_list:
    info = reindeer.split()
    reindeers.update({info[0]:Reindeer(int(info[3]), int(info[6]), int(info[13]))})

print sorted(reindeers.keys())
scores = [0]*9
time = 2503
for seconds in range(1,time + 1):
    curr_dist = [reindeers[reindeer].distance_travelled(seconds) for reindeer in sorted(reindeers.keys())]
    for i in range(len(curr_dist)):
        if curr_dist[i] == max(curr_dist):
            scores[i] += 1
            
print scores