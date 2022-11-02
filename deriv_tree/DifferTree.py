from Node import Node


class DifferTree:
    RootNode = None
    pos = 0

    def BuildTree(self, s):
        n = Node(s[self.pos])
        if self.IsOperation(n.data):
            self.pos += 1
            n.left = self.BuildTree(s)
            self.pos += 1
            n.right = self.BuildTree(s)
        else:
            n.left = None
            n.right = None
        return n

    def PrintTree(self, node, separator="", side="M"):
        if node is None:
            return
        print(f"{separator} [{side}] {node.data}")
        separator += '\t'
        self.PrintTree(node.left, separator, "L")
        self.PrintTree(node.right, separator, "R")

    # region Differ functions
    def Differ(self, node):
        if node is None:
            return
        result_node = None
        if node.data == '+':
            result_node = self.DiffSum(node)
        elif node.data == '-':
            result_node = self.DiffSub(node)
        elif node.data == '*':
            result_node = self.DiffProd(node)
        elif node.data == '/':
            result_node = self.DiffDiv(node)
        elif node.data == 'x':
            result_node = Node('1')
        return result_node

    def DiffSum(self, node):
        if node is None:
            return None

        resultNode = Node('+')
        resultNode.left = self.Differ(node.left)
        resultNode.right = self.Differ(node.right)
        return resultNode

    def DiffSub(self, node):
        if node is None:
            return None
        resultNode = Node('-')
        resultNode.left = self.Differ(node.left)
        resultNode.right = self.Differ(node.right)
        return resultNode

    # D(u*v) = D(u)*v+u*D(v)
    def DiffProd(self, node):
        if node is None:
            return None
        leftNode = Node('*')
        rightNode = Node('*')
        resultNode = Node('+')

        leftNode.left = self.Differ(node.left)
        leftNode.right = node.right
        resultNode.left = leftNode

        rightNode.left = node.left
        rightNode.right = self.Differ(node.right)
        resultNode.right = rightNode
        return resultNode

    # D(u/v) = D(u)/v-(u*D(v))/(v*v)
    def DiffDiv(self, node):
        if node is None:
            return None
        resultNode = Node('-')
        leftNode = Node('/')
        rightNode = Node('/')
        leftOfRightNode = Node('*')
        rightOfRightNode = Node('*')

        leftNode.left = self.Differ(node.left)
        leftNode.right = node.right
        resultNode.left = leftNode

        leftOfRightNode.left = node.left
        leftOfRightNode.right = self.Differ(node.right)
        rightNode.left = leftOfRightNode
        rightOfRightNode.left = node.right
        rightOfRightNode.right = node.right
        rightNode.right = rightOfRightNode
        resultNode.right = rightNode
        return resultNode

    def SimpleTree(self, node):
        resNode = self.RootNode
        resNode = self.SimpleNode(resNode)
        return resNode

    def SimpleNode(self, node):
        if node is None:
            return None
        resultNode = Node(node.data)
        resultNode.left = self.SimpleNode(node.left)
        resultNode.right = self.SimpleNode(node.right)
        if node.data == '+':
            if node.left.data == '0':
                resultNode = node.right
            elif node.right.data == '0':
                resultNode = node.left
        elif node.data == '-':
            if node.right.data == '0':
                resultNode = node.left
        elif node.data == '*':
            if node.left.data == '0':
                resultNode = node.left
            elif node.right.data == '0':
                resultNode = node.right
            elif node.left.data == '1':
                resultNode = node.right
            elif node.right.data == '1':
                resultNode = node.left
        elif node.data == '/':
            if node.left.data == '0':
                resultNode = node.left
            elif node.right.data == '1':
                resultNode = node.left
        return resultNode

    # endregion

    def NodeToInfixForm(self, rootNode):
        self.resString = None
        self.arrList = []
        self.NodeToInfix(rootNode)
        return self.arrList[0]

    def NodeToInfix(self, node):
        if node is None:
            return
        self.NodeToInfix(node.right)
        self.NodeToInfix(node.left)
        if '+-/*'.__contains__(node.data):
            a = self.arrList[len(self.arrList) - 1]
            b = self.arrList[len(self.arrList) - 2]
            del self.arrList[-2:]
            self.arrList.append("(" + a + node.data + b + ")")
        else:
            self.arrList.append(node.data)

    def IsOperation(self, symbol):
        return symbol == '/' or symbol == '*' or symbol == '+' or symbol == '-'
