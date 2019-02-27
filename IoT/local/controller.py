from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import rpyc
from drag_drop_container import *

class Controller():

    def __init__(self):

        self.app = QApplication([])
        
        dd_container = DragDropContainer()

        connection_pane = self.create_connect_panel()

        connection_pane.hostname = None

        # window = QWidget()
        # layout = QVBoxLayout()
        # layout.addWidget(connect_panel)
        # window.setLayout(layout)
        # window.show()

        dd_container.add_child(connection_pane)

        self.dd_container = dd_container

        f = open("savefile", "r")
        
        for x in f:
            connection = rpyc.classic.connect(x.strip())
            device = connection.modules.__main__.my_device
            self.add_device_panel(device, x.strip())

        dd_container.show()
               

    def create_connect_panel(self):
        panel = QFrame()
        panel.setFrameShape(QFrame.Panel)
        layout = QVBoxLayout()
        lbl_ip_address = QLabel('Enter IP address or hostname:')
        inp_ip_address = QLineEdit()
        inp_ip_address.setText('127.0.0.2')
        btn_connect = QPushButton('Link new device')

        layout.addWidget(lbl_ip_address)
        layout.addWidget(inp_ip_address)
        layout.addWidget(btn_connect)

        def connect():
            hostname = inp_ip_address.text()
            connection = rpyc.classic.connect(hostname)
            device = connection.modules.__main__.my_device
            self.add_device_panel(device, hostname)

        btn_connect.clicked.connect(connect)

        panel.setLayout(layout)

        return panel

    def add_device_panel(self, device, hostname):
        panel = QFrame()
        panel.setFrameShape(QFrame.Box)
        layout = QVBoxLayout()

        lbl_name = QLabel('Device: ' + device.get_name())
        lbl_label = QLabel(device.get_label())

        layout.addWidget(lbl_name)
        layout.addWidget(lbl_label)
        if hasattr(device, 'turn_on'):
            rad_on = QRadioButton(device.get_on_label())
            rad_off = QRadioButton(device.get_off_label())
            layout.addWidget(rad_on)
            layout.addWidget(rad_off)

            if device.read() == True:
                rad_on.setChecked(True)
            else:
                rad_off.setChecked(True)

            def rad_change():
                if rad_on.isChecked():
                    device.turn_on()
                else:
                    device.turn_off()

            rad_on.toggled.connect(rad_change)

        elif hasattr(device, 'write'):
            inp_value = QLineEdit()
            inp_value.setText(str(device.read()))

            btn_set = QPushButton('Set new value')

            def set_value():
                device.write(inp_value.text())

            btn_set.clicked.connect(set_value)

            layout.addWidget(inp_value)
            layout.addWidget(btn_set)

        elif hasattr(device, 'read'):
            lbl_value = QLabel(str(device.read()))
            layout.addWidget(lbl_value)

        panel.setLayout(layout)
        panel.hostname = hostname
        self.dd_container.add_child(panel)



    def run(self):
        self.app.exec_()

        file_open = open("savefile", "w")

        list_of_device = self.dd_container.list_widgets()

        for x in list_of_device:
            if x.hostname is not None:
                if x is not "\n":
                    file_open.write(x.hostname+"\n")
