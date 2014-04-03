Gremlin.defineStep('filterVariables', [Vertex, Pipe], {
        _() // Identifer node
        .as('var')
        .parents()
        .filter{it.type == 'IdentifierDecl'}
        .back('variable')
});

Gremlin.defineStep('filterParameters', [Vertex, Pipe], {
        _() // Identifer node
        .as('param')
        .parents()
        .filter{it.type == 'Parameter'}
        .back('param')
});

Gremlin.defineStep('filterCallee', [Vertex, Pipe], {
        _() // Identifer node
        .as('callee')
        .parents()
        .filter{it.type == 'Callee'}
        .back('callee')
});

Gremlin.defineStep('identifierToType', [Vertex, Pipe], {
        _()
        .parents()
        .ithChildren('0')
        .filter{it.type == 'IdentifierDeclType' || it.type == 'ParameterType'}
});

Gremlin.defineStep('symbolToUsingConditions', [Vertex, Pipe], {
	_() // Symbol node
	.in('USE', 'DEF')
	.filter{it.type != 'BasicBlock'}
        .ifThenElse{it.type == 'Condition'}
		{it}
		{it.parents().loop(1){true}{it.object.type == 'Condition'}}
});

Gremlin.defineStep('functionToAPISymbolNodes', [Vertex, Pipe], {
	_() // Function node
	.functionToASTNodes()
	.filter{it.type == 'IdentifierDeclType' || it.type == 'ParameterType' || it.type == 'Callee'}
});

Gremlin.defineStep('calleeToArguments', [Vertex, Pipe], {
	_() // Callee node
	.parents()
	.ithChildren(0)
	//.filter{it.type == 'ArgumentList'}
        .children()
	.out('USE')
});

Gremlin.defineStep('calleeToReturnValue', [Vertex, Pipe], {
	_() // Callee node
	.statements()
	.out('DEF')
})

Gremlin.defineStep('taintUpwards', [Vertex, Pipe], {
	_() // Symbol node
	.in('DEF')
	.filter{it.isCFGNode == 'True'}
	.out('USE')
	.simplePath()
	.loop(4){it.loops < 5}{true}
	.dedup()
});

Gremlin.defineStep('taintDownwards', [Vertex, Pipe], {
	_() // Symbol node
	.in('USE')
	.filter{it.isCFGNode == 'True'}
	.out('DEF')
	.simplePath()
	.loop(4){it.loops < 5}{true}
	.dedup()
});
