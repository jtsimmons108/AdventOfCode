import re

class Ingredient(object):
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.vals = [capacity, durability, flavor, texture, calories]
        
ingredients = open('AC_15_Start.txt').read().strip().split('\n')
ing_list = []
for ingr in ingredients:
    info = re.split(' |,', ingr)
    ing_list.append(Ingredient(info[0][:-1],int(info[2]), int(info[5]), int(info[8]), int(info[11]), int(info[14])))
print ing_list

all_totals = []
for amt1 in range(101):
    for amt2 in range(101):
        for amt3 in range(101):
                totals = 1
                for i in range(4):
                    totals *= max(amt1 * ing_list[0].vals[i] + amt2 * ing_list[1].vals[i] + amt3 * ing_list[2].vals[i] + (100-amt1-amt2-amt3)*ing_list[3].vals[i], 0)
                if amt1 * ing_list[0].vals[-1] + amt2 * ing_list[1].vals[-1] + amt3 * ing_list[2].vals[-1] + (100-amt1-amt2-amt3)*ing_list[3].vals[-1] == 500:
                    all_totals += [totals]
    
print max(all_totals)