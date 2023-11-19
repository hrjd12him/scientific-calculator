from future.moves import tkinter
import math


def click(val):
    e = entry.get()  # getting the value

    try:
        if val == "C":
            e = e[0 : len(e) - 1]  # deleting the last entered value
            entry.delete(0, "end")
            entry.insert(0, e)
        elif val == "CE":
            entry.delete(0, "end")
        elif val == "√":
            ans = math.sqrt(eval(e))
        elif val == "π":
            ans = math.pi
        elif val == "cose":
            ans = math.cos(math.radians(eval(e)))
        elif val == "sine":
            ans = math.sin(math.radians(eval(e)))
        elif val == "tane":
            ans = math.tan(math.radians(eval(e)))
        elif val == "2π":
            ans = 2 * math.pi
        elif val == "cosh":
            ans = math.cosh(eval(e))
        elif val == "sinh":
            ans = math.sinh(eval(e))
        elif val == "tanh":
            ans = math.tanh(eval(e))
        elif val == chr(8731):
            ans = eval(e) ** (1 / 3)
        elif val == "x\u02b8":
            entry.insert("end", "**")
            return
        elif val == "x\u00B3":
            ans = eval(e) ** 3
        elif val == "x\u00B2":
            ans = eval(e) ** 2
        elif val == "ln":
            ans = math.log(eval(e))
        elif val == "deg":
            ans = math.degrees(eval(e))
        elif val == "rad":
            ans = math.radians(eval(e))
        elif val == "e":
            ans = math.e
        elif val == "log10":
            ans = math.log10(eval(e))
        elif val == "x!":
            ans = math.factorial(eval(e))
        elif val == chr(247):
            entry.insert("end", "/")
            return
        elif val == "=":
            ans = eval(e)
        else:
            entry.insert("end", val)
            return

        # Do something with the result 'ans', such as displaying it in the Entry widget
        entry.delete(0, "end")
        entry.insert(0, ans)

    except Exception as ex:
        # Handle errors (e.g., division by zero, invalid input, etc.)
        entry.delete(0, "end")
        entry.insert(0, "Error")


# Create the main window
root = tkinter.Tk()
root.title("Scientific Calculator")
root.geometry("680x486+100+100")
root.config(bg="black")

entry = tkinter.Entry(
    root, font=("arial", 20, "bold"), bg="black", fg="white", bd=10, width=30
)
entry.grid(row=0, column=0, columnspan=8)

# buttons list
button_list = [
    "C",
    "CE",
    "√",
    "+",
    "π",
    "cose",
    "tane",
    "sine",
    "1",
    "2",
    "3",
    "-",
    "2π",
    "cosh",
    "tanh",
    "sinh",
    "4",
    "5",
    "6",
    "*",
    chr(8731),
    "x\u02b8",
    "x\u00B3",
    "x\u00B2",
    "7",
    "8",
    "9",
    chr(247),
    "ln",
    "deg",
    "rad",
    "e",
    "0",
    ".",
    "%",
    "=",
    "log10",
    "(",
    ")",
    "x!",
]

r = 1
c = 0

# Loop to get the buttons on window
for i in button_list:
    button = tkinter.Button(
        root,
        width=5,
        height=2,
        bd=2,
        text=i,
        bg="black",
        fg="white",
        font=("arial", 18, "bold"),
        command=lambda button=i: click(button),
    )
    button.grid(row=r, column=c, pady=1)

    c += 1
    if c > 7:
        c = 0
        r += 1

# Start the Tkinter event loop
root.mainloop()
