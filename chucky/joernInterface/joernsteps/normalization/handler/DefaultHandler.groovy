class DefaultHandler implements Handler {

	static final String CMP = "\$CMP";
	static final String NUM = "\$NUM";

	boolean prune;
	boolean store;

	DefaultHandler(boolean prune, boolean store) {
		this.prune = prune;
		this.store = store;
	}

	String apply(node, children) {
		return node.code;
	};

	boolean prune(String code) {
		return prune;
	}

	boolean store(String code) {
		return store;
	}    

}
