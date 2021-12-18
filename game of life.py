from tkinter import *

root = Tk()
root['bg'] = '#FFFFFF'
root.title('Фентези приключение')
root.geometry('500x500')
root.resizable(width=False, height=False)

need_eat = 25
need_sleep = 0

def eat():
    eat_egg = Button(text='кушать яйцо', command=eategg)
    eat_egg.place(relx=0.50, rely=0.30, relwidth=0.25, relheight=0.1)
    
    eat_fish = Button(text='кушать рыбу', command=eategg)
    eat_fish.place(relx=0.75, rely=0.30, relwidth=0.25, elheight=0.1)
    
    fish = 1
    egg = 5
    info = Label(text='У вас есть: \n' + str(fish) + ' Рыбы\n' + str(egg) + ' Яичек!', bg='#FFFFFF', font=30)
    info.place(relx=0.50, relwidth=0.5, relheight=0.3)
    if egg != 0:
        def eategg():
            egg - 1
            if need_eat == 0:
                info = Label(text='Вы не хотите кушать!', bg='#FFFFFF', font=30)
                info.place(relx=0.50, relwidth=0.5, relheight=0.3)
            else:
                need_eat - 25
        if egg != 0:
        
info1 = Label(text='Ваш голод: ' + str(need_eat) + '\nВы хотите спать: ' + str(need_sleep), bg='#FFFFFF', font=30)
info1.place(relx=0.50, rely=0.70 ,relwidth=0.5, relheight=0.3)

btn = Button(text='кушать', command=eat)
btn.place(relx=0, rely=0, relwidth=0.5, relheight=0.1)

btn1 = Button(text='спать')
btn1.place(relx=0, rely=0.10, relwidth=0.5, relheight=0.1)

btn2 = Button(text='роботать')
btn2.place(relx=0, rely=0.20, relwidth=0.5, relheight=0.1)
