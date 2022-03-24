#
#   CS304
#   Assignment 3-tic-tac-toe
#   March 24 2022
#

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
                if j % 3 == 0 and j != 0:
                    print("\n_______")
                print(str(self.element[j]), end="")
                if (j + 1) % 3 != 0:
                    print("|", end="")
            print("\n\n")


    def __init__(self):
        self._root = self._Node(None, [' '] * 9, 0)


    def dfs(self):
        self._dsf_exit = False
        self._dfs_recur(self._root)


    _exit_recur = False

    def _dfs_recur(self, node):
        for nodes in node.child:
            prompt = input("type exit to exit. for next anything else: ")
            if prompt == 'exit':
                self._exit_recur = True
                return
            print("\ngoing down!")
            nodes.printTic()
            self._dfs_recur(nodes)
            if self._exit_recur:
                return
            print("going up!")

    def bfs(self):
        self._exit_recur = False
        self._bfs_recur([self._root])

    def _bfs_recur(self, arr):
        count = 0
        new_arr = []

        for node in arr:
            for i in node.child:
                count += 1
            new_arr = new_arr + node.child
        for node in new_arr:
            node.printTic()
        print("there is " + str(count) + " nodes in this generation\n")
        prompt = input("type 'exit' to exit, anything else for next gen: ")
        if prompt == 'exit':
            self._exit_recur = True
            return
        self._bfs_recur(new_arr)
        if self._exit_recur:
            return


    counter = 0
    leaf_counter = 0
    def generateTree(self, node, printfl):
        self.counter += 1
        if printfl:
            print("\n" + str(self.counter))
            node.printTic()
        if node.game_status() == "Tie":
            self.leaf_counter += 1
        if node.gameWon():
            self.leaf_counter += 1
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
                self.generateTree(tempNode, printfl)
                if tempNode is not None:
                    node.child.append(tempNode)





tree = Tree()
prompt = input("type 'yes' to print grids while generating, else nothing: ")
if prompt == 'yes':
    tree.generateTree(tree._root, True)
else:
    tree.generateTree(tree._root, False)
print("Number of leaves: " + str(tree.leaf_counter))
print("Number of nodes: " + str(tree.counter))
prompt = ''
while prompt != 'exit':
    prompt = input("\nwhat type of search would you like to perform bfs or dfs.\nType exit to exit: ")
    if prompt == 'bfs':
        tree.bfs()
    if prompt == 'dfs':
        tree.dfs()