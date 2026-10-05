from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If the endWord isn't in the list, a transformation is impossible
        if endWord not in wordList:
            return 0

        # Include beginWord in the list to easily build patterns
        wordList.append(beginWord)
        
        # Build adjacency list where keys are patterns (e.g., "*at") 
        # and values are lists of words matching that pattern
        nei = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        # Initialize BFS queue and visited set
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1 # Number of words in the sequence

        while q:
            # Iterate through the current level
            for _ in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return res
                
                # Check all neighbors through the intermediate patterns
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
                            
            # Increment sequence length after finishing a level
            res += 1

        return 0