import tkinter as tk
from board import *

GAME_TIME = 180
INITIAL_SCORE = 0
DEFAULT_FONT = 'David'
GAME_BG = 'yellow green'
BUTTON_BG = 'white'
GOOD_PICTURE = 'good.png'
BAD_PICTURE = 'bad.png'


class MainScreen:
    """
    Initiate the main screen of the game.
    """
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.title = self.root.title('Boogle Game')  # page title
        self.size = self.root.geometry('800x700')  # size of window
        self.bg = self.root.config(bg=GAME_BG)  # window's bg
        self.game_time = GAME_TIME
        self.score = INITIAL_SCORE
        self.board = Board(self)
        self._creating_labels()
        self._creating_buttons()
        self._create_word_box()
        self.another = 'no'
        self.board_lst = [['button_object'] * len(board_lst()[0])
                          for _ in board_lst()]

    def _creating_buttons(self):
        """
        :return: None default, creating the buttons.
        """
        self.start_game = tk.Button(self.root, font=(DEFAULT_FONT, 22),
                                    bg=BUTTON_BG, text='Start Game',
                                    command=self._board_setter)
        self.start_game.pack(side=tk.BOTTOM, fill=tk.X)
        self.end_game = tk.Button(self.root, font=(DEFAULT_FONT, 22),
                                  bg=BUTTON_BG, width=10, height=2,
                                  text='End Game',
                                  command=self.root_destroy_and_start)
        self.end_game.place(x=312, y=550)

    def _creating_labels(self):
        """
        :return: None default, creating the labels.
        """
        self.score_label = tk.Label(self.root, font=(DEFAULT_FONT, 22),
                                    width=10, height=2, bg=GAME_BG,
                                    text=('Score: ' + str(self.score)))
        self.score_label.place(x=310, y=65)
        self.current_word_label = tk.Label(self.root, font=(DEFAULT_FONT, 22),
                                           bg=GAME_BG, width=10, height=2,
                                           text='Current Word: ')
        self.current_word_label.pack(side=tk.TOP, fill=tk.X)
        self.timer = tk.Label(self.root, font=(DEFAULT_FONT, 22), width=15,
                              height=2, bg=GAME_BG, text='Time: 03:00')
        self.timer.place(x=530, y=65)
        self.words_found_label = tk.Label(self.root, font=(DEFAULT_FONT, 22),
                                          width=12, height=20, anchor='n',
                                          bg=GAME_BG, text='Words Found: ')
        self.words_found_label.place(x=20, y=80)

    def _create_word_box(self):
        """
        :return: None default, creating listbox for words.
        """
        self.frame1 = tk.Frame(self.root)
        self.frame1.place(x=40, y=150, width=150, height=300)
        self.frame1a = tk.Frame(master=self.frame1)
        self.frame1a.place(x=0, y=0, width=150, height=299)
        self.lb = tk.Listbox(self.frame1a, bg=GAME_BG, width=23, height=19)
        self.lb.grid(row=0, column=0)
        self.scrollbar = tk.Scrollbar(self.frame1, orient="vertical",
                                      bg=GAME_BG, command=self.lb.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.lb.config(yscrollcommand=self.scrollbar.set)
        self.used_words = set()

    def update_box(self, word_c):
        """
        :param word_c: A string that represent a word.
        :return: None default, update the words in the listbox.
        """
        if word_c not in self.used_words:
            self.lb.insert(tk.END, word_c)

    def _board_setter(self):
        """
        :return: None default, build the board game.
        """
        self.start_game.destroy()
        self.frame = tk.Frame(self.root, bg='#F2B33D')
        self.frame.place(x=250, y=150)
        submit_word = tk.Button(self.root, font=(DEFAULT_FONT, 22),
                                bg=BUTTON_BG, text='Submit Word',
                                command=self.board.submit_word)
        submit_word.pack(side=tk.BOTTOM, fill=tk.X)
        for i in range(len(board_lst())):
            for j in range(len(board_lst()[0])):
                self.board_lst[i][j] = tk.Button(self.frame,
                                                 font=(DEFAULT_FONT, 12),
                                                 bg=BUTTON_BG, width=13,
                                                 height=5,
                                                 text=board_lst()[i][j],
                                                 command=lambda i=i, j=j:
                                                 self.board.choose_letter(
                                                     self.board_lst[i][j], i,
                                                     j))
                self.board_lst[i][j].grid(row=i, column=j)
        self.countdown_timer(self.game_time)

    def change_letter_gui(self, button):
        """
        :param button: button.
        :return: None default, update the letter in the gui.
        """
        button['background'] = 'green'
        self.current_word_label['text'] += button['text']

    def picture_after_submit(self, picture):
        """
        :param picture: png image.
        :return: None default, place the image after submit.
        """
        image1 = tk.PhotoImage(file=picture)
        panel1 = tk.Label(self.root, image=image1)
        panel1.image = image1
        panel1.place(x=40, y=480)

    def change_submit_gui(self):
        """
        :return: None default, update the image after submit.
        """
        self.score = self.board.score
        self.score_label['text'] = 'Score: ' + str(self.score)
        for word in self.board.word_lst:
            if word not in self.used_words:
                self.update_box(word)
                self.used_words.add(word)
        self.current_word_label['text'] = 'Current Word: '
        for row in self.board_lst:
            for button in row:
                button['bg'] = BUTTON_BG
        if self.board.success_message == 'Well Done':
            self.picture_after_submit(GOOD_PICTURE)
        else:
            self.picture_after_submit(BAD_PICTURE)

    def countdown_timer(self, game_time):
        """
        :param game_time: count the time of the game.
        :return: None default, update the time of the game and closes when
        finished.
        """
        minute, second = divmod(game_time, 60)
        self.timer.config(
            text='Time: ' + str('{:02d}:{:02d}'.format(minute, second)))
        x = self.timer.after(1000, lambda: self.countdown_timer(game_time - 1))
        self.end_game.config(command=lambda: self.root_destroy_and_start(x))
        if game_time == 0:
            self.timer.after_cancel(x)
            self.root_destroy_and_start()

    def root_destroy_and_start(self, x=None):
        """
        :param x: None default, variable that changes.
        :return: A string, closes the window and moves to another one.
        """
        if x:
            self.timer.after_cancel(x)
        self.root.destroy()
        self.another = 'yes'
        return self.another

    def run_page(self):
        """
        :return: A string, running his own window.
        """
        self.root.mainloop()
        return self.another
