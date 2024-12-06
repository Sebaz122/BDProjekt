import psycopg2 as ps
import os
from tkinter import *  # To change- import * are bad habit
from dotenv import load_dotenv


def load_database():
    connection = ps.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    return connection

def print_uczestnik(cursor):
    cursor.execute("SELECT * FROM uczestnik")
    dataset = cursor.fetchall()
    for data in dataset:
        print(data)

def set_path(cursor):
    cursor.execute("SET SEARCH_PATH to kurs")

def window_center(root):
    window_width=1280
    window_height=720
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    center_x=int((screen_width-window_width)/2)
    center_y=int((screen_height-window_height)/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def print_uczestnik_on_screen(root,cursor):
    cursor.execute("SELECT * FROM uczestnik")
    dataset=cursor.fetchall()
    total_rows=len(dataset)
    total_cols=len(dataset[0])
    for i in range(total_rows):
        for j in range(total_cols):
            e=Entry(root, width=20, fg='blue', background="lightblue", font=('Arial', 16 , 'bold'))
            e.grid(row=i, column=j, sticky="NEWS")
            e.insert(END,dataset[i][j])

def add_table(root,cursor):
    top=Toplevel(root)
    top.geometry("400x400")
    top.attributes('-topmost',True)


if __name__ == "__main__":
    load_dotenv()
    ### Simple window
    root = Tk()
    root.title("Shop simulation")
    root.configure(bg="lightblue")
    window_center(root) 
    ###
    connection = load_database()
    cursor = connection.cursor()
    set_path(cursor)
    ###Dividing root frame to parts and placing them
    left_frame=Frame(root,width=200, height=200, background="crimson")
    left_frame.pack(side=LEFT)
    right_frame=Frame(root, width=800, height=500, background="lightgreen")
    right_frame.pack(side=RIGHT)
    ### Table_test

    button1= Button(left_frame, text="Wyprintuj uczestników kursu", command=lambda:print_uczestnik_on_screen(right_frame,cursor))
    button2= Button(left_frame, text="Dodaj tabelę", command=lambda:add_table(root,cursor)) #włóż oba w widget
    button1.place(x=50,y=50)
    button2.place(x=100,y=100)
    root.mainloop()
    
    
