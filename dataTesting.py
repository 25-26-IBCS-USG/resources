from graphics import*
from button import*

def showUsers(ul):
    win2 = GraphWin("List of Users", 400, 500)
    t1 = Text(Point(150, 20), "USERNAME              |              PASSWORD")
    t1.draw(win2)
    for i in range(len(ul)):
        eT = Text(Point(20, 20*i + 60), "|" + str(i+1) + "|")
        eT.draw(win2)
        uT = Text(Point(100, 20*i + 60), ul[i][0])
        uT.draw(win2)
        pT = Text(Point(200, 20*i + 60), ul[i][1])
        pT.draw(win2)
    

def main():

    #generate GUI
    win = GraphWin("Testing Sample", 600, 600)
    userName = Entry(Point(300,300), 30)
    userName.draw(win)
    userName.setSize(24)
    passWord = Entry(Point(300,400), 30)
    passWord.draw(win)
    passWord.setSize(24)
    uText = Text(Point(300,260), "Please enter your username:")
    uText.draw(win)
    uText.setSize(20)
    pText = Text(Point(300,360), "Please enter your password:")
    pText.draw(win)
    pText.setSize(20)

    #Generate Initial Text and prompts
    wText = Text(Point(300, 40), "Username Storage")
    wText.setSize(36)
    wText.draw(win)
    r1Text = Text(Point(300,80), "Your Username must...")
    r1Text.draw(win)
    r2Text = Text(Point(300,140), "Your Password must...")
    r2Text.draw(win)
    
    #  --   EDIT THE NUMBERED RULES BELOW   --
    # usernames
    r11Text = Text(Point(300, 110), "1. \n2. \n3. ")
    # passwords
    r21Text = Text(Point(300, 170), "1. \n2. \n3. ")

    r11Text.draw(win)
    r21Text.draw(win)

    addB = Button(win, "ADD USER", 100, Point(300, 500))
    closeB = Button(win, "EXIT", 80, Point(500, 500))
    showB = Button(win, "SHOW USERS", 80, Point(100, 500))
    userList = []

    #allow user to add names/pw
    
    while True:
        m = win.getMouse()
        if addB.isClicked(m):
            t1 = userName.getText()
            t2 = passWord.getText()
            userList.append([t1, t2])

        if showB.isClicked(m):
            showUsers(userList)

        if closeB.isClicked(m):
            break

    win.close()


if __name__ == "__main__":
    main()
