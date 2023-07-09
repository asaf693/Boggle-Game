import tkinter as tk

GAME_BG = 'yellow green'
BUTTON_BG = 'white'
DEFAULT_FONT = 'David'
END_PICTURE = 'end.png'


class EndScreen:
    """
    Initiate the end screen of the game.
    """
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.title = self.root.title('End Screen')  # page title
        self.size = self.root.geometry('470x530')  # size of window
        self._creating_buttons()
        self._creating_labels()
        self.another = 'no'

    def _creating_buttons(self):
        """
        :return: None default, creating the buttons.
        """
        self.another_game = tk.Button(self.root, font=(DEFAULT_FONT, 20),
                                      bg=GAME_BG, fg=BUTTON_BG,
                                      text='Click To Start Another Game',
                                      command=self.root_destroy_and_start)
        self.another_game.pack(side=tk.BOTTOM, fill=tk.X)

    def _creating_labels(self):
        """
        :return: None default, creating the labels.
        """
        self.headline = tk.Label(self.root, font=(DEFAULT_FONT, 28),
                                 bg=GAME_BG, fg=BUTTON_BG,
                                 text='Game Has Ended!')
        self.headline.pack(side=tk.TOP, fill=tk.X)
        self.img = tk.PhotoImage(file=END_PICTURE)
        self.label_img = tk.Label(self.root, image=self.img)
        self.label_img.pack(side=tk.TOP, fill=tk.X)

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
