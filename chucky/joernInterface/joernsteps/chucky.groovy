Gremlin.defineStep('argumentToAtomName', [Vertex,Pipe], {
	_()
	.children().loop(1){!(it.object.type in ['Identifier', 'MemberAccess', 'PtrMemberAccess'])}
});

Gremlin.defineStep('callToLVal', [Vertex,Pipe], {
	_()
	.parents().loop(1){true}{it.object.type == 'AssignmentExpr'}
	.lval()
});

Gremlin.defineStep('symbolToUsingConditions', [Vertex, Pipe], {
	_() // Symbol node
	.in('USE', 'DEF')
	.ifThenElse{it.type == 'Condition'}
		{it}
		{it.parents().loop(1){true}{it.object.type == 'Condition'}}
});

Gremlin.defineStep('taintUpwards', [Vertex, Pipe], {
	_() // Symbol node
	.copySplit(
		_(),
		_().in('DEF')
		.filter{it.isCFGNode == 'True'}
		.out('USE')
		.simplePath()
		.loop(4){it.loops < 5}{true}
	).fairMerge()
	.dedup()
});

Gremlin.defineStep('taintDownwards', [Vertex, Pipe], {
	_() // Symbol node
	.copySplit(
		_(),
		_().in('USE')
		.filter{it.isCFGNode == 'True'}
		.out('DEF')
		.simplePath()
		.loop(4){it.loops < 5}{true}
	).fairMerge()
	.dedup()
});
