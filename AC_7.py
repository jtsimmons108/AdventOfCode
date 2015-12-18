
circuits = {}

def update_circuits(circuit, value):
    if circuit not in circuits.keys():
        circuits.update({circuit:value})
    else:
        circuits[circuit] += value
        
    if circuits[circuit] < 0:
        circuits[circuit] += 2**16
        
def operate(line):
    sides = [val.strip() for val in line.split('->')]
    inputs = sides[0].split()
    circuit = sides[1]
    if len(inputs) == 1:
        try:
            num = int(inputs[0])
            update_circuits(circuit, num)
        except ValueError:
            try:
                num = circuits[inputs[0]]
                update_circuits(circuit, num)
            except KeyError:
                pass
    if len(inputs) == 2:
        try:
            num = circuits[inputs[1]]
            update_circuits(circuit, ~num)
        except KeyError:
            pass
    else:
        try:
            left_operand = circuits[inputs[0]]
            try:
                right_operand = circuits[inputs[2]]
            except KeyError:
                try:
                    right_operand = int(inputs[2])
                except ValueError:
                    right_operand = -1
            if right_operand != -1:
                if 'AND' in inputs:
                    update_circuits(circuit, left_operand & right_operand)
                elif 'OR' in inputs:
                    update_circuits(circuit, left_operand | right_operand)
                elif 'LSHIFT' in inputs:
                    update_circuits(circuit, left_operand << right_operand)
                elif 'RSHIFT' in inputs:
                    update_circuits(circuit, left_operand >> right_operand)
        except KeyError:
            pass

instruction_list = open('AC_7_Start.txt').read().strip().split('\n')

for instruction in instruction_list:
    operate(instruction)

print circuits

