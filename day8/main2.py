import copy

with open('input2') as f:
    lines_raw = [line.rstrip().split(' ') + [False] for line in f]
    lines = copy.deepcopy(lines_raw)
    print(lines)
    stop = False
    pc = 0
    acc = 0

    modif_instruction_line = 0
    while not stop:
        if pc == len(lines) - 1:
            print('WIN')
            print(lines)
            print(pc)
            break
        if lines[pc][2] == True:
            lines = copy.deepcopy(lines_raw)
            while lines[modif_instruction_line][0] == 'acc':
                modif_instruction_line += 1
            if lines[modif_instruction_line][0] == 'jmp':
                lines[modif_instruction_line][0] = 'nop'
            else:
                lines[modif_instruction_line][0] = 'jmp'
            modif_instruction_line += 1
            pc = 0
            acc = 0
            print('New Try ', modif_instruction_line)
        if lines[pc][0] == 'acc':
            lines[pc][2] = True
            acc += int(lines[pc][1])
            pc += 1
        elif lines[pc][0] == 'nop':
            lines[pc][2] = True
            pc += 1
        elif lines[pc][0] == 'jmp':
            lines[pc][2] = True
            pc += int(lines[pc][1])
    print(lines)
    print(acc)
