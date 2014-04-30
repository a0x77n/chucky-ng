class ArgumentListHandler extends DefaultHandler {
	
	ArgumentListHandler() {
		super(true, false)
	}

	String apply(node, children) {
		return children.join(", ");
	};
    
}
