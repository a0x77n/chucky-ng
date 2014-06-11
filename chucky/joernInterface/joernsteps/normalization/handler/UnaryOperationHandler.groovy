class UnaryOperationHandler extends DefaultHandler {

        def symbols

	UnaryOperationHandler(symb) {
		super(false, true);
                symbols = symb
	}

	String apply(node, children) {
		if (node.code in symbols) {
			return symbols[node.code];
		} else if (children[0] == "!") {
			return children[1];
		} else {
			return "${children[0]}  ${children[1]}";
		}
	};

	boolean prune(String code) {
		return prune || !(code.startsWith('!'))
	}
}
