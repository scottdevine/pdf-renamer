#!/usr/bin/env python3
"""
Test script for the PDF Renamer GUI
"""

import sys
import os
import tkinter as tk

# Test if tkinter is available
try:
    root = tk.Tk()
    root.destroy()
    print("Tkinter is available.")
except Exception as e:
    print(f"Error initializing Tkinter: {str(e)}")
    sys.exit(1)

# Test if the GUI module can be imported
try:
    import pdf_renamer_gui
    print("PDF Renamer GUI module imported successfully.")
except Exception as e:
    print(f"Error importing PDF Renamer GUI module: {str(e)}")
    sys.exit(1)

# Test if the main function exists
try:
    if hasattr(pdf_renamer_gui, 'main') and callable(pdf_renamer_gui.main):
        print("PDF Renamer GUI main function exists.")
    else:
        print("PDF Renamer GUI main function not found.")
        sys.exit(1)
except Exception as e:
    print(f"Error checking PDF Renamer GUI main function: {str(e)}")
    sys.exit(1)

# Test if the PDFRenamerGUI class exists
try:
    if hasattr(pdf_renamer_gui, 'PDFRenamerGUI'):
        print("PDFRenamerGUI class exists.")
    else:
        print("PDFRenamerGUI class not found.")
        sys.exit(1)
except Exception as e:
    print(f"Error checking PDFRenamerGUI class: {str(e)}")
    sys.exit(1)

print("All tests passed. The PDF Renamer GUI should work correctly.")
