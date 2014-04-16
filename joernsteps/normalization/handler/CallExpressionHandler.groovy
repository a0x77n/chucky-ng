class CallExpressionHandler extends DefaultHandler {

	CallExpressionHandler() {
		super(false, true);
	}

	def execute(node, children) {
		return "${children[0]} ( ${children[1]} )"
	};
    
}
