from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSpacerItem
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QTextEdit

class Hangman():
    """Creating a cless which encapsulates out our application"""
    def __init__(self):
        """ The constructor for this class"""

        # Create a GUI application
        app = QApplication([])

        # Create our root window
        window = QWidget()

        # create the main empty layout and set the layout to the window
        main_layout = QVBoxLayout()
        window.setLayout(main_layout)

        # create a label for the choice
        lbl_side = QLabel("Which Side do you want?")

        # Create the button for user to choose which side they want,
        # Giver, or Guesser
        btn_giver = QPushButton("Giver")
        btn_guesser = QPushButton("Guesser")

        # Add the button on the layout
        main_layout.addWidget(lbl_side)
        main_layout.addWidget(btn_giver)
        main_layout.addWidget(btn_guesser)

        window.show()

        self.app = app
        self.window = window
        self.main_layout = main_layout
        self.btn_giver = btn_giver
        self.btn_guesser = btn_guesser

    def run(self):
        """ Method that start the application main loop """
        self.app.exec_()

        print("Application was closed")