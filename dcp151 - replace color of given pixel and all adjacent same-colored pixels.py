"""
dcp#151

Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B

Becomes

B B G
G G G
G G G
B B B
"""


# assume image is rectangular list of lists
def replace_pixel_color(image, loc, color):
    x, y = loc
    old_color = image[x][y]
    image[x][y] = color

    min_x = max(x - 1, 0)
    max_x = min(x + 1, len(image[0]))

    min_y = max(y - 1, 0)
    max_y = min(y + 1, len(image))

    for row in range(min_x, max_x + 1):
        for col in range(min_y, max_y + 1):
            if image[row][col] == old_color:
                image[row][col] = color


image = [
    ['B', 'B', 'W'], 
    ['W', 'W', 'W'], 
    ['W', 'W', 'W'], 
    ['B', 'B', 'B']]

loc = (1, 1) # change to 0-based instead of 1-based of problem statement
color = 'G'

print("loc = {}".format(loc))
print("color = {}".format(color))

print("\nold image:")
print('\n'.join([''.join([str(cell) for cell in row]) for row in image]))

replace_pixel_color(image, loc, color)

print("\nnew image:")
print('\n'.join([''.join([str(cell) for cell in row]) for row in image]))

