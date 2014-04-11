class PrimaryExpressionHandler {

    def NUM = "\$NUM";
    
    def prune = false;
    
    def execute(node, children) {
        if (node.code.startsWith(/'/) || node.code.startsWith(/"/)) {
			return node.code;
		} else {
			return NUM;
		};
    };
}
