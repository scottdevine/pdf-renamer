#!/usr/bin/env python3
"""
PDF Renamer GUI (Mock Version)
--------------
A simplified mock version of the PDF Renamer GUI to demonstrate the concept.
"""

import os
import sys
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import threading
import queue
import time

class PDFRenamerGUIMock:
    def __init__(self, root):
        """Initialize the GUI components"""
        self.root = root
        self.root.title("PDF Renamer (Mock)")
        self.root.geometry("600x400")
        self.root.minsize(600, 400)
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", padding=6)
        self.style.configure("TLabel", background="#f0f0f0")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create and place widgets
        self._create_source_selection()
        self._create_dest_selection()
        self._create_format_config()
        self._create_options_frame()
        self._create_progress_indicators()
        self._create_log_area()
        self._create_action_buttons()
        
        # Initialize variables
        self.processing = False
        self.process_thread = None
        self.queue = queue.Queue()
        
        # Start queue processing
        self._process_queue()
        
        # Log initial message
        self.log("PDF Renamer GUI started (MOCK VERSION). Select source and destination folders to begin.")
        self.log("Note: This is a mock version for demonstration purposes only.")
        self.log("The actual implementation will integrate with the pdf-renamer library.")
    
    def _create_source_selection(self):
        """Create source folder selection components"""
        source_frame = ttk.Frame(self.main_frame)
        source_frame.pack(fill=tk.X, pady=5)
        
        source_label = ttk.Label(source_frame, text="Source Folder:")
        source_label.pack(side=tk.LEFT, padx=5)
        
        self.source_var = tk.StringVar()
        source_entry = ttk.Entry(source_frame, textvariable=self.source_var, width=50)
        source_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        source_button = ttk.Button(source_frame, text="Browse...", command=self.browse_source)
        source_button.pack(side=tk.RIGHT, padx=5)
    
    def _create_dest_selection(self):
        """Create destination folder selection components"""
        dest_frame = ttk.Frame(self.main_frame)
        dest_frame.pack(fill=tk.X, pady=5)
        
        dest_label = ttk.Label(dest_frame, text="Output Folder:")
        dest_label.pack(side=tk.LEFT, padx=5)
        
        self.dest_var = tk.StringVar()
        dest_entry = ttk.Entry(dest_frame, textvariable=self.dest_var, width=50)
        dest_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        dest_button = ttk.Button(dest_frame, text="Browse...", command=self.browse_dest)
        dest_button.pack(side=tk.RIGHT, padx=5)
    
    def _create_format_config(self):
        """Create filename format configuration components"""
        format_frame = ttk.Frame(self.main_frame)
        format_frame.pack(fill=tk.X, pady=5)
        
        format_label = ttk.Label(format_frame, text="Filename Format:")
        format_label.pack(side=tk.LEFT, padx=5)
        
        self.format_var = tk.StringVar(value="{YYYY} - {Jabbr} - {A3etal} - {T}")
        format_entry = ttk.Entry(format_frame, textvariable=self.format_var, width=50)
        format_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
    
    def _create_options_frame(self):
        """Create options frame with checkboxes"""
        options_frame = ttk.Frame(self.main_frame)
        options_frame.pack(fill=tk.X, pady=5)
        
        # Recursive processing checkbox
        self.recursive_var = tk.BooleanVar(value=False)
        recursive_check = ttk.Checkbutton(
            options_frame, 
            text="Process Subfolders", 
            variable=self.recursive_var
        )
        recursive_check.pack(side=tk.LEFT, padx=5)
        
        # Force rename checkbox
        self.force_rename_var = tk.BooleanVar(value=True)
        force_check = ttk.Checkbutton(
            options_frame, 
            text="Force Rename", 
            variable=self.force_rename_var
        )
        force_check.pack(side=tk.LEFT, padx=5)
        
        # Read-only mode checkbox
        self.readonly_var = tk.BooleanVar(value=False)
        readonly_check = ttk.Checkbutton(
            options_frame, 
            text="Read-only Mode", 
            variable=self.readonly_var
        )
        readonly_check.pack(side=tk.LEFT, padx=5)
    
    def _create_progress_indicators(self):
        """Create progress indicators"""
        progress_frame = ttk.Frame(self.main_frame)
        progress_frame.pack(fill=tk.X, pady=5)
        
        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(progress_frame, textvariable=self.status_var)
        status_label.pack(side=tk.LEFT, padx=5)
        
        self.progress = ttk.Progressbar(progress_frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.progress.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=5)
    
    def _create_log_area(self):
        """Create log display area"""
        log_frame = ttk.LabelFrame(self.main_frame, text="Log")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD, height=10)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.log_text.config(state=tk.DISABLED)
    
    def _create_action_buttons(self):
        """Create action buttons"""
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(fill=tk.X, pady=5)
        
        self.start_button = ttk.Button(button_frame, text="Start Renaming", command=self.start_renaming)
        self.start_button.pack(side=tk.RIGHT, padx=5)
        
        clear_button = ttk.Button(button_frame, text="Clear Log", command=self.clear_log)
        clear_button.pack(side=tk.RIGHT, padx=5)
    
    def browse_source(self):
        """Handle source folder selection"""
        folder = filedialog.askdirectory(title="Select Source Folder")
        if folder:
            self.source_var.set(folder)
            # If destination is empty, set it to the same as source
            if not self.dest_var.get():
                self.dest_var.set(folder)
    
    def browse_dest(self):
        """Handle destination folder selection"""
        folder = filedialog.askdirectory(title="Select Destination Folder")
        if folder:
            self.dest_var.set(folder)
    
    def log(self, message):
        """Add message to log window"""
        self.queue.put(("log", message))
    
    def clear_log(self):
        """Clear log window"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)
    
    def validate_inputs(self):
        """Validate user inputs"""
        source = self.source_var.get()
        dest = self.dest_var.get()
        format_str = self.format_var.get()
        
        if not source:
            self.log("Error: Source folder is required")
            return False
        
        if not os.path.exists(source):
            self.log(f"Error: Source folder '{source}' does not exist")
            return False
        
        if not dest:
            self.log("Error: Destination folder is required")
            return False
        
        if not os.path.exists(dest):
            self.log(f"Error: Destination folder '{dest}' does not exist")
            return False
        
        # Validate format string
        if not format_str:
            self.log("Error: Filename format is required")
            return False
        
        return True
    
    def start_renaming(self):
        """Initiate renaming process"""
        if self.processing:
            self.log("Already processing files. Please wait...")
            return
        
        if not self.validate_inputs():
            return
        
        # Update UI state
        self.processing = True
        self.start_button.config(state=tk.DISABLED)
        self.status_var.set("Processing...")
        self.progress['value'] = 0
        
        # Start processing thread
        self.process_thread = threading.Thread(
            target=self.mock_rename_files,
            args=(
                self.source_var.get(),
                self.dest_var.get(),
                self.format_var.get()
            )
        )
        self.process_thread.daemon = True
        self.process_thread.start()
    
    def mock_rename_files(self, source, dest, format_str):
        """Mock renaming logic - runs in a separate thread"""
        try:
            self.log(f"Starting mock renaming process...")
            self.log(f"Source: {source}")
            self.log(f"Destination: {dest}")
            self.log(f"Format: {format_str}")
            
            # Simulate processing
            self.queue.put(("progress", 10))
            self.log("Scanning for PDF files...")
            time.sleep(1)
            
            # Find PDF files in the source directory
            pdf_files = [f for f in os.listdir(source) if f.lower().endswith('.pdf')]
            num_files = len(pdf_files)
            
            if num_files == 0:
                self.log("No PDF files found in the source directory.")
                self.queue.put(("status", "No files found"))
                self.queue.put(("complete", None))
                return
            
            self.log(f"Found {num_files} PDF file(s)")
            self.queue.put(("progress", 20))
            time.sleep(0.5)
            
            # Simulate processing each file
            for i, pdf_file in enumerate(pdf_files):
                progress = 20 + int(70 * (i + 1) / num_files)
                self.queue.put(("progress", progress))
                
                self.log(f"Processing: {pdf_file}")
                time.sleep(0.5)
                
                # Simulate successful rename for some files, failures for others
                if i % 3 == 0:
                    new_name = f"2023 - Journal - Author et al - Sample Paper {i+1}.pdf"
                    self.log(f"Renamed: {pdf_file} -> {new_name}")
                else:
                    self.log(f"Could not find identifier for: {pdf_file}")
            
            self.queue.put(("progress", 100))
            self.queue.put(("status", f"Processed {num_files} file(s)"))
            self.log("Mock renaming process completed.")
            self.queue.put(("complete", None))
            
        except Exception as e:
            self.queue.put(("log", f"Error: {str(e)}"))
            self.queue.put(("status", "Error occurred"))
            self.queue.put(("complete", None))
    
    def _process_queue(self):
        """Process messages from the queue"""
        try:
            while not self.queue.empty():
                message_type, message = self.queue.get(block=False)
                
                if message_type == "log":
                    # Add message to log
                    self.log_text.config(state=tk.NORMAL)
                    self.log_text.insert(tk.END, message + "\n")
                    self.log_text.see(tk.END)  # Auto-scroll to the end
                    self.log_text.config(state=tk.DISABLED)
                
                elif message_type == "progress":
                    # Update progress bar
                    self.progress['value'] = message
                
                elif message_type == "status":
                    # Update status text
                    self.status_var.set(message)
                
                elif message_type == "complete":
                    # Processing complete
                    self.processing = False
                    self.start_button.config(state=tk.NORMAL)
                    self.progress['value'] = 100
        except queue.Empty:
            pass
        
        # Schedule to run again
        self.root.after(100, self._process_queue)


def main():
    """Main entry point for the application"""
    root = tk.Tk()
    app = PDFRenamerGUIMock(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (root.quit(), root.destroy()))
    root.mainloop()


if __name__ == "__main__":
    main()
