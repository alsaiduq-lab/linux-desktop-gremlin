import sys
import os
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QListWidget, 
                               QPushButton, QLabel)
from PySide6.QtCore import Qt

class GremlinPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gremlin Picker")
        self.resize(300, 400)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label = QLabel("Choose your Gremlin:")
        layout.addWidget(label)
        
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        
        # Populate list
        # Assumes this script is in src/ and spritesheet/ is in project root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        spritesheet_dir = os.path.join(base_dir, "spritesheet")
        
        if os.path.exists(spritesheet_dir):
            # List directories in spritesheet folder
            gremlins = sorted([
                d for d in os.listdir(spritesheet_dir) 
                if os.path.isdir(os.path.join(spritesheet_dir, d))
            ])
            for g in gremlins:
                self.list_widget.addItem(g)
        
        self.list_widget.itemDoubleClicked.connect(self.select_gremlin)
        
        btn = QPushButton("Launch")
        btn.clicked.connect(self.select_gremlin)
        layout.addWidget(btn)

    def select_gremlin(self):
        item = self.list_widget.currentItem()
        if item:
            # Print to stdout so the shell script can capture it
            print(item.text())
            # Exit immediately indicating success (though printing is the real payload)
            sys.exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GremlinPicker()
    window.show()
    # Execute the app
    app.exec()
    # If we close the window without selecting, we exit here.
    # We print nothing.
    sys.exit(1)
