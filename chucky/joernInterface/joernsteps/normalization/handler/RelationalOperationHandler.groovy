class RelationalOperationHandler extends DefaultHandler {

	RelationalOperationHandler() {
		super(false, true);
	}

	String apply(node, children) {
		return "( ${children[0]} ${CMP} ${children[1]} )";
	}

}
