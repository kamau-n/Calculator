from tkinter import *
import math

root=Tk()
root.title('calculator')
root.resizable(False,False)

try:
   def insertion_(num):
        pre=ent.get()
        ent.delete(0,END)
        ent.insert(0,str(pre) + str(num))
    
    
   def addition():
      try:
         global num1
         num1=float(ent.get())
         global sign
         sign="addition"
         ent.delete(0,END)
      except:
         ent.delete(0,END)
         ent.insert(0,"SYNTAX ERROR")
    
    
   def subtraction(): 
       global num1
       try:
          num1=float(ent.get())
          global sign
          sign="subtraction"
          ent.delete(0,END)
       except:
         ent.delete(0,END)
         ent.insert(0,"SYNTAX ERROR")
           
    
   def multiply():
      try:
         global num1
         num1=float(ent.get())
         global sign
         sign="times"
         ent.delete(0,END)
      except:
         ent.delete(0,END)
         ent.insert(0,"SYNTAX ERROR")
    
   def division():
       try:
          global num1
          num1=float(ent.get())
          global sign
          sign="divide"
          ent.delete(0,END)
       except:
          ent.delete(0,END)
          ent.insert(0,"SYNTAX ERROR")
    
   def square():
       global sign
       sign='sq'
        

   def square_root():
      global sign 
      sign='sqrt'
     
   def log():
       global sign 
       sign='logarithm'
       

   def delete():
       length=(ent.get())
       len_=len(length)
       ent.delete(len_-1,END)
    
   def inverse_():
         global num1
         num1=float(ent.get())
         global sign
         sign='inv' 
         ent.delete(0,END)
         
   def cos_():
         global sign
         sign='cos' 
         ent.delete(0,END)
      
   def tan_():
        global sign
        sign='tan' 
        ent.delete(0,END)


   def sin_():
      global sign
      sign='sin' 
      ent.delete(0,END)

   
   def asin_():
      global sign
      sign='asin' 
      ent.delete(0,END)

   
   def acos_():
      global sign
      sign='acos' 
      ent.delete(0,END)

   def ceil():
      global sign
      sign='ceil' 
      ent.delete(0,END)


   def floor():
      global sign
      sign='floor' 
      ent.delete(0,END)
 
   def atan_():
      global sign
      sign='atan' 
      ent.delete(0,END)
      
      
   def power():
       try:
          global num1
          num1=float(ent.get())
          global sign
          sign="pow"
          ent.delete(0,END)
       except:
          ent.delete(0,END)
          ent.insert(0,"SYNTAX ERROR")

   def cuberoot():
      global sign
      sign ='cuberoot'
      ent.delete(0,END)
    
   

   def modulus():
      try:
        global num1
        num1=float(ent.get())
        global sign
        sign="mod"
        ent.delete(0,END)
      except:
        ent.delete(0,END)
        ent.insert(0,"SYNTAX ERROR")

   def factorial():
       global sign
       sign = 'fact'
       ent.delete(0,END)

   def cube():
       global sign
       sign ='cube'
       global num1
       num1=float(ent.get())
       ent.delete(0,END)


    
   def answer_equals():
       try:
          if sign=='addition':
             num2 = float(ent.get())
             ent.delete(0,END)
             answer=num1+num2
             ent.insert(0, str(answer))
             text.insert('1.0',answer+'\n')
          elif sign=='subtraction':
               num2 = float(ent.get())
               ent.delete(0,END)
               answer=num1-num2
               ent.insert(0,answer)
               text.insert('end',answer+'\n')
          elif sign=="times":
               num2 = float(ent.get())
               ent.delete(0,END)
               answer=num1*num2
               ent.insert(0,answer)
               text.insert('end',answer+'\n')

          elif sign=="divide":
               try:
                  num2 = float(ent.get())
                  ent.delete(0,END)
                  answer=float(num1/num2)
                  ent.insert(0,answer)
               except:
                  ent.insert(0,"Math Error")
        
          elif sign=='sq':
               num=float(ent.get())
               ent.delete(0,END)
               answer=num*num
               ent.insert(0,answer)
              

          elif sign=='sqrt':
               num=float(ent.get())
               answer=float(math.sqrt(num))
               ent.insert(0,answer)
               text.insert('end',answer+'\n')
        
          elif sign =='logarithm':
               log_num=float(ent.get())
               ent.delete(0,END)
               answer=(math.log10(log_num))
               ent.insert(0,answer)
               text.insert('end',answer)
              
          elif sign=='inv':
               try:            
                  answer=float(1/num1)
                  ent.insert(0,answer)
                  text.insert('end',answer+'\n')
               except:
                  ent.insert(0,"MATH ERROR")
           
          elif sign=='tan':
               tan_num=float(ent.get())
               ent.delete(0,END)
               answer=float(math.tan(tan_num))
               ent.insert(0,answer)
               text.insert('end',answer+'\n')
           
          elif sign=='cos':
               cos_num=float(ent.get())
               ent.delete(0,END)
               answer=float(math.cos(cos_num)) 
               ent.insert(0,answer)
               text.insert('end',answer+'\n')

          elif sign=='sin':
               sin_num=float(ent.get())
               ent.delete(0,END)
               answer=float(math.sin(sin_num)) 
               ent.insert(0,answer)
               text.insert('end',answer+'\n')

          elif sign=='asin':
               sin_num=float(ent.get())
               ent.delete(0,END)
               answer=float(math.asin(sin_num)) 
               ent.insert(0,answer)
               text.insert('end',answer+'\n')
       
          elif sign=='acos':
               sin_num=float(ent.get())
               ent.delete(0,END)
               answer=float(math.acos(sin_num)) 
               ent.insert(0,answer)
               text.insert('end',answer+'\n')
               
          elif sign =='atan':
               tan_num=float(ent.get())
               ent.delete(0,END)
               answer=float(math.atan(tan_num))
               ent.insert(0,answer)
               
                            
             
          elif sign=='pow':
               num2=float(ent.get())
               ent.delete(0,END)
               answer=math.pow(num1,num2)
               ent.insert(0,answer)
              
               
               
          elif sign=='mod':
               num2=float(ent.get())
               ent.delete(0,END)
               answer=math.remainder(num1,num2)
               ent.insert(0,answer)
                 

      
          elif sign=='fact':
               fact_num=float(ent.get())
               ent.delete(0,END)
               answer=math.factorial(fact_num)
               ent.insert(0,answer)
               
               
          elif sign=='ceil':
               ceil_num=float(ent.get())
               ent.delete(0,END)
               answer=math.ceil(ceil_num)
               ent.insert(0,answer)
               
          elif sign=='floor':
               num=float(ent.get())
               ent.delete(0,END)
               answer=math.floor(num)
               ent.insert(0,answer)
               text.insert('end',answer+'\n') 
          elif sign=='cube':
              
               ent.delete(0,END)
               answer=float(num1**3)
               ent.insert(0,answer)

               
          elif sign=='cuberoot':
             try:
                num=float(ent.get())
                ent.delete(0,END)
                answer=(num** (1./3.))+0.000000000000001
                ent.insert(0,answer)
             except:
                ent.insert(0,"SYNTAX ERROR")
          
             
       except Exception as err:
         onscreen=float(ent.get())
         ent.delete(0,END)
         ent.insert(0,onscreen)
         
         

       
       
       

   def clear():
       ent.delete(0,END)
