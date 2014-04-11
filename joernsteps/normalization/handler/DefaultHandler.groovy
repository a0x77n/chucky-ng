class DefaultHandler {

    def prune = true;

    def execute(node, children) {
		return node.code + " [WARNING]";
    };
    
}
