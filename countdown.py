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

        # Veľkosť okna = 90 % rozlíšenia
        width = int(screen_width * 0.7)
        height = int(screen_height * 0.7)
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Veľkosť písma – prispôsobí sa menšiemu rozmeru okna
        font_size = min(width, height) // 4
        self.label = tk.Label(self.root, text="", font=("Arial", font_size, "bold"),
                              bg="black", fg="white")
        self.label.pack(expand=True, fill=tk.BOTH)

        self.count = 5
        self.update_countdown()
        self.root.after(6000, self.finish)   # 5..1 + GO = cca 6 sekúnd

    def update_countdown(self):
        if self.count > 0:
            self.label.config(text=str(self.count))
            self.count -= 1
            self.root.after(1000, self.update_countdown)
        else:
            self.label.config(text="GO!")
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
