class PassThroughHandler extends DefaultHandler {

	PassThroughHandler() {
		super(false, false);
	}

	String apply(node, children) {
		return children[0];
	};
    
}
