"""
dcp#213

This problem was asked by Snapchat.

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
"""

# Clarify that "00" and "000" are not allowed.

# There must be between 4 and 12 digits in a valid IP address. (7-15 chars in string)
# There are 3 to 11 spots (in between digits) to place a period.
# Without further constraints, there are sum( nC3 : n=3..11) = 495 ways to place 3 periods.
# There are significantly fewer ways when considering constraints.


import random

# Assume given "ip" has only digits and "."
def is_valid_ip(ip):
    if (len(ip) < 7) or (len(ip) > 15):
        return False

    parts = ip.split(".")
    print("parts = {}".format(parts))

    for part in parts:
        if int(part) > 255:
            return False

        if (part[0] == '0') and (len(part) > 1):
            return False

    return True


def test_is_valid_ip():
    print("Testing for valid ips:")
    ips = [
        "254.254.0.123", # True
        "254.254.01.23", # False
        "254.254.012.3", # False
        "254.254.00.23", # False
        "0.0.0.0", # True
        "255.255.255.255", # True
    ]

    for ip in ips:
        valid = is_valid_ip(ip)
        print("{}\t{}".format(ip, valid))


def get_ips(s):
    if (len(s) < 4) or (len(s) > 12):
        return []

    ips = []

    # p1, p2, p3 are positions in string "s" to place "."s
    for p1 in range(1,4):
        for p2 in range(p1 + 1, p1 + 4):
            for p3 in range(p2 + 1, p2 + 4):
                ip = s[:p1] + "." + s[p1:p2] + "." + s[p2:p3] + "." + s[p3:]
                if is_valid_ip(ip):
                    ips.append(ip)

    return ips


s = "0000" # 1 IP address
s = "00000" # no valid IP addresses
s = "000" # no valid IP addresses; too short
s = "2552552552552" # no valid IP addresses; too long
s = "255255255255" # 1 IP address
s = "2542540123" # given in problem statement

print("\nstring of digits = {}\n".format(s))

ips = get_ips(s)
print("\nall possible IP address combinations = {}".format(ips))

#test_is_valid_ip()

