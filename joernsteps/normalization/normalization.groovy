Gremlin.defineStep('normalize', [Vertex, Pipe], { args, ret ->
    def normalizer = new ASTNormalizer();
    def handler;
    
    handler = new DefaultHandler();
    normalizer.addHandler('IncDec', handler);
    
    handler = new IdentifierNodeHandler(args, ret);
    normalizer.addHandler('Identifier', handler);
    normalizer.addHandler('PtrMemberAccess', handler);
    normalizer.addHandler('MemberAccess', handler);
    
    handler = new PassThroughHandler();
    normalizer.addHandler('Argument', handler);
    normalizer.addHandler('Callee', handler);
    normalizer.addHandler('Condition', handler);
    
    handler = new ArgumentListHandler()
    normalizer.addHandler('ArgumentList', handler);
    
    handler = new CastExpressionHandler()
    normalizer.addHandler('CastExpression', handler);
    
    handler = new BinaryOperationHandler()
    normalizer.addHandler('AndExpression', handler);
    normalizer.addHandler('BitAndExpression', handler);
    normalizer.addHandler('InclusiveOrExpression', handler);
    normalizer.addHandler('ExclusiveOrExpression', handler);
    normalizer.addHandler('OrExpression', handler);
    normalizer.addHandler('ShiftExpression', handler);
    normalizer.addHandler('AndExpression', handler);
    
    handler = new RelationalOperationHandler()
    normalizer.addHandler('RelationalExpression', handler);
    normalizer.addHandler('EqualityExpression', handler);
    
    handler = new ArithmeticOperationHandler()
    normalizer.addHandler('AdditiveExpression', handler);
    normalizer.addHandler('MultiplicativeExpression', handler);
    
    handler = new PrimaryExpressionHandler()
    normalizer.addHandler('PrimaryExpression', handler);
    
    handler = new CallExpressionHandler()
    normalizer.addHandler('CallExpression', handler);
    
    handler = new AssignmentExpressionHandler()
    normalizer.addHandler('AssignmentExpr', handler);
    
    handler = new ArrayIndexingHandler()
    normalizer.addHandler('ArrayIndexing', handler);
    
    handler = new ConditionalExpressionHandler()
    normalizer.addHandler('ConditionalExpression', handler);
	_().transform{ normalizer.normalizeTree(it) }.scatter()
});
