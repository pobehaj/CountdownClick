import tkinter as tk
import pyautogui

class Countdown:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.9)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        width = int(screen_width * 0.7)
        height = int(screen_height * 0.7)
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Hlavný rám (čierne pozadie)
        main_frame = tk.Frame(self.root, bg="black")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Centrovaný obsah (vertikálne aj horizontálne)
        center_frame = tk.Frame(main_frame, bg="black")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Malý text odpočtu (NAD veľkým číslom) - zmenšený a tmavší
        font_size_small = min(width, height) // 32   # ešte menšie ako predtým
        self.small_label = tk.Label(center_frame, text="", font=("Arial", font_size_small),
                                    bg="black", fg="#333333")   # tmavosivá (takmer čierna)
        self.small_label.pack(pady=(0, 10))

        # Veľké číslo
        big_font = min(width, height) // 4
        self.main_label = tk.Label(center_frame, text="", font=("Arial", big_font, "bold"),
                                   bg="black", fg="white")
        self.main_label.pack()

        # Spodný rám pre nohy (úplne dole)
        bottom_frame = tk.Frame(main_frame, bg="black", height=80)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        bottom_frame.pack_propagate(False)

        # Dve nohy na spodnom riadku, zarovnané ÚPLNE VPRAVO
        foot_font = max(30, min(width, height) // 10)
        self.foot_label = tk.Label(bottom_frame, text=">>👣", font=("Arial", foot_font),
                                   bg="black", fg="white")
        self.foot_label.pack(side=tk.RIGHT, padx=20)   # RIGHT + malý odstup od okraja

        self.count = 3
        self.update_countdown()
        self.root.after(4000, self.finish)

    def update_countdown(self):
        if self.count > 0:
            self.main_label.config(text=str(self.count))
            self.small_label.config(text=f"Odpočet: {self.count} s")
            self.count -= 1
            self.root.after(1000, self.update_countdown)
        else:
            self.main_label.config(text="GO!")
            self.small_label.config(text="Štart!")
            self.root.after(500, self.click_and_exit)

    def click_and_exit(self):
        self.root.destroy()
        pyautogui.click()

    def finish(self):
        try:
            self.root.destroy()
            pyautogui.click()
        except:
            pass

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    Countdown().run()
