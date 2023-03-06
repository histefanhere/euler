#!/usr/bin/env python3
"""Project Euler #82 - Path sum: three ways (06/03/2023)"""

from dataclasses import dataclass

@dataclass
class vertex:
    x: int
    y: int
    val: int

class PriorityQueue:
    def __init__(self):
        self.q = []

    def insert(self, v, weight):
        i = 0
        while i < len(self.q) and self.q[i][1] < weight:
            i += 1
        self.q.insert(i, (v, weight))

    def pop(self):
        return self.q.pop(0)
    
    def is_empty(self):
        return len(self.q) == 0
    
    def get_weight(self, v):
        for u in self.q:
            if u[0] == v:
                return u[1]
    
    def reprioritise(self, v, new_weight):
        for u in self.q:
            if u[0] == v:
                self.q.remove(u)
                self.insert(v, new_weight)
                return

def get_input():
    with open('resources/p082_matrix.txt', 'r') as file:
        return [[int(x) for x in line.split(',')] for line in file.read().splitlines()]

def solve(matrix):
    # Useful observation: matrix is square
    n = len(matrix)

    # Convert the integer matrix into a grid of vertices
    for i in range(n):
        for j in range(n):
            matrix[i][j] = vertex(i, j, matrix[i][j])

    queue = PriorityQueue()

    colour = [[0 for i in range(n)] for j in range(n)]
    distance = [[0 for i in range(n)] for j in range(n)]

    # Start the algorithm by putting every vertex in the left column into the queue
    for i in range(n):
        v = matrix[i][0]
        colour[i][0] = 1
        queue.insert(v, v.val)

    while not queue.is_empty():
        u, u_dist = queue.pop()

        adjacent = []
        if u.x > 0:
            adjacent.append(matrix[u.x - 1][u.y])
        if u.x < n - 1:
            adjacent.append(matrix[u.x + 1][u.y])
        if u.y < n - 1:
            adjacent.append(matrix[u.x][u.y + 1])
        
        for adj in adjacent:
            adj_dist = u_dist + adj.val

            if colour[adj.x][adj.y] == 0:
                colour[adj.x][adj.y] = 1
                queue.insert(adj, adj_dist)
            elif colour[adj.x][adj.y] == 1 and queue.get_weight(adj) > adj_dist:
                queue.reprioritise(adj, adj_dist)
        
        colour[u.x][u.y] = 2
        distance[u.x][u.y] = u_dist

        if u.y == n - 1:
            # We got the last row, meaning this is the shortest path to it
            return u_dist

if __name__ == "__main__":
    print(solve(get_input()))
