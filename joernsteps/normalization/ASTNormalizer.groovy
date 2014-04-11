class ASTNormalizer {

    def handlers;
    def defaultHandler;
    def expressions;

	ASTNormalizer() {
	    handlers = [:];
	    expressions = [];
	    defaultHandler = new DefaultHandler();
	};

	def addHandler(nodeType, handler) {
	    handlers[nodeType] = handler
	};
	
	def normalizeTree(root) {
	    expressions = [];
	    normalize(root, true);
	    return expressions;
    }

	def normalize(node, store = false) {
	    def handler;
	    if (node.type in handlers) {
	        handler = handlers[node.type];
	    } else {
	        handler = defaultHandler;
	    }
		def children = node.children();
		def subexpr = [];
		def expr;
		if (children) {
		    children.each() { child ->
		        subexpr.add(normalize(child, store && !handler.prune));
		    };
		};
		expr = handler.execute(node, subexpr);
		if (store) {
	        //expressions.add([expr, node.type]);
	        expressions.add(expr);
	    }
		return expr;
	};
};
