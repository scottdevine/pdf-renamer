# PDF Renamer GUI Implementation Plan

## Overview
A graphical user interface for the pdf-renamer tool using tkinter to provide an easy-to-use alternative to the command-line interface.

## Core Features

### 1. Main Window Layout
- Title: "PDF Renamer"
- Window size: 600x400
- Resizable interface
- Clean, modern styling using ttk widgets

### 2. Primary Components
- Source folder selection
  - Text entry field
  - Browse button
  - Directory dialog integration
- Output folder selection
  - Text entry field
  - Browse button
  - Directory dialog integration
- Filename format configuration
  - Text entry with default format
  - Format: "{YYYY} - {Jabbr} - {A3etal} - {T}"
- Progress indicators
  - Status text
  - Progress bar
- Log display area
  - Scrollable text window
  - Auto-scroll functionality
- Action buttons
  - Start Renaming
  - Clear Log

### 3. Core Functionality
- Threading implementation for non-blocking operations
- File processing status updates
- Error handling and validation
- Move renamed files to destination
- Progress tracking
- Detailed logging

## Implementation Details

### Class Structure
```python
class PDFRenamerGUI:
    def __init__(self, root)
    def browse_source()
    def browse_dest()
    def log(message)
    def clear_log()
    def rename_files()
    def validate_inputs()
    def start_renaming()
```

### Key Methods
- `browse_source()`: Handle source folder selection
- `browse_dest()`: Handle destination folder selection
- `log()`: Add messages to log window
- `clear_log()`: Clear log window
- `rename_files()`: Core renaming logic
- `validate_inputs()`: Input validation
- `start_renaming()`: Initiate renaming process

## Future Enhancements

### 1. User Interface Improvements
- Dropdown menu for common filename formats
- Checkboxes for additional options
  - Recursive folder processing
  - Force rename
  - Read-only mode
- Preview feature for renamed files
- Dark/light theme toggle
- Settings persistence

### 2. Additional Features
- Batch processing capabilities
- Custom format templates
- Format syntax helper
- File filtering options
- Undo/revert capability
- Export log functionality

### 3. User Experience
- Tooltips for format tags
- Format validation
- Error recovery options
- Progress estimation
- Operation cancellation
- Keyboard shortcuts

## Technical Requirements
- Python 3.x
- tkinter/ttk
- pdf-renamer >= 1.1
- pdf2doi >= 1.6
- Threading support
- File system access permissions

## Installation & Usage
1. Save as `pdf_renamer_gui.py`
2. Install dependencies:
   ```bash
   pip install pdf-renamer>=1.1 pdf2doi>=1.6
   ```
3. Run application:
   ```bash
   python pdf_renamer_gui.py
   ```

## Notes
- Maintain compatibility with existing pdf-renamer functionality
- Ensure proper error handling and user feedback
- Consider cross-platform compatibility
- Follow tkinter best practices
- Implement proper cleanup on exit