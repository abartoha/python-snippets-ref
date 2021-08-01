import tkinter as tk
master = tk.Tk()

your_text = "I'm reading a book about anti-gravity.\nIt's impossible to put down.."

msg = tk.Message(master, text =your_text)
msg.config(bg='skyblue', font=('times', 18, 'italic'))
msg.grid()

tk.mainloop()
