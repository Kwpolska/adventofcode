#!/usr/bin/env python3
with open("input/10.txt") as fh:
    file_data = fh.read().strip()


def solve_sparse(data, size=256):
    # The instructions are kinda unclear about this.
    lengths = [ord(i) for i in data]
    lengths += [17, 31, 73, 47, 23]

    L = list(range(0, size))
    current = 0
    skip = 0

    for _round in range(64):
        for length in lengths:
            # print("start", length, L, L[current])
            # Select as many as possible.
            right = L[current:current+length]
            right_l = len(right)
            # And the overflow.  The maximum length is <= size
            overflow, overflow_l = [], 0
            if right_l < length:
                overflow = L[0:length - right_l]
                overflow_l = len(overflow)
            assert overflow_l + right_l == length

            sum = right + overflow
            sum.reverse()

            # Insert back into the list.
            new_right = sum[0:right_l]
            new_overflow = sum[right_l:]
            assert len(new_right) == right_l and len(new_overflow) == overflow_l
            L[current:current+length] = new_right
            L[0:length - right_l] = new_overflow

            # Push indexes forward.
            current = (current + length + skip) % size
            skip += 1
            # print("end  ", length, L)

    sparse = []
    # print(L)
    for i in range(16):
        _l = (i * 16)
        segment = L[(_l if _l > 0 else 0):((i + 1) * 16)]
        # print(i, segment, len(segment))
        assert len(segment) == 16
        result = segment[0]
        for digit in segment[1:]:
            result ^= digit
        sparse.append(result)
    return sparse

def solve(data, size=256):
    sparse = solve_sparse(data, size)
    return ''.join(f"{c:02x}" for c in sparse)

def solve_bin(data, size=256):
    sparse = solve_sparse(data, size)
    return ''.join(f"{c:08b}" for c in sparse)


if __name__ == '__main__':
    test_data = ""
    test_output = solve(test_data)
    test_expected = "a2582a3a0e66e6e86e3812dcb672a272"
    print(test_output, test_expected)
    assert test_output == test_expected
    print(solve(file_data))