except:
    ent.delete(0,END)
    print("Syntax Error")       



  
ent=Entry(bd=2,bg='grey',fg='black',width=40)
ent.grid(row=0,column=0,columnspan=5)



button9=Button(root,relief='raised',bd=1,text='9',width=4,height=4,command =lambda :insertion_(9))
button9.grid(row=1,column=0)

button8=Button(root,relief='raised',bd=1,text='8',width=4,height=4,command=lambda :insertion_(8))
button8.grid(row=1,column=1)

button7=Button(root,relief='raised',bd=1,text='7',width=4,height=4,command=lambda : insertion_(7))
button7.grid(row=1,column=2)

button6=Button(root,relief='raised',bd=1,text='6',width=4,height=4,command=lambda :insertion_(6))
button6.grid(row=2,column=0)

button5=Button(root,relief='raised',bd=1,text='5',width=4,height=4,command= lambda :insertion_(5))
button5.grid(row=2,column=1)

button4=Button(root,relief='raised',bd=1,text='4',width=4,height=4,command=lambda : insertion_(4))
button4.grid(row=2,column=2)

button3=Button(root,relief='raised',bd=1,text='3',width=4,height=4,command=lambda : insertion_(3))
button3.grid(row=3,column=0)

button2=Button(root,relief='raised',bd=1,text='2',width=4,height=4,command=lambda : insertion_(2))
button2.grid(row=3,column=1)

