# PDF Renamer macOS Application

This document explains how to create a macOS application for PDF Renamer that you can add to your Dock for easy access.

## Creating the Application

### Method 1: Using the Provided Script (Recommended)

1. Open Terminal
2. Navigate to the pdf-renamer directory:
   ```bash
   cd /path/to/pdf-renamer
   ```
3. Run the create_app.sh script:
   ```bash
   ./create_app.sh
   ```
4. The application will be created in the `dist` folder

### Method 2: Manual Creation

If you prefer to create the application manually:

1. Open Terminal
2. Navigate to the pdf-renamer directory:
   ```bash
   cd /path/to/pdf-renamer
   ```
3. Run the following command to create the application in development mode:
   ```bash
   python setup_app.py py2app -A
   ```
4. The application will be created in the `dist` folder

## Adding to Dock

1. Open Finder and navigate to the `dist` folder in your pdf-renamer directory
2. Drag the "PDF Renamer.app" to your Dock
3. You can now launch PDF Renamer by clicking this icon in your Dock

## Adding to Applications Folder

1. Open Finder and navigate to the `dist` folder in your pdf-renamer directory
2. Drag the "PDF Renamer.app" to your Applications folder
3. You can now launch PDF Renamer from Launchpad or Spotlight

## Troubleshooting

- If the application doesn't launch, try running it from Terminal to see any error messages:
  ```bash
  open "/path/to/pdf-renamer/dist/PDF Renamer.app"
  ```
- If you encounter issues, try rebuilding the application:
  ```bash
  rm -rf build dist
  python setup_app.py py2app -A
  ```
- Make sure all required Python packages are installed:
  ```bash
  pip install -r requirements.txt
  ```

## Notes

- The application is created in "development mode," which means it links to your Python installation rather than bundling Python with the application. This makes the application smaller and more reliable.
- If you update the PDF Renamer code, you'll need to rebuild the application.
- The application will only work on the computer where it was created unless you create a standalone application (which is more complex and prone to issues).
