


from graphics import *
from math import sqrt




win = GraphWin("Calculator", 400,600)
win.setCoords(0,0,30,51)

Equation = ""

display = Text(Point(25,45), Equation)
display.draw(win)


Memory = ""

def inside(point, rectangle):

    ll = rectangle.getP1()  
    ur = rectangle.getP2()  

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def Press(x): 
    
    global Equation
    global display
  
    
    Equation += str(x)
  
    
    display.setText(Equation)


def Equal_Press():
    global Equation
    global display
    
 
    total = str(eval(Equation)) 
  
    display.setText(total) 
    Equation = str(total)

def Pos_neg():
    global Equation
    global display

    Converted = eval(Equation) *-1
    Equation = str(Converted)
    
    display.setText(Converted)


def Off():
    Calc_on = False
    
    while Calc_on == False:
        Click = win.getMouse()
        if inside(Click, On_key):
            return Calc_on == True

def Find():
    global Equation
    global display
    num = True
    while num == True:
        if Equation[-1].isdigit() == True:
            Equation = Equation[:-1]
        else:
            num = False
            display.setText(Equation)
                      
                      
            
        
        
        
     
    
    


def buttons():
    Pos_Neg_key = Rectangle(Point(1,1),Point(6,6))
    Zero_key = Rectangle(Point(7,1),Point(12,6))
    Decimal_key = Rectangle(Point(13,1),Point(18,6))
    Equal_key = Rectangle(Point(23,1),Point(28,6))
    One_key = Rectangle(Point(1,7),Point(6,12))
    Two_key = Rectangle(Point(7,7),Point(12,12))
    Three_key = Rectangle(Point(13,7),Point(18,12))
    Add_key = Rectangle(Point(23,7),Point(28,12))
    Four_key = Rectangle(Point(1,13),Point(6,18))
    Five_key = Rectangle(Point(7,13),Point(12,18))
    Six_key = Rectangle(Point(13,13),Point(18,18))
    Subtract_key = Rectangle(Point(23,13),Point(28,18))
    Seven_key = Rectangle(Point(1,19),Point(6,24))
    Eight_key = Rectangle(Point(7,19),Point(12,24))
    Nine_key = Rectangle(Point(13,19),Point(18,24))
    Multiply_key = Rectangle(Point(23,19),Point(28,24))
    
    Reciprocal_key = Rectangle(Point(1,25),Point(6,30))
    Squared_key = Rectangle(Point(7,25),Point(12,30))
    Sqrt_key = Rectangle(Point(13,25),Point(18,30))
    Divide_key = Rectangle(Point(23,25),Point(28,30))
    Percent_key = Rectangle(Point(1,31),Point(6,36))
    CE_key = Rectangle(Point(7,31),Point(12,36))
    Clear_key = Rectangle(Point(13,31),Point(18,36))
    Backspace_key = Rectangle(Point(23,31),Point(28,36))
    Mem_Add_key = Rectangle(Point(1,37),Point(6,39))
    Mem_Subtract_key = Rectangle(Point(7,37),Point(12,39))
    Mem_Store_key = Rectangle(Point(13,37),Point(18,39))
    On_key = Rectangle(Point(20,37),Point(24,39))
    Off_key = Rectangle(Point(25,37),Point(29,39))

    return Pos_Neg_key, Zero_key, Decimal_key, Equal_key, One_key, Two_key, Three_key, Add_key, Four_key, Five_key, Six_key, Subtract_key, Seven_key, Eight_key, Nine_key, Multiply_key, Reciprocal_key, Squared_key, Sqrt_key, Divide_key, Percent_key, CE_key, Clear_key, Backspace_key, Mem_Add_key, Mem_Subtract_key, Mem_Store_key, On_key, Off_key

## 1st Row  #############################################

Pos_Neg_key = Rectangle(Point(1,1),Point(6,6))
t1 = Text(Point(3,3), "+ / -")
t1.draw(win)
Pos_Neg_key.draw(win)


Zero_key = Rectangle(Point(7,1),Point(12,6))
t2 = Text(Point(9.5,3), "0")
t2.draw(win)
Zero_key.draw(win)

Decimal_key = Rectangle(Point(13,1),Point(18,6))
t3 = Text(Point(15.5,3), ".")
t3.draw(win)
Decimal_key.draw(win)

Equal_key = Rectangle(Point(23,1),Point(28,6))
t4 = Text(Point(25.5,3), "=")
t4.draw(win)
Equal_key.draw(win)
    
## 1st Row  #############################################






## 2nd Row  #############################################

One_key = Rectangle(Point(1,7),Point(6,12))
t5 = Text(Point(3,9.5), "1")
t5.draw(win)
One_key.draw(win)


Two_key = Rectangle(Point(7,7),Point(12,12))
t6 = Text(Point(9.5,9.5), "2")
t6.draw(win)
Two_key.draw(win)

Three_key = Rectangle(Point(13,7),Point(18,12))
t7 = Text(Point(15.5,9.5), "3")
t7.draw(win)
Three_key.draw(win)

Add_key = Rectangle(Point(23,7),Point(28,12))
t8 = Text(Point(25.5,9.5), "+")
t8.draw(win)
Add_key.draw(win)
    
## 2nd Row  #############################################






## 3rd Row  #############################################

Four_key = Rectangle(Point(1,13),Point(6,18))
t9 = Text(Point(3,15.5), "4")
t9.draw(win)
Four_key.draw(win)

Five_key = Rectangle(Point(7,13),Point(12,18))
t10 = Text(Point(9.5,15.5), "5")
t10.draw(win)
Five_key.draw(win)

Six_key = Rectangle(Point(13,13),Point(18,18))
t11 = Text(Point(15.5,15.5), "6")
t11.draw(win)
Six_key.draw(win)

Subtract_key = Rectangle(Point(23,13),Point(28,18))
t12 = Text(Point(25.5,15.5), "-")
t12.draw(win)
Subtract_key.draw(win)

## 3rd Row  #############################################








## 4th Row  #############################################

Seven_key = Rectangle(Point(1,19),Point(6,24))
t13 = Text(Point(3, 21.5), "7")
t13.draw(win)
Seven_key.draw(win)

Eight_key = Rectangle(Point(7,19),Point(12,24))
t14 = Text(Point(9.5, 21.5), "8")
t14.draw(win)
Eight_key.draw(win)

Nine_key = Rectangle(Point(13,19),Point(18,24))
t15 = Text(Point(15.5, 21.5), "9")
t15.draw(win)
Nine_key.draw(win)

Multiply_key = Rectangle(Point(23,19),Point(28,24))
t16 = Text(Point(25.5, 21.5), "*")
t16.draw(win)
Multiply_key.draw(win)

## 4th Row  #############################################






## 5th Row  #############################################

Reciprocal_key = Rectangle(Point(1,25),Point(6,30))
t17 = Text(Point(3, 27.5), "1/x")
t17.draw(win)
Reciprocal_key.draw(win)

Squared_key = Rectangle(Point(7,25),Point(12,30))
t18 = Text(Point(9.5, 27.5), "X^2")
t18.draw(win)
Squared_key.draw(win)

Sqrt_key = Rectangle(Point(13,25),Point(18,30))
t19 = Text(Point(15.5, 27.5), "SQRT")
t19.draw(win)
Sqrt_key.draw(win)

Divide_key = Rectangle(Point(23,25),Point(28,30))
t20 = Text(Point(25.5, 27.5), "÷")
t20.draw(win)
Divide_key.draw(win)



## 5th Row  #############################################


## 6th Row  #############################################

Percent_key = Rectangle(Point(1,31),Point(6,36))
t21 = Text(Point(3, 33.5), "%")
t21.draw(win)
Percent_key.draw(win)

CE_key = Rectangle(Point(7,31),Point(12,36))
t22 = Text(Point(9.5, 33.5), "CE")
t22.draw(win)
CE_key.draw(win)

Clear_key = Rectangle(Point(13,31),Point(18,36))
t23 = Text(Point(15.5, 33.5), "C")
t23.draw(win)
Clear_key.draw(win)

Backspace_key = Rectangle(Point(23,31),Point(28,36))
t24 = Text(Point(25.5, 33.5), "←")
t24.draw(win)
Backspace_key.draw(win)


## 6th Row  #############################################






## 7th Row  #############################################


Mem_Add_key = Rectangle(Point(1,37),Point(6,39))
t25 = Text(Point(3, 38), "M+")
t25.draw(win)
Mem_Add_key.draw(win)

Mem_Subtract_key = Rectangle(Point(7,37),Point(12,39))
t26 = Text(Point(9.5, 38), "M-")
t26.draw(win)
Mem_Subtract_key.draw(win)

Mem_Store_key = Rectangle(Point(13,37),Point(18,39))
t27 = Text(Point(15.5, 38), "MS")
t27.draw(win)
Mem_Store_key.draw(win)

On_key = Rectangle(Point(20,37),Point(24,39))
On_key.setOutline("green")
t28 = Text(Point(22, 38), "ON")
t28.draw(win)
On_key.draw(win)


Off_key = Rectangle(Point(25,37),Point(29,39))
Off_key.setOutline("red")
t29 = Text(Point(27, 38), "OFF")
t29.draw(win)
Off_key.draw(win)

win.setBackground("Light Blue")





## 7th Row  #############################################



Pos_Neg_key, Zero_key,Decimal_key, Equal_key, One_key, Two_key, Three_key, Add_key, Four_key, Five_key, Six_key, Subtract_key, Seven_key, Eight_key, Nine_key, Multiply_key, Reciprocal_key, Squared_key, Sqrt_key, Divide_key, Percent_key, CE_key, Clear_key, Backspace_key, Mem_Add_key, Mem_Subtract_key, Mem_Store_key, On_key, Off_key = buttons()





Calc_on = True


   

    

while Calc_on == True:
    Click = win.getMouse()

    if Click is None:
        Equation = ""
    elif inside(Click, Pos_Neg_key):
        Pos_neg()                        
    elif inside(Click, One_key):
        Press("1")
    elif inside(Click, Zero_key):
        Press("0")
    elif inside(Click, Decimal_key):
        Press(".")
    elif inside(Click, Equal_key):
        Equal_Press()
    elif inside(Click, Two_key):
        Press("2")
    elif inside(Click, Three_key):
        Press("3")
    elif inside(Click, Add_key):
        Press("+")
    elif inside(Click, Four_key):
        Press("4")
    elif inside(Click, Five_key):
        Press("5")
    elif inside(Click, Six_key):
        Press("6")
    elif inside(Click, Subtract_key):
        Press("-")
    elif inside(Click, Seven_key):
        Press("7")
    elif inside(Click, Eight_key):
        Press("8")
    elif inside(Click, Nine_key):
        Press("9")
    elif inside(Click, Multiply_key):
        Press("*")
    elif inside(Click, Reciprocal_key):
        Converted = 1/eval(Equation)
        display.setText(str(Converted))
        Equation = str(Converted)
    elif inside(Click, Squared_key):
        Converted = eval(Equation)**2
        Equation = str(Converted)
        display.setText(str(Converted))
        
    elif inside(Click, Sqrt_key):
        Converted = sqrt(eval(Equation))
        Equation = str(Converted)
        display.setText(str(Converted))
        
    elif inside(Click, Divide_key):
        Press("/")
        
    elif inside(Click, Percent_key):
        Percent = eval(display.getText()) * .01
        Equation = str(Percent)
        display.setText(Equation)
        
    elif inside(Click, CE_key):
        Find()
        
        

    elif inside(Click, Clear_key):
        display.setText("")
        Equation = ""
        if Memory.isdigit() == True:
            Memory = ""
            display.setText("Memory Cleared")
            time.sleep(1.5)
            display.setText("")
        

    elif inside(Click, Backspace_key):
        Equation = Equation[:-1]
        display.setText(Equation)
        
    elif inside(Click, Mem_Add_key):
        Memory = eval(Memory) + eval(Equation)
        Equation = ""
        Memory = str(Memory)
        display.setText(Memory)

    elif inside(Click, Mem_Subtract_key):
        Memory = eval(Memory) - eval(Equation)
        Memory = str(Memory)
        display.setText(Memory)
        
        Equation = ""

    elif inside(Click, Mem_Store_key):
        Memory = Equation
        display.setText("Memory Stored")
        time.sleep(3)
        display.setText("")
        Equation = ""

    elif inside(Click, Off_key):
        Off()

        

    
                    
        
        
    
        
        
        
