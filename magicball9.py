#!/usr/bin/env python
# coding: utf-8

# In[37]:


import random
import tkinter as tk

root = tk.Tk()
root.title("Magic ball")

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It's certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

answerNumber = random.randint(1, 9)
fortune = getAnswer(answerNumber)

lbl = tk.Label(root, font=('calibri', 11, 'bold'),
               background='black',
               foreground='white')
lbl.pack(anchor='center')
lbl.config(text=fortune)

root.mainloop()


# In[ ]:




