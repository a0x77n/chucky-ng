class AssignmentExpressionHandler extends DefaultHandler {

	AssignmentExpressionHandler() {
		super(false, true);
	}

	String apply(node, children) {
		return "${children[0]} = ${children[1]}";
	}
    
}
