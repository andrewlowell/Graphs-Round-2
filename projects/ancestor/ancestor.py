
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
    def values(self):
        return self.stack

def earliest_ancestor(ancestors, starting_node):
    print(f"Starting earliest ancestor search, starting node is {starting_node}")
    relationships = {}
    for a in ancestors:
      if not a[1] in relationships:
        relationships[a[1]] = set()
      relationships[a[1]].add(a[0])
      if not a[0] in relationships:
        relationships[a[0]] = set()

    # Return -1 if the starting node doesn't have any parents
    if len(relationships[starting_node]) == 0:
      return -1

    s = Stack()
    path = Stack()
    paths = []
    visited = set()
    s.push(starting_node)

    while s.size() > 0:
      v = s.pop()
      visited.add(v)
      path.push(v)

      # If the current node does have parents
      if len(relationships[v]) > 0:
        for a in relationships[v]:
          s.push(a)
      # If the current node has no parents
      else:
        paths.append((v, path.size()))
        path.pop()

    solution = None
    for p in paths:
      if not solution:
        solution = p
      if p[1] == solution[1]:
        if p[0] < solution[0]:
          solution = p
      elif p[1] > solution[1]:
        solution = p

    return solution[0]