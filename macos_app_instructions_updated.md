# Creating a macOS Dock Icon for PDF Renamer

This guide explains how to create a macOS application that you can add to your Dock for easy access to the PDF Renamer GUI.

## Method 1: Using AppleScript (Recommended)

### Step 1: Open Script Editor

1. Open **Script Editor** (you can find it in Applications > Utilities or search for it in Spotlight)
2. Copy and paste the following code:

```applescript
-- PDF Renamer Launcher
-- This script launches the PDF Renamer GUI application

-- Get the path to the pdf-renamer directory
set pdfRenamerPath to "/Users/scottdevine/Documents/GitHub/pdf-renamer"

-- Launch the PDF Renamer GUI
tell application "Terminal"
    do script "cd " & quoted form of pdfRenamerPath & " && python pdf_renamer_gui.py"
    delay 1
    set miniaturized of front window to true
end tell

-- Display a notification
display notification "PDF Renamer GUI has been launched." with title "PDF Renamer"
```

3. **Important**: Replace `/Users/scottdevine/Documents/GitHub/pdf-renamer` with the actual path to your pdf-renamer directory.

### Step 2: Save as Application

1. Click **File > Save**
2. Choose a name (e.g., "PDF Renamer")
3. Select **Application** as the File Format
4. Choose a location to save (e.g., Applications folder)
5. Click **Save**

### Step 3: Add to Dock

1. Find your newly created application in Finder
2. Drag it to the Dock
3. Now you can launch PDF Renamer by clicking this icon in your Dock

### Step 4: Customize the Icon (Optional)

1. Find an icon you want to use (PNG or ICNS format)
2. In Finder, select the icon file and press **Cmd+C** to copy it
3. Select your application, press **Cmd+I** to open the Info panel
4. Click on the small icon in the top-left corner of the Info panel
5. Press **Cmd+V** to paste the new icon
6. Close the Info panel

## Method 2: Using Automator (Alternative)

If you prefer not to see a Terminal window at all:

1. Open **Automator** (from Applications)
2. Create a new **Application**
3. Search for "Run Shell Script" and drag it to the workflow
4. Enter the following script:

```bash
cd /Users/scottdevine/Documents/GitHub/pdf-renamer
/usr/bin/python3 pdf_renamer_gui.py
```

5. Replace the path with your actual path to the pdf-renamer directory
6. Save as an Application
7. Drag to your Dock

## Troubleshooting

- If the application doesn't launch, check that the path in the script is correct
- Make sure Python and all required dependencies are installed
- If you see a Terminal window briefly open and close, it might indicate an error. Try running the command directly in Terminal to see the error message.
