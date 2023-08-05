

# ----------------------------------------------------------------------
def write(buffer, string, font, x0=0, y0=0, color=(255, 255, 255), bgcolor=(0, 0, 0)):
    """"""
    colors = (color, color, bgcolor, bgcolor)

    font, _w, _h = font._FONT, font._W, font._H

    x = x0
    for c in string:
        if c == '\n':
            y0 += _h
            x = x0
            continue
        index = min(95, ord(c) - 0x20)
        if index < 0:
            continue
        row = y0
        index *= _h
        for byte in font[index:index + _h]:
            unsalted = byte
            for col in range(x, x + _w):
                color = colors[unsalted & 0x03]
                if color is not None:
                    buffer.pixel(col, row, color)
                unsalted >>= 2
            row += 1
        x += _w

