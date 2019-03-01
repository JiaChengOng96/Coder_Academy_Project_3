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
        """ The constructor for this class 
        infomation about Qt widget:
        https://doc.qt.io/qtforpython/PySide2/QtWidgets/index.html"""

        # Create a GUI application
        app = QApplication([])

        # Create our root window
        window = QMainWindow()

        self.create_main_pane()
        self.create_selection_pane()
        self.create_game_pane()
        self.create_status_pane()
        
        window.setCentralWidget(self.connection_pane)
        window.show()

        self.app = app
        self.window = window

        self.accepting = False
        self.receiving = False
        self.connection = None

        self.timer = QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.tick)
        self.player = 0
        self.attempt = 1
        self.current_guess = []
        self.guessAttempted = []
        self.lives = 2
        self.status = "going"
        self.help_show = False
    
    def run(self):
        """ Method that start the application main loop """
        self.app.exec_()

        print("Application was closed")

    def create_status_pane(self):
        """ Create the status pane for the giver """
        # Create the read only status box
        status_box = QTextEdit()
        status_box.setPlainText('')
        status_box.setReadOnly(True)

        status_pane = create_widget_container([status_box])

        self.status_box = status_box
        self.status_pane = status_pane

    def create_game_pane(self):
        """ Create the game pane for the guesser to guess, the main game """
        game_box = QTextEdit()
        game_box.setPlainText('')
        game_box.setReadOnly(True)

        lbl_character = QLabel('Enter the character')
        inp_character = QLineEdit()
        inp_character.returnPressed.connect(self.send_character)

        instruction = """Game instruction:
        1. input the character you want to guess into the input box
        2. Press enter to send the character
        
        Notes::
        Input only one character!!! 
        Visit here for more information:
        https://www.wikihow.com/Play-Hangman
        Visit here for this gameplay instruction
        https://github.com/JiaChengOng96/Coder_Academy_Project_3/blob/master/Task2_Peer2Peer/README.md
        """

        lbl_help = QLabel(instruction)
        btn_instruction = QPushButton('Help??')

        instruction_pane = create_widget_container([lbl_help])

        def show_help():
            """ The local method on showing and hiding the instruction for the game """
            if self.help_show == False:
                self.help_show = True
                instruction_pane.show()
            else:
                self.help_show = False
                instruction_pane.hide()

        game_pane = create_widget_container([game_box, lbl_character, inp_character, btn_instruction, instruction_pane])

        instruction_pane.hide()
        btn_instruction.clicked.connect(show_help)
        
        self.game_box = game_box
        self.game_pane = game_pane
        self.inp_character = inp_character
    
    def create_main_pane(self):
        """ Create the main pane for the user to connect or wait for connection """
        # Create a pane with the choice to connect or listen to others

        # provide choice to connect or wait for connection
        rad_connect = QRadioButton("Connect")
        rad_listen = QRadioButton("Wait for Connection")

        # initialise the connect radio button as checked
        rad_connect.setChecked(True)

        ## The connect pane

        # Create the ip address txt box for ip input
        lbl_connection_address = QLabel('IP address')
        inp_connection_address = QLineEdit()
        inp_connection_address.setText('localhost')

        # the button to initiate the connection
        btn_connect = QPushButton('Connect')
        btn_connect.clicked.connect(self.btn_connect_clicked)

        # asseble everything of connection pane into a container layout
        connect_pane = create_widget_container([lbl_connection_address, inp_connection_address, btn_connect])

        ## The listening pane

        # Show the ip address of current machine
        lbl_ip_address = QLabel(Networking.get_ip())

        btn_listening = QPushButton("Wait for connection")
        btn_listening.clicked.connect(self.btn_listen_clicked)

        # assemble all listening widget into a container
        listen_pane = create_widget_container([lbl_ip_address, btn_listening])

        connection_pane = create_widget_container([rad_connect, rad_listen, connect_pane, listen_pane])

        # set up a method to show or hide based on user choice
        def show_connect_pane():
            """ show the connection pane when user click the connect to radiobutton """
            listen_pane.hide()
            connection_pane.adjustSize()
            connect_pane.show()

        def show_listen_pane():
            """ show the listening pane when user click the listen radiobutton """
            connect_pane.hide()
            connection_pane.adjustSize()
            listen_pane.show()

        rad_connect.clicked.connect(show_connect_pane)
        rad_listen.clicked.connect(show_listen_pane)

        show_connect_pane()

        self.connection_pane = connection_pane
        self.inp_connection_address = inp_connection_address


    def create_selection_pane(self):
        """ method that create the selection pane for the user to choose which side they want to be on, but is not used in the mvp """
        # create a label for the choice
        lbl_choose_side = QLabel("Which Side do you want?")

        # Create the button for user to choose which side they want,
        # Giver, or Guesser
        btn_giver = QPushButton("Giver")
        btn_giver.clicked.connect(self.btn_giver_clicked)
        btn_guesser = QPushButton("Guesser")
        btn_guesser.clicked.connect(self.btn_guesser_clicked)

        # create the horizontal pane for the button
        btn_group = create_widget_container([btn_giver, btn_guesser], False)

        # create the pane vertically to store the label and button group
        selection_pane = create_widget_container([lbl_choose_side, btn_group])

        # create the label and button for the giver to give word
        inp_word_enter = QLineEdit()
        btn_word_enter = QPushButton("Send")
        btn_word_enter.clicked.connect(self.send_word)

        # giver pane
        giver_pane = create_widget_container([inp_word_enter, btn_word_enter])

        # create the waiting logo for the waiting side
        label = QLabel("Loading....")
        movie = QMovie("loading.gif")
        label.setMovie(movie)
        movie.start()

        guesser_pane = create_widget_container([label])

        self.inp_word_enter = inp_word_enter
        self.giver_pane = giver_pane
        self.guesser_pane = guesser_pane
        self.selection_pane = selection_pane
        

    def btn_connect_clicked(self):
        """ The method would process when the user click on the connect button """
        # when connect button is clicked, show the chat pane
        self.window.setCentralWidget(self.giver_pane)

        self.connection = Networking.Connection(self.inp_connection_address.text(), 5000)
        print("Connecting into port 5000")
        self.player = 1
    
    def btn_listen_clicked(self):
        """ The method would process when user click the waiting for connection/listen button """
        # When listen button is clicked, show the selection pane
        self.window.setCentralWidget(self.guesser_pane)
        self.listener = Networking.Listener(5000)
        print("Listening on port 5000")

        self.accepting = True
        self.player = 2
    
    def btn_giver_clicked(self):
        """ Method which set the giver to the pane for giver
        visit here for more info about setCentralWidget: 
        https://doc.qt.io/qtforpython/PySide2/QtWidgets/QMainWindow.html#PySide2.QtWidgets.PySide2.QtWidgets.QMainWindow.setCentralWidget"""
        self.window.setCentralWidget(self.giver_pane)

    def btn_guesser_clicked(self):
        """ Method which set the guesser to the pane for guesser """
        self.window.setCentralWidget(self.guesser_pane)

    def send_character(self):
        """ Method which send the character enter by the guesser """
        self.character = self.inp_character.text()
        self.inp_character.setText("")
        
        print("Input character is " + self.character)
        self.status_box.append("_ " * len(self.character))
        self.connection.send(bytes(self.character, 'utf-8'))

    def send_word(self):
        """ Method which send the word by the giver to the guesser to guess """
        self.word = self.inp_word_enter.text()
        for i in range(0, len(self.word)):
            self.current_guess.append("_ ")

        self.window.setCentralWidget(self.status_pane)
        self.status_box.append("The word you have given: " + self.word)
        temp = "_ " * len(self.word)
        self.connection.send(bytes(temp, 'utf-8'))

    def tick(self):
        """ the method which used to check for incoming connection """
        if self.accepting:
            self.connection = self.listener.try_get_connection()
            if self.connection is not None:
                self.accepting = False
                self.receiving = True
                print("Connected!!!")
        
        elif self.receiving:
            they_sent = self.connection.try_receive()
            if they_sent is not None:
                word_recv = str(they_sent, 'utf-8')
                if self.player == 1:
                    self.status_box.append("Guesser attempt : " + str(self.attempt))
                    self.attempt += 1
                    if word_recv not in self.guessAttempted:
                        self.guessAttempted.append(word_recv + " ")
                    output = "Attempted : " + ','.join(self.guessAttempted) + '\n'
                    self.connection.send(str.encode(output))
                    if self.compare_word(word_recv):
                        self.connection.send(bytes("Correctly Guess for : ", 'utf-8'))
                        if "_ " not in self.current_guess:
                            self.connection.send(bytes("Congrats"))
                            self.app.quit()
                    else:
                        self.lives -= 1
                        self.connection.send(bytes("Remaining tries : " + str(self.lives) + '\n', 'utf-8'))
                        self.connection.send(bytes("Wrongly Guess for : ", 'utf-8'))
                        if self.lives == 0:
                            self.connection.send(bytes("Lost", 'utf-8'))
                            self.app.quit()
                    self.connection.send(bytes(''.join(self.current_guess), 'utf-8'))
                    self.status_box.append(word_recv)
                else:
                    self.game_box.append(word_recv)
                    self.window.setCentralWidget(self.game_pane)

        elif self.connection is not None:
            self.connection.try_connect()
            if self.connection.connected:
                self.receiving = True
                print("Connected!!")
        
    def compare_word(self, guess):
        """ method to check for the given character by guesser is in the word provide by giver """
        if guess in self.word:
            indices = [i for i, x in enumerate(self.word) if x == guess]
            for b in indices:
                self.current_guess[b] = guess + " "
            return True
        else:
            return False