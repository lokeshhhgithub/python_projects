from tkinter import *

first_number = second_number = operator = None

def get_operator(op):
    global first_number, operator

    first_number = int(result_label['text'])
    operator = op
    # second_number = result_label['text']
    result_label.config(text ='')

def equal():
    global first_number, operator, second_number

    second_number = int(result_label['text'])

    if operator == '+':
        result_label.config(text = str(first_number + second_number))

    elif operator == '-':
        result_label.config(text = str(first_number - second_number))
   
    elif operator == '*':
        result_label.config(text = str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text = 'Error')
        else:
            result_label.config(text = str(first_number / second_number))



def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text = new)

def clear():
    result_label.config(text = '')

root =Tk()

root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)
root.config(background= 'black')


result_label = Label(root, text = '' , bg = 'black', fg = 'white')
result_label.grid(row = 0, column = 0, columnspan = 5, pady=(50,25), sticky= 'w')
result_label.config(font =('Times New Roman','30', 'bold'))
 
btn7 = Button(root, text = '7', bg ='green', fg = 'white',width =5,height = 2, command= lambda : get_digit(7))
btn7.grid(row = 1, column = 0)
btn7.config(font=('Times New Roman',14, 'bold'))

btn8 = Button(root, text = '8', bg ='green', fg = 'white',width =5,height = 2, command= lambda : get_digit(8))
btn8.grid(row = 1, column = 1)
btn8.config(font=('Times New Roman',14, 'bold'))

btn9 = Button(root, text = '9', bg ='green', fg = 'white',width =5,height = 2,command= lambda : get_digit(9))
btn9.grid(row = 1, column = 2)
btn9.config(font=('Times New Roman',14, 'bold'))

btn_add = Button(root, text = '+', bg ='green', fg = 'white',width =5,height = 2, command = lambda : get_operator('+'))
btn_add.grid(row = 1, column = 3)
btn_add.config(font=('Times New Roman',14, 'bold'))



btn4 = Button(root, text = '4', bg ='green', fg = 'white',width =5,height = 2,command= lambda : get_digit(4))
btn4.grid(row = 2, column = 0)
btn4.config(font=('Times New Roman',14, 'bold'))

btn5 = Button(root, text = '5', bg ='green', fg = 'white',width =5,height = 2, command= lambda : get_digit(5))
btn5.grid(row = 2, column = 1)
btn5.config(font=('Times New Roman',14, 'bold'))

btn6 = Button(root, text = '6', bg ='green', fg = 'white',width =5,height = 2, command= lambda : get_digit(6))
btn6.grid(row = 2, column = 2)
btn6.config(font=('Times New Roman',14, 'bold'))

btn_sub = Button(root, text = '-', bg ='green', fg = 'white',width =5,height = 2, command = lambda : get_operator('-'))
btn_sub.grid(row = 2, column = 3)
btn_sub.config(font=('Times New Roman',14, 'bold'))

btn1 = Button(root, text = '1', bg ='green', fg = 'white',width =5,height = 2, command= lambda : get_digit(1))
btn1.grid(row = 3, column = 0)
btn1.config(font=('Times New Roman',14, 'bold'))

btn2 = Button(root, text = '2', bg ='green', fg = 'white',width =5,height = 2, command= lambda : get_digit(2))
btn2.grid(row = 3, column = 1)
btn2.config(font=('Times New Roman',14, 'bold'))

btn3 = Button(root, text = '3', bg ='green', fg = 'white',width =5,height = 2, command= lambda : get_digit(3))
btn3.grid(row = 3, column = 2)
btn3.config(font=('Times New Roman',14, 'bold'))

btn_mul = Button(root, text = '*', bg ='green', fg = 'white',width =5,height = 2, command = lambda : get_operator('*'))
btn_mul.grid(row = 3, column = 3)
btn_mul.config(font=('Times New Roman',14, 'bold'))

btn_clear = Button(root, text = 'C', bg ='green', fg = 'white',width =5,height = 2, command = lambda : clear())
btn_clear.grid(row = 4, column = 0)
btn_clear.config(font=('Times New Roman',14, 'bold'))

btn0 = Button(root, text = '0', bg ='green', fg = 'white',width =5,height = 2,command= lambda : get_digit(0))
btn0.grid(row = 4, column = 1)
btn0.config(font=('Times New Roman',14, 'bold'))

btn_equal = Button(root, text = '=', bg ='green', fg = 'white',width =5,height = 2, command= equal)
btn_equal.grid(row = 4, column = 2)
btn_equal.config(font=('Times New Roman',14, 'bold'))

btn_div = Button(root, text = '/', bg ='green', fg = 'white',width =5,height = 2, command = lambda : get_operator('/'))
btn_div.grid(row = 4, column = 3)
btn_div.config(font=('Times New Roman',14, 'bold'))


root.mainloop()