# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 16:02:02 2023

@author: user
"""

def backtrace(parent, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def BFS(graph, start, goal):
    frontier = []
    explored = set()
    parent = {}
    frontier.append(start)
    result = 'Fail'
    if start == goal:
        return start
    while frontier:
        current_node = frontier.pop(0)
        explored.add(current_node)
        for child in graph[current_node]:
            if (child not in frontier) or (child not in explored):
                if child == goal:
                    parent[child] = current_node
                    return backtrace(parent, start, goal)
                parent[child] = current_node
                frontier.append(child)
    return result


graph = {'s': ['a','b','c'],
         'a': ['s', 'd', 'e'],
         'b': ['s', 'f', 'g'],
         'c': ['s', 'h'],
         'd': ['a'],
         'e': ['a'],
         'f': ['b'],
         'g': ['b'],
         'h': ['c', 'i', 'j'],
         'i': ['h', 'k', 'L', 'm'],
         'j': ['h'],
         'k': ['i'],
         'l': ['i'],
         'm': ['i']}
