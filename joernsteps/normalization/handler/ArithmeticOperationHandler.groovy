class ArithmeticOperationHandler {

    def NUM = "\$NUM";
    
    def prune = false;

    def execute(node, children) {
        if (children[0] == NUM && children[1] == NUM) {
            return NUM;
        } else {
            return "( " + children[0] + " ${node.operator} " + children[1] + " )";
        }
    };
}
