class ArgumentListHandler {

    def prune = true;

    def execute(node, children) {
		return children.join(", ");
    };
    
}
