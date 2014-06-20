class CalleeHandler extends DefaultHandler {

	CalleeHandler() {
		super(true, false);
	}

	String apply(node, children) {
		return node.code
	};
    
}
