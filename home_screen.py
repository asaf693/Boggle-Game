import tkinter as tk

HOME_PICTURE = 'boggle_img.png'
DEFAULT_FONT = 'David'
BUTTON_BG = 'white'
GAME_BG = 'yellow green'


class HomeScreen:
    """
    Initiate the home screen of the game.
    """
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.title = self.root.title('Home Screen')  # page title
        self.size = self.root.geometry('480x490')  # size of window
        self.another = 'no'
        self._creating_buttons()
        self._creating_labels()

    def _creating_buttons(self):
        """
        :return: None default, creating the buttons.
        """
        self.start_game = tk.Button(self.root, font=(DEFAULT_FONT, 22),
                                    bg=GAME_BG,
                                    fg=BUTTON_BG, text='Start Game',
                                    command=self.root_destroy_and_start)
        self.start_game.pack(side=tk.BOTTOM, fill=tk.X)

    def _creating_labels(self):
        """
        :return: None default, creating the labels.
        """
        self.headline = tk.Label(self.root, font=('David', 26), bg=GAME_BG,
                                 fg=BUTTON_BG, text='Welcome To The Boggle '
                                                    'Game!')
        self.headline.pack(side=tk.TOP, fill=tk.X)
        self.img = tk.PhotoImage(file=HOME_PICTURE)
        self.label_img = tk.Label(self.root, image=self.img)
        self.label_img.pack()

    def root_destroy_and_start(self):
        """
        :return: A string, closes the window and moves to another one.
        """
        self.root.destroy()
        self.another = 'yes'
        return self.another

    def run_page(self):
        """
        :return: A string, running his own window.
        """
        self.root.mainloop()
        return self.another
