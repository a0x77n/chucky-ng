class ArithmeticOperationHandler extends DefaultHandler {

	ArithmeticOperationHandler() {
		super(false, true);
	}

	String apply(node, children) {
		if (children[0] == NUM && children[1] == NUM) {
			return NUM;
		} else {
			return "( ${children[0]} ${node.operator} ${children[1]} )";
		}
	}

}
