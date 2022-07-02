import time

def render(luminance_index):
    
    screen_width = 50 # 50 
    screen_height = 35 # 50 

    char_output = []
    zbuffer = []
    char_seq = ' .,-_~:;=!*#$@'
    
    char_append = char_seq[int(len(char_seq)*luminance_index)]
    
    for i in range(screen_height + 1):
        char_output.append([char_append] * (screen_width + 0))
        zbuffer.append([0] * (screen_width + 0))
    

    # char_output[xp][yp] = '.,-~:;=!*#$@'[int(luminance_index)]




    print('\x1b[H')
    for i in range(screen_height):
        for j in range(screen_width):
            print(char_output[i][j], end='')
        print()






# print('\x1b[2J') # clear screen escape sequence

max_range = 20

for i in range(max_range):
    luminance_index = i/max_range
    render(luminance_index)
    time.sleep(0.5)
