class TrieNode:
    """
    class for a node in the trie
    """
    def __init__(self):
        self.isWord = False
        self.next_char = {}

def build_helper (remaining, node):
    """
    used to help build the trie recursively

    param: 
    remaining: string (remaining part of the word)
    node: TrieNode (current node of the trie)

    return:
    none
    """
    if len(remaining) == 0: #exit of recursion
        node.isWord = True
        return 
        
    if remaining[0] not in node.next_char:
        node.next_char[remaining[0]] = TrieNode()
    node = node.next_char[remaining[0]]
    build_helper (remaining[1:], node)


def build_trie (words):
    """
    used to build the trie data structure according to the given word list

    param: 
    words: list (all valid words)

    return:
    TrieNode (the root node of trie)
    """
    root = TrieNode()
    for word in words:
        build_helper(word, root)
    return root


def get_neighbors(row, col, board):
    """
    used to find all possible next move from current position

    param: 
    row: int (row coordinate of the current char to visit)
    col: int (column coordinate of the current char to visit)
    board: list of list (the board of char)

    return:
    list of tuples
    """
    row_max = len(board)
    col_max = len(board[0])
    delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = []
    for delta_row, delta_col in delta:
        next_row = row + delta_row
        next_col = col + delta_col
        if next_row < row_max and next_row >= 0 and next_col < col_max and next_col >= 0:
            neighbors.append((next_row, next_col))
    return neighbors


def dfs (row, col, curr_word, visited, results, board, trie):
    """
    used to perform dfs search on the given board from current location

    param: 
    row: int (row coordinate of the current char to visit)
    col: int (column coordinate of the current char to visit)
    curr_word: list (prefix of a possible word)
    visited: set (coordinate of char that has been visited)
    results: set (words found)
    board: list of list (the board of char)
    tire: TrieNode (current node of the trie)

    return: none
    """
    if (row, col) in visited: #exit of recursion
        return 
    curr_char = board[row][col]
    if curr_char not in trie.next_char:
        return 

    visited.add((row, col))
    curr_word.append(curr_char)
    trie = trie.next_char[curr_char]
    if len(curr_word) > 2 and trie.isWord:
        results.add("".join(curr_word))
    neighbors = get_neighbors(row, col, board)
    for neighbor_row, neighbor_col in neighbors:
        dfs(neighbor_row, neighbor_col, curr_word, visited, results, board, trie)
    visited.remove((row, col))
    curr_word.pop()

def find_words(board, words):
    """
    solution to the challenge, will print each found words and return the set of all found words

    param: 
    board: list of list (the char board)
    words: list (all valid words)

    return: set (all found words)
    """
    #convert all char to lower case firstly
    for row in range(len(board)):
        for col in range(len(board[0])):
            board[row][col] = board[row][col].lower()
    results = set()
    visited = set()
    trie_root = build_trie(words)
    for row in range(len(board)):
        for col in range(len(board[0])):
            dfs(row, col, [], visited, results, board, trie_root)
    print('words found:')
    for word in results:
        print(word)
    print(f'total number of words found: {len(results)}')
    return results


if __name__ == "__main__":
    #use nltk package to get all possible words
    from nltk.corpus import words 
    eng_words = words.words()

    #initialize the board
    board1 = [['c', 'n', 't', 's', 's'],
              ['d', 'a', 't', 'i', 'n'],
              ['o', 'o', 'm', 'e', 'l'],
              ['s', 'i', 'k', 'n', 'd'],
              ['p', 'i', 'c', 'l', 'e']]

    board2 = [['R', 'A', 'E', 'L'],
              ['M', 'O', 'F', 'S'],
              ['T', 'E', 'O', 'K'],
              ['N', 'A', 'T', 'I']]

    find_words(board1, eng_words)
    print('\n-----------------\n')
    find_words(board2, eng_words)

