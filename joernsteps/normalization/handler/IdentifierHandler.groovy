class IdentifierHandler extends DefaultHandler {

	def args;
	def ret;
    
	IdentifierHandler(arguments, return_value) {
		super(true, true);
		args = arguments;
		ret = return_value;
	}
    
	def execute(node, children) {
		if (ret.contains(node.code)) {
			return RET;
		} else if (args.contains(node.code)) {
			return ARG;
		} else {
			return node.code;
		}
	}

}
