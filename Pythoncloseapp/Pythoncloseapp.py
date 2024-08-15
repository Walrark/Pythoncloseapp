from PIL import Image
from PIL import ImageTk
import tkinter as tk
from tkinter import ACTIVE, DISABLED, NORMAL, ttk
import random



windx0 = 2000
windy0 = 1200
window_size = "{}x{}".format(windx0,windy0)
num_of_closes = 0



# Create the main window
root = tk.Tk()
root.title("Close me.app")

# Set the window size
root.geometry(window_size)
root.overrideredirect(True)
var = tk.BooleanVar()

def display_text():
    global num_of_closes
    t1 = "Haha, you did it!"
    t2 = "Hey well done, you did it again."
    t3 = "Alright bud, we get it now. You wanna close me."
    t4 = "Look man, you already closes me 3 times! What do you want from me?"
    t5 = "Ok dude. You've had your fun, let me just do my thing!"
    t6 = "You are such a child!"
    t7 = "I really don't like you now."
    t8 = "What if I hide?"
    t9 = "Ok, look I'll just be quiet now and see if that changes anything."
    if num_of_closes == 1:
        label.config(text= t1)
    if num_of_closes == 2:
        label.config(text= t2)
    if num_of_closes == 3:
        label.config(text= t3)
    if num_of_closes == 4:
        label.config(text= t4)
    if num_of_closes == 5:
        label.config(text= t5)
    if num_of_closes == 6:
        label.config(text= t6)
    if num_of_closes == 7:
        label.config(text= t7)
    if num_of_closes == 8:
        label.config(text= t8)
    if num_of_closes == 9:
        label.config(text= t9)
    if num_of_closes == 10:
        label.config(text= "")

def update_counter():
    root.after(800, window_size_increase)
    root.after(800, update_counter)

def resize_window(x,y):
    window_size = "{}x{}".format(x,y)
    root.geometry(window_size)

def close_button_move(x_dir, y_dir):
    global num_of_closes
    global windx0
    global windy0
    speed = 1+ num_of_closes/5
    info = close_button.place_info()
    cur_x = int(info.get('x'))
    cur_y = int(info.get('y'))
    if cur_x + x_dir <= 0:
        x_dir = x_dir * (-1)
    if cur_y + y_dir <= 0:
        y_dir = y_dir * (-1)
    if cur_y + y_dir >= windy0-20:
        y_dir = y_dir * (-1)
    if cur_x + x_dir >= windx0-20:
        x_dir = x_dir * (-1)
    new_x = cur_x + x_dir * speed
    new_y = cur_y + y_dir * speed
    close_button.place(x = f"{new_x}", y = f"{new_y}")
    root.after(10, lambda: close_button_move(x_dir,y_dir))
    


def create_new_close_button():
    #creat a new button which is positioned in a random spot, also updates the label
    global close_button
    global windx0
    global windy0
    randx = random.randint(0,windx0)
    randy = random.randint(0,windy0)
    close_button.destroy()
    close_button = tk.Button(root, text="Close", command=on_close, state=tk.DISABLED)
    close_button.place(x = randx, y = randy)
    label.place(x = windx0/2, y = windy0/2)

def on_check():
    #if checkbox is checked closed button is active
    if var.get():
        close_button.config(state=tk.NORMAL)
    else:
        close_button.config(state=tk.DISABLED)

def window_size_increase():
    #updates the size of the window
    global windy0
    global windx0
    windy0 += 8
    windx0 += 10
    resize_window(windx0,windy0)

def on_close():
    #call updates and check if we've done 10 closes
    global num_of_closes
    global windy0
    global windx0  
    if num_of_closes == 10:
        print("Fine, you win")
        print("FINAL SCORE: {}/800".format(8000-(windx0 + windy0)))
        root.destroy()
    else:
        num_of_closes += 1
        if num_of_closes == 5:
            close_button_move(1,1)
        windx0 -= 150 
        windy0 -= 100 
        display_text()
        resize_window(windx0,windy0)
        create_new_close_button()
        check_button.deselect()
        on_check()
        open_popup_window()

def open_popup_window():
    global gif_file
    global windy0
    global windx0
    ymax = abs(windy0-400)
    xmax = abs(windx0-500)
    new_window = tk.Toplevel(root)
    new_window.overrideredirect(True)
    new_window.geometry("1000x800+{}+{}".format(random.randint(0,xmax),random.randint(0,ymax)))
    new_window.attributes("-topmost", True)
    new_canvas = tk.Canvas(new_window, width=1000, height=700, bg='black')
    new_canvas.pack()
    gif_player = GifPlayer(new_canvas, gif_file)
    close_popup_button = tk.Button(new_window, text = "Begone popup", command = new_window.destroy)
    close_popup_button.pack(pady=10)
    new_window.focus_force
    
def button_flash(button):
    original_colour = button.cget("background")
    button.config(background = 'green')
    root.after(400, lambda: button.config(background=original_colour ))

def text_box_entry():
    user_input = text_box.get()
    responce_message = tk.Label(root, wraplength = 120, text=f"You said {user_input}, which means nothing to me.")
    text_box.delete(first = 0, last=len(user_input))
    
    if user_input == "Help" or user_input == "help":
        responce_message = tk.Label(root, wraplength = 120, text="Here is a list of commands: Pedro, highlight closebutton, highlight checkbutton")
        
    if user_input == "highlight closebutton" :
        responce_message = tk.Label(root, wraplength = 120, text="highlighting closebutton")
        button_flash(close_button)
        root.after(800, lambda: button_flash(close_button))
    
    if user_input == "highlight checkbutton":
        responce_message = tk.Label(root, wraplength = 120, text="highlighting checkbutton")
        button_flash(check_button)
        root.after(800, lambda: button_flash(check_button))
        
    if user_input == "Pedro" or user_input == 'pedro':
        open_popup_window()
        responce_message = tk.Label(root, wraplength = 50, text="Pedro, pedro, pedro")
    
    responce_message.place(x = 10, y = 151)



# Create a close button
close_button = tk.Button(root, text="Close", command=on_close, state=tk.DISABLED)
close_button.place(x = windx0/2, y = windy0/4)

# Create a check button
check_button = tk.Checkbutton(root, text="Really?", command=on_check, variable=var)
check_button.pack(pady=20)

# Create a Label widget to display text
label = tk.Label(root, text="Close me, please.")
label.place(x = windx0/2, y = windy0/2)

# Create an entry widget
text_box = tk.Entry(root, text = "Feel free to type things in here")
text_box.place(x = 10, y = 100)
# Create a button for the entry widget
submit_button = tk.Button(root, text="Submit", command = text_box_entry)
submit_button.place(x = 45, y = 121)

#gif image
gif_file =r"C:\Users\wbwin\OneDrive\Pictures\pedro-racoon.gif"

class GifPlayer:
    def __init__(self, canvas, gif_file):
        self.canvas = canvas
        self.gif_file = gif_file
        self.frames = []
        self.current_frame = 0
        
        # Load frames
        self.load_frames()
        
        # Display the first frame
        self.image_id = canvas.create_image(0, 0, anchor=tk.NW, image=self.frames[0])
        self.update_gif()

    def load_frames(self):
        """Load and cache all frames of the GIF."""
        with Image.open(self.gif_file) as img:
            try:
                while True:
                    frame = ImageTk.PhotoImage(img.copy())
                    self.frames.append(frame)
                    img.seek(img.tell() + 1)
            except EOFError:
                pass  # End of GIF

    def update_gif(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.canvas.itemconfig(self.image_id, image=self.frames[self.current_frame])
        self.canvas.after(25, self.update_gif)  # Update every 25 ms



#update on tick
update_counter()

# Run the application
root.mainloop()