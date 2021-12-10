class Rule:
    def __init__(self, id, left, right):
        self.id = id
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.id) + ":" + self.left + ":" + self.right


class state:
    def __init__(self, left, right, dot_pos, root, id):
        self.id = id
        self.left = left
        self.right = right
        self.dot_pos = dot_pos
        self.root = root
        self.dot_val = (
            self.right[self.dot_pos] if self.dot_pos < len(self.right) else ""
        )
        self.is_last = 1 if self.dot_pos == len(self.right) else 0

    def move_dot(self):
        return state(
            self.left,
            self.right,
            min(self.dot_pos + 1, len(self.right)),
            self.root,
            self.id,
        )

    def next_sym(self):
        return self.right[self.dot_pos + 1]

    def __hash__(self):
        return hash(
            self.left
            + "->"
            + self.right[: self.dot_pos]
            + "."
            + self.right[self.dot_pos :]
            + ","
            + str(self.root)
        )

    def __eq__(self, other):
        if (
            self.left == other.left
            and self.right == other.right
            and self.dot_pos == other.dot_pos
            and self.root == other.root
            and self.dot_val == other.dot_val
            and self.is_last == other.is_last
            and self.id == other.id
        ):
            return True
        else:
            return False

    def __repr__(self):
        return (
            self.left
            + "->"
            + self.right[: self.dot_pos]
            + "."
            + self.right[self.dot_pos :]
            + ","
            + str(self.root)
        )


class Vertex:
    def __init__(self, states):
        self.states = states

    def __hash__(self):
        return hash(str(self.states))

    def __eq__(self, other):
        if self.states == other.states:
            return True
        else:
            return False
