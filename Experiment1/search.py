"""Implementation of the A* algorithm.

This file contains a skeleton implementation of the A* algorithm. It is a single
method that accepts the root node and runs the A* algorithm
using that node's methods to generate children, evaluate heuristics, etc.
This way, plugging in root nodes of different types, we can run this A* to
solve different problems.

"""


def Astar(root):
    """Runs the A* algorithm given the root node. The class of the root node
    defines the problem that's being solved. The algorithm either returns the solution
    as a path from the start node to the goal node or returns None if there's no solution.

    Parameters
    ----------
    root: Node
        The start node of the problem to be solved.

    Returns
    -------
        path: list of Nodes or None
            The solution, a path from the initial node to the goal node.
            If there is no solution it should return None
    """

    # Some helper pseudo-code:
    # 1. Create an empty fringe and add your root node (you can use lists, sets, heaps, ... )
    # 2. While the container is not empty:
    # 3.      Pop the best? node (Use the attribute `node.f` in comparison)
    # 4.      If that's a goal node, return node.get_path()
    # 5.      Otherwise, add the children of the node to the fringe
    # 6. Return None
    #
    # Some notes:
    # You can access the state of a node by `node.state`. (You may also want to store evaluated states)
    # You should consider the states evaluated and the ones in the fringe to avoid repeated calculation in 5. above.
    # You can compare two node states by node1.state == node2.state
    open_set = [root]
    close_set = []
    # ans = None
    while open_set:
        open_set.sort(key=lambda node: node.f)
        cur = open_set[0]
        open_set.remove(cur)
        if cur.is_goal():
            return cur.get_path()
        elif cur in close_set:
            continue
        else:
            close_set.append(cur)
            open_set.extend(cur.generate_children())

    return None