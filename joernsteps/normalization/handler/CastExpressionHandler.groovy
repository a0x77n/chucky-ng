class CastExpressionHandler {

    def prune = false;

    def execute(node, children) {
        return "(" + children[0] + ") ( " + children[1] + " )";
    };
}
