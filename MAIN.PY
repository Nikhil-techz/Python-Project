import tkinter as tk
from tkinter import messagebox

def check_winner():
    for i in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[i[0]]["text"]==buttons[i[1]]["text"]==buttons[i[2]]["text"]!="":
            buttons[i[0]].config(bg="green")
            buttons[i[1]].config(bg="green")
            buttons[i[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"player {buttons[i[0]]['text']}wins!")
            root.quit()

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
       buttons[index]["text"] = current_player
       check_winner()
       toggle_player() 

def toggle_player():
    global current_player
    current_player = "x" if current_player =="o" else "o" 
    label.config(text=f"player {current_player}'s turn") 

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons=[tk.Button(root,text="",font=("normal",25), width=6,height=2,command= lambda j=j: button_click(j)) for j in range(9)] 

for j ,button in enumerate(buttons) :
    button.grid(row=j//3,column= j%3)

current_player = "x"
winner = False
label = tk.Label(root,text=f"player{current_player}'s turn",font=("normal",16))
label.grid(row = 3,column=0,columnspan = 3) 
root.mainloop() 
