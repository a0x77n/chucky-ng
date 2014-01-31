Gremlin.defineStep('subTrees', [Vertex, Pipe], {
	_()
	.out('IS_AST_PARENT')
	.loop(1){it.loops < 10}{true}
});

Gremlin.defineStep('taint', [Vertex, Pipe], {
	_()
	.copySplit(_().taintUpwards(), _().taintDownwards())
	.fairMerge()
});

Gremlin.defineStep('taintUpwards', [Vertex, Pipe], {
	_()
	.as('back')
	.copySplit(_().hasArguments(), _().isAssignedBy())
	.fairMerge()
	.loop('back'){true}{true}
	.dedup()
});

Gremlin.defineStep('taintDownwards', [Vertex, Pipe], {
	_()
	.as('back')
	.copySplit(_().isArgumentOf(), _().assigns())
	.fairMerge()
	.loop('back'){true}{true}
	.dedup()
});

Gremlin.defineStep('isArgumentOf', [Vertex, Pipe], {
	_()
	.in('USE')
	.filter{ it.type == 'Argument' }
	.in('IS_AST_PARENT')
	.loop(1){ it.object.out('USE').count() == 0 }
	.out('USE')
	.filter{ it.code != "" }
});

Gremlin.defineStep('assigns', [Vertex, Pipe], {
	_()
	.sideEffect{ symbol = it.code }
	.in('USE')
	.filter{ it.type != 'BasicBlock' }
	.out('IS_AST_PARENT')
	.loop(1){ true }{ it.object.type == 'AssignmentExpr' }
	.as('candidate')
	.outE('IS_AST_PARENT')
	.filter{it.n == '1' }
	.inV()
	.out('IS_AST_PARENT')
	.loop(1){true}{it.object.type == 'Identifier'}
	.filter{it.code.equals(symbol)}
	.back('candidate')
	.out('DEF')
	.filter{ it.code != "" }
});

Gremlin.defineStep('hasArguments', [Vertex, Pipe], {
	_()
	.sideEffect{ symbol = it.code }
	.in('USE')
	.filter{ it.type != 'BasicBlock' }
	.out('IS_AST_PARENT')
	.loop(1){true}{it.object.type == 'CallExpression'}
	.as('candidate')
	.out('IS_AST_PARENT')
	.filter{it.type == 'Identifier' && it.code.equals(symbol) }
	.back('candidate')
	.out('IS_AST_PARENT')
	.filter{ it.type == 'ArgumentList' }
	.out('IS_AST_PARENT')
	.filter{ it.type == 'Argument' }
	.out('USE')
	.filter{ it.code != "" }
});

Gremlin.defineStep('isAssignedBy', [Vertex, Pipe], {
	_()
	.sideEffect{ symbol = it.code }
	.in('DEF')
	.filter{ it.type == 'AssignmentExpr' }
	.in('IS_AST_PARENT')
	.out('USE')
	.filter{ it.code != "" }
});
