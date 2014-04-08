
class FunctionAPISymbols:
    
    def __init__(self, obj):
        self.obj = obj
    
    def getKey(self):
        return int(self.obj.node_id)
    
    def getFeatures(self):
        return self.obj.api_symbol_nodes()

    