import math
import time
try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559



def get_char_bar(luminance_index: float, screen_width: int) -> list:
    """uses maths to get the horizontal bar that is repeated vertically"""
    
    char_bar_output = []
    char_seq = ' .,-_~:;=!*#$@'
    
    # char_append = char_seq[int(len(char_seq)*luminance_index)]

    max_value = int(len(char_seq)*luminance_index) -1
    
    # char_append_width: list = [char_append] * (screen_width + 0)
    for i in range(screen_width):
        proportion_across_screen = i/screen_width
        wave_val = math.sin(math.pi*proportion_across_screen) # at far left of screen, sin(0)=0, at right:sin(pi)=0, in middle:sin(pi/2)=1

        char_bar_output.extend(char_seq[int(max_value*wave_val)])


    return "".join(char_bar_output)



def render(luminance_index):
    
    screen_width = 50 # 50 
    screen_height = 35 # 50 

    char_append_width = get_char_bar(luminance_index, screen_width)

    char_output = []
    for i in range(screen_height + 1):
        char_output.append(char_append_width)
    
    # char_output[xp][yp] = '.,-~:;=!*#$@'[int(luminance_index)]

    print('\x1b[H')
    for i in range(screen_height):
        for j in range(screen_width):
            print(char_output[i][j], end='')
        print()



def get_level():
    lux_list = []
    lux = ltr559.get_lux()
    if lux == 0:
        lux = 0.01

    lux_list.append(lux)
    if len(lux_list)>30:
        del lux_list[0]
    
    max_lux = max(lux_list)

    return lux, max_lux

# print('\x1b[2J') # clear screen escape sequence

# max_range = 20
# mock_input = [0,0,0,1,2,3,5,7,5,4,2,1,1,1,0,0,3,4,7,8,9,5,4,3,0,0,1]
# max_in = max(mock_input)

refresh_time = 0.01


if __name__ == "__main__":
    while True:
        lux, max_lux = get_level()
        luminance_index = lux/max_lux # take this into a normalize luminance function - for now, int between 0,1
        render(luminance_index)
        time.sleep(refresh_time)
