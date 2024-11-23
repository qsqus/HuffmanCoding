from __future__ import annotations


class TreeNode:
    def __init__(self, label: str, value: float, left: TreeNode = None, right: TreeNode = None):
        self.label = label
        self.value = value
        self.children = (left, right)

    def __getitem__(self, index: int):
        if index < 0 or index > 1:
            raise IndexError('Index out of range')
        else:
            return self.children[index]

    def __len__(self):
        return len(self.children)

    def __str__(self):
        return f'({self.label}:{self.value}/{self[0]}-{self[1]})'

    def __repr__(self):
        return f'TreeNode(label={self.label}, value={self.value}, left={self[0]}, right={self[1]})'
