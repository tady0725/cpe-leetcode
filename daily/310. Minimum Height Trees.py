from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # edge cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves


n, edges = 4, [[1, 0], [1, 2], [1, 3]]
print(Solution().findMinHeightTrees(n, edges))


'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [x for x in range(n)]

        neighbors = [set() for x in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            temp = []

            for leaf in leaves:
                for neighbor in neighbors[leaf]:
                    neighbors[neighbor].remove(leaf)
                    if len(neighbors[neighbor]) == 1:
                        temp.append(neighbor)
            leaves = temp

        return leaves
'''
