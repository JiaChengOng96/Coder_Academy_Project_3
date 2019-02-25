from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSpacerItem, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QTextEdit, QRadioButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from networking import Networking
import sys

def create_widget_container(widgets, vertical = True):
    """ The method to accept argument of list of widget and add it into the layout of vertical(default to vertical) else horizontal if specify and return the widget containing the layout """

    new_widget = QWidget()

    if not vertical:
        new_layout = QHBoxLayout()
    else:
        new_layout = QVBoxLayout()
    
    for widget in widgets:
        new_layout.addWidget(widget)
    
    new_widget.setLayout(new_layout)

    return new_widget


class Hangman():
    """ Creating a cless which encapsulates out our application """
    def __init__(self):
        """ The constructor for this class """

        # Create a GUI application
        app = QApplication([])

        # Create our root window
        window = QMainWindow()

        self.create_main_pane()
        self.create_selection_pane()
        self.create_game_pane()
        self.create_status_pane()
        
        window.setCentralWidget(self.main_pane)
        window.show()

        self.app = app
        self.window = window

        self.accepting = False
        self.receiving = False
        self.connection = None

        self.timer = QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.tick)
    
    def run(self):
        """ Method that start the application main loop """
        self.app.exec_()

        print("Application was closed")
    
    def main_pane(self):
        """ Create the main pane for the user to connect or wait for connection """

        ## The connect pane

        # Create the ip address txt box for ip input
        lbl_connection_address = QLabel('IP address')
        inp_connection_address = QLineEdit()
        inp_connection_address.setText('localhost')

        # the button to initiate the connection
        btn_connect = QPushButton('Connect')
        #btn_connect.clicked.connect(self.btn_connect_clicked)

        # asseble everything of connection pane into a container layout
        connect_pane = create_widget_container([lbl_connection_address, inp_connection_address, btn_connect])

        rad_one = QRadioButton("Speed: one")
        rad_two = QRadioButton("Speed: two")
        rad_three = QRadioButton("Speed: three")

        fan_pane = create_widget_container([rad_one, rad_two, rad_three])

        rad_one = QRadioButton("Speed: one")
        rad_two = QRadioButton("Speed: two")
        rad_three = QRadioButton("Speed: three")

        fan_pane = create_widget_container([rad_one, rad_two, rad_three])

        lbl_temperature = QLabel('Enter temperature')
        inp_temperature = QLineEdit()
        inp_temperature.setText('24')

        air_conditional_pan = create_widget_container([lbl_temperature, inp_temperature])

        rad_on = QRadioButton("Light On")
        rad_off = QRadioButton("Light Off")

        light_pane = create_widget_container([rad_on, rad_off])

        connection_pane = create_widget_container([connect_pane, fan_pane, air_conditional_pan, light_pane])
   