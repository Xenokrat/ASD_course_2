from typing import Optional, List


class BSTNode:

    def __init__(self, key: int, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self) -> None:
        self.Node = None # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node: Optional[List]) -> None:
        self.Root = node

    def FindNodeByKey(self, key: int) -> BSTFind:
        # ищем в дереве узел и сопутствующую информацию по ключу
        return None # возвращает BSTFind

    def AddKeyValue(self, key: int, val) -> Optional[bool]:
        # добавляем ключ-значение в дерево
        return False # если ключ уже есть

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
        # ищем максимальный/минимальный ключ в поддереве
        return None

    def DeleteNodeByKey(self, key: int) -> Optional[bool]:
        # удаляем узел по ключу
        return False # если узел не найден

    def Count(self) -> int:
        if self.Root is None:
            return 0

        def _count(node: BSTNode) -> int:
            if node is None:
                return 0
            return _count(node.LeftChild) + _count(node.RightChild) + 1

        return _count(self.Root)

