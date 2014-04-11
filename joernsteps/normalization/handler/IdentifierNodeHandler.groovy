class IdentifierNodeHandler {

    def ARG = "\$ARG";
    def RET = "\$RET";
    
    def prune = true;
    
    def args;
    def ret;
    
    IdentifierNodeHandler(arguments, return_value) {
        args = arguments;
        ret = return_value;
    };
    
    def execute(node, children) {
        if (ret.contains(node.code)) {
		    return RET;
	    } else if (args.contains(node.code)) {
		    return ARG;
	    } else {
		    return node.code;
	    };
    };
}
