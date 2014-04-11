class BinaryOperationHandler {

    def prune = false;

    def execute(node, children) {
        return "( " + children[0] + " ${node.operator} " + children[1] + " )";
    };
}
