"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result
in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""


def rgb_to_hex(r, g, b):
    # Ensure values are within the valid range [0, 255]
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))

    # Convert decimal values to hexadecimal and format the result
    return '{:02X}{:02X}{:02X}'.format(r, g, b)


print(rgb_to_hex(255, 255, 255))
print(rgb_to_hex(255, 255, 300))
print(rgb_to_hex(0, 0, 0))
print(rgb_to_hex(-20, 275, 125))