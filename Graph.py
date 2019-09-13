import queue

class Node:
    def __init__(self ,info):
        self.info = info
        self.visited = False
        self.tag = 0
        self.adj = dict()
        self.adj_weight = dict()

    def __eq__(self, other):
        if other is Node:
            return self.info == other.info
        return False

    def __lt__(self, other):
        if other is Node:
            return self.info < other.info
        return False

    def __hash__(self):
        return hash(self.info)



# class Edge:
#     def __init__(self, neighbor, info=None ):
#         self.info = info
#         self.neighbor = neighbor

class Graph:
    def __init__(self):
        self.nodes_dict = dict()
        self.nodes_list = list()
        self.arc_counted = 0

    def is_empty(self):
        return len(self.nodes_list )==0

    def add_vertex(self ,vertex):
        if vertex not in self.nodes_dict:
            node = Node(vertex)
            self.nodes_list.append(node)
            self.nodes_dict[vertex ] =node

    def remove_vertex(self ,vertex):
        if vertex in self.nodes_dict:
            node_v = self.nodes_dict[vertex]
            self.nodes_list.remove(node_v)
            del self.nodes_dict[vertex]
            for node in self.nodes_list:
                if vertex in node.adj:
                    del node.adj[vertex]
                    del node.adj_weight[vertex]

    def add_arc(self ,alfa ,beta ,weight):
        if beta != alfa and alfa in self.nodes_dict and beta in self.nodes_dict:
            node_a = self.nodes_dict[alfa]
            node_b = self.nodes_dict[beta]
            if beta not in node_a.adj:
                node_a.adj[beta] = node_b
                node_a.adj_weight[beta] = weight
                node_b.adj[alfa] = node_a
                node_b.adj_weight[alfa] = weight
                self.arc_counted += 1


    def remove_arc(self ,alfa ,beta):
        if beta != alfa and alfa in self.nodes_dict and beta in self.nodes_dict:
            node_a = self.nodes_dict[alfa]
            node_b = self.nodes_dict[beta]
            del node_a.adj[beta]
            del node_a.adj_weight[beta]
            del node_b.adj[alfa]
            del node_b.adj_weight[alfa]
            self.arc_counted -= 1

    def arc_count(self):
        return self.arc_counted

    def get_arc_weight(self, alfa, beta):
        if alfa in self.nodes_dict:
            node_a = self.nodes_dict[alfa]
            if beta in node_a.adj_weight:
                return node_a.adj_weight[beta]

    def get_neighbours(self, alfa):
        if alfa in self.nodes_dict:
            node_a = self.nodes_dict[alfa]
            return node_a.adj.keys()

    def ver_count(self):
        return len(self.nodes_list)

    def clear_marks(self):
        for node in self.nodes_list:
            node.visited = False

    def algo_DFS(self, alfa):
        self.clear_marks()
        dfs_list = list()
        to_visit = list()
        if alfa in self.nodes_dict:
            node_a = self.nodes_dict[alfa]
            to_visit.append(node_a)
            while len(to_visit) > 0:
                node = to_visit.pop()
                if node.visited:
                    continue
                node.visited = True
                dfs_list.append(node.info)
                for node2 in node.adj.values():
                    to_visit.append(node2)
        return dfs_list

    def algo_BFS(self, alfa):
        self.clear_marks()
        bfs_list = list()
        to_visit = list()
        if alfa in self.nodes_dict:
            node_a = self.nodes_dict[alfa]
            to_visit.append(node_a)
            while len(to_visit) > 0:
                node = to_visit.pop(0)
                if node.visited:
                    continue
                node.visited = True
                bfs_list.append(node.info)
                for node2 in node.adj.values():
                    to_visit.append(node2)
        return bfs_list


    def is_path(self, alfa, beta):
        dfs = self.algo_DFS(alfa)
        if beta in dfs:
            return True
        return False

    def algo_Dijkstra(self,alfa):
        if alfa not in self.nodes_dict:
            return dict()

        node_a = self.nodes_dict[alfa]
        self.clear_marks()
        distance = dict()
        visited = list()
        distance[alfa]=0
        node_a.visited = True
        visited.append(node_a)
        pq = queue.PriorityQueue()
        for node in node_a.adj.values():
            pq.put((node_a.adj_weight[node.info],node))
        while not pq.empty():
            cost, node = pq.get()
            if node.visited:
                continue
            node.visited = True
            distance[node.info] = cost

            for nd in node.adj.values():
                pq.put((node.adj_weight[nd.info]+cost, nd))

        return distance


