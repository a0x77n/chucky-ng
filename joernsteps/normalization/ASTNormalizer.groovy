class ASTNormalizer {

	def handlers;
	def defaultHandler;
	def expressions;

	ASTNormalizer() {
		handlers = [:];
		expressions = [];
		defaultHandler = new DefaultHandler(true, true);
	};

	def addHandler(String nodeType, Handler handler) {
		handlers[nodeType] = handler
	};
	
	def normalizeTree(root) {
		expressions = [];
		normalize(root, true);
		return expressions;
	}

	def normalize(node, store = false) {
		def handler;
		def children = node.children();
		def subexpr = [];
		def expr;
		if (node.type in handlers) {
			handler = handlers[node.type];
		} else {
			handler = defaultHandler;
		}
		if (children) {
			children.each() { child ->
				subexpr.add(normalize(child, store && !handler.prune()));
			}
		}
		expr = handler.apply(node, subexpr);
		if (store && handler.store()) {
			//expressions.add([expr, node.type]);
			expressions.add(expr);
		}
		return expr;
	};
};
