from display import *
from draw import *
screen = new_screen()
color = [ 0, 255, 255 ]
##Octant 1
#0 Test
draw_line(0, 50, 200, 50, screen, color )#works
#1 test
draw_line(0, 50, 200, 450, screen, [128,128,128] )#works
#.5 test
draw_line(0, 0, 200, 100, screen, [16,255,56] )#works
##Octant 8
#-.5 test
draw_line(0, 500, 200, 400, screen, [64,128,128] )#works
#-1 test
draw_line(0, 300, 300, 0, screen, [64,255,128] )#works
##Octant 7
#-2 test
draw_line(0, 400, 300, 0, screen, [64,64,200] )
##Octant 2
draw_line(0, 0, 200, 400, screen, color )#works
#infinity test
draw_line(50, 0, 50, 400, screen, color )#works
#-infinity test
save_ppm(screen,'test.ppm')
#display(screen)
#save_extension(screen, 'img.png')
