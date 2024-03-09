# This is going to be my main Python Webcrawler
# ---------------------------
import tkinter as tk
import time
import requests
from tkinter import ttk
from bs4 import BeautifulSoup

# Global variables:

# Setting up Main Functions:

# Setting up Main Window functionality:

root = tk.Tk()
root.title("My (own) Personal Crawler")
root.geometry("425x345")

helloLabel = ttk.Label(text="Enter a (valid) URL here:", padding=(0, 15, 0, 5))
helloLabel.pack()

urlTextInput = ttk.Entry(root)
urlTextInput.pack()

def settingLabelURL():
    label1 = ttk.Label(text=f"{urlTextInput.get()}")
    label1.pack()

runButton = ttk.Button(root, text="Crawl", command=settingLabelURL, padding=(5, 5, 5, 5))
runButton.pack()

# Run a while loop here, displaying each passing URL:
# ----------------------


root.mainloop()
