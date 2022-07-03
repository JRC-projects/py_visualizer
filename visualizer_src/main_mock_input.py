import math
import time

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


# print('\x1b[2J') # clear screen escape sequence

max_range = 20
mock_input = [0,0,0,1,2,3,5,7,5,4,2,1,1,1,0,0,3,4,7,8,9,5,4,3,0,0,1]
max_in = max(mock_input)
refresh_time = 0.01


if __name__ == "__main__":
    for i in mock_input:
        luminance_index = i/max_in # take this into a normalize luminance function - for now, int between 0,1
        render(luminance_index)
        time.sleep(refresh_time)
