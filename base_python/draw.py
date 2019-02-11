from display import *
def draw_line( x0, y0, x1, y1, screen, color ):
    if x0==x1: ##infinite line, use octant 2!
        if y0>y1:
            ystor=y0
            y0=y1
            y1=ystor
        draw_line_octant2( x0, y0, x1, y1, screen, color )
    else:
        slope=(y1-y0) / (x1-x0)
        if slope>1:
            draw_line_octant2( x0, y0, x1, y1, screen, color )
        elif slope<-1:
            draw_line_octant7( x0, y0, x1, y1, screen, color )
        elif slope>=-1 and slope<=0:
            draw_line_octant8( x0, y0, x1, y1, screen, color )
        else:
            draw_line_octant1( x0, y0, x1, y1, screen, color )        
def draw_line_octant1( x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=2*A+B
    while x<=x1:
        plot(screen, color, x,y)
        if d>0:
            y+=1
            d+=2*B
        x+=1
        d+=2*A
def draw_line_octant2( x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=A+2*B
    while y<=y1:
        plot(screen,color,x,y)
        if d<0:
            x+=1
            d+=2*A
        y+=1
        d+=2*B
def draw_line_octant7( x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=A-2*B
    while y>=y1:
        plot(screen,color,x,y)
        if d<0:
            x+=1
            d-=2*A
        y-=1
        d+=2*B
def draw_line_octant8( x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    d=2*A-B
    while x<x1:
        plot(screen,color,x,y)
        if d<0:
            y-=1
            d-=2*B
        x+=1
        d+=2*A
