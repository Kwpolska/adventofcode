#!/usr/bin/env python3
def calc_checksum(data):
    csum = ""
    pairs = list(zip(data[::2], data[1::2]))
    for a, b in pairs:
        if a == b:
            csum += '1'
        else:
            csum += '0'
    return csum

def solve(data, length):
    while len(data) < length:
        b = ''.join(reversed(data))
        b = b.replace('1', 'I').replace('0', '1').replace('I', '0')
        data += '0' + b
    data = data[:length]
    checksum = calc_checksum(data)
    while len(checksum) % 2 == 0:
        checksum = calc_checksum(checksum)
    return checksum


test_data = "10000" # 111100001010
test_expected = "01100"
# test_expected = "1111000010100101011110000"
test_output = solve(test_data, 20)
print(test_output, test_expected)
assert test_output == test_expected
# print(solve("10111011111001111", 272))
# Part 2:
print(solve("10111011111001111", 35651584))
