import pandas as pd
import tkinter as tk
from tkinter import ttk


def search():
    search_query = entry.get().lower()
    # Read Excel file
    df = pd.read_excel('data.xlsx')
    # Filter relevant entries based on search query
    filtered_df = df[df['Product Name'].str.lower().str.contains(search_query)]
    # Get the relevant product codes as a list
    results = filtered_df['Product Code'].tolist()

    # Update the drop-down list with relevant results
    combo['values'] = results


# Create the main window
window = tk.Tk()
window.title("Product Search")

# Create a label and entry for search input
label = tk.Label(window, text="Search:")
label.pack()
entry = tk.Entry(window)
entry.pack()
entry.focus()

# Create a drop-down list for displaying results
combo = ttk.Combobox(window)
combo.pack()

# Create a button to trigger the search
button = tk.Button(window, text="Search", command=search)
button.pack()

window.mainloop()
