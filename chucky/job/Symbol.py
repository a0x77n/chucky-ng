
class Symbol:
    def __init__(self):
        pass
    
    def setName(self, name):
        self.target_name = name

    def setType(self, aType):
        self.target_type = aType
        
    def __hash__(self):
        return hash(self.target_name) ^\
            hash(self.target_type) ^\
            hash(self.target_decl_type)
      
    def setDeclType(self, declType):
        self.target_decl_type = declType
