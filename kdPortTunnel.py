# coding: utf-8
import time
import os
import sys
import socket
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt, QFile, QTextCodec
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from fileutil import check_and_create, check_and_create_dir


class kdPortTunnel(QWidget):
    def __init__(self):
        super(kdPortTunnel, self).__init__()
        loadUi("kdPortTunnel.ui", self)
        self.config_path = os.environ["HOME"] + \
            "/.config/kdPortTunnel/config.json"
        check_and_create(self.config_path)
        self.init_confs()
        #~ print(dir(self.pte_local_host))
        self.lw_confs.itemClicked.connect(self.on_lw_confs_itemClicked)

    @pyqtSlot()
    def on_pb_start_clicked(self):
        self.local_host = self.pte_local_host.toPlainText()
        self.local_port = self.pte_local_port.toPlainText()
        self.target_host = self.pte_target_host.toPlainText()
        self.target_port = self.pte_target_port.toPlainText()
        #~ for conf in self.confs:
        #~ self.create_target_client(
            #~ conf["target_host"], int(conf["target_port"]))
        #~ self.create_local_server(
            #~ conf["local_host"], int(conf["local_port"]))
        #~ self.begin_listen()
        self.create_target_client(
            self.target_host, int(self.target_port))
        self.create_local_server(
            self.local_host, int(self.local_port))
        self.begin_listen()

    def create_local_server(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # ~ host = "192.168.43.67"
        # ~ host = "192.168.1.77"
        # ~ host = "localhost"
        path = "host:" + host + ",port:" + str(port)
        #~ print(path)
        s.bind((host, port))
        s.listen(5)
        self.server = s
        self.local_socket, self.local_addr = self.server.accept()
        # ~ self.local_socket.send(b"Thank you for connecting")
        print("创建本地socket成功,IP:{},Port:{}".format(host,port))

    def create_target_client(self, host, port):
        self.target_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.target_client.connect((host, int(port)))
        #~ self.target_client.settimeout(None)
        print("新建服务器连接成功，IP:{},Port:{}".format(host,port))

    @pyqtSlot()
    def on_pb_send_clicked(self):
        send_info = self.le_send.text()

        if send_info != "":
            print("开始发送数据1:", send_info)
            #~ self.target_client.send(send_info.encode(encoding="utf-8"))
            self.target_client.send(bytes.fromhex(send_info))
            # ~ self.local_socket, self.local_addr = self.server.accept()
            #~ print("开始发送数据2:", send_info)
            #~ self.local_socket.send(send_info)
            #~ self.local_socket.close()
            #~ self.server.close()

    def begin_listen(self):
        while True:
            # ~ 发送数据
            # ~ if self.local_socket is None:
                #~ create_local_server(self.local_port)
            info = self.local_socket.recv(1024)
            print("原始的待发送文本:", info)
            data = str(info.strip(), 'utf-8').replace("\t", "")
            if data != "" and data is not None:
                if data == "bye":
                    sys.exit(1)
                else:
                    #~ print(self.local_addr, ":", data)
                    # ~ self.create_target_client(self.target_addr, int(self.target_port))
                    # ~ data = "52"
                    print("开始发送数据:", data)
                    self.target_client.send(bytes.fromhex(data))
                    time.sleep(1)
                    # ~ ret = self.target_client.recv(1024)
                    ret = "bye".encode()
                    self.local_socket.send(ret)
                    print("接收到的数据:" + str(ret))
                    #~ self.local_socket.close()
                    #~ time.sleep(2)
                    # ~ self.local_socket, self.local_addr = self.server.accept()
            else:
                time.sleep(1)

            # ~ 接收数据
            # ~ ret = self.target_client.recv(10240)
            # ~ if ret :
                #~ print("receive msg from server:" + str(ret, encoding="utf-8"))
                #~ self.local_socket.send(ret)
                #~ self.local_socket.close()
                # ~ self.local_socket, self.local_addr = self.server.accept()
    @pyqtSlot()
    def on_lw_confs_itemClicked(self):
        cur_item = self.lw_confs.currentItem().text()
        print(cur_item + " clicked")
        for conf in self.confs:
            tmp_name = conf["target_host"] + ":" + conf["target_port"]
            if tmp_name == cur_item:
                self.pte_dev_name.setPlainText(conf["dev_name"])
                self.pte_local_host.setPlainText(conf["local_host"])
                self.pte_local_port.setPlainText(conf["local_port"])
                self.pte_target_host.setPlainText(conf["target_host"])
                self.pte_target_port.setPlainText(conf["target_port"])

    @pyqtSlot()
    def on_mainWindow_destroyed(self):
        print("destroyed")

    @pyqtSlot()
    def on_pb_close_socket_clicked(self):
        print("close")
        if self.local_socket:
            self.local_socket.close()
        if self.server:
            self.server.close()

        if self.target_client:
            self.target_client.close()

    @pyqtSlot()
    def on_pb_del_config_clicked(self):
        target_port = self.pte_target_port.toPlainText()
        tmp_name = ""
        for f in self.confs:
            tmp_name = f["target_host"] + ":" + f["target_port"]
            if tmp_name== target_port:
                self.confs.remove(f)
                with open(self.config_path, "w+") as f:
                    f.write(json.dumps(self.confs))
                    self.lw_confs.takeItem(self.lw_confs.currentRow())
                    print("删除配置成功")

    @pyqtSlot()
    def on_pb_save_config_clicked(self):
        conf = {}
        conf["dev_name"] = self.pte_dev_name.toPlainText()
        conf["local_host"] = self.pte_local_host.toPlainText()
        conf["local_port"] = self.pte_local_port.toPlainText()
        conf["target_host"] = self.pte_target_host.toPlainText()
        conf["target_port"] = self.pte_target_port.toPlainText()
        new_conf_flag = True
        for f in self.confs:
            if f["target_port"] == conf["target_port"]:
                self.confs.remove(f)
                self.confs.append(conf)
                new_conf_flag = False
        if new_conf_flag:
            self.confs.append(conf)
            self.lw_confs.addItem(conf["target_port"])
        with open(self.config_path, "w+") as f:
            f.write(json.dumps(self.confs))
        print("保存配置成功")

    def init_confs(self):
        check_and_create(self.config_path)
        with open(self.config_path, "r") as f:
            content = f.read().strip()
            print("content:" + content)
            if content != "":
                self.confs = json.loads(content)
                for conf in self.confs:
                    self.lw_confs.addItem(conf["target_host"]+ ":" + conf["target_port"])
            else:
                self.confs = []

    def closeEvent(self,QCloseEvent):
        print("close")

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = kdPortTunnel()
    win.show()
    sys.exit(app.exec_())
