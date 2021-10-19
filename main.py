# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Node:
    """ Simple node object, simulates the node of a neural network, but it is hardcoded """
    def __init__(self, threshold=None, input_node=False, input_value=0):
        self.threshold = threshold
        self.input_node = input_node
        self.input_value = input_value
        self.nodes = []

    def create_connection(self, node, weight):
        self.nodes.append((node, weight))

    def output(self):
        if self.input_node:
            return self.input_value
        
        value = 0
        for i, j in self.nodes:
            value += i.output() * j
            
        if value > self.threshold:
            return 1
        else:
            return 0


class A:
    """ Grouping of three node that compares three inputs and returns true if and only if 2 are active """
    def __init__(self, input1, input2, input3):
        self.sum_node = Node(1)
        self.dif_node = Node(2)
        
        self.sum_node.create_connection(input1, 1)
        self.sum_node.create_connection(input2, 1)
        self.sum_node.create_connection(input3, 1)

        self.dif_node.create_connection(input1, 1)
        self.dif_node.create_connection(input2, 1)
        self.dif_node.create_connection(input3, 1)

        self.res_node = Node(0)

        self.res_node.create_connection(self.sum_node, 1)
        self.res_node.create_connection(self.dif_node, -1)

    def output(self):
        return self.res_node.output()


class B:
    """ Grouping of three node that compares three inputs and returns true if and only if 1 is active """
    def __init__(self, input1, input2, input3):
        self.sum_node = Node(0)
        self.dif_node = Node(1)

        self.sum_node.create_connection(input1, 1)
        self.sum_node.create_connection(input2, 1)
        self.sum_node.create_connection(input3, 1)

        self.dif_node.create_connection(input1, 1)
        self.dif_node.create_connection(input2, 1)
        self.dif_node.create_connection(input3, 1)

        self.res_node = Node(0)

        self.res_node.create_connection(self.sum_node, 1)
        self.res_node.create_connection(self.dif_node, -1)

    def output(self):
        return self.res_node.output()


class C:
    """ Complex grouping of nodes, made of three A objects and one B object
        This object checks if the three given positions make a immediately winnable position (eg. XX* or O*O) """
    def __init__(self, x_list, o_list, e_list, pos1, pos2, pos3):
        self.ax = A(x_list[pos1], x_list[pos2], x_list[pos3])
        self.ao = A(o_list[pos1], o_list[pos2], o_list[pos3])
        self.be = B(e_list[pos1], e_list[pos2], e_list[pos3])

        self.ar = A(self.ax, self.ao, self.be)

    def output(self):
        return self.ar.output()


class Position:
    """ Helper object, used for creating the input nodes """
    def __init__(self, character):
        if character == "x":
            self.x = 1
            self.o = 0
            self.e = 0
        elif character == "o":
            self.x = 0
            self.o = 1
            self.e = 0
        else:
            self.x = 0
            self.o = 0
            self.e = 1


if __name__ == '__main__':
    # Read the input three lines into a single string
    text = input()
    text += input()
    text += input()

    # Populate a list with the 9 positions
    input_nodes = ["pass"]
    for char in text:
        input_nodes.append(Position(char))

    # Create nodes representing each possible input
    x = ["pass"]
    o = ["pass"]
    e = ["pass"]
    for pos in input_nodes[1:10]:
        x.append(Node("pass", True, pos.x))
        o.append(Node("pass", True, pos.o))
        e.append(Node("pass", True, pos.e))

    # Create C objects that check for all 8 lines
    c123 = C(x, o, e, 1, 2, 3)
    c456 = C(x, o, e, 4, 5, 6)
    c789 = C(x, o, e, 7, 8, 9)
    c147 = C(x, o, e, 1, 4, 7)
    c258 = C(x, o, e, 2, 5, 8)
    c369 = C(x, o, e, 3, 6, 9)
    c159 = C(x, o, e, 1, 5, 9)
    c357 = C(x, o, e, 3, 5, 7)

    # Create the output node that "sums" the outputs of all C objects
    output_node = Node(0)

    output_node.create_connection(c123, 1)
    output_node.create_connection(c456, 1)
    output_node.create_connection(c789, 1)
    output_node.create_connection(c147, 1)
    output_node.create_connection(c258, 1)
    output_node.create_connection(c369, 1)
    output_node.create_connection(c159, 1)
    output_node.create_connection(c357, 1)

    # Print result
    print(output_node.output())
