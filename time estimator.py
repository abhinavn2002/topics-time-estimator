import pandas as pd
import tkinter as tk

file = open("source.txt", "r")

root = tk.Tk()

reading_rate = 12 * 60
writing_rate = 2
concepts_density = 1 / 100

# for i in file:
def enterMain():
    global name
    name = tk.Entry(root)
    name.pack()
    # i = input("enter value")
    # label = tk.Label(root, text=i)
    # label.pack()
    global entry
    entry = tk.Entry(root)
    entry.pack()
    button = tk.Button(root, command=getValue, text="submit")
    button.pack()
    root.mainloop()


def getValue():
    submit = entry.get()
    time = 0
    time += len(submit) / reading_rate
    time += len(submit) * concepts_density / writing_rate
    df = pd.DataFrame([[name.get(), time]])
    df.to_csv("solution.csv", mode="a", header=False)


enterMain()
