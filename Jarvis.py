from os import name
import tkinter as tk
from tkinter.constants import BOTTOM, END
from typing import Collection, Text
# importing speech recognition package from google api 
import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import webbrowser
root = tk.Tk()
root.title("Python Math")
# specify size of window.
root.geometry("450x370")
# Create text widget and specify size.
T = tk.Text(root, height = 5, width = 52)
# Create label
l = tk.Label(root, text = "Jarvis version1.0",font =("Courier", 14)) 
Fact = """Fact:
1-Just ask Jarvis to open or search in google 
2-wikipedia also available  
3-With Funy calculator
4-Give your personal detail to remember""" 
def function1():
    root = tk.Tk()
    root.geometry("450x370")
    def function2():
      INPUT = input.get("1.00","end-1c")
      NAME = name.get("1.00","end-1c")
      print(NAME)
      print(INPUT)
      if(INPUT == "perass"):#p-Personal,a-Assistant
         root = tk.Tk()
         root.geometry("450x370")
         output_label=tk.Label(root,text="Output:")
         simple = tk.Text(root,height= 10,width = 27,bg = "light cyan")
         def function3():                     
           def assistant_speaks(output):
            Fact = """
*HYPER:"""+output+"""."""           
            print("Jarvis: ", output)            
            toSpeak = gTTS(text = output, lang ='en', slow = False)
            num = "audio by Roshan"
            file = str(num)+".mp3"
            toSpeak.save(file)
            # playsound package is used to play the same file. 
            playsound.playsound(file, True)  
            os.remove(file)
            simple.insert(tk.END,Fact)
           def get_audio(): 
            rObject = sr.Recognizer() 
            audio = '' 
            with sr.Microphone() as source: 
              print("Speak...")
              Fact = """
*Speak..."""
              # recording the audio using speech recognition 
              audio = rObject.listen(source, phrase_time_limit = 10)  
            print("Stop.") # limit 10 secs
            Fact = """
*Stop...""" 
            simple.insert(tk.END,Fact)
            try: 
              text = rObject.recognize_google(audio, language ='en-US') 
              print(NAME," : ", text)
              Fact = """
*You:"""+text+""".""" 
              return text 
            except: 
              assistant_speaks("Could not understand your audio, PLease try again !") 
              return 0
            # Driver Code 

           if __name__ == "__main__": 
            assistant_speaks("I am Jarvis version 1.0") 
            name ='Human'
            name = NAME 
            assistant_speaks("Hello, " + name + '.') 
            while(1): 
               assistant_speaks("What can i do for you?") 
               text = get_audio().lower()
               if text == 0: 
                 continue               
        
               if "who are you" in str(text) or "define yourself" in str(text): 
                 speak = '''Hello, I am Person. Your personal Assistant. 
                 I am here to make your life easier. You can command me to perform 
                 various tasks such as calculating sums or opening applications etcetra'''
                 assistant_speaks(speak) 
                 
               if "who made you" in str(text) or "created you" in str(text): 
                 speak = "I have been created by Roshan Melvin."
                 assistant_speaks(speak) 
                 
               if "who am i" in str(text):
                 speak = NAME
                 assistant_speaks(speak)
               if "tell me roshan phone number" in str(text) or "roshan phone number" in str(text) :
                 speak = "roshan phone number is 8098210136"
                 assistant_speaks(speak)
               if "Jarvis" in str(text):
                 assistant_speaks("Tell me what i need to do")
                 
               if "open youtube" in str(text):
                 assistant_speaks("Opening in youtube") 
                 webbrowser.open("http://www.youtube.com/") 
                 return
               if "open instagram" in str(text) or "open my instagram" in str(text):
                 assistant_speaks("Opening in instagram") 
                 webbrowser.open("http://www.instagram.com/") 
                 return
               if "open twitter" in str(text) or "open my twitter" in str(text) :
                 assistant_speaks("Opening in twitter") 
                 webbrowser.open("http://www.twitter.com/") 
                 return
               if "open google" in str(text):
                 assistant_speaks("Opening in google") 
                 webbrowser.open("http://www.google.com/") 
                 return
               if 'search' in str(text):
                 assistant_speaks("showing your result") 
                 webbrowser.open("https://www.google.com/"+text)
                 return
                 
               if "show tables" in str(text) or "open tables" in str(text):
                 assistant_speaks("Opening tables in google") 
                 webbrowser.open("https://images-na.ssl-images-amazon.com/images/I/81rWaSC+7QL.jpg") 
                 return
               if "calculate" in str(text) or "calculator" in str(text):
                # Python program for simple calculator 
                root = tk.Tk()
                root.geometry("450x370") 
                T = tk.Text(root, height = 10, width = 35)
                def add(num1,num2): 
                  return num1 + num2 
                  # Function to subtract two numbers  
                def subtract(num1,num2): 
                 return int(num1) - int(num2)
                 # Function to multiply two numbers 
                def multiply(num1, num2): 
                 return int(num1) * int(num2) 
                 # Function to divide two numbers 
                def divide(num1, num2): 
                 return int(num1) / int(num2)
  
   
                 # Take input from the user
                Fact = """Please select operation 
1.Add(+)\n
2.Subtract(-)\n
3.Multiply(x)\n
4.Divide(%)\n 
Select operations form 1,2,3,4 :"""
                def function():    
                  SEL = select.get("1.00","end-1c")
                  NUM1 = number1.get("1.00","end-1c")
                  NUM2 = number2.get("1.00","end-1c")
                  print(SEL)
                  print(NUM1)
                  print(NUM2)
                  if SEL == "1": 
                    print("Your answer is:",NUM1+"+",NUM2,"=",
                add(NUM1,NUM2))
                  elif SEL == "2": 
                    print("Your answer is:",NUM1,"-",NUM2,"=",
                subtract(NUM1,NUM2)) 
                  elif SEL == "3": 
                    print("Your answer is:",NUM1,"x",NUM2,"=",
                multiply(NUM1,NUM2)) 
                  elif SEL == "4":
                    print("Your answer is:",NUM1,"%",NUM2,"=",
                divide(NUM1,NUM2))
                  else:
                    print("Invalid input")
                r_b1 = tk.Button(root, text = "Next",command = function)
                refer_label=tk.Label(root,text="Refer this:")
                select_label=tk.Label(root,text="Select operation form:")
                number1_label=tk.Label(root,text="Enter first number:")
                number2_label=tk.Label(root,text="Ender second number:")
                select = tk.Text(root,height= 1,width = 25,bg ="light cyan")
                number1 = tk.Text(root,height= 1,width = 25,bg ="light cyan")
                number2 = tk.Text(root,height= 1,width = 25,bg ="light cyan")
                T.grid(column=2,row=1)
                select.grid(column=2,row=2)
                number1.grid(column=2,row=3)
                number2.grid(column=2,row=4)
                refer_label.grid(column=1,row=1)
                select_label.grid(column=1,row=2)
                number1_label.grid(column=1,row=3)
                number2_label.grid(column=1,row=4)
                r_b1.grid(column=2,row=5)
                T.insert(tk.END, Fact) 
                return  
               if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
                 assistant_speaks("Ok bye, "+ name+'.')
                 break
         def function4():
               # Python program for simple calculator 
               root = tk.Tk()
               root.geometry("450x370") 
               T = tk.Text(root, height = 10, width = 35)
               def add(num1,num2): 
                 return num1 + num2 
                 # Function to subtract two numbers  
               def subtract(num1,num2): 
                 return int(num1) - int(num2)
                 # Function to multiply two numbers 
               def multiply(num1, num2): 
                 return int(num1) * int(num2) 
                 # Function to divide two numbers 
               def divide(num1, num2): 
                 return int(num1) / int(num2)
  
   
                 # Take input from the user
               Fact = """Please select operation: 
1.Add(+)\n
2.Subtract(-)\n
3.Multiply(x)\n
4.Divide(%)\n 
Select operations form 1,2,3,4 :
See answer in cmd or terminal"""
               def function():    
                  SEL = select.get("1.00","end-1c")
                  NUM1 = number1.get("1.00","end-1c")
                  NUM2 = number2.get("1.00","end-1c")
                  print(SEL)
                  print(NUM1)
                  print(NUM2)
                  if SEL == "1": 
                    print("Your answer is:",NUM1+"+",NUM2,"=",
            add(NUM1,NUM2))
                  elif SEL == "2": 
                    print("Your answer is:",NUM1,"-",NUM2,"=",
            subtract(NUM1,NUM2)) 
                  elif SEL == "3": 
                    print("Your answer is:",NUM1,"x",NUM2,"=",
            multiply(NUM1,NUM2)) 
                  elif SEL == "4":
                    print("Your answer is:",NUM1,"%",NUM2,"=",
            divide(NUM1,NUM2))
                  else:
                    print("Invalid input")
               r_b1 = tk.Button(root, text = "Next",command = function)
               refer_label=tk.Label(root,text="Refer this:")
               select_label=tk.Label(root,text="Select operation form:")
               number1_label=tk.Label(root,text="Enter first number:")
               number2_label=tk.Label(root,text="Ender second number:")
               select = tk.Text(root,height= 1,width = 25,bg ="light cyan")
               number1 = tk.Text(root,height= 1,width = 25,bg ="light cyan")
               number2 = tk.Text(root,height= 1,width = 25,bg ="light cyan")
               T.grid(column=2,row=1)
               select.grid(column=2,row=2)
               number1.grid(column=2,row=3)
               number2.grid(column=2,row=4)
               refer_label.grid(column=1,row=1)
               select_label.grid(column=1,row=2)
               number1_label.grid(column=1,row=3)
               number2_label.grid(column=1,row=4)
               r_b1.grid(column=2,row=5)
               T.insert(tk.END, Fact)              
         h_b2 = tk.Button(root, text = "Calculator",command = function4)                            
         r_b2 = tk.Button(root, text = "HYPER",command = function3)
         Fact = """
*Hello!!"""+NAME+"""...
*HYPER is a voice assistant 
*Made for personal use"""   
         simple.insert(tk.END, Fact)
         output_label.grid(column=1,row=1)
         r_b2.grid(column=2,row=3)
         h_b2.grid(column=2,row=4)
         simple.grid(column=2,row=2)
    name = tk.Text(root,height= 1,width = 25,bg ="light cyan") 
    input = tk.Text(root,height= 1,width = 25,bg ="light cyan")
    #
    name_label=tk.Label(root,text="Username:")
    option_label=tk.Label(root,text="Option:")
    #Button for .....
    r_b1 = tk.Button(root, text = "Next",command = function2)
    
    name.grid(column=2,row=1)
    input.grid(column=2,row=2)
    name_label.grid(column=1,row=1)
    option_label.grid(column=1,row=2) 
    r_b1.grid(column=2,row=3)

    b1.pack()
    l.pack()

# Create button for next text.
b1 = tk.Button(root, text = "Next",command = function1) 
# Create an Exit button.
b2 = tk.Button(root, text = "Exit",
            command = root.destroy)

l.pack()
T.pack() 
b1.pack()
b2.pack() 
# Insert The Fact.
T.insert(tk.END, Fact)
  
tk.mainloop()
