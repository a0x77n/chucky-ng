class RelationalOperationHandler {

    def prune = false;

    def execute(node, children) {
        return "( " + children[0] + " \$CMP " + children[1] + " )";
    };
}
