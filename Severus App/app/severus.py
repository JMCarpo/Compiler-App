import lexical
import syntax
from tkinter import *
from tkinter import constants
from pyglet import font

font.add_file('assets/OpenSans-ExtraBold.ttf')
font.add_file('assets/OpenSans-Regular.ttf')


def run_lex():                                  # Run Lexical Analyzer
    inputValue = editorPane.get("1.0", "end-1c")
    lex = lexical.lexer(inputValue)
    print_lex(lex.type, lex.value)
    print_error(lex.error)
    lexPane.config(state="disabled")
    errorPane.config(state="disabled")


def run_syntax():
    inputValue = editorPane.get("1.0", "end-1c")
    lexPane.config(state="normal")
    lexPane.delete('1.0', constants.END)
    errorPane.config(state="normal")
    errorPane.delete('1.0', constants.END)
    syntax_error = syntax.parser(inputValue)
    print_error(syntax_error)
    lexPane.config(state="disabled")
    errorPane.config(state="disabled")


def print_lex(type, value):                      # Print Text to Lexical Pane
    lexPane.config(state="normal")
    lexPane.delete('1.0', constants.END)
    lexPane.insert(constants.END, "LEXEME\t\t\tTOKEN\n\n")
    for i in range(len(type)):
        if type[i] == 'lex-error' or type[i] == 'newline' or type[i] == 'whitespace':
            continue
        else:
            lexPane.insert(
                constants.END, f'{str(value[i]) if len(str(value[i]))<=15 else str(value[i])[:10] + "..."}\t\t\t{str(type[i])}\n')


def print_error(error):
    errorPane.config(state="normal")
    errorPane.delete('1.0', constants.END)
    for err in range(len(error)):
        if err+1 == len(error):
            if error[err] != '':
                errorPane.insert(constants.END, f'{error[err]}\n')
        else:
            if error[err] != '':
                if error[err] != error[err+1]:
                    errorPane.insert(constants.END, f'{error[err]}\n')
            else:
                continue


def refresh():
    editorPane.config(state="normal")
    lexPane.config(state="normal")
    errorPane.config(state="normal")
    editorPane.delete('1.0', constants.END)
    lexPane.delete('1.0', constants.END)
    errorPane.delete('1.0', constants.END)
    lexPane.config(state="disabled")
    errorPane.config(state="disabled")


window = Tk()

window.geometry("939x617")
window.resizable(False, False)
window.title("Severus")
#window.iconbitmap("assets/logo.ico")
window.configure(bg="#251c3b")
canvas = Canvas(
    window,
    bg="#334232",
    height=617,
    width=939,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

# Title Bar
titlebar_img = PhotoImage(file=f"assets/background.png")
titlebar = canvas.create_image(
    469.5, 23,
    image=titlebar_img)
titlebarIcon_img = PhotoImage(file=f"assets/img2.png")
titleIcon = canvas.create_image(
    20, 22,
    image=titlebarIcon_img,
)
title = canvas.create_text(
    70, 22,
    text=" ",
    font=('Open Sans ExtraBold', 20),
    fill="#211B36",
)

# Buttons
runIcon_img = PhotoImage(file=f"assets/img0.png")
lexicalBtn = Button(
    image=runIcon_img,
    compound=LEFT,
    bg="#fee2c1",
    borderwidth=0,
    highlightthickness=0,
    activebackground="#211B36",
    fg="#000000",
    text=" Lexical Button",
    font=('Open Sans', 10),
    activeforeground="#FFFFFF",
    justify="center",
    command=run_lex,
)
lexicalBtn.place(
    x=13, y=57,
    width=148,
    height=30,
)
# semButton.place(
#     x=200, y=52,
#     width=200,
#     height=30)
syntaxBtn = Button(
    image=runIcon_img,
    compound=LEFT,
    bg="#fee2c1",
    borderwidth=0,
    highlightthickness=0,
    activebackground="#211B36",
    fg="#000000",
    text=" Syntax Button",
    font=('Open Sans', 10),
    activeforeground="#FFFFFF",
    justify="center",
    command=run_syntax,
)
syntaxBtn.place(
    x=170, y=57,
    width=148,
    height=30,
)


# Editor Pane
editorPane = Text(
    bd=0,
    bg="#000000",
    highlightthickness=0,
    fg="#E9E7E7",
    padx=10,
    pady=10,
    font=('Open Sans', 10),
)

editorPane.place(
    x=13, y=100,
    width=577,
    height=324
)


# Lexeme Table Pane
lexPane = Text(
    bd=0,
    bg="#000000",
    highlightthickness=0,
    fg="#E9E7E7",
    padx=10,
    pady=10,
    font=('Open Sans', 10),
    state="disabled",
)

lexPane.place(
    x=616, y=100,
    width=297,
    height=487,
)

# Error Pane
errorPane = Text(
    bd=0,
    bg="#000000",
    highlightthickness=0,
    fg="#E9E7E7",
    padx=10,
    pady=10,
    font=('Open Sans', 10),
    state="disabled",)

errorPane.place(
    x=13, y=445,
    width=577,
    height=152,
)

#scrollBar = Scrollbar(editorPane, orient='vertical', command=editorPane.yview)
#scrollBar.pack(side=RIGHT, fill=Y)

#  communicate back to the scrollbar
#editorPane['yscrollcommand'] = scrollBar.set

window.mainloop()
