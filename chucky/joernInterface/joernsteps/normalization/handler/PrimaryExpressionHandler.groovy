class PrimaryExpressionHandler extends DefaultHandler {
	
	PrimaryExpressionHandler() {
		super(true, false);
	}

	String apply(node, children) {
		if (node.code.startsWith(/'/) || node.code.startsWith(/"/)) {
			return node.code;
		} else {
			return NUM;
		}
	}

}
