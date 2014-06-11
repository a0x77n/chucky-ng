class UnaryOperatorHandler extends DefaultHandler {

	UnaryOperatorHandler() {
		super(true, false);
	}

	String apply(node, children) {
                return node.code
	};
}
