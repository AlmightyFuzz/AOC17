import json
from day10 import knot_hash2

TEST = 'flqrgnkx'
PUZZLE_INPUT = 'ugkiagan'


def save_disk_data(key_string):
    '''Computes the disk data and saves the resulting bits and bytes to file'''

    if key_string == 'TEST':
        disk_data = [TEST + '-' + str(i) for i in range(128)]
    if key_string == 'PUZZLE_INPUT':
        disk_data = [PUZZLE_INPUT + '-' + str(i) for i in range(128)]

    disk = [[0 for x in range(128)] for y in range(128)]

    # Counts the number of used bits (bit == 1)
    count = 0
    for row_num, row in enumerate(disk_data):
        hash_str = knot_hash2(row)
        barray = bytes.fromhex(hash_str)

        bit_num = 0
        for b in barray:
            for i in range(8):
                # reads through each bit in the byte and checks if it's a 1, and then counts it
                if (b >> i) & 1 == 0:
                    count += 1
                    disk[row_num][bit_num] = 1

                bit_num += 1

    with open('day14data\\' + key_string + '.txt', 'w') as f:
        # uses the json module to serialize the data
        json.dump(disk, f)

    print(count)


def find_regions(disk_data):
    '''Applies the flood fill algorithm to the disk data to find the number of unique regions'''


def flood_fill(coords, disk):
    if disk[coords[0]][coords[1]] == 0:
        return

    # check 4 surrounding coords


def load_disk_data(run_str):
    return json.load(open('day14data\\' + run_str + '.txt', 'r'))


if __name__ == '__main__':
    run = 'TEST'
    # run = 'PUZZLE_INPUT'

    # save_disk_data(run)

    find_regions(load_disk_data(run))
