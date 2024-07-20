# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # find LCA and keep track of the path 
        node, leftPath, rightPath = self.LCA(root, startValue, destValue, "", "")
        print("node", node.val)
        print("left", leftPath)
        print("right", rightPath)
    def LCA(self, root, startVal, destVal, leftPath, rightPath):
        # LCA from nodes on opposite branches or from same branch

        if not root:
            return None, leftPath, rightPath
        if root:
            if root.val == startVal: return root, leftPath, rightPath
            if root.val == destVal: return root, leftPath, rightPath
            left, lleftPath, rightPath = self.LCA(root.left, startVal, destVal, leftPath + "L", rightPath)
            if left: print("left val", left.val)
            print("left left path", leftPath, rightPath)
            # if root.right:
            # if left: return left, leftPath, rightPath
            
            right,leftPath, rrightPath = self.LCA(root.right, startVal, destVal, leftPath, rightPath + "R")
            if right: print("right val", right.val)
            print("right left path", leftPath, rightPath)            
            #if right: return right, leftPath, rightPath
            
            if left and right:
                return root, lleftPath, rrightPath
            if right:
                return right, leftPath, rrightPath
            if left:
                return left, lleftPath, rightPath

        return None, leftPath, rightPath # don't forget this
                

# 5:43pm july 18 2024
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        if root.val == startValue:
            return (self.findPathThruBFS(root, destValue, ""))
        if root.val == destValue:
            path = (self.findPathThruBFS(root, startValue, ""))
            newPath = ""
            for p in range(len(path)):
                newPath += "U"
            return newPath
        
        # find start and dest in left and right subtree
        leftRoot, isStart, leftPath = self.traverseTree(root.left, startValue, destValue, "L", False)
        print(isStart)
        rightRoot, isDest, rightPath = self.traverseTree(root.right, startValue, destValue, "R", False)
        if leftRoot: print("leftRoot", leftRoot.val)
        if rightRoot: print("rightRoot", rightRoot.val)
        print(isDest)
        print(leftPath)
        if isStart:
            newLeftPath = ""
            for i in range(len(leftPath)):
                newLeftPath += "U"
            print(leftPath)
            return newLeftPath + rightPath
        
        if isDest:
            newRightPath = ""
            for i in range(len(rightPath)):
                newRightPath += "U"
            print(leftPath)
            return newRightPath + leftPath
        # handle case when results are in a single branch/subtree
    def findPathThruBFS(self, root, destVal, path):
        queue = []
        queue.append([root, path])

        while queue:
            root, path = queue.pop(0)
            if root.val == destVal:
                return path
            if root.left: queue.append([root.left, path + "L"])
            if root.right: queue.append([root.right, path + "R"])
    
    def traverseTree(self, root, startVal, destVal, path, isStart):
        if not root:
            return root, isStart, path
        if root:
            if root.val == startVal: return root, True, path
            if root.val == destVal: return root, False, path

            leftResult, leftIsStart, leftPath = self.traverseTree(root.left, startVal, destVal, path + "L", isStart)
            if leftResult:
                return leftResult, leftIsStart, leftPath
            rightResult, rightIsStart, rightPath = self.traverseTree(root.right, startVal, destVal, path + "R", isStart)
            if rightResult:
                return rightResult, rightIsStart, rightPath

        # return root, isStart, path IT'S RETURN NONE!!
        return None, isStart, path 
    
    # july 20 2024 9 am
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # find path to startval
        # find path to destVal
        # remove their common nodes
        # append both paths

        startValPath, startNodePath = self.BFS(root, startValue)
        print("startValPath", startValPath)
        for s in startNodePath:
            print(s)
        destValPath, destNodePath = self.BFS(root, destValue)
        
        print("destValPath", destValPath)
        for s in destNodePath:
            print(s)
        limit = len(startNodePath) if len(startNodePath) < len(destNodePath) else len(destNodePath)
        threshold = -1
        startAfterDest = True if len(startNodePath) > len(destNodePath) else False
                
        # now remove directions and shared ancestors until the lowest ancestor is reached
        i = 1
        while (i < limit):
            print("inside")
            if startNodePath[i-1] == destNodePath[i-1] and startNodePath[i] != destNodePath[i]:
                threshold = i - 1
            i+=1
        print ("threshold", threshold)
        print ("limit", limit)
        
        if threshold > -1:
            if threshold == 0:
                startValPath.pop(0)
                destValPath.pop(0)
                limit -= 1
            else:
                for i in range((threshold)):
                    startValPath.pop(0)
                    destValPath.pop(0)
                    limit -= 1
        print("newstartValPath", startValPath)
        print("newdestValPath", destValPath)
        # edge case: if start and dest share the same path
        if limit > 0 and startValPath[0] == destValPath[0]:
        # start comes before dest: remove all similar paths
            i = 0
            while (i < limit and startValPath[0] == destValPath[0]):
                startValPath.pop(0)
                destValPath.pop(0) 
                i += 1
        # dest comes before start: remove all similar paths and replace new path with U
            startPath = ""
            destPath = ''.join(destValPath)

            if startAfterDest:
                for i in range(len(startValPath)):
                    startPath += "U"
            else:
                startPath = ''.join(startValPath)
            return startPath + destPath
        
        startPath = ""
        for i in range(len(startValPath)):
            startPath += "U"
        print("newstartValPath", startPath)
        print("newdestValPath", destValPath)
        destPath = ''.join(destValPath)
        return startPath + destPath

    def BFS(self, root, target):
        queue = []
        queue.append([root, [], []])
        isVisited = set()

        while queue:
            node, currPath, nodePath = queue.pop(0)
            if node.val == target:
                return currPath, nodePath
            if node.val not in isVisited:
                isVisited.add(node.val)
                if node.left: queue.append([node.left, currPath + ["L"], nodePath + [node.val]])
                if node.right: queue.append([node.right, currPath + ["R"], nodePath + [node.val]]) 

    # 9:47 am
                # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # find path to startval
        # find path to destVal
        # remove their common nodes
        # append both paths

        # startValPath, startNodePath = self.BFS(root, startValue)
        # destValPath, destNodePath = self.BFS(root, destValue)
        startValPath, startNodePath = self.DFS(root, startValue, [],[])
        destValPath, destNodePath = self.DFS(root, destValue, [], [])

        limit = len(startNodePath) if len(startNodePath) < len(destNodePath) else len(destNodePath)
        i = 0        
        while i < limit and startValPath[0] == destValPath[0]:
        # remove all similar paths
            startValPath.pop(0)
            destValPath.pop(0) 
            i += 1

        startPath = 'U' * len(startValPath)
        # for i in range(len(startValPath)):
        #     startPath += "U"
        destPath = ''.join(destValPath)
        return startPath + destPath

    
    def DFS(self, root, target, path, nodes):
        if not root:
            return None, None

        if root.val == target:
            return path, nodes

        # Try left subtree
        if root.left:
            left_path, left_nodes = self.DFS(root.left, target, path + ['L'], nodes + [root.val])
            if left_path is not None:
                return left_path, left_nodes

        # Try right subtree
        if root.right:
            right_path, right_nodes = self.DFS(root.right, target, path + ['R'], nodes + [root.val])
            if right_path is not None:
                return right_path, right_nodes

        # If target not found in this subtree
        return None, None

    
    def BFS(self, root, target):
        queue = []
        queue.append([root, [], []])
        isVisited = set()

        while queue:
            node, currPath, nodePath = queue.pop(0)
            if node.val == target:
                return currPath, nodePath
            if node.val not in isVisited:
                isVisited.add(node.val)
                if node.left and node.left.val not in isVisited: queue.append([node.left, currPath + ["L"], nodePath + [node.val]])
                if node.right and node.right.val not in isVisited: queue.append([node.right, currPath + ["R"], nodePath + [node.val]]) 
