#!/bin/bash

#  Taken from https://superuser.com/questions/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality
#  and slightly adjusted

ffmpeg -i input.mov \
    -vf "fps=10,scale=1024:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
    -loop 0 output.gif
