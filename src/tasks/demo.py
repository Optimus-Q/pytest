from collections import namedtuple





Color = namedtuple('Color', ['red', 'green', 'blue'])

color_val = Color(55, 155, 255)

print(f"Red: {color_val.red}")
print(f"Green: {color_val.green}")
print(f"Blue: {color_val.blue}")
