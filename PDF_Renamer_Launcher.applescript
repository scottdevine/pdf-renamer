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
