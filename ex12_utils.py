from copy import deepcopy


def legit_words_list(filename):
    """
    :param filename: A file name in txt format, each line in the file is a
    string that represent a valid word
    :return: A list string, each string represent a valid word.
    """
    words_lst = []
    with open(filename, 'r') as words_file:
        for word in words_file:
            words_lst.append(word[:-1])
    return words_lst


def is_valid_path(board, path, words):
    """
    :param board: A list of lists with strings.
    :param path: A list of tuples with the coordinates of the path.
    :param words: A list with strings, each string is a valid word.
    :return: The word, if the word for the given path is valid, else
    returns None.
    """
    word_str = ''
    coordinates_board = board_cord(board)
    if not check_duplicates(path):
        return
    if not check_env(path, coordinates_board):
        return
    for (x, y) in path:
        word_str += board[x][y]
    if word_str in words:
        return word_str


def check_duplicates(path):
    """
    :param path: A list of tuples with the coordinates of the path.
    :return: True if there is not duplicates coordinates, else returns False.
    """
    for j in range(len(path) - 1):
        if path[j] in path[j + 1:]:
            return False
    return True


def check_env(path, cord_of_board):
    """
    :param path: A list of tuples with the coordinates of the path.
    :param cord_of_board: A list of tuples with the coordinates of the board.
    :return: True if the env of each coordinate in the path is valid, else
    returns False.
    """
    for cord in path:
        if cord not in cord_of_board:
            return False
    for p in range(1, len(path)):
        env_lst = []
        for row in range(-1, 2):
            for col in range(-1, 2):
                x, y = path[p - 1][0] + row, path[p - 1][1] + col
                if (x, y) in cord_of_board and (x, y) != path[p - 1]:
                    env_lst.append((x, y))
        if path[p] not in env_lst:
            return False
    return True


def board_cord(board):
    """
    :param board: A list of lists with strings.
    :return: A list of lists with tuples, where each tuple is a coordinate in
    the board.
    """
    x_y_set = set()
    col_length = len(board[0])
    row_length = len(board)
    for x in range(row_length):
        for y in range(col_length):
            x_y_set.add((x, y))
    return x_y_set


def find_length_n_paths(n, board, words):
    """
    :param n: Int that represent the length of  path by the cubes in the board.
    :param board: A list of lists with strings.
    :param words: A list with strings, each string is a valid word.
    :return: A list of lists with tuples, where each tuple is a coordinate on
    the board.
    """
    correct_words = set()
    all_paths_n = []
    for check_word in words:
        if len(check_word) >= n:
            correct_words.add(check_word)
    for checked_word in correct_words:
        checking_paths = helper_find_words_or_paths(board, checked_word,
                                                    False, n)
        if checking_paths:
            for i in checking_paths:
                all_paths_n.append(i)
    return all_paths_n


def find_length_n_words(n, board, words):
    """
    :param n: Int that represent the length of  path by the letters in the word
    :param board: A list of lists with strings.
    :param words: A list with strings, each string is a valid word.
    :return: A list of lists with tuples, where each tuple is a coordinate on
    the board.
    """
    correct_words = set()
    all_paths_n = []
    for check_word in words:
        if len(check_word) == n:
            correct_words.add(check_word)
    for checked_word in correct_words:
        checking_paths = helper_find_words_or_paths(board, checked_word, True)
        if checking_paths:
            for i in checking_paths:
                all_paths_n.append(i)
    return all_paths_n


def is_valid(board, x, y, path):
    """
    :param board: A list of lists with strings.
    :param x: Int that represent the coordinate x.
    :param y: Int that represent the coordinate y.
    :param path: A list of tuples with the coordinates of the path.
    :return: bool value, True of False.
    """
    return (0 <= x < len(board)) and (0 <= y < len(board[0])) \
           and (x, y) not in path


def search_in_recursive(board, word_search, x, y, n, var, end=0, path_lst=None,
                        path=None):
    """
    :param board: A list of lists with strings.
    :param word_search: A string that represent the word we are searching.
    :param x: Int that represent the coordinate x.
    :param y: Int that represent the coordinate y.
    :param n: Int that represent the length of the path.
    :param var: bool variable.
    :param end: Int with default 0, that indicates the slicing point of  word.
    :param path_lst: None default, a list that will be filled the paths.
    :param path: None default, a list that'll be filled the tuples as coords.
    :return: A list with all the paths.
    """
    if path is None:
        path = []
    if path_lst is None:
        path_lst = []
    r = [-1, -1, -1, 0, 0, 1, 1, 1]
    c = [-1, 0, 1, -1, 1, -1, 0, 1]
    start = end
    end = start + len(board[x][y])
    if board[x][y] != word_search[start:end]:
        return path_lst

    path.append((x, y))

    if end == len(word_search) and var:
        current_path = deepcopy(path)
        path_lst.append(current_path)
    elif end == len(word_search) and len(path) == n and not var:
        current_path = deepcopy(path)
        path_lst.append(current_path)
    else:
        for k in range(8):
            if is_valid(board, x + r[k], y + c[k], path):
                search_in_recursive(board, word_search, x + r[k], y + c[k], n,
                                    var, end, path_lst, path)
    path.pop()
    return path_lst


def helper_find_words_or_paths(board, word_search, var=False, n=0):
    """
    :param board: A list of lists with strings.
    :param word_search: A string that represent the word we are searching.
    :param var: bool variable.
    :param n: Int that represent the length of the path.
    :return: A list with all the paths.
    """
    object_lst = []
    for a in range(len(board)):
        for b in range(len(board[0])):
            if board[a][b] == word_search[:len(board[a][b])]:
                object_x = search_in_recursive(board, word_search, a, b, n,
                                               var, 0, [])
                if object_x:
                    for i in object_x:
                        object_lst.append(i)
    return object_lst


def max_score_paths(board, words):
    """
    :param board: A list of lists with strings.
    :param words: A string that represent the word we are searching.
    :return: A list with all the paths with the highest score.
    """
    highest_scoring_lst = []
    for word in words:
        lst = (find_length_n_words(len(word), board, [word]))
        if lst:
            highest_scoring_lst.append(max(lst, key=len))
    return highest_scoring_lst
