"""
This is a setup.py script to create a standalone macOS application
for the PDF Renamer GUI using py2app.
"""

from setuptools import setup

APP = ['pdf_renamer_gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,  # Changed to False to avoid potential issues
    'packages': ['pdfrenamer', 'pdf2bib', 'pdf2doi'],
    # 'iconfile': 'pdf_renamer_icon.icns',  # Commented out until we have an icon
    'includes': ['tkinter', 'queue', 'threading', 'shutil', 'os'],  # Explicitly include required modules
    'excludes': ['matplotlib', 'numpy', 'scipy', 'pandas'],  # Exclude large packages
    'frameworks': [],  # No additional frameworks needed
    'site_packages': True,  # Include site-packages
    'resources': [],  # No additional resources
    'strip': True,  # Strip debug symbols to reduce size
    'optimize': 0,  # No bytecode optimization to avoid issues
    'semi_standalone': True,  # Use system Python if available
    'plist': {
        'CFBundleName': 'PDF Renamer',
        'CFBundleDisplayName': 'PDF Renamer',
        'CFBundleIdentifier': 'com.scottdevine.pdfrenamer',
        'CFBundleVersion': '1.1.1',
        'CFBundleShortVersionString': '1.1.1',
        'NSHumanReadableCopyright': 'Copyright © 2023 Scott Devine',
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeName': 'PDF Document',
                'CFBundleTypeExtensions': ['pdf'],
                'CFBundleTypeRole': 'Viewer',
            }
        ]
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
