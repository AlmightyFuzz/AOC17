TEST = '''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2'''


def duet(instructions):
    # Reg name = int value
    registers = {x: 0 for x in 'abcdefghijklmnopqrstuvwxyz'}
    sound = 0
    recovered_freq = 0

    idx = 0

    while idx < len(instructions):

        instr = instructions[idx][:3]
        reg = instructions[idx][4]
        val_str = instructions[idx][6:]

        if val_str is not '':
            try:
                val = int(val_str)
            except ValueError:
                val = registers[val_str]

        if instr == 'snd':
            sound = registers[reg]

        elif instr == 'set':
            registers[reg] = val

        elif instr == 'add':
            registers[reg] += val

        elif instr == 'mul':
            registers[reg] *= val

        elif instr == 'mod':
            registers[reg] %= val

        elif instr == 'rcv':
            if registers[reg] != 0:
                recovered_freq = sound
                break

        if instr == 'jgz':
            if registers[reg] > 0:
                idx += val
                # What about infint loops?
            else:
                # register <= 0
                idx += 1
        else:
            idx += 1

    print('Recovered sound: ', recovered_freq)


def load_puzzle():
    return [x.strip('\n') for x in open('day18input.txt', 'r').readlines()]


if __name__ == '__main__':
    # duet(TEST.split('\n'))
    duet(load_puzzle())
