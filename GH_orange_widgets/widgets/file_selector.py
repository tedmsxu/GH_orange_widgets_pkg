from Orange.widgets import widget, gui
from Orange.widgets.settings import Setting
from Orange.widgets.utils.filedialogs import open_filename_dialog
from Orange.data import Table

class FileSelector(widget.OWWidget):
    name = "File Selector"
    description = "Select a .mat file to load."
    icon = "icons/file_selector.svg"  # You can use any SVG or remove this line for no icon.
    priority = 10 

    # Outputs
    outputs = [("File Path", str)]

    # Settings
    file_path = Setting("") # Default value

    def __init__(self):
        super().__init__()

        # User interface
        self.controlArea.layout().addWidget(gui.label(self.controlArea, self, "Select a .mat file:"))
        gui.button(self.controlArea, self, "Browse", callback=self.browse_file)
        self.file_label = gui.label(self.controlArea, self, self.file_path)

    def browse_file(self):
        # Open file dialog
        file_path, _ = open_filename_dialog(None, "Select a .mat file", start_dir=".", file_filter="MAT files (*.mat)")
        if file_path:
            self.file_path = file_path # Update the setting
            self.file_label.setText(file_path) # Update the label
            self.send("File Path", file_path) # Send the output