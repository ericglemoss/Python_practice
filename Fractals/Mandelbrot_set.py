from PIL import Image, ImageDraw

# Max iteration of the sequence process. Longer iterations may take too long
MAX_ITER = 80


def gen_mandelbrot(c):
    """
    :param c: complex number that will be added af each iteration of the sequence
    :return: max iteration achieved during the process
    """
    z_n = 0
    k = 0
    while abs(z_n) <= 2 and k < MAX_ITER:
        # The figure format will change according to the power of z_n
        z_n = z_n**6 + c
        k += 1
    return k


# Size of the image that will be generated
WIDTH = 800
HEIGHT = 600

# Plot window configuration
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

palette = []

im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

# Iterate over each pixel of the figure and transform it in a complex number
for x_coord in range(0, WIDTH):
    for y_coord in range(0, HEIGHT):
        c = complex(RE_START + (x_coord / WIDTH) * (RE_END - RE_START),
                    IM_START + (y_coord / HEIGHT) * (IM_END - IM_START))
        m = gen_mandelbrot(c)
        # Change the constant multiplying 'm' for different color patterns in output figure
        color = 255 - int(m * 255 / MAX_ITER)
        draw.point([x_coord, y_coord], (color, color, color))

im.save('Mandelbrot_output.png', 'PNG')
