PUZZLE_LIST = [x for x in range(256)]  # [0 -> 255]
PUZZLE_LENGTHS = [120, 93, 0, 90, 5, 80, 129,
                  74, 1, 165, 204, 255, 254, 2, 50, 113]
TEST_LENGTHS = [3, 4, 1, 5]
TEST_LIST = [x for x in range(5)]  # [0 -> 4]


def knot_hash(run=None):

    if run == 'test':
        circle = TEST_LIST
        lengths = TEST_LENGTHS
    else:
        circle = PUZZLE_LIST
        lengths = PUZZLE_LENGTHS

    curr_pos = 0
    skip_size = 0

    circle_len = len(circle)

    for length in lengths:

        # -Get twisted list-
        if (curr_pos + length) >= circle_len:
            # if we're going to go past the end of the list then manually pull out the relevant
            # values, jump to the start and then carry on

            twist_list = []
            for i in range(length):
                pos = curr_pos + i

                if pos >= circle_len:
                    pos = pos - circle_len

                twist_list.append(circle[pos])
        else:
            # otherwise just slice the list
            twist_list = circle[curr_pos:curr_pos + length]

        twist_list.reverse()

        # -Update circle list with new twisted values-
        for i, num in enumerate(twist_list):
            pos = curr_pos + i

            if pos >= circle_len:
                pos = pos - circle_len

            circle[pos] = num

        # -Update position in circle-
        curr_pos += (length + skip_size)
        if curr_pos >= circle_len:
            curr_pos = curr_pos - circle_len

        skip_size += 1

    print('Hash is: ', circle[0] * circle[1])


if __name__ == '__main__':
    # knot_hash('test')
    knot_hash()
