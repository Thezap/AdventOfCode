with open('input') as f:
    lines = [line.rstrip().split(' ') for line in f]
    print(lines)
    stop = False
    pc = 0
    acc = 0
    while not stop:
        if lines[pc][0] == 'YO':
            break
        if lines[pc][0] == 'acc':
            lines[pc][0] = 'YO'
            acc += int(lines[pc][1])
            pc += 1
        elif lines[pc][0] == 'nop':
            lines[pc][0] = 'YO'
            pc += 1
        elif lines[pc][0] == 'jmp':
            lines[pc][0] = 'YO'
            pc += int(lines[pc][1])
    print(acc)
