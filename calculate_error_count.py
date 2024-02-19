""" calculate error count

    This script calculates the errors made in a test,
    based on the number of tasks presented and the achieved percentages.
"""


import tkinter as tk


def calculate_wrong_questions():
    total_questions = int(line02_total_questions_entry.get())
    percentage = float(line03_percentage_entry.get())
    wrong_questions = round(total_questions * (100 - percentage) / 100)
    line06_result_textbox.config(text=f"""
    If you answered {percentage}%
    of {total_questions} questions correctly,
    then you answered
    {wrong_questions} questions incorrectly.""")


# ------ GUI - root frame
root = tk.Tk()
    
root.title("calculator error count")
root_frame_width = 300
root_frame_height = 280
root.minsize(root_frame_width, root_frame_height)
root.resizable(False, False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root_frame_screen_x = int(screen_width/2 - root_frame_width / 2)
root_frame_screen_y = int(screen_height/2 - root_frame_height / 2)
root.geometry(f"{root_frame_width}x{root_frame_height}+{root_frame_screen_x}+{root_frame_screen_y}")


line01_empty_label = tk.Label(root, text="")
line01_empty_label.grid(row=1, column=0)

line02_total_questions_label = tk.Label(root, text="Number of questions")
line02_total_questions_label.grid(row=2, column=0, padx=10, pady=10)
line02_total_questions_entry = tk.Entry(root)
line02_total_questions_entry.grid(row=2, column=1, padx=10, pady=10)

line03_percentage_label = tk.Label(root, text="percentage achieved")
line03_percentage_label.grid(row=3, column=0, padx=10, pady=10)
line03_percentage_entry = tk.Entry(root)
line03_percentage_entry.grid(row=3, column=1, padx=10, pady=10)

line04_empty_label = tk.Label(root, text="")
line04_empty_label.grid(row=4, column=0)

line05_wrong_button = tk.Button(root, text="calculate", command=calculate_wrong_questions)
line05_wrong_button.grid(row=5, column=0)

line06_result_textbox = tk.Label(root, text="")
line06_result_textbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()