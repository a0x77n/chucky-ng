class CallExpressionHandler extends DefaultHandler {

	CallExpressionHandler() {
		super(false, false);
	}

	String apply(node, children) {
		return "${children[0]} ( ${children[1]} )"
	};
    
}
