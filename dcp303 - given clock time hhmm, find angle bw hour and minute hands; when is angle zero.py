"""
dcp#303

This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?

"""

"""
Let angles be clockwise with respect to 12 o'clock.
Angle measure of minute hand is (m/60) * 360 degrees.
Angle measure of hour hand is ((h + m/60) / 12) * 360 degrees.
Subtracting gives 11*m/2 - 30 * h.

Return signed angle from hour to minute hand.

Angle is 0 when m = 60*h/11.  This happens 22 times in a day
(24-hour period).

h, m
0, 0
1, 5 + 5/11 = 5.4545...
2, 10 + 10/11
3, 16 + 4/11
4, 21 + 9/11
5, 27 + 3/11
6, 32 + 8/11
7, 38 + 2/11
8, 43 + 7/11
9, 49 + 1/11
10, 54 + 6/11
12, 0
13, 5+ 5/11
etc.
"""

# Assume time_str has format "hh:mm" where 00 <= hh <= 23
# and 00 <= mm <= 59.
def time_angle(time_str):
    h = int(time_str[:2])
    m = int(time_str[3:])

    if h >= 12:
        h -= 12

    # h_ang = (h + m/60)/12 * 360
    # m_ang = m/60 * 360

    return 11*m/2 - 30*h


time_str = "12:33"

time_angle = time_angle(time_str)

print("\ntime = {}".format(time_str))
print("\nsigned angle from hour to minute hand (degrees) = {}".format(time_angle))

