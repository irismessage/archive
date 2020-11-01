# Hierarchal skill tree example implementation.

class Skill():
    """Class for a skill  node.

    Has a sum xp value, with methods to increment or set it;
    tier on the hierarchy;
    etc (TODO)
    """

    def __init__(self, name, exp=None, level=None,
                 tier, transmit_coeff=None, absorb_coeff=None, links,
                 ):
        self.name = name
        if exp is not None:
            self.exp = exp
        else:
            self.exp = 0
        if level is not None:
            self.level = level
        else:
            self.level = 0

        default_coeff = 1
        default_transmit_coeff = default_coeff
        default_aborb_coeff = default_coeff
        
        self.transmit_coeff = transmit_coeff
        self.absorb_coeff = absorb_coeff

        # Function to  split links into ancestors and descendants
        self.parents = []
        self.children = []
        for link in links:
            if link.tier >= self.tier:
                self.parents.append(link)
            elif link.tier <= self.tier:
                self.children.append(link)
        
    def exp_up(self, value):
        self.exp += amount

    def exp_set(self, value):
        self.exp = value

    # TODO
    # What to use
    def compute_absorb(self, modify, value):
        return value

    def compute_transmit(self, modify, value):
        return value
    
    # Make cascade two functions or one with argument?

    def exp_cascade_down(self, source, node, value):
        node.exp_up(node.compute_absorb(node.absorb_coeff, value))

        if node.tier == 0:
            exp_cascade_up(source, node, value)
        else:
            for parent in node.parents:
                return exp_cascade_down(source, parent, value)

    def exp_cascade_up(self, source, node, value):
        value = node.compute_absorb(node.absorb_coeff, value)

        if node is source:
            node.exp_up(value)
        else:
            for child in node.children:
                return exp_cascade_up(source, child, value)

