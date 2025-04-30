#!/bin/bash
# Simple launcher script for PDF Renamer GUI

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Change to the script directory
cd "$SCRIPT_DIR"

# Launch the PDF Renamer GUI
python pdf_renamer_gui.py
