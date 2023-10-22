from cherry_types import *


class baseNode:
    def __init__(self, type, value, children):
        self.type = type
        self.value = value
        self.children = children
        
    def add_child(self, child):
        self.children.append(child)

class NumberNode(baseNode):
    def __init__(self, value):
        super().__init__("NUMBER", value, None)

class AddNode(baseNode):
    def __init__(self, children):
        super().__init__("OPERATOR",operator_name["+"], parent, children)

class SubNode(baseNode):
    def __init__(self, children):
        super().__init__("OPERATOR",operator_name["-"], parent, children)