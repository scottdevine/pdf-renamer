# Creating a macOS Application for PDF Renamer

This document explains how to create a standalone macOS application (.app) for the PDF Renamer GUI that can be added to your Dock.

## Method 1: Using py2app (Recommended)

This method creates a standalone application that doesn't require Python to be installed.

### Prerequisites

Install py2app:

```bash
pip install py2app
```

### Building the Application

1. Navigate to the pdf-renamer directory:

```bash
cd /path/to/pdf-renamer
```

2. Create an icon file (optional):

You'll need an .icns file for the application icon. You can convert a PNG to ICNS using:

```bash
# Install the required tool
brew install makeicns

# Convert a PNG to ICNS
makeicns -in your_icon.png -out pdf_renamer_icon.icns
```

3. Build the application:

```bash
# For development/testing (faster build, but requires Python)
python setup_app.py py2app -A

# For production (standalone app, doesn't require Python)
python setup_app.py py2app
```

4. The application will be created in the `dist` folder. You can drag it to your Applications folder and/or Dock.

## Method 2: Using AppleScript (Simple)

This method creates a simple launcher that requires Python and the pdf-renamer package to be installed.

1. Open Script Editor (Applications > Utilities > Script Editor)
2. Paste the following code:

```applescript
do shell script "cd /Users/scottdevine/Documents/GitHub/pdf-renamer && python pdf_renamer_gui.py"
```

3. Replace the path with the actual path to your pdf-renamer directory
4. Save as an Application (.app) with a name like "PDF Renamer"
5. Drag the saved .app file to your Dock

## Customizing the Icon

To change the icon of your AppleScript application:

1. Find an icon you want to use (PNG or ICNS format)
2. In Finder, select the icon file and press Cmd+C to copy it
3. Select your application, press Cmd+I to open the Info panel
4. Click on the small icon in the top-left corner of the Info panel
5. Press Cmd+V to paste the new icon
6. Close the Info panel
