#!/bin/bash
# Script to create a macOS application for PDF Renamer

# Clean up previous builds
echo "Cleaning up previous builds..."
rm -rf build dist

# Create the application in development mode (faster and more reliable)
echo "Creating PDF Renamer application in development mode..."
python setup_app.py py2app -A

# Make sure the application is executable
echo "Setting permissions..."
chmod -R +x "dist/PDF Renamer.app"

echo "Done! The application is available at: dist/PDF Renamer.app"
echo "You can drag this application to your Applications folder or Dock."
