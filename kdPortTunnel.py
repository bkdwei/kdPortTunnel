# coding: utf-8
import time
import os
import sys
import socket
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt, QFile, QTextCodec
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi


class kdPortTunnel(QWidget):
    def __init__(self):
        super(kdPortTunnel, self).__init__()
        loadUi("kdPortTunnel.ui", self)

    @pyqtSlot()
    def on_pb_start_clicked(self):
        self.local_port = self.pte_local_port.toPlainText()
        self.target_addr = self.pte_target_addr.toPlainText()
        self.target_port = self.pte_target_port.toPlainText()
        self.create_local_server(int(self.local_port))
        self.create_target_client(self.target_addr, int(self.target_port))
        self.begin_listen()

    def create_local_server(self, port):
        s = socket.socket()
        host = "localhost"
        path = "host:" + host + ",port:" + str(port)
        print(path)
        s.bind((host, port))
        s.listen(500)
        self.server = s
        self.local_socket, self.local_addr = s.accept()
        # ~ self.local_socket.send(b"Thank you for connecting")
        print("创建本地socket成功")

    def create_target_client(self, host, port):
        self.target_client = socket.socket()
        self.target_client.connect((host, int(port)))
        self.target_client.settimeout(None)
        print("connect server success")

    def begin_listen(self):
        while True:
            # ~ 发送数据
            data = self.local_socket.recv(10240)
            if data:
                print("开始发送数据:", data)
                if data == "bye":
                    sys.exit(1)
                else:
                    print(self.local_addr, ":", data)
                    # ~ self.create_target_client(self.target_addr, int(self.target_port))
                    self.target_client.send(data)
            else:
                time.sleep(1)

            # ~ 接收数据
            ret = self.target_client.recv(10240)
            if ret :
                print("receive msg from server:" + str(ret, encoding="utf-8"))
                self.local_socket.send(ret)
                self.local_socket.close()
                self.local_socket, self.local_addr = self.server.accept()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = kdPortTunnel()
    win.show()
    sys.exit(app.exec_())
