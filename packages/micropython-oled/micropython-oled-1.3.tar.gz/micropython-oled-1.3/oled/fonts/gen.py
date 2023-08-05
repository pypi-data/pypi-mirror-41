import pygame
pygame.init()

FONTS = (
    # ("Small 5x3", 15),
    # ("Bit5x3", 20),
    # ("Ubuntu Mono", (15, 10)),
    # ("AnakinMono", 15),
    # ("Cutive Mono", 15),
    ("Ubuntu Mono", 15),
    ("Press Start 2P", 15),
)


SAMPLE_TEXT = "micropython-oled by @yeisoneng"
CHARACTERS = ''.join(chr(i) for i in range(32, 127))


COLORS = {
    (0, 0, 0, 0xff): 0,
    # (0x7f, 0x7f, 0x7f, 0xff): 1,
    (0x66, 0x66, 0x66, 0xff): 1,
    (0x99, 0x99, 0x99, 0xff): 2,
    (0xff, 0xff, 0xff, 0xff): 3,
}


COLORS_ = [tuple(k) for k in COLORS]


########################################################################
class Buffer(object):
    """"""
    # ----------------------------------------------------------------------

    def __init__(self, w, h):
        """"""
        self.surface = pygame.Surface((w, h))
        self.surface.fill((0, 0, 0))

    # ----------------------------------------------------------------------
    def pixel(self, x, y, color):
        """"""
        self.surface.set_at((x, y), color)

    # ----------------------------------------------------------------------
    def save(self, filename):
        """"""
        pygame.image.save(self.surface, filename)


# ----------------------------------------------------------------------
def get_template(font, size):
    """"""
    font_ = pygame.font.SysFont(font, size)
    template = font_.render(CHARACTERS, False, (0, 0, 0), (255, 255, 255))
    # pygame.image.save(template, "filename.png")

    return template


# ----------------------------------------------------------------------
def pack(font, w, h):
    font_ = []
    for character in font:
        font_.extend((sum(COLORS[tuple(character.get_at((x, y)))] << (x * 2) for x in range(w))) for y in range(h))
    return font_


# ----------------------------------------------------------------------
def get_font(template):
    """"""
    font = []

    w_, h_ = template.get_size()
    w = w_ // len(CHARACTERS)
    h = h_

    for tile_x in range(0, template.get_size()[0] // w):
        rect = (tile_x * w, 0, w, h)
        font.append(template.subsurface(rect))

    list_font = pack(font, w, h)

    return list_font, w, h


# ----------------------------------------------------------------------
def text(buffer, string, font, x0=0, y0=0, color=(255, 255, 255), bgcolor=(0, 0, 0), _w=10, _h=6):
    """"""
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
            unsalted = byte
            for col in range(x, x + _w):
                color = colors[unsalted & 0x03]
                if color is not None:
                    buffer.pixel(col, row, color)
                unsalted >>= 2
            row += 1
        x += _w


# ----------------------------------------------------------------------
def generate_font(font, size):
    """"""

    template = get_template(font, size - 1)
    oled_font, w, h = get_font(template)

    font_name = font.lower().replace(" ", '_')

    with open(f"{font_name}_{size}.py", 'w') as file:
        file.write(f"_FONT = {oled_font}\n")
        file.write(f"_W = {w}\n")
        file.write(f"_H = {h}\n")

    return oled_font, w, h, f"{font_name}_{size}.py"


if __name__ == "__main__":

    buffer = Buffer(1000, 500)
    l = 0
    for font_ in FONTS:
        oled_font, w, h, name = generate_font(*font_)

        text(buffer, f"{name}: {SAMPLE_TEXT}", oled_font, 5, l, _w=w, _h=h)
        l += (h + 10)

    buffer.save("sample.png")


