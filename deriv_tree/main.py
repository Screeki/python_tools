from DifferTree import DifferTree


def main():
    formula = input('Enter formula')
    differ_tree = DifferTree()
    differ_tree.RootNode = differ_tree.BuildTree(formula)

    infixForm = differ_tree.NodeToInfixForm(differ_tree.RootNode)
    print(infixForm)

    differ_tree.PrintTree(differ_tree.RootNode)

    differ_tree = DifferTree()
    differ_tree.RootNode = differ_tree.BuildTree(formula)

    differ_tree.RootNode = differ_tree.Differ(differ_tree.RootNode)
    differ_tree.PrintTree(differ_tree.RootNode)

    differ_tree.RootNode = differ_tree.SimpleTree(differ_tree.RootNode)
    differ_tree.PrintTree(differ_tree.RootNode)

    infixForm = differ_tree.NodeToInfixForm(differ_tree.RootNode)
    print(infixForm)


if __name__ == '__main__':
    main()
