import pandas as pd
import tkinter as tk
from tkinter import ttk, font

def search():
    search_query = entry.get().lower()
    # Read Excel file
    df = pd.read_excel('data.xlsx')
    # Filter relevant entries based on search query
    filtered_df = df[df['Product Name'].str.lower().str.contains(search_query)]
    # Get the relevant product names, codes, prices, and expiry dates as lists
    results = [f"{name} ({code})" for name, code in zip(filtered_df['Product Name'], filtered_df['Product Code'])]
    prices = filtered_df['Price'].tolist()
    codes = filtered_df['Product Code'].tolist()
    expiry_dates = filtered_df['Expiry Date'].tolist()  # Fetch the expiry dates

    # Update the drop-down list with relevant results
    combo['values'] = results

    # Clear the price, code, and expiry date boxes
    price_box.delete(1.0, tk.END)
    code_box.delete(1.0, tk.END)
    expiry_date_box.delete(1.0, tk.END)

    # Update the price, code, and expiry date boxes with the selected item's details
    if combo.current() != -1:
        selected_price = prices[combo.current()]
        selected_code = codes[combo.current()]
        selected_expiry_date = expiry_dates[combo.current()]  # Fetch the corresponding expiry date
        price_box.insert(tk.END, f"{selected_price}")
        code_box.insert(tk.END, f"{selected_code}")
        expiry_date_box.insert(tk.END, f"{selected_expiry_date}")  # Display the expiry date

# Create the main window
window = tk.Tk()
window.title("ANAND STORES STOCK SEARCH V1.2")

# Set the window to maximize
window.state('zoomed')

# Increase the font size
default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=20)

# Increase the font size for the drop-down list
combostyle = ttk.Style()
combostyle.configure('TCombobox', font=('TkDefaultFont', 20))
combostyle.configure('TCombobox.Listbox', font=('TkDefaultFont', 20))  # Set font size for the combobox list items

# Create empty labels for spacing
for _ in range(6):
    tk.Label(window, text="").pack()

# Create a label and entry for search input
label = tk.Label(window, text="Welcome! Please Enter Product Name to Search", font=('TkDefaultFont', 20))
label.pack()

# Create empty label for spacing
tk.Label(window, text="").pack()

entry = tk.Entry(window, width=40, font=('TkDefaultFont', 20))  # Set the width of the entry textbox
entry.pack()
entry.focus()

# Bind the Enter key to the search function
entry.bind('<Return>', lambda event: search())

# Create empty label for spacing
tk.Label(window, text="").pack()

# Create a button to trigger the search
button = tk.Button(window, text="Search Item", command=search, font=('TkDefaultFont', 20))
button.pack()

# Create empty label for spacing
tk.Label(window, text="").pack()

# Create a drop-down list for displaying results
combo = ttk.Combobox(window, style='TCombobox', width=40, font=('TkDefaultFont', 20))  # Set the width of the combobox
combo.pack()

# Configure the font size for the combobox list items
combo.bind("<<ComboboxSelected>>", lambda event: combo.configure(font=('TkDefaultFont', 20)))

# Create empty label for spacing
tk.Label(window, text="").pack()

# Create a button to trigger the search
button = tk.Button(window, text="Retrieve Data", command=search, font=('TkDefaultFont', 20))
button.pack()

# Create empty label for spacing
tk.Label(window, text="").pack()
tk.Label(window, text="").pack()  # Add one line spacing

# Create a frame for holding the price, product code, and expiry date boxes
frame = tk.Frame(window)
frame.pack()

# Create a label and text box for displaying the price
price_label = tk.Label(frame, text="Price:", font=('TkDefaultFont', 20))
price_label.pack(side=tk.LEFT)
price_box = tk.Text(frame, height=1, width=10, font=('TkDefaultFont', 20), bg='light green')
price_box.pack(side=tk.LEFT, padx=10)  # Add padx for spacing

# Create a label and text box for displaying the product code
code_label = tk.Label(frame, text="Product Code:", font=('TkDefaultFont', 20))
code_label.pack(side=tk.LEFT)
code_box = tk.Text(frame, height=1, width=10, font=('TkDefaultFont', 20), bg='light green')
code_box.pack(side=tk.LEFT, padx=10)  # Add padx for spacing

# Create a label and text box for displaying the expiry date
expiry_date_label = tk.Label(frame, text="Expiry Date:", font=('TkDefaultFont', 20))
expiry_date_label.pack(side=tk.LEFT, padx=10)  # Add padx for spacing
expiry_date_box = tk.Text(frame, height=1, width=10, font=('TkDefaultFont', 20), bg='light green')
expiry_date_box.pack(side=tk.LEFT)  # Remove unnecessary padx

window.mainloop()
