class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w

        rows, cols = len(board), len(board[0])
        res = set()
        visited = set()

        def dfs(r, c, node, cur_word):
            if (
                r < 0 or c < 0 or 
                r == rows or c == cols or 
                (r, c) in visited or 
                board[r][c] not in node.children
            ):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            
            if node.word:
                res.add(node.word)

            dfs(r + 1, c, node, cur_word)
            dfs(r - 1, c, node, cur_word)
            dfs(r, c + 1, node, cur_word)
            dfs(r, c - 1, node, cur_word)
            
            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)