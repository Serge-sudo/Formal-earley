from copy import deepcopy
from auxiliary_structures import *


class Earley_parser:
    def fit(self, start, terms, non_terms, rules_list):
        self.check_input_accuracy(start, terms, non_terms, rules_list)
        self.terms = terms
        self.non_terms = non_terms
        self.start = start
        self.non_terms.append("&")
        self.rules = dict()
        self.Buildrules(start, list(rules_list))
        self.vertices = dict()

    def check_input_accuracy(self, start, terms, non_terms, rules_list):
        if start not in non_terms:
            raise RuntimeError("Start must be non-terminal symbol.")
        if len(set(non_terms) & set(terms)) != 0:
            raise RuntimeError(
                "Set of terminal and non-terminal symbols should not intersect."
            )
        for rule in rules_list:
            rule_ = list(rule.split("->"))
            if len(rule_) != 2:
                raise RuntimeError(
                    "Rules should consist from two parts, divided by '->' symbol"
                )
            if len(rule_[0]) != 1:
                raise RuntimeError("LHS of rule shoud be one symbol")
            if rule_[0] not in non_terms:
                raise RuntimeError("Rules should start with non-terminal symbol")
            for char in rule_[1]:
                if char not in non_terms and char not in terms:
                    raise RuntimeError(f"Symbol '{char}' is not in symbols list.")

    def Buildrules(self, start, rules_list):
        for i in self.non_terms:
            self.rules[i] = set()
        for i in range(len(rules_list)):
            rule = Rule(i + 1, *rules_list[i].split("->"))
            self.rules[rule.left].add(rule)
        self.rules["&"].add(Rule(0, "&", start))

    def Predict(self, vertex_number):
        stack = []
        stack.extend(list(self.vertices[vertex_number]))
        done = set()
        while stack:
            item = stack.pop(0)
            if item in done:
                continue
            if item.dot_val in self.terms or item.dot_val == "":
                done.add(item)
                continue
            for rule in self.rules[item.dot_val]:
                if rule.left == item.dot_val:
                    new_item = state(rule.left, rule.right, 0, vertex_number, rule.id)
                    if new_item not in stack:
                        stack.append(new_item)
            done.add(item)
        if self.vertices[vertex_number] == done:
            return False
        else:
            self.vertices[vertex_number] = done
            return True

    def Complete(self, vertex_number):
        check = False
        res = set()
        for item in self.vertices[vertex_number]:
            if item.is_last:
                for expcect in self.vertices[item.root]:
                    if expcect.dot_val == item.left:
                        new_item = expcect.move_dot()
                        if (
                            new_item not in self.vertices[vertex_number]
                            and new_item not in res
                        ):
                            res.add(new_item)
                            check = True
        self.vertices[vertex_number].update(res)
        return check

    def Scan(self, vertex_number, symbol):
        self.vertices[vertex_number + 1] = set()
        for item in self.vertices[vertex_number]:
            if item.dot_val == symbol:
                self.vertices[vertex_number + 1].add(item.move_dot())

    def predict(self, word):
        self.vertices[0] = set()
        for rule in self.rules[self.start]:
            self.vertices[0].add(state(rule.left, rule.right, 0, 0, rule.id))
        while self.Predict(0) or self.Complete(0):
            continue
        for i in range(1, len(word) + 1):
            self.Scan(i - 1, word[i - 1])
            while self.Predict(i) or self.Complete(i):
                continue
        for item in self.vertices[len(word)]:
            if item.is_last and item.root == 0 and item.left == self.start:
                return True
        return False
