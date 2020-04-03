try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

#tkinter._test()

main_window = tkinter.Tk()
main_window.title("Hello World")
main_window.geometry('960x480')

label = tkinter.Label(main_window, text="Hello World")
label.pack(side='top')

left_frame = tkinter.Frame(main_window)
left_frame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=2)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(main_window)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')
button2.pack(side='top')
button3.pack(side='top')
button1.pack(side='top')

main_window.mainloop()
