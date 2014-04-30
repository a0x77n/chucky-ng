class CallExpressionHandler extends DefaultHandler {

	CallExpressionHandler() {
		super(false, true);
	}

	String apply(node, children) {
		return "${children[0]} ( ${children[1]} )"
	};
    
}
