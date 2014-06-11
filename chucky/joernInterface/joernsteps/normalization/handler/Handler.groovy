interface Handler {

	String apply(node, children);
	
	boolean prune(String code);
	boolean store(String code);

}
