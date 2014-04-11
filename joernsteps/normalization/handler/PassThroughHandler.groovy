class PassThroughHandler {

    def prune = false;

    def execute(node, children) {
		return children[0];
    };
    
}
