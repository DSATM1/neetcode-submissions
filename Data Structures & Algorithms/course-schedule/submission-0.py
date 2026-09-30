class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # visitSet stores all courses along the current DFS path
        visitSet = set()
        
        def dfs(crs):
            # Base cases
            if crs in visitSet:  # Cycle detected
                return False
            if preMap[crs] == []: # Course has no prerequisites (or we already verified it)
                return True
                
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            
            # Optimization: Clear the prerequisites once verified so we don't revisit
            preMap[crs] = []
            return True
            
        # Call DFS for every course to handle disconnected graphs
        for crs in range(numCourses):
            if not dfs(crs):
                return False
                
        return True