class CastExpressionHandler extends DefaultHandler {

	CastExpressionHandler() {
		super(false, false);
	}

	String apply(node, children) {
		return "(${children[0]}) ( ${children[1]} )";
	};

}
