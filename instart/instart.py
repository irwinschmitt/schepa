import cv2
import numpy as np
import re

def hex_to_rgb(value):
    value = value.lstrip("#")
    lv = len(value)
    return tuple( int( value[i:i + lv // 3], 16)
    for i in range(0, lv, lv // 3))
    

# hex_color = "#f4a460"

hex_colors = [
    ["#33325c", "#42458a", "#555abe", "#88bbfd", "#9cdaff", "#c5f0ff"],
    ["#07427a", "#135a98", "#2179b8", "#68d4f8", "#8feffb", "#b7fdfd"],
    ["#025450", "#097261", "#159670", "#73e4a2", "#b0f1b7", "#d5facf"],
    ["#9d341e", "#b6572b", "#cd7c3a", "#fcd669", "#fbe882", "#fcf4b3"],
    ["#7c0e3d", "#9e2246", "#c13d4b", "#ffa17b", "#ffcca5", "#ffe7cb"],
    ["#4b2477", "#6c3791", "#9251ad", "#f6a4ec", "#ffc7ee", "#ffe0f5"],
    ["#3e2c6a", "#573e8f", "#7456b6", "#bdb0f5", "#cdd1f7", "#e1e8fa"]
]

rgb_colors = numpy.empty((len(hex_colors), len(hex_colors[0])))

# rgb_tuple = reversed(hex_to_rgb(hex_color))

for i, hex_colors in enumerate(hex_colors):
    for j, hex_color in enumerate(hex_colors):
        rgb_colors[i][j] = reversed(hex_to_rgb(hex_color))
        # print(reversed(hex_to_rgb(hex_color)))




background_image = np.full((1000, 1000, 3), tuple(rgb_tuple), np.uint8)
cv2.imShow("background_image", background_image)
cv2.waitKey(0)
cv2.destroyAllWindows()