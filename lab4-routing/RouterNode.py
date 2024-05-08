#!/usr/bin/env python
import GuiTextArea, RouterPacket, F
from copy import deepcopy
from tabulate import tabulate


class RouterNode():
    myID = None
    myGUI = None
    sim = None
    costs = None

    # Access simulator variables with:
    # self.sim.POISONREVERSE, self.sim.NUM_NODES, etc.

    # --------------------------------------------------
    def __init__(self, ID, sim, costs):
        self.myID = ID
        self.sim = sim

        # list is to store the next node for each destination in the routing table.
        self.next_node = [i for i in range(sim.NUM_NODES)]

        self.myGUI = GuiTextArea.GuiTextArea("  Output window for Router #" + str(ID) + "  ")
        self.costs = deepcopy(costs)

        # fill distance vector with infinity
        self.distance_vector = [[sim.INFINITY] * sim.NUM_NODES for i in range(sim.NUM_NODES)]
        self.distance_vector[self.myID] = self.costs


    # --------------------------------------------------
    def recvUpdate(self, pkt):
        """
        Called when a node receives an update from one of its neighbors.

        Updates the distance vector with the received minimum costs,
        performs the Bellman-Ford algorithm, and updates the neighbors if the costs have been changed.
        """

        # id of source packet 
        source = pkt.sourceid

        minimum_cost = pkt.mincost

        # update the minimum cost for the packet
        self.distance_vector[source] = minimum_cost

        # create a deep copy to compare before and after bellman ford
        cost = deepcopy(self.costs)

        # run the bellman ford algorithm
        self.bellman_ford_algorithm()

        #check if the cost has been updated
        if not self.costs == cost:
            self.update_neighbour_with_new_distance_vector()


    def update_neighbour_with_new_distance_vector(self):
        """
        Updates neighbors with new distance vectors if the distance vector for the router has changed.
        """

        # Send update to neighbors if the distance vector for router i has changed
        for i in range(self.sim.NUM_NODES):

            # check so the node isn't itself and that there is a path from the current node to node i
            if not (i == self.myID and self.distance_vector[self.myID][i] == self.sim.INFINITY): 
                packet = RouterPacket.RouterPacket(self.myID, i, self.create_distance_vector(i))

                # send the update to the neighbour node
                self.sendUpdate(packet)


    def create_distance_vector(self, destination_node):
        """
        Creates a distance vector for a destination, considering poison reverse if enabled.
        """

        # list to represent a distance vector
        distance_vector = []

        # iterate over all the nodes
        for i in range(self.sim.NUM_NODES):

            # check if poison reverse is enabled and if the next node is the destination node
            if self.sim.POISONREVERSE and self.next_node[i] == destination_node:

                # the route from the node to destination node should be considered unreachable
                distance_vector.append(self.sim.INFINITY)

            else:
                # add the cost to reach the destination node
                distance_vector.append(self.costs[i])

        return distance_vector


    def bellman_ford_algorithm(self):
        """
        Performs the Bellman-Ford algorithm to calculate the shortest paths and update costs and next hop.
        Source for implementation of algorithm: https://www.geeksforgeeks.org/bellman-ford-algorithm-in-python/
        """

        # initialize distances
        distances = [self.sim.INFINITY for i in range(self.sim.NUM_NODES)]
        distances[self.myID] = 0
        
        next_node = [self.myID for i in range(self.sim.NUM_NODES)]

        # maximum number of iterations required to guarantee that the shortest paths are found
        for i in range(self.sim.NUM_NODES - 1):
            for u in range(self.sim.NUM_NODES):
                for v in range(self.sim.NUM_NODES):

                    if self.distance_vector[u][v] != self.sim.INFINITY and distances[u] + self.distance_vector[u][v] < distances[v]:
                        # update cost with shorter path
                        distances[v] = distances[u] + self.distance_vector[u][v]

                        # determine the next hop based on the shortest path
                        # if distances[u] is 0, it means that the source node u itself is the destination v,
                        # so next_node[v] is set to v
                        if distances[u] == 0:
                            next_node[v] = v

                        # else set the next hop to the node along the shortest path
                        else:
                            next_node[v] = u

        # check for negative weight cycles, the presence of a negative weight cycle means that there is no shortest path.
        # one could continuously traverse the cycle to decrease the path's weight indefinitely.
        for u in range(self.sim.NUM_NODES):
            for v in range(self.sim.NUM_NODES):

                if self.distance_vector[u][v] != self.sim.INFINITY and distances[u] + self.distance_vector[u][v] < distances[v]:
                    raise ValueError("Graph contains negative weight cycle")

        # update
        self.costs = distances
        self.next_node = next_node
        


    # --------------------------------------------------
    def sendUpdate(self, pkt):
        """
        Sends updates to other routers via the simulator.
        """

        self.sim.toLayer2(pkt)



    # --------------------------------------------------
    def printDistanceTable(self):
        """
        Prints the distance table for the router, including the distance vector and routes.
        """
        
        # print current router and time
        self.myGUI.println("Current state for " + str(self.myID) + " at time " + str(self.sim.getClocktime()) + "\n")

        # print the destination node as headers for each column
        self.myGUI.println("Distance table:")
        column_headers = ["Destination node"] + [str(i) for i in range(self.sim.NUM_NODES)]

        # create a list containing 
        table_data = []
        for i in range(self.sim.NUM_NODES):
            temp = [f"neighbour {i}"] + self.distance_vector[i]
            table_data.append(temp)

        # create a table with tabulate of the column headers and the data
        table = tabulate(table_data, headers=column_headers, tablefmt="fancy_grid")
        self.myGUI.println(table + "\n")

        # physical cost to each of the neighbors and the minimum distance vectors received from neighboring nodes
        self.myGUI.println("Our distance vector and routes:")
        data = [["costs"] + self.costs] + [["route"] + self.next_node]

        # create a table with tabulate of the column headers and the data
        cost_table = tabulate(data, headers=column_headers, tablefmt="fancy_grid")
        self.myGUI.println(cost_table + "\n")
        


    # --------------------------------------------------
    def updateLinkCost(self, destination_node, new_cost):
        """
        Called when the cost of a link of a node is about to change.
        Updates the distance vector, performs Bellman-Ford, and updates neighbors if costs have changed.
        Method is run RouterSimulator file.
        """

        self.distance_vector[self.myID][destination_node] = new_cost
        cost = deepcopy(self.costs)
        self.bellman_ford_algorithm()

        # check if the cost has been updated after running the bellman ford
        if not self.costs == cost:
            self.update_neighbour_with_new_distance_vector()
