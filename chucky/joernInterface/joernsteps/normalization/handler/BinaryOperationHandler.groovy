class BinaryOperationHandler extends DefaultHandler {

	BinaryOperationHandler() {
		super(false, true);
	}

	String apply(node, children) {
		return "( ${children[0]} ${node.operator} ${children[1]} )";
	}

}
