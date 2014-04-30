class ArrayIndexingHandler extends DefaultHandler {

	ArrayIndexingHandler() {
		super(false, true);
	}

	String apply(node, children) {
		return "${children[0]} [${children[1]}]";
	}
    
}
