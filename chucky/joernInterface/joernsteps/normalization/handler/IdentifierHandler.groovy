class IdentifierHandler extends DefaultHandler {

	def symbols;
	def except;
    
	IdentifierHandler(symb, excp) {
		super(true, true);
		symbols = symb
		except = excp;
	}
    
	String apply(node, children) {
		if (node.code in symbols) {
			return symbols[node.code];
		} else {
			return node.code;
		}
	}

	boolean store(String code) {
		return store && !(code in except);
	}    
	

}
