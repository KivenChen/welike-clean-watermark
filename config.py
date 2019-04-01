from PIL import ImageDraw
from PIL.ImageColor import getcolor
config = dict(
    weizuotu = [
        dict(
            name='rectangle',
            kwargs=dict(
                xy=[(x0, y0), (x1, y1)],
                fill=getcolor((r, g, b))
            )
        )
    ]
)

name_to_op = dict(

)
