#!/bin/bash
# Script to update the macOS application for PDF Renamer

# Get the current version from the setup_app.py file
CURRENT_VERSION=$(grep -o "CFBundleVersion': '[0-9.]*'" setup_app.py | cut -d "'" -f 2)
echo "Current version: $CURRENT_VERSION"

# Ask for the new version if not provided as an argument
if [ -z "$1" ]; then
    read -p "Enter new version number (leave blank to keep $CURRENT_VERSION): " NEW_VERSION
    if [ -z "$NEW_VERSION" ]; then
        NEW_VERSION=$CURRENT_VERSION
    fi
else
    NEW_VERSION=$1
fi

echo "Updating to version $NEW_VERSION..."

# Update the version numbers in setup_app.py
sed -i '' "s/'CFBundleVersion': '[0-9.]*'/'CFBundleVersion': '$NEW_VERSION'/g" setup_app.py
sed -i '' "s/'CFBundleShortVersionString': '[0-9.]*'/'CFBundleShortVersionString': '$NEW_VERSION'/g" setup_app.py

# Clean up previous builds
echo "Cleaning up previous builds..."
rm -rf build dist

# Create the application in development mode (faster and more reliable)
echo "Creating PDF Renamer application in development mode..."
python setup_app.py py2app -A

# Make sure the application is executable
echo "Setting permissions..."
chmod -R +x "dist/PDF Renamer.app"

echo "Done! The application has been updated to version $NEW_VERSION"
echo "The application is available at: dist/PDF Renamer.app"
echo "You can drag this application to your Applications folder or Dock."
