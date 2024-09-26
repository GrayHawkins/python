#importing tkinter
from tkinter import*
from tkinter import ttk

#colors

color1 = "#1e1f1e" #black
color2 = "#4a4a4a" #gray
color3 = "#7b00ff" #roxo
color4 = "#0048ff" #azul
color5 = "#d40000" #vermelho
color6 = "#ffffff" #branco
# Window Config
window =Tk()
window.title("Calculator")
window.geometry("235x318")
window.config(bg=color2)

#frames

frame_display = Frame(window, width=235, height=75)
frame_display.grid(row=0, column=0)
frame_display.config(bg=color1)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)
frame_body.config(bg=color2)

#botões
b_1=Button(frame_body, text="C", width=15, height=2, bg=color3, fg=color6)
b_1.place(x=3, y=0)
b_2=Button(frame_body, text="%", width=6, height=2, bg=color3, fg=color6)
b_2.place(x=121, y=0)
b_3=Button(frame_body, text="/", width=6, height=2, bg=color3, fg=color6)
b_3.place(x=180, y=0)

b_4=Button(frame_body, text="7", width=6, height=2, bg=color3, fg=color6)
b_4.place(x=3, y=45)
b_5=Button(frame_body, text="8", width=6, height=2, bg=color3, fg=color6)
b_5.place(x=63, y=45)
b_6=Button(frame_body, text="9", width=6, height=2, bg=color3, fg=color6)
b_6.place(x=121, y=45)
b_7=Button(frame_body, text="*", width=6, height=2, bg=color3, fg=color6)
b_7.place(x=180, y=45)

b_8=Button(frame_body, text="4", width=6, height=2, bg=color3, fg=color6)
b_8.place(x=3, y=90)
b_9=Button(frame_body, text="5", width=6, height=2, bg=color3, fg=color6)
b_9.place(x=63, y=90)
b_10=Button(frame_body, text="6", width=6, height=2, bg=color3, fg=color6)
b_10.place(x=121, y=90)
b_11=Button(frame_body, text="-", width=6, height=2, bg=color3, fg=color6)
b_11.place(x=180, y=90)

b_12=Button(frame_body, text="1", width=6, height=2, bg=color3, fg=color6)
b_12.place(x=3, y=135)
b_13=Button(frame_body, text="2", width=6, height=2, bg=color3, fg=color6)
b_13.place(x=63, y=135)
b_14=Button(frame_body, text="3", width=6, height=2, bg=color3, fg=color6)
b_14.place(x=121, y=135)
b_16=Button(frame_body, text="+", width=6, height=2, bg=color3, fg=color6)
b_16.place(x=180, y=135)

b_17=Button(frame_body, text="0", width=15, height=2, bg=color3, fg=color6)
b_17.place(x=3, y=180)
b_18=Button(frame_body, text=".", width=6, height=2, bg=color3, fg=color6)
b_18.place(x=121, y=180)
b_19=Button(frame_body, text="=", width=6, height=2, bg=color3, fg=color6)
b_19.place(x=180, y=180)

window.mainloop()
