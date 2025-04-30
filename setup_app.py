"""
This is a setup.py script to create a standalone macOS application
for the PDF Renamer GUI using py2app.
"""

from setuptools import setup

APP = ['pdf_renamer_gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pdfrenamer', 'pdf2bib', 'pdf2doi'],
    'iconfile': 'pdf_renamer_icon.icns',
    'plist': {
        'CFBundleName': 'PDF Renamer',
        'CFBundleDisplayName': 'PDF Renamer',
        'CFBundleIdentifier': 'com.scottdevine.pdfrenamer',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
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
