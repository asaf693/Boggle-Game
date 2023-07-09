from boggle_board_randomizer import randomize_board

INITIAL_BUTTON_INDEXES = (-1, -1)


def legit_words_list(filename="boggle_dict.txt"):
    """
    :param filename: Txt file with strings as words.
    :return: A list with strings that represents words.
    """
    # return: A list string, each string represent a valid word
    words_lst = []
    with open(filename, 'r') as words_file:
        for word in words_file:
            words_lst.append(word[:-1])
    return words_lst


def board_lst():
    """
    Initiate the board.
    :return: A list of lists with strings.
    """
    return randomize_board()


def check_env(path):
    """
    :param path: A list of tuples with the coordinates of the path.
    :return: True if the env of each coordinate in the path is valid, else
    returns False.
    """
    for p in range(1, len(path)):
        env_lst = []
        for row in range(-1, 2):
            for col in range(-1, 2):
                x, y = path[p - 1][0] + row, path[p - 1][1] + col
                if (x, y) != path[p - 1]:
                    env_lst.append((x, y))
        if path[p] not in env_lst:
            return False
    return True


class Board:
    """
    Initiate the board.
    """
    def __init__(self, main_screen):
        self.score = 0
        self.path_lst = []
        self.current_word = ''
        self.word_lst = []
        self.success_message = ''
        self.last_button_indexes = INITIAL_BUTTON_INDEXES
        self.main_screen = main_screen

    def choose_letter(self, button, i, j):
        """
        :param button: button.
        :param i: Int that represent coordinate i.
        :param j: Int that represent coordinate j.
        :return: None default, press the chosen  letter.
        """
        # checks if current letter chosen is allowed
        if (i, j) in self.path_lst:
            return 'error'
        if self.last_button_indexes != INITIAL_BUTTON_INDEXES and not \
                check_env([(i, j), self.last_button_indexes]):
            return 'error'
        self.path_lst.append((i, j))
        self.last_button_indexes = (i, j)
        self.main_screen.change_letter_gui(button)
        self.current_word += button['text']

    def submit_word(self):
        """
         :return: None default, submit the chosen word.
         """
        if self.current_word in legit_words_list() and \
                self.current_word not in self.word_lst:
            self.word_lst.append(self.current_word)
            self.score += (len(self.current_word)) ** 2
            self.success_message = 'Well Done'
        else:
            self.success_message = 'Wrong'
        self.main_screen.change_submit_gui()
        self.path_lst.clear()
        self.current_word = ''
        self.last_button_indexes = INITIAL_BUTTON_INDEXES
