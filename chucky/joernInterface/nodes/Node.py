from joernInterface.JoernInterface import jutils

class Node(object):

    def __init__(self, node_id, properties = None):
        self.node_id = node_id
        self.properties = properties
        self.node_selection = 'g.v("{}")'.format(self.node_id)
        if not self.properties:
            self.load_properties()

    def __str__(self):
        return str(self.node_id)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.node_id == other.node_id

    def __ne__(self, other):
        return self.node_id != other.node_id

    def __hash__(self):
        return self.node_id

    def load_properties(self):
        _, node = jutils.raw_lookup(self.node_selection)[0]
        self.properties = node.get_properties()

    def get_property(self, label):
        if label in self.properties:
            return self.properties[label]
        else:
            return None

    @property
    def node_type(self):
        return self.get_property('type')
