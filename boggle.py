from home_screen import *
from main_screen import *
from end_screen import *


class Game:
    """
    Manage the entire game.
    """
    def manage(self):
        """
        :return: None default, loading the home screen.
        """
        home_screen_root = tk.Tk()
        home_screen = HomeScreen(home_screen_root)
        if home_screen.run_page() == 'yes':
            self.middle_end_game()

    def middle_end_game(self):
        """
        :return: None default, loading the main screen
        and switch to the end screen if chosen.
        """
        game_root = tk.Tk()
        main_game = MainScreen(game_root)
        if main_game.run_page() == 'yes':
            end_screen_root = tk.Tk()
            end_screen = EndScreen(end_screen_root)
            if end_screen.run_page() == 'yes':
                self.middle_end_game()


if __name__ == "__main__":
    game = Game()
    game.manage()