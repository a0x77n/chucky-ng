Gremlin.defineStep('filterParameters', [Vertex, Pipe], {
	_()
	.as('symbol')
	.in('DEF')
	.filter{ it.type == 'Parameter' }
	.back('symbol')
});

Gremlin.defineStep('filterIdentifiers', [Vertex, Pipe], {
	_()
	.as('symbol')
	.in('DEF')
	.filter{ it.type == 'IdentifierDecl' }
	.back('symbol')
});

Gremlin.defineStep('filterCallees', [Vertex, Pipe], {
	_()
	.sideEffect{ code = it.code }
	.as('symbol')
	.in('USE')
	.filter{ it.type != 'BasicBlock' }
	.out('IS_AST_PARENT')
	.loop(1){true}{it.object.type == 'CallExpression'}
	.out('IS_AST_PARENT')
	.filter{it.type == 'Identifier' && it.code.equals(code) }
	.back('symbol')
});

Gremlin.defineStep('isArgumentOf', [Vertex, Pipe], {
	_()
	.in('USE')
	.filter{ it.type == 'Argument' }
	.in('IS_AST_PARENT')
	.loop(1){ it.object.type != 'CallExpression' }
	.as('callExpression')
	.out('IS_AST_PARENT')
	.filter{ it.type == 'Identifier' }
	.sideEffect{ callee = it.code }
	.back('callExpression')
	.in('IS_AST_PARENT')
	.loop(1){true}{it.object.out('USE').count() > 0}
	.out('USE')
	.filter{ it.code == callee }
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
});

Gremlin.defineStep('isAssignedBy', [Vertex, Pipe], {
	_()
	.sideEffect{ symbol = it.code }
	.in('DEF')
	.filter{ it.type == 'AssignmentExpr' }
	.in('IS_AST_PARENT')
	.out('USE')
});

Gremlin.defineStep('symbolToUsingConditions', [Vertex, Pipe], {
	_()
	.in('USE', 'DEF')
	.filter{it.type != 'BasicBlock'}
        .ifThenElse{it.type == 'Condition'}
		{it}
		{it.in('IS_AST_PARENT').loop(1){true}{it.object.type == 'Condition'}}
});

Gremlin.defineStep('filterAPISymbols', [Vertex, Pipe], {
	_()
	.filter{it.type == 'IdentifierDeclType'
		|| it.type == 'ParameterType'
		|| (it.type == 'Identifier' && it.in.has('type', 'CallExpression'))}
});
