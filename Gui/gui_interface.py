import tkinter as tk
from tkinter import ttk, messagebox

from metadata.fetch_metadata_db import fetch_db
from metadata.delete_from_db import delete_db
from metadata.download import download_video

from utils.logger import logger 

def start_gui():
    root = tk.Tk() # Create the main window
    root.title("Video Metadata Manager") # Set the window title
    root.geometry("600x450") # Set the window size
    
    tk.Label(root, text="Search by Keyword", font=("Arial", 16)).pack(pady=10) # Creates a label (text on the window)
    
    keyword_var = tk.StringVar() # Creates a special variable like a box to store text entered by the user
    tk.Entry(root, textvariable=keyword_var, width=50).pack(pady=10) # Adds an input box where user can type a word
    # Input box is connected to keyword_var so we can see what user types
    
    result_box = tk.Listbox(root, width=80, height=10) # Creates a Listbox where search results will be shown.
    result_box.pack(pady=10) # Adds the Listbox to the window with some padding
    
    # Define search logic
    def search():
        keyword = keyword_var.get().lower() # gets text from the input field
        result_box.delete(0, tk.END) # Delete old results - clear listbox before showing results
        
        data = fetch_db()
        for row in data:
            title = row[1]
            id = row[0]
            if keyword in title.lower():
                result_box.insert(tk.END, f"🎥 {id} | {title} | Duration: {row[2]} | Format: {row[3]}") # tk.END means add it to end of the list
        logger.info(f"Search completed for keyword: {keyword}") # Log the search action
        
    def delete():
        selected = result_box.curselection() # Get the index of the selected item in the Listbox # It is a tuple of selected items
        if not selected:
            messagebox.showwarning("No Selection", "Please select a video to delete.")
            return
        
        # Need to fetch id from the selected item to call delete function
        selected_text = result_box.get(selected[0]) # fetch the selected text - select first item from selected tuple
        id = selected_text.split('|')[0].replace("🎥","").strip() # Extract the title from whole line
        
        # Call delete function
        delete_count = delete_db(id)
        if delete_count > 0:
            messagebox.showinfo("Success", f"✅ Deleted {delete_count} video(s) with ID: {id}.")
            search() # Refresh list
        else:
            messagebox.showerror("Error", f"❌ No video found with ID: {id}.")
        logger.info(f"Delete action performed for ID: {id}") # Log the delete action
        
    def download():
        selection = result_box.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a video to download.")
            return
        
        # fetch the selected text and extract id from it
        selected_text = result_box.get(selection[0])
        id = selected_text.split("|")[0].replace("🎥", "").strip()
        
        # Now we need to fetch url from looking into db with help of id to download
        data = fetch_db()
        print("Data:", data)
        url = None
        
        for row in data:
            if str(row[0]) == id:
                url = row[4]
                break
            
        if not url:
            print("❌ No URL found for the selected video.")
            return
        
        # download the video
        try:
            download_video(url)
            messagebox.showinfo("Success", f"✅ Downloaded video with ID: {id}.")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Failed to download video: {str(e)}")
            logger.error(f"Failed to download video with ID: {id}. Error: {str(e)}")
        logger.info(f"Download action performed for ID: {id}")
        
    def clear_all():
        logger.info("Clearing all results from the listbox.")
        result_box.delete(0, tk.END) # Delete old results - clear listbox before showing results
        keyword_var.set("")
    
    # search() # so user dont see empty list
    tk.Button(root, text="Search", command=search).pack()
    tk.Button(root, text="Delete Selected", command=delete).pack()
    tk.Button(root, text="Download Selected Video", command=download).pack()
    tk.Button(root, text="Clear Results", command=clear_all).pack() # Button to clear results
    
    root.mainloop() # Start the GUI event loop so it waits for user actions