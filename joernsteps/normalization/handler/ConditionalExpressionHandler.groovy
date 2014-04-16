class ConditionalExpressionHandler extends DefaultHandler {

	ConditionalExpressionHandler() {
		super(false, true);
	}

	String apply(node, children) {
		return "${children[0]} ? ${children[1]} : ${children[2]}"
	}
    
}
