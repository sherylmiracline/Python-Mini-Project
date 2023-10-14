import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox, ttk


def enter_game():
    player1 = entry_player1.get()
    player2 = entry_player2.get()

    if player1 and player2:
        conn = sqlite3.connect('tictactoe.db')
        cursor = conn.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS tictactoe (Player1 TEXT, Player2 TEXT)')

        cursor.execute('INSERT INTO tictactoe VALUES (?, ?)', (player1, player2))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Names Entered Successfully!")

        print(f"Player1: {player1}\nPlayer2: {player2}")

        reset_data()
    else:
        messagebox.showerror("Error", "Please fill out all the fields.")

    window.pack_forget()
    main.pack(fill="both", expand=True)


def CheckforWin():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or button4["text"] == "X" and \
            button5["text"] == "X" and button6["text"] == "X" or button7["text"] == "X" and button8["text"] == "X" and \
            button9["text"] == "X" or button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or \
            button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or button1["text"] == "X" and \
            button4["text"] == "X" and button7["text"] == "X" or button2["text"] == "X" and button5["text"] == "X" and \
            button8["text"] == "X" or button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        messagebox.showinfo("Tic Tac Toe", "Player X has won!!")
        view_data_base()
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or button4["text"] == "O" and \
            button5["text"] == "O" and button6["text"] == "O" or button7["text"] == "O" and button8["text"] == "O" and \
            button9["text"] == "O" or button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or \
            button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or button1["text"] == "O" and \
            button4["text"] == "O" and button7["text"] == "O" or button2["text"] == "O" and button5["text"] == "O" and \
            button8["text"] == "O" or button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        messagebox.showinfo("Tic Tac Toe", "Player O has won!!")
        view_data_base()
    elif flag == 8:
        messagebox.showinfo("Tic Tac Toe", "Game Tied!")
        view_data_base()



def reset_data():
    entry_player1.delete(0, tk.END)
    entry_player2.delete(0, tk.END)


def ButtonClick(button):
    global x_o, flag
    button["bg"] = "#2ec4b6"
    if button["text"] == "" and x_o == True:
        button["text"] = "X"
        x_o = False
        CheckforWin()
        flag = flag + 1
    elif button["text"] == "" and x_o == False:
        button["text"] = "O"
        x_o = True
        CheckforWin()
        flag = flag + 1
    else:
        messagebox.showinfo("Tic Tac Toe", "Player has already entered!")


def view_data_base():
    conn = sqlite3.connect('tictactoe.db')
    cursor = conn.cursor()
    root1 = tk.Tk()
    root1.title("SQLite Table Viewer")
    conn4 = sqlite3.connect('tictactoe.db')
    cursor4 = conn4.cursor()

    query = 'select * from tictactoe;'

    cursor4.execute(query)
    data = cursor4.fetchall()
    columns = [desc[0] for desc in cursor4.description]
    tree = ttk.Treeview(root1, columns=columns)
    column_alignments = {
        col: "center"  # Default to center alignment for all columns
        for col in columns
    }

    for col in columns:
        heading_text = col.replace("_", " ").title()
        alignment = column_alignments.get(col, "center")
        tree.heading(col, text=heading_text, anchor=alignment)

    for col in columns:
        tree.column(col, width=100, anchor=column_alignments.get(col, "center"))

    vsb = ttk.Scrollbar(root1, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(side="right", fill="y")
    hsb = ttk.Scrollbar(root1, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(side="bottom", fill="x")

    for row in data:
        tree.insert("", "end", values=row)
    tree.pack(fill="both", expand=True)

    conn4.close()
    root1.geometry("300x300")
    root1.resizable(False, False)
    root1.mainloop()


root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("410x350")

window = tk.Frame(root, width=200, height=100, bg="purple")
window.pack(fill="both", expand=True)

main = tk.Frame(root, width=200, height=100, bg="purple")


player1_label = tk.Label(window, text="Name of Player1: ")
player1_label.pack()
entry_player1 = tk.Entry(window)
entry_player1.pack()

player2_label = tk.Label(window, text="Name of Player2: ")
player2_label.pack()
entry_player2 = tk.Entry(window)
entry_player2.pack()

enter_button = tk.Button(window, text="Enter Game", command=enter_game)
enter_button.pack()

reset_button = tk.Button(window, text="Reset", command=reset_data)
reset_button.pack()


x_o = True
flag = 0

button1 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3,
                 command=lambda: ButtonClick(button1))
button1.grid(row=0, column=0)

button2 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3,
                 command=lambda: ButtonClick(button2))
button2.grid(row=0, column=1)

button3 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3,
                 command=lambda: ButtonClick(button3))
button3.grid(row=0, column=2)

button4 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3,
                 command=lambda: ButtonClick(button4))
button4.grid(row=1, column=0)

button5 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3,
                 command=lambda: ButtonClick(button5))
button5.grid(row=1, column=1)

button6 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3,
                 command=lambda: ButtonClick(button6))
button6.grid(row=1, column=2)

button7 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3,
                 command=lambda: ButtonClick(button7))
button7.grid(row=2, column=0)

button8 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3,
                 command=lambda: ButtonClick(button8))
button8.grid(row=2, column=1)

button9 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3,
                 command=lambda: ButtonClick(button9))
button9.grid(row=2, column=2)


window.mainloop()