button1=Button(root,relief='raised',bd=1,text='1',width=4,height=4,command=lambda : insertion_(1))
button1.grid(row=3,column=2)

button_zero=Button(root,relief='raised',bd=1,text='0',width=4,height=4,command=lambda : insertion_(0))
button_zero.grid(row=4,column=0)

button_add=Button(root,relief='raised',width=4,bd=1,text='+',height=4,command=addition)
button_add.grid(row=5,column=1)

button_equals=Button(root,relief='raised',bd=1,width=4,text='=',height=9,fg='white',bg='green',command=answer_equals)
button_equals.grid(row=6,column=4,rowspan=2)

button_clear=Button(root,relief='raised',bd=1,width=4,text='CE',fg='green',height=4,command=clear)
button_clear.grid(row=4,column=1)

button_sub=Button(root,relief='raised',bd=1,width=4,text='-',height=4,fg='green',command=subtraction)
button_sub.grid(row=3,column=3)

button_multiply=Button(root,relief='raised',bd=1,width=4,text='×',height=4,command=multiply)
button_multiply.grid(row=2,column=3)

button_divide=Button(root,relief='raised',bd=1,width=4,text='÷',height=4,command=division).grid(row=1,column=3)

button_square=Button(root,relief='raised',bd=1,width=4,text='x²',height=4,command=square).grid(row=2,column=4)

button_sqrt=Button(root,relief='raised',bd=1,width=4,text='√',height=4,command=square_root).grid(row=3,column=4)

button_log=Button(root,relief='raised',bd=1,text='log',width=4,height=4,command=log).grid(row=1,column=4)

button_delete =Button(root,relief='raised',bd=1,text='DEL',width=4,fg='red',height=4,command=delete).grid(row=4,column=2)

button_float =Button(root,relief='raised',bd=1,text='.',width=4,height=4,command = lambda :insertion_('.') ).grid(row=5,column=0)

button_inv =Button(root,relief='raised',bd=1,text='inv',width=4,height=4,command =inverse_ ).grid(row=5,column=2)

button_cos =Button(root,relief='raised',bd=1,text='cos',width=4,height=4,command = cos_ ).grid(row=5,column=3)

button_tan =Button(root,relief='raised',bd=1,text='tan',width=4,height=4,command = tan_).grid(row=4,column=3)

button_sin =Button(root,relief="raised",text='sin',width=4,height=4,command=sin_).grid(row=6,column=0)

button_power =Button(root,relief="raised",text='x^y',width=4,height=4,command=power).grid(row=6,column=1)

button_acos =Button(root,relief="raised",text='acos',width=4,height=4,command=acos_).grid(row=6,column=2)
button_atan =Button(root,relief="raised",text='atan',width=4,height=4,command=atan_).grid(row=6,column=3)
button_asin =Button(root,relief="raised",text='asin',width=4,height=4,command=asin_).grid(row=5,column=4)

button_mod = Button(root,relief='raised',text='%',width=4,height=4,command=modulus).grid(row=7,column=0)

button_fact = Button(root,relief='raised',text='fact',width=4,height=4,command=factorial).grid(row=7,column=1)
button_ceil = Button(root,relief='raised',text='ceil',width=4,height=4,command=ceil).grid(row=7,column=2)
button_floor = Button(root,relief='raised',text='floor',width=4,height=4,command=floor).grid(row=7,column=3)
button_cube = Button(root,relief='raised',text='x³',width=4,height=4,command=cube).grid(row=7,column=3)

button_cuberoot=Button(root,text='3√' ,width=4,height=4,command = cuberoot).grid(row=4,column=4)



root.mainloop()

