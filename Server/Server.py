import socket
import threading

class Player:
    def __init__(self, socket, address):
        self.socket = socket
        self.address = address
        self.nickname = None
        self.score = 0

class Note:
    def __init__(self, note_number, question, answer, points):
        self.note_number = note_number
        self.question = question
        self.answer = answer
        self.points = points

class MusicGameServer:
    def __init__(self):
        self.HOST = "0.0.0.0"
        self.PORT = 12345
        self.registered_nicknames = set()
        self.notes = {
            1: Note(1, "Câu hỏi cho nốt 1?", "1", 100),
            2: Note(2, "Câu hỏi cho nốt 2?", "2", 150),
            3: Note(3, "Câu hỏi cho nốt 3?", "3", 100),
            4: Note(4, "Câu hỏi cho nốt 4?", "4", 200),
            5: Note(5, "Câu hỏi cho nốt 5?", "5", 100),
            6: Note(6, "Câu hỏi cho nốt 6?", "6", 150),
        }
        self.notes_with_points = [2, 5]
        self.current_player_index = 0
        self.players = []
        self.players_sem = threading.Semaphore()
        self.isPlay = False
    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.HOST, self.PORT))
        server_socket.listen(5)
        print(f"Server đang lắng nghe kết nối trên cổng {self.PORT}!")

        while True:
            client_socket, client_address = server_socket.accept()
            print("Đã kết nối với", client_address)
            player = Player(client_socket, client_address)
            self.players_sem.acquire()
            self.players.append(player)
            self.players_sem.release()
            client_handler = threading.Thread(target=self.handle_client, args=(player,))
            client_handler.start()
            


    def handle_client(self, player):
        player.socket.send("Nhập nickname của bạn: ".encode())
        nickname = player.socket.recv(1024).decode().strip()

        while not self.is_valid_nickname(nickname):
            player.socket.send("Nickname đã được sử dụng hoặc không hợp lệ. Vui lòng chọn một nickname khác: ".encode())
            nickname = player.socket.recv(1024).decode().strip()
            

        player.nickname = nickname
        self.registered_nicknames.add(nickname)
        player.socket.send("Bạn đã đăng ký thành công.\n".encode())
        player.socket.send(f"Tổng số câu hỏi:{len(self.notes)}:".encode())
        if len(self.players) >= 3 and not self.isPlay:
            self.play_game()
            self.isPlay = True
    def is_valid_nickname(self, nickname):
        return nickname.isalnum() and len(nickname) <= 10 and nickname not in self.registered_nicknames

    def play_game(self):
        for player in self.players:
                player.socket.send("Trò chơi bắt đầu!\n".encode())
        while len(self.notes) > 0:
            self.current_player_index = self.current_player_index % len(self.players)
            current_player = self.players[self.current_player_index]
            self.current_player_index += 1

            self.send_notes(current_player)
            chosen_note = self.receive_chosen_note(current_player)
            print(chosen_note)
            question = self.notes[chosen_note].question
            current_player.socket.send(f"Bạn đã chọn nốt nhạc số {chosen_note}. {question}\n".encode())
            client_answer = current_player.socket.recv(1024).decode()

            if client_answer.lower() == self.notes[chosen_note].answer.lower():
                points = self.notes[chosen_note].points
                if chosen_note in self.notes_with_points:
                    points += chosen_note * 100
                current_player.score += points
                current_player.socket.send(f"Chúc mừng! Bạn nhận được {points} điểm.\n".encode())
            else:
                current_player.socket.send("Câu trả lời sai. Lượt chơi tiếp theo.\n".encode())

            del self.notes[chosen_note]

        self.end_game()

    def send_notes(self, player):
        note_list = "-".join([f"{note_num}" for note_num in self.notes.keys()])
        message = "Các nốt nhạc có sẵn:" + note_list
        player.socket.send(message.encode())

    def receive_chosen_note(self, player):
        print(1)
        while True:
            chosen_note = player.socket.recv(1024).decode()
            print(chosen_note)
            try:
                chosen_note = int(chosen_note)
                if chosen_note in self.notes:
                    return chosen_note
                player.socket.send("Nốt nhạc không hợp lệ hoặc không có điểm thưởng. Vui lòng chọn lại.\n".encode())
            except ValueError:
                player.socket.send("Lựa chọn không hợp lệ. Vui lòng chọn lại.\n".encode())

    def end_game(self):
        winner = max(self.players, key=lambda player: player.score)
        for player in self.players:
            if player == winner:
                player.socket.send(f"Bạn thắng cuộc với {player.score} điểm!\n".encode())
            else:
                player.socket.send(f"Bạn đạt được {player.score} điểm.\n".encode())


if __name__ == "__main__":
    game_server = MusicGameServer()
    game_server.start()
