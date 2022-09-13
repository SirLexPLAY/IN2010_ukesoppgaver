
class TreNode():
    
    def __init__(self, value):
        self.element = element
        self.parent = None
        self.children = []


class TreBinNode():

    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None


def depth(v):
    """
    Funksjonen tar inn en node v og returnerer dybden av noden.
    Roten har dybde 0, og et tomt tre har dybde -1.

    input: En node v
    output: Dybden av noden
    """
    if v == None:
        return -1
    return 1 + depth(v)


def height(v):
    """
    Funksjonen tar inn en node v og returnerer høyden av noden.
    Med andre ord den høyeste avstanden til en etterkommer,
    eller dybden av den høyeste løvnoden.
    Roten har høyde 0, og et tomt tre har høyde 0.

    input: En node v
    output: Høyden av noden
    """
    h = -1
    if v == None:
        return h
    
    for node in v.children:
        h = max(h, height(node))

    return h + 1


def preorder(v, func):
    """
    Preorder traversering. Utfører først en operasjon func på seg selv, så på barna sine.

    input: en node v, en funksjon func
    output: ?
    """
    func(v)
    for node in v.children:
        preorder(node)


def postorder(v, func):
    """
    Postorder travesering. Utfører først en operasjon på mest etterkommede barna, så på seg selv.

    input: en node v, en funksjon func
    output: ?
    """
    for node in v.children:
        postorder(node)
    func(v)


def insert(v, x):
        """
        Tar inn en v og en x og setter den i treet.

        input: En node v og et element x
        output: En oppdatert node v der en node som inneholder x er en etterkommer av v
        """
        if v == None:
            v = TreBinNode(x)
        elif v.element > x:
            v.left = v.insert(v.left, x)
        elif v.element < x:
            v.right = v.insert(v.right, x)
        return v


def search(v, x):
    """
    Tar inn en v og en x og søker etter den i treet.

    input: En node v og et element x
    output: En node med element x, None dersom ikke elementet finnes
    """
    if v == None:
        return None
    if v.element == x:
        return v
    if v.element > x:
        return search(v.left, x)
    if v.element < x:
        return search(v.right, x)