from Orange.widgets import widget, gui
from Orange.widgets.settings import Setting
from Orange.data import Table
from scipy.io import loadmat

class LoadData(widget.OWWidget):
    name = "Load Data"
    description = "Load data from a .mat file."
    icon = "icons/load_data.svg"  # You can use any SVG or remove this line for no icon.
    priority = 20

    # Inputs and Outputs
    inputs = [("File Path", str, "set_file_path")] # Receive the file path from the FileSelector widget
    outputs = [("MAT Data", dict)] # Send the loaded data

    # Settings
    file_path = Setting("") # Store the file path

    # User interface
    def __init__(self):
        super().__init__()
        self.mat_data = None # Store the loaded data

        # User interface
        gui.label(self.controlArea, self, "Load data from a .mat file:")
        self.info_label = gui.label(self.controlArea, self, "No file selected.")
        gui.button(self.controlArea, self, "Load Data", callback=self.load_data)

    def set_file_path(self, file_path):
        self.file_path = file_path
        self.info_label.setText(f"Selected file: {file_path}")

    def load_data(self):
        if self.file_path:
            try:
                self.mat_data = loadmat(self.file_path)
                self.info_label.setText("Data loaded successfully.")
                self.send("MAT Data", self.mat_data) # Send the loaded data
            except Exception as e:
                self.info_label.setText(f"Error loading file: {e}")
        else:
            self.info_label.setText("No file selected.")