# This is going to be my main Python Webcrawler
# ---------------------------
import tkinter as tk
import time
import requests
from tkinter import ttk
from bs4 import BeautifulSoup

# Global variables:

collection_labels = []

# Setting up Main Functions:

# Setting up Main Window functionality:

root = tk.Tk()
root.title("My (own) Personal Crawler")
root.geometry("425x345")

helloLabel = ttk.Label(text="Enter a (valid) URL here:", padding=(0, 15, 0, 5))
helloLabel.pack()

urlTextInput = ttk.Entry(root)
urlTextInput.pack()

def packLabels():
    if len(collection_labels) > 0:
        for x in range(len(collection_labels)):
            collection_labels[x].pack()

def settingLabelURL():
    label = ttk.Label(text=f"{urlTextInput.get()}")
    
    try:
        collection_labels[9].destroy()
        del(collection_labels[9])
        collection_labels.insert(0, label)
    except:
        collection_labels.insert(0, label)

    packLabels() 

runButton = ttk.Button(root, text="Crawl", command=settingLabelURL, padding=(5, 5, 5, 5))
runButton.pack()

labelEmpty = ttk.Label(root, text=f"")
labelEmpty.pack()

labelOriginalInput = ttk.Label(root, text=f"{urlTextInput.get()}")
labelOriginalInput.pack()

# Run a while loop here, displaying each passing URL:
# ----------------------


root.mainloop()
