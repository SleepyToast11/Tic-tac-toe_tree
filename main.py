class Tree:

    class _Node:

        __slots__ = 'element', 'parent', 'child', 'depth'
        def __init__(self, parent, element, depth):
            self.parent = parent
            self.element = element
            self.child = []
            self.depth = depth

        def gameWon(self):
            arr = self.element
            for i in range(3):
                    if arr[3*i] == arr[3*i+1] == arr[3*i+2] != ' ':
                        return True
                    elif arr[0+i] == arr[3+i] == arr[6+i] != ' ':
                        return True
            if arr[0] == arr[4] == arr[8] != ' ':
                return True
            elif arr[2] == arr[4] == arr[6] != ' ':
                return True
            else:
                return False

        def game_status(self):
            if self.gameWon():
                if self.depth % 2 == 0:
                    return "O won!"
                else:
                    return "x won!"
            elif ' ' in self.element:
                return "Ongoing"
            else:
                return "Tie"

        def printTic(self):
            print(self.game_status())
            for j in range(9):
                if j % 3 == 0 and j is not 0:
                    print("\n_______")
                print(str(self.element[j]), end="")
                if (j + 1) % 3 != 0:
                    print("|", end="")
            print("\n\n")


    def __init__(self):
        self._root = self._Node(None, [' '] * 9, 0)

    def bfs(self):
        arr = [self._root]
        new_arr = []
        for node in arr:
            new_arr = new_arr + node.child
        for node in new_arr:
            node.printTic()
        input("press enter for next gen")
        self.bfs(new_arr)


    def dfs(self):
        arr = [0] * 9
        index = 0
        node = tree._root
        self.dfe(node)


    def dfe(self, node):
        for nodes in node.child:
            input("next\n")
            print("going down!")
            nodes.printTic()
            self.dfe(nodes)
            print("going up!")

    def bfs(self, arr):
        if arr is self._root:
            arr = [self._root]
        count = 0
        new_arr = []
        for node in arr:
            for i in node.child:
                count += 1
            new_arr = new_arr + node.child
        for node in new_arr:
            node.printTic()
        print(count)
        input("press enter for next gen")
        self.bfs(new_arr)


    counter = 0
    leaf_counter = 0
    def generateTree(self, node):
        self.counter += 1
        print("\n" + str(self.counter))
        node.printTic()
        if node.game_status() == "Tie" or node.gameWon():
            self.leaf_counter += 1
        if node.gameWon():
            return node
        if node.depth % 2 == 0:
            char = 'X'
        else:
            char = 'O'
        for i in range(9):
            if node.element[i] == ' ':
                temp = node.element[:]
                temp[i] = char
                tempNode = self._Node(node, temp, node.depth+1)
                self.generateTree(tempNode)
                if tempNode is not None:
                    node.child.append(tempNode)





tree = Tree()
tree.generateTree(tree._root)
print("Number of leaves: " + str(tree.leaf_counter))
tree.dfs()

input("hello")
input("helloj")

