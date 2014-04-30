interface Handler {

	String apply(node, children);
	
	boolean prune();
	boolean store();

}
