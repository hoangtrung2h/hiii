import turtle

#draw star by python
def drawStar(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.seth(0)
    for i in range(5):
        turtle.fd(400)
        turtle.rt(1440)

#draw rectangle by python
def drawRectangle(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.seth(0)
    for i in range(4):
        turtle.fd(400)
        turtle.rt(900)

if __name__ == '__main__':
    
    while True:
        #show menu
        print("1. Draw a star")
        print("2. Draw a rectangle")
        print("3. Exit")

        option =  int(input("Please select an option:"))

        if option == 1:
            x = int(input("Please input x:"))
            y = int(input("Please input y:"))
            drawStar(x,y)
        elif option == 2:
            x = int(input("Please input x:"))
            y = int(input("Please input y:"))
            drawRectangle(x,y)
        elif option == 3:
            break

    print("Exit")
