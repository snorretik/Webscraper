# This is going to be my main Python Webcrawler
# ---------------------------
import tkinter as tk
import time
import requests
from tkinter import ttk
from bs4 import BeautifulSoup

# Setting up Main Window functionality:

root = tk.Tk()
root.title("My (own) Personal Crawler")
root.geometry("425x345")

helloLabel = ttk.Label(text="Enter a (valid) URL here:", padding=(0, 15, 0, 5))
helloLabel.pack()

urlTextInput = tk.Text(root, width=24, height=1)
urlTextInput.pack()

runButton = ttk.Button(root, text="Crawl", padding=(5, 5, 5, 5))
runButton.pack()

# Run a while loop here, displaying each passing URL:
# ----------------------

label1 = ttk.Label(text=f"first found url", padding=(0, 25, 0, 0))
label1.pack()
label2 = ttk.Label(text=f"second found url")
label2.pack()
label3 = ttk.Label(text=f"third found url")
label3.pack()
label4 = ttk.Label(text=f"fouth found url")
label4.pack()
label5 = ttk.Label(text=f"fifth found url")
label5.pack()
label6 = ttk.Label(text=f"sixth found url")
label6.pack()
label7 = ttk.Label(text=f"seventh found url")
label7.pack()
label8 = ttk.Label(text=f"eighth found url")
label8.pack()

root.mainloop()
