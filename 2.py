import moviepy.editor as mpy
from moviepy.video.tools.segmenting import findObjects

# Creating a White Background
WHITE = (255, 255, 255)
SCREEN_SIZE = (640, 480)
VERTICAL_SPACE = 30
HORIZONTAL_SPACE = 100

# Adding Image
SB_LOGO_PATH = "E:\\Learning\\Gradio\\GIF\\assets\\StackBuildersLogo.jpg"

# Position and Resizing the Image.
sb_logo = mpy.ImageClip(SB_LOGO_PATH).\
    set_position(('center', 0)).\           
    resize(width=200)

    # Positioning Text
    txt_clip = mpy.TextClip(
        "Let's build together",
        font="Charter-bold",
        color="RoyalBlue4",
        kerning=4,
        fontsize=30,
    ).\
    set_position(("center", sb_logo.size[1] + VERTICAL_SPACE]))