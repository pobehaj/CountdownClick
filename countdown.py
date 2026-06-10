import tkinter as tk
import pyautogui

class Countdown:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.9)

        # Force focus and grab keyboard events
        self.root.focus_force()
        self.root.grab_set()  # Zablokuje vstupy pre iné okná, kým beží toto

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        width = int(screen_width * 0.7)
        height = int(screen_height * 0.7)
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Main frame (black background)
        main_frame = tk.Frame(self.root, bg="black")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Centered content
        center_frame = tk.Frame(main_frame, bg="black")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        font_size_small = min(width, height) // 32
        self.small_label = tk.Label(center_frame, text="", font=("Arial", font_size_small),
                                    bg="black", fg="#333333")
        self.small_label.pack(pady=(0, 10))

        big_font = min(width, height) // 4
        self.main_label = tk.Label(center_frame, text="", font=("Arial", big_font, "bold"),
                                   bg="black", fg="white")
        self.main_label.pack()

        bottom_frame = tk.Frame(main_frame, bg="black", height=80)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        bottom_frame.pack_propagate(False)

        foot_font = max(30, min(width, height) // 10)
        self.foot_label = tk.Label(bottom_frame, text=">>👣", font=("Arial", foot_font),
                                   bg="black", fg="white")
        self.foot_label.pack(side=tk.RIGHT, padx=20)

        self.count = 5
        self.paused = False
        self.after_id = None

        # Bind space on root AND main frame for safety
        self.root.bind('<space>', self.toggle_pause)
        main_frame.bind('<space>', self.toggle_pause)
        self.root.bind('<Escape>', lambda e: self.quit())  # Esc for emergency exit

        # Show initial "PAUSED" text when paused? We'll add a small indicator.
        self.pause_label = tk.Label(center_frame, text="", font=("Arial", font_size_small),
                                    bg="black", fg="yellow")
        self.pause_label.pack(pady=(10, 0))

        self.update_countdown()

    def toggle_pause(self, event=None):
        if self.count <= 0:
            return
        if self.paused:
            self.paused = False
            self.pause_label.config(text="")
            self.update_countdown()
        else:
            self.paused = True
            self.pause_label.config(text="⏸ PAUSED (space to resume)")
            if self.after_id:
                self.root.after_cancel(self.after_id)
                self.after_id = None

    def update_countdown(self):
        if self.paused:
            return

        if self.count > 0:
            self.main_label.config(text=str(self.count))
            self.small_label.config(text=f"Countdown: {self.count} s")
            self.count -= 1
            self.after_id = self.root.after(1000, self.update_countdown)
        else:
            self.main_label.config(text="GO!")
            self.small_label.config(text="Start!")
            self.after_id = self.root.after(500, self.click_and_exit)

    def click_and_exit(self):
        self.root.destroy()
        pyautogui.click()

    def quit(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    Countdown().run()
