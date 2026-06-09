import tkinter as tk
import pyautogui

class Countdown:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)          # Bez okrajov
        self.root.attributes('-topmost', True)    # Vždy na vrchu
        self.root.attributes('-alpha', 0.9)       # Mierne priehľadné

        # Získanie rozlíšenia obrazovky
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Veľkosť okna = 70 % rozlíšenia
        width = int(screen_width * 0.7)
        height = int(screen_height * 0.7)
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # ----- Vytvorenie rozloženia -----
        main_frame = tk.Frame(self.root, bg="black")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Ľavá časť (centrovaný countdown)
        left_frame = tk.Frame(main_frame, bg="black")
        left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Pravá časť (ikona stopy)
        right_frame = tk.Frame(main_frame, bg="black", width=100)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=20)
        right_frame.pack_propagate(False)   # zachovať šírku 100 px

        # Center frame pre hlavný label a malý label (odpočet dole)
        center_frame = tk.Frame(left_frame, bg="black")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Veľkosť písma – prispôsobí sa menšiemu rozmeru okna
        font_size = min(width, height) // 4
        self.main_label = tk.Label(center_frame, text="", font=("Arial", font_size, "bold"),
                                   bg="black", fg="white")
        self.main_label.pack()

        # Malý text pod hlavným číslom (zobrazuje zostávajúce sekundy)
        small_font = max(12, font_size // 4)
        self.small_label = tk.Label(center_frame, text="", font=("Arial", small_font),
                                    bg="black", fg="gray")
        self.small_label.pack(pady=20)

        # Jedna ikona stopy na pravej strane (👣 - dve chodidlá)
        foot_font = max(30, font_size // 2)
        self.foot = tk.Label(right_frame, text="👣", font=("Arial", foot_font),
                             bg="black", fg="white")
        self.foot.pack(expand=True)

        self.count = 3   # ZMENENÉ z 5 na 3 sekundy
        self.update_countdown()
        self.root.after(4000, self.finish)   # 3 sekundy odpočet + 0.5s GO = cca 3.5s, rezerva 4s

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
        pyautogui.click()   # Ľavý klik na aktuálnej pozícii kurzora

    def finish(self):
        # Bezpečnostné ukončenie
        try:
            self.root.destroy()
            pyautogui.click()
        except:
            pass

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    Countdown().run()
