# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 19:51:48 2023

@author: user
"""


import heapq


def backtrace(parent, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


h_cost = {'Arad': 366,
          'Bucharest': 0,
          'Craiova': 160,
          'Dobreta': 242,
          'Fagaras': 176,
          'Lugoj': 244,
          'Mehadia': 241,
          'Oradea': 380,
          'Pitesti': 100,
          'Rimnicu': 193,
          'Sibiu': 253,
          'Timisoara': 329,
          'Zerind': 374}



class Graph:
    def __init__(self):
        self._graph = {}
        self._vertexNo = 0
    def add_vertex(self, v):
        if v in self._graph:
            print('The vertex Already Exsits!')
        else:
            self._graph[v] = []
            self._vertexNo += 1
    def add_edges(self, v1, v2, w=0):
        if v1 not in self._graph:
            print(f'{v1} does not exist in the graph!')
        elif v2 not in self._graph:
            print(f'{v2} does not exist in the graph!')
        else:
            self._graph[v1].append([v2, w])
            self._graph[v2].append([v1, w])
            
    def __len__(self):
        return len(self._graph)
    def __getitem__(self, v):
        return self._graph[v]
    def show_graph(self):
        return(self._graph)
            
               
graph = Graph()

graph.add_vertex('Arad')
graph.add_vertex('Zerind')
graph.add_vertex('Timisoara')
graph.add_vertex('Sibiu')
graph.add_vertex('Fagaras')
graph.add_vertex('Rimnicu')
graph.add_vertex('Oradea')
graph.add_vertex('Lugoj')
graph.add_vertex('Mehadia')
graph.add_vertex('Dobreta')
graph.add_vertex('Pitesti')
graph.add_vertex('Craiova')
graph.add_vertex('Bucharest')

graph.add_edges('Arad', 'Zerind', 75)   
graph.add_edges('Arad', 'Timisoara', 118)
graph.add_edges('Arad', 'Sibiu', 140)   
graph.add_edges('Sibiu', 'Fagaras', 99)
graph.add_edges('Sibiu', 'Rimnicu', 80)   
graph.add_edges('Sibiu', 'Oradea', 151)
graph.add_edges('Timisoara', 'Lugoj', 111)
graph.add_edges('Lugoj', 'Mehadia', 70)
graph.add_edges('Mehadia', 'Dobreta', 75)
graph.add_edges('Dobreta', 'Craiova', 120)
graph.add_edges('Rimnicu', 'Pitesti', 97)
graph.add_edges('Craiova', 'Rimnicu', 146)
graph.add_edges('Fagaras', 'Bucharest', 211)
graph.add_edges('Craiova', 'Pitesti', 138)
graph.add_edges('Bucharest', 'Pitesti', 101)
               


def AStar(graph, start, goal):
    frontier = []
    explored = set()
    parent = {}
    f_cost = {}
    result = 'fail'
    g_cost = {}
    g_cost[start] = 0
    f_cost[start] = g_cost[start] + h_cost[start]
    heapq.heappush(frontier, (f_cost[start], start))
    while frontier:
        heapq.heapify(frontier)
        current_node = heapq.heappop(frontier)
        explored.add(current_node[1])
        if current_node[1] == goal:
             print(frontier)
             return backtrace(parent, start, goal)
        for i in range(len(graph[current_node[1]])):
            child = graph[current_node[1]][i]
            if child[0] not in explored:
                if child[0] not in frontier:  
                    g_cost[child[0]] = g_cost[current_node[1]] + child[1]
                    f_cost[child[0]] = g_cost[child[0]] + h_cost[child[0]]
                    heapq.heappush(frontier, (f_cost, child[0]))
                    parent[child[0]] = current_node[1]
                elif child[0] in frontier:
                    new = child
                    value = g_cost[current_node[1]] + new[1] + h_cost[new[0]]
                    if f_cost[child[0]] > value:
                        parent[child[0]] = current_node[1]
                        f_cost[child[0]] = value
                        heapq.heappush(frontier, (f_cost[child[0]], child[0])) 
    return result          
                        
        
         
            
         
            
         
            
         
            
         
            
         
            
         
            
         