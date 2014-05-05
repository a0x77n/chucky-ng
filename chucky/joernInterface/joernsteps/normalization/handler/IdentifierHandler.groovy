class IdentifierHandler extends DefaultHandler {

	def args;
	def ret;
	def except;
    
	IdentifierHandler(arguments, return_value, excp) {
		super(true, true);
		args = arguments;
		ret = return_value;
		except = excp;
	}
    
	String apply(node, children) {
		if (ret.contains(node.code)) {
			return RET;
		} else if (args.contains(node.code)) {
			return ARG;
		} else {
			return node.code;
		}
	}

	boolean store(String code) {
		return store && !(code in except);
	}    
	

}
