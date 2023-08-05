

########################################################################
class Write:
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, buffer, font):
        """Constructor"""

        self.buffer = buffer
        self.font = font

    # ----------------------------------------------------------------------
    def text(self, string, x0=0, y0=0, color=0xffff, bgcolor=0, colors=None):
        """"""

        buffer = self.buffer
        font = self.font

        font, _w, _h = font._FONT, font._W, font._H
        _SALT = 1

        if colors is None:
            colors = (color, color, bgcolor, bgcolor)
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
                unsalted = byte ^ _SALT
                for col in range(x, x + _w):
                    color = colors[unsalted & 0x03]
                    if color is not None:
                        buffer.pixel(col, row, color)
                    unsalted >>= 2
                row += 1
            x += _w
