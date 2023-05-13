import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from Searchengine import search

class SearchEngineGUI:
    def __init__(self, master):
        self.master = master
        master.title("Search Engine")
        master.geometry("500x400")
        master.configure(bg="#f0f0f0")

        # Header
        self.header_frame = tk.Frame(master, bg="#000080", pady=20)
        self.header_frame.pack(fill=tk.X)

        self.logo_label = tk.Label(self.header_frame, text="Search Engine", font=("Arial Bold", 20), fg="white", bg="#000080")
        self.logo_label.pack(side=tk.LEFT, padx=20)

        # Query entry
        self.query_frame = tk.Frame(master, bg="#f0f0f0", padx=20, pady=20)
        self.query_frame.pack(fill=tk.X)

        self.label = tk.Label(self.query_frame, text="Enter your query:", font=("Arial", 14), bg="#f0f0f0")
        self.label.pack(side=tk.LEFT)

        self.query_entry = tk.Entry(self.query_frame, font=("Arial", 14), width=30, bd=2, relief="groove")
        self.query_entry.pack(side=tk.LEFT, padx=10)

        self.search_button = tk.Button(self.query_frame, text="Search", font=("Arial", 14), bg="#000080", fg="white", bd=2, relief="groove", command=self.search_button_clicked)
        self.search_button.pack(side=tk.LEFT, padx=10)

    def search_button_clicked(self):
        query = self.query_entry.get()
        if query:
            results = search(query)
            if results:
                self.display_results(results)
            else:
                messagebox.showinfo("No Results", "No results found for your query")
        else:
            messagebox.showinfo("Empty Query", "Please enter a query")

    def display_results(self, results):
        self.results_window = tk.Toplevel(self.master)
        self.results_window.title("Search Results")

        self.results_text = scrolledtext.ScrolledText(self.results_window, width=80, height=30, font=("Arial", 12))
        self.results_text.pack(fill=tk.BOTH, expand=True)

        for result in results:
            self.results_text.insert(tk.END, result + "\n")

root = tk.Tk()
gui = SearchEngineGUI(root)
root.mainloop()