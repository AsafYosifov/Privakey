from tkinter import Tk, Label
import requests
from bs4 import BeautifulSoup
from re import compile

URL = "https://check.torproject.org/"   # Target URL


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("DOK Status")

        self.label = Label(master, text="DOK Status", bg="red")  # Red = Disconnected color
        self.label.pack()

    def update_background_color(self):
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Check if the string 'Sorry. You are not using Tor.' exists on check.torproject.org
        not_using_tor_client = soup.findAll(text=compile('Sorry. You are not using Tor.'))
        # If it does exist, it means that the tor client isn't being used on the router
        # which means the DoK is disconnected.

        if not_using_tor_client:
            color = "red"   # Color the background red if the DoK is disconnected.
        else:
            color = "green" # Color the background green if the DoK is connected.

        self.label.configure(bg=color)
        # Repeat this function every 1,000 milliseconds (1 second)
        self.label.after(1000, self.update_background_color)


if __name__ == "__main__":
    root = Tk()
    root.attributes("-topmost", True)   # Keep the window always at the top of displayed windows
    my_gui = GUI(root)
    my_gui.update_background_color()
    root.mainloop()