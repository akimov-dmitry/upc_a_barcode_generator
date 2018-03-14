from math import *
from tkinter import *



x=0
w=5
s=10*w      


def guard_start():
    global x,w,s
    canv.create_line(s,0,s,90,width=w, fill='black')#1
    x=x+w+s
    canv.create_line(x,0,x,90,width=w, fill='white') #2
    x=x+w
    canv.create_line(x,0,x,90,width=w, fill='black') #3
    x=x+w



def guard_stop():
    global x,w
    canv.create_line(x,0,x,90,width=w, fill='black')#1
    x=x+w
    canv.create_line(x,0,x,90,width=w, fill='white') #2
    x=x+w
    canv.create_line(x,0,x,90,width=w, fill='black') #3
    x=x+w

def guard_middle():
    global x,w
    canv.create_line(x,0,x,90,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,90,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,90,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,90,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,90,width=w, fill='white')
    x=x+w



def zeroL():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w

def zeroR():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w


def oneL():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w



def oneR():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w


def twoL():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w


def twoR():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w

def threeL():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    
def threeR():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
def fourL():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
def fourR():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w


def fiveL():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w

def fiveR():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w


def sixL():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w

def sixR():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w

def sevenL():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w

def sevenR():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w

def eightL():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w

def eightR():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w

def nineL():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w

def nineR():
    global x,w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='black')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
    canv.create_line(x,0,x,75,width=w, fill='white')
    x=x+w
root = Tk()
exit_flag=False
while 1==1:
        if exit_flag==True:quit();
        str_code=input('Введите 11 значный код: ')
        if len(str_code)!=11 or str_code.isdecimal()==False:
            print('Ошибка!')
        
        else:
            code = list(str_code)
            print(code)
            i=0
            k=6
            j=1
            sum_nech=0
            sum_ch=0
            sum_o=0
            last_digit=0
            canv = Canvas(root, width = 12*7*w+6*7*w+5*7*w+10*w, height = 90, bg = "white", cursor = "pencil")
            guard_start()
            while i<6:
                if int(code[i])==0:zeroL()
                if int(code[i])==1:oneL()
                if int(code[i])==2:twoL()
                if int(code[i])==3:threeL()
                if int(code[i])==4:fourL()
                if int(code[i])==5:fiveL()
                if int(code[i])==6:sixL()
                if int(code[i])==7:sevenL()
                if int(code[i])==8:eightL()
                if int(code[i])==9:nineL()
                i=i+1
                print(i)
            guard_middle()
            while k<11:
                if int(code[k])==0:zeroR()
                if int(code[k])==1:oneR()
                if int(code[k])==2:twoR()
                if int(code[k])==3:threeR()
                if int(code[k])==4:fourR()
                if int(code[k])==5:fiveR()
                if int(code[k])==6:sixR()
                if int(code[k])==7:sevenR()
                if int(code[k])==8:eightR()
                if int(code[k])==9:nineR()
                k=k+1
                print(k)
            while j<12:
                if j%2!=0:
                    sum_nech=sum_nech+int(code[j-1])
                    j=j+1
                    print(j)
                else:
                    sum_ch=sum_ch+int(code[j-1])
                    j=j+1
                    print(j)
            sum_nech=sum_nech*3
            print('Сумма нечётных: '+str(sum_nech))
            print('Сумма чётных: '+str(sum_ch))
            sum_o=sum_ch+sum_nech
            print('Общая сумма: '+str(sum_o))
            last_digit=sum_o%10
            print('Последняя цифра: '+str(last_digit))
            last_digit=10-last_digit
            #last_digit=last_digit%10
            print("Контрольная цифра: "+str(last_digit))
            if last_digit==0:zeroR()
            if last_digit==1:oneR()
            if last_digit==2:twoR()
            if last_digit==3:threeR()
            if last_digit==4:fourR()
            if last_digit==5:fiveR()
            if last_digit==6:sixR()
            if last_digit==7:sevenR()
            if last_digit==8:eightR()
            if last_digit==9:nineR()
            if last_digit==10:zeroR()
            guard_stop()
            canv.pack()
            exit_flag=True
            root.mainloop()
            
            
