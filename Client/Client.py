import socket
from GiaoDienClient import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QPushButton, QDialog
from PyQt5.QtCore import QThread, pyqtSignal
import sys

class MusicGameClient(QMainWindow):
    def __init__(self, host, port):
        super().__init__()
        self.HOST = host
        self.PORT = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.uic = Ui_Form()
        self.uic.setupUi(self)
        self.uic.btnSend.clicked.connect(self.send_answer)
        self.uic.btnSend.setEnabled(False)
        self.note_buttons = []
        self.totalQuestion = 0
        self.current_question = None
        self.isShowQuestion = False
        self.thread = ClientThread(self.client_socket)
        self.thread.message_received.connect(self.handle_message)
        self.thread.start()
        self.show()
    
    def closeEvent(self, event):
        self.client_socket.send("close".encode())
        event.accept()  
        self.client_socket.close()
        self.thread.quit()
        self.thread.wait()
        QApplication.quit()


    def note_button_clicked(self, note_num):
        self.client_socket.send(str(note_num).encode())
        for button in self.note_buttons:
            button.setEnabled(False)

    def send_answer(self):
        answer = self.uic.txtAnswer.text()
        self.client_socket.send(answer.encode())
        self.uic.txtAnswer.clear()
        self.uic.btnSend.setEnabled(False)
    def handle_message(self, message):
        print(message)
        if "Nhập nickname của bạn" in message:
            self.handle_nickname_input(message)
        elif "Nickname đã được sử dụng hoặc không hợp lệ" in message:
            self.handle_invalid_nickname(message)
        elif "Bạn đã đăng ký thành công" in message:
            self.handle_registration_success(message)
        elif "Các nốt nhạc có sẵn:" in message:
            self.handle_available_notes(message)
        elif "Bạn đã chọn nốt nhạc số" in message:
            self.handle_note_selection(message)
        elif "Chúc mừng! Bạn nhận được" in message:
            self.handle_congratulations(message)
        elif "Câu trả lời sai. Lượt chơi tiếp theo." in message:
            self.handle_wrong_answer(message)
        elif "Bạn thắng cuộc với" in message:
            self.handle_game_end(message)
        elif "Bạn đạt được" in message:
            self.handle_game_end(message)
        elif "Tổng số câu hỏi" in message:
            self.totalQuestion = int(message.split(":")[1])
    def handle_nickname_input(self, message):
        dialog = QDialog(self)
        nickname, ok = QInputDialog.getText(dialog, "Nhập nickname", message)
        if ok:
            self.client_socket.send(nickname.encode())
            dialog.accept()  # Đóng hộp thoại

    def handle_invalid_nickname(self, message):
        dialog = QDialog(self)
        nickname, ok = QInputDialog.getText(dialog, "Nhập nickname", message)
        if ok:
            self.client_socket.send(nickname.encode())
            dialog.accept()

    def handle_registration_success(self, message):
       self.uic.labelNotify.setText(message)


    def handle_game_end(self, message):
        self.uic.labelNotify.setText(message)

    def handle_available_notes(self, message):
        message = message.split(":")[1]
        available_notes = message.split("-")
        print(available_notes)
        if not self.isShowQuestion:
            for note_num in range(1, self.totalQuestion + 1):
                button = QPushButton(f"Nốt {note_num}", self)
                button.setStyleSheet("QPushButton{border: 2px solid #282a36;font: 13pt MS Shell Dlg 2;}")
                button.clicked.connect(lambda _, num=str(note_num): self.note_button_clicked(num))
                button.setEnabled(str(note_num) in available_notes)
                self.uic.horizontalLayout.addWidget(button)
                self.note_buttons.append(button)
            self.isShowQuestion = True
        else:
            for i in range(len(self.note_buttons)):
                if str(i+1) in available_notes:
                    print(i + 1)
                    print(available_notes)
                    self.note_buttons[i].setEnabled(True)
        

    def handle_note_selection(self, message):
        self.uic.txtQuestion.clear()
        self.uic.txtQuestion.setText(message)
        self.uic.btnSend.setEnabled(True)


    def handle_congratulations(self, message):
        self.uic.labelNotify.setText(message)

    def handle_wrong_answer(self, message):
        self.uic.labelNotify.setText(message)


        

class ClientThread(QThread):
    message_received = pyqtSignal(str)
    
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket

    def run(self):
        try:
            while True:     
                message = self.client_socket.recv(1024).decode()
                print(message)
                self.message_received.emit(message)
        except ConnectionError as e:
            print(f"Connection error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.client_socket.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MusicGameClient("127.0.0.1", 12345)  
    sys.exit(app.exec_())
