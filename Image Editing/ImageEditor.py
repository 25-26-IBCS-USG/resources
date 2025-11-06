from graphics import*
from button import*
import random

def brighten(myImg):
    for i in range(myImg.getWidth()):
        for j in range(myImg.getHeight()):
            pix = myImg.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            #BRIGHTEN BELOW
            
            myImg.setPixel(i, j, color_rgb(r,g,b))
def darken(myImg):
    for i in range(myImg.getWidth()):
        for j in range(myImg.getHeight()):
            pix = myImg.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            #DARKEN BELOW
            
            myImg.setPixel(i, j, color_rgb(r,g,b))

def blurr(myImg):
    pixels = []
    for i in range(myImg.getWidth()):
        pixels.append([])
        for j in range(myImg.getHeight()):
            totR = 0
            totG = 0
            totB = 0
            for k in range(-2,3):
                for l in range(-2,3):
                    if (i + k < 0) or (i + k > 499):
                        break
                    if (j + l < 0) or (j + l > 450):
                        break
                    pix = myImg.getPixel(i + k, j + l)
                    totR += pix[0]
                    totG += pix[1]
                    totB += pix[2]
            r, g, b = totR//25, totG//25, totB//25
            pixels[i].append(color_rgb(r, g, b))
    for i in range(myImg.getWidth()):
        for j in range(myImg.getHeight()):
            myImg.setPixel(i, j, pixels[i][j])
          
def onlyBlue(myImg):
    for i in range(myImg.getWidth()):
        for j in range(myImg.getHeight):
            pix = myImg.getPixel(i,j)
            r, g, b = pix[0], pix[1], pix[2]
            save = False
            if b > r * 3:
                if r < 150:
                    save = True
            if not save:
                avg = (r + g + b)//3
                myImg.setPixel(i, j, color_rgb(avg, avg, avg))
                        
def specialFilter(myImg):
    for i in range(myImg.getWidth()):
        for j in range(myImg.getHeight()):
            pix = myImg.getPixel(i,j)
            r, g, b = pix[0], pix[1], pix[2]
            
def contrast(myImg):
    for i in range(myImg.getWidth()):
        for j in range(myImg.getHeight()):
            pix = myImg.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            #CONTRAST BELOW
            
            myImg.setPixel(i, j, color_rgb(r,g,b))
            
def main():

    win = GraphWin("Image Editor", 800, 600)
    sh = Button(win, "Show", Point(150, 40), 45)
    hi = Button(win, "Hide", Point(300, 40), 45)
    close = Button(win, "Quit", Point(150, 560), 45)
    bright = Button(win, "Brighten", Point(720, 50), 45)
    dark = Button(win, "Darken", Point(720, 150), 45)
    blur = Button(win, "Blur", Point(720, 250), 45)
    cont = Button(win, "Contrast", Point(720, 350), 45)
    filt = Button(win, "Filter", Point(720, 450), 45)
    oB = Button(win, "only Blue", Point(720, 550), 45)

    myImg = Image(Point(400,300), "daisyBlank.png")

    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if sh.isClicked(m):
            myImg.undraw()
            myImg.draw(win)
        if hi.isClicked(m):
            myImg.undraw()
        if dark.isClicked(m):
            darken(myImg)
        if bright.isClicked(m):
            brighten(myImg)
        if blur.isClicked(m):
            blurr(myImg)
        if cont.isClicked(m):
            contrast(myImg)
        if filt.isClicked(m):
            specialFilter(myImg)
        if oB.isClicked(m):
            onlyBlue(myImg)
        m = win.getMouse()

    win.close()
    
if __name__ == "__main__":
    main()
