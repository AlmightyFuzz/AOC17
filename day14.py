from day10 import knot_hash2

TEST = 'flqrgnkx'
PUZZLE_INPUT = 'ugkiagan'


def defragmenter(key_string):

    disk_space = [key_string + '-' + str(i) for i in range(128)]

    count = 0
    for row in disk_space:
        hash_str = knot_hash2(row)
        barray = bytes.fromhex(hash_str)

        for b in barray:
            for i in range(8):
                # reads through each bit in the byte and checks if it's a 1, and then counts it
                if (b >> i) & 1 == 1:
                    count += 1

    print(count)


if __name__ == '__main__':
    # defragmenter(TEST)
    defragmenter(PUZZLE_INPUT)
