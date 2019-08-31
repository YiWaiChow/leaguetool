from Champion.Champion import Champions


class Treenode:
    def __init__(self, score):
        self.score = score
        self.champlist = []
        self.left = None
        self.right = None
        self.height = 1

    def add_champ(self, champion):
        self.champlist.append(champion)

class ScoreAVLTree:
    "store score as a node in the tree, each node has a list of champion with that score"
    def insert(self, root, champion):
        if not root:
            x = Treenode(champion.get_score())
            x.add_champ(champion)
            return x
        elif champion.get_score() == root.score:
            root.add_champ(champion)
            return root
        elif champion.get_score() < root.score:
            root.left  = self.insert(root.left, champion)
        else:
            root.right  =self.insert(root.right, champion)
        root.height = 1 + max(self.getheight(root.left),self.getheight(root.right))
        bf = self.balance_factor(root)
        if bf > 1 and champion.get_score() < root.left.score:
            return self.rR(root)
        if bf <-1 and champion.get_score() > root.right.score:
            return self.lR(root)
        if bf > 1 and champion.get_score() >root.left.score:
            root.left = self.lr(root.left)
            return self.rR(root)
        if bf <-1 and champion.get_score() < root.right.score:
            root.right = self.rR(root.right)
            return self.lr(root)
        return root

    def balance_factor(self, root):
        if not root:
            return 0
        return self.get_height(root.right) - self.get_height(root.left)

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def lr(self, root):
        temp = root.right
        temp1 = temp.left
        temp.left = root
        root.right = temp1

        root.height = 1 +(max((self.getheight(root.left)), (self.getheight(root.right))))
        temp.height = 1 +(max((self.getheight(temp.left)), (self.getheight(temp.right))))
        return temp

    def rR(self, root):
        temp = root.left
        temp2 = temp.right
        temp.right = root
        root.left = temp2
        root.height = 1 + (max((self.getheight(root.left)), (self.getheight(root.right))))
        temp.height = 1 + (max((self.getheight(temp.left)), (self.getheight(temp.right))))

        return y

    def max_score(self, root):
        if not root:
            return None
        self.max_score(root.right)
        return root
