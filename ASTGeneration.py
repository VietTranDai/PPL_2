"""
 * Initial code for Assignment 1, 2
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 07.01.2025
"""
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce
from dataclasses import dataclass

class ASTGeneration(MiniGoVisitor):
    # Visit a MiniGo program consisting of one or more declarations followed by EOF.
    def visitProgram(self, ctx: MiniGoParser.ProgramContext):
        decls = [self.visit(d) for d in ctx.decl()]
        return Program(decl=decls)

    # Visit a declaration, which can be a main function, variable, constant, type, or function declaration.
    def visitDecl(self, ctx: MiniGoParser.DeclContext):
        if ctx.mainFuncDecl():
            return self.visit(ctx.mainFuncDecl())
        elif ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl())
        elif ctx.typedecl():
            return self.visit(ctx.typedecl())
        elif ctx.funcdecl():
            return self.visit(ctx.funcdecl())
        return None

    # Visit the main function declaration: 'func main() block' with no parameters and no return type.
    def visitMainFuncDecl(self, ctx: MiniGoParser.MainFuncDeclContext):
        body = self.visit(ctx.block())
        return FuncDecl(name="main", params=[], retType=VoidType(), body=body)

    # Visit a variable declaration: 'var IDENTIFIER (typeDef [ = expr ] | = expr) ;'.
    def visitVardecl(self, ctx: MiniGoParser.VardeclContext):
        varName = ctx.IDENTIFIER().getText()
        if ctx.typeDef():
            varType = self.visit(ctx.typeDef())
            varInit = self.visit(ctx.expr()) if ctx.expr() else None
        else:
            varType = None
            varInit = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(varName, varType, varInit)

    # Visit a constant declaration: 'const IDENTIFIER = expr ;'.
    def visitConstdecl(self, ctx: MiniGoParser.ConstdeclContext):
        conName = ctx.IDENTIFIER().getText()
        iniExpr = self.visit(ctx.expr())
        return ConstDecl(conName, None, iniExpr)

    # Visit a type declaration: 'type IDENTIFIER typeDef ;?'.
    def visitTypedecl(self, ctx: MiniGoParser.TypedeclContext):
        typeName = ctx.IDENTIFIER().getText()
        typeDef = self.visit(ctx.typeDef())

        # Handle different cases of typeDef
        if isinstance(typeDef, (IntType, FloatType, BoolType, StringType, VoidType)):
            return typeDef
        elif isinstance(typeDef, StructType):
            return StructType(name=typeName, elements=typeDef.elements, methods=typeDef.methods)
        elif isinstance(typeDef, InterfaceType):
            return InterfaceType(name=typeName, methods=typeDef.methods)
        elif isinstance(typeDef, ArrayType):
            return typeDef
        elif isinstance(typeDef, Id):
            return Id(typeName)
        else:
            return typeDef

    # Visit a function declaration: 'func [(receiver)] IDENTIFIER (paramList?) typeDef? block ;'.
    def visitFuncdecl(self, ctx: MiniGoParser.FuncdeclContext):
        if ctx.receiver():
            recName, recType = self.visit(ctx.receiver())
            funName = ctx.IDENTIFIER().getText()
            params = self.visit(ctx.paramList()) if ctx.paramList() else []
            retType = self.visit(ctx.typeDef()) if ctx.typeDef() else VoidType()
            body = self.visit(ctx.block())
            func = FuncDecl(name=funName, params=params, retType=retType, body=body)
            return MethodDecl(receiver=recName, recType=recType, fun=func)
        else:
            funName = ctx.IDENTIFIER().getText()
            params = self.visit(ctx.paramList()) if ctx.paramList() else []
            retType = self.visit(ctx.typeDef()) if ctx.typeDef() else VoidType()
            body = self.visit(ctx.block())
            return FuncDecl(name=funName, params=params, retType=retType, body=body)

    # Visit a receiver: 'IDENTIFIER IDENTIFIER' for method declarations.
    def visitReceiver(self, ctx: MiniGoParser.ReceiverContext):
        recName = ctx.IDENTIFIER(0).getText()
        recType = Id(ctx.IDENTIFIER(1).getText())
        return (recName, recType)

    # Visit a parameter list: 'param (, param)*'.
    def visitParamList(self, ctx: MiniGoParser.ParamListContext):
        params = []
        for p in ctx.param():
            params.extend(self.visit(p))
        return params

    # Visit a parameter: 'IDENTIFIER (, IDENTIFIER)* typeDef'.
    def visitParam(self, ctx: MiniGoParser.ParamContext):
        idents = [id.getText() for id in ctx.IDENTIFIER()]
        parType = self.visit(ctx.typeDef())
        return [ParamDecl(parName=name, parType=parType) for name in idents]

    # Visit a type definition: can be a basic type, struct, interface, array, or identifier.
    def visitTypeDef(self, ctx: MiniGoParser.TypeDefContext):
        if ctx.basictype():
            return self.visit(ctx.basictype())
        elif ctx.structType():
            return self.visit(ctx.structType())
        elif ctx.interfaceType():
            return self.visit(ctx.interfaceType())
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return None

    # Visit a basic type: 'int', 'float', 'string', or 'boolean'.
    def visitBasictype(self, ctx: MiniGoParser.BasictypeContext):
        if ctx.INT_TYPE():
            return IntType()
        elif ctx.FLOAT_TYPE():
            return FloatType()
        elif ctx.STRING_TYPE():
            return StringType()
        elif ctx.BOOLEAN_TYPE():
            return BoolType()
        return None

    # Visit a struct type: 'struct { fieldList+ }'.
    def visitStructType(self, ctx: MiniGoParser.StructTypeContext):
        fields = []
        for fl in ctx.fieldList():
            fields.extend(self.visit(fl))
        return StructType(name="", elements=fields, methods=[])

    # Visit a field list: 'field (; field)* ;'.
    def visitFieldList(self, ctx: MiniGoParser.FieldListContext):
        return [self.visit(f) for f in ctx.field()]

    # Visit a field: 'IDENTIFIER typeDef'.
    def visitField(self, ctx: MiniGoParser.FieldContext):
        fieldName = ctx.IDENTIFIER().getText()
        fieldType = self.visit(ctx.typeDef())
        return (fieldName, fieldType)

    # Visit an interface type: 'interface { methodList+ }'.
    def visitInterfaceType(self, ctx: MiniGoParser.InterfaceTypeContext):
        methods = []
        for ml in ctx.methodList():
            methods.extend(self.visit(ml))
        return InterfaceType(name="", methods=methods)

    # Visit a method list: 'method (; method)* ;'.
    def visitMethodList(self, ctx: MiniGoParser.MethodListContext):
        return [self.visit(m) for m in ctx.method()]

    # Visit a method signature: 'IDENTIFIER (method_param_opt) method_type_opt'.
    def visitMethod(self, ctx: MiniGoParser.MethodContext):
        name = ctx.IDENTIFIER().getText()
        params = self.visit(ctx.method_param_opt()) if ctx.method_param_opt() else []
        retType = self.visit(ctx.method_type_opt()) if ctx.method_type_opt() else VoidType()
        return Prototype(name, params, retType)

    # Visit optional method parameters: 'paramList?'.
    def visitMethod_param_opt(self, ctx: MiniGoParser.Method_param_optContext):
        if ctx.paramList():
            plist = self.visit(ctx.paramList())
            return [p.parType for p in plist]  # Extract types for method prototype
        return []

    # Visit optional method return type: 'typeDef | empty'.
    def visitMethod_type_opt(self, ctx: MiniGoParser.Method_type_optContext):
        if ctx.typeDef():
            return self.visit(ctx.typeDef())
        return VoidType()

    # Visit an array type: 'dim+ typeDef'.
    def visitArrayType(self, ctx: MiniGoParser.ArrayTypeContext):
        dims = [self.visit(d) for d in ctx.dim()]
        eleType = self.visit(ctx.typeDef())
        return ArrayType(dims, eleType)

    # Visit an array dimension: '[ intExpr ]'.
    def visitDim(self, ctx: MiniGoParser.DimContext):
        return self.visit(ctx.intExpr())

    # Visit an integer expression: 'INT | IDENTIFIER'.
    def visitIntExpr(self, ctx: MiniGoParser.IntExprContext):
        if ctx.INT():
            return IntLiteral(int(ctx.INT().getText()))
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        return None

    # Visit a block: '{ stmt_list }'.
    def visitBlock(self, ctx: MiniGoParser.BlockContext):
        stmts = []
        if ctx.stmt_list():
            stmts = [self.visit(s) for s in ctx.stmt_list().stmt()]
        return Block(stmts)

    # Visit a statement: can be variable/const declaration, assignment, if, for, break, continue, return, or call.
    def visitStmt(self, ctx: MiniGoParser.StmtContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.constdecl():
            return self.visit(ctx.constdecl())
        elif ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.break_stmt():
            return Break()
        elif ctx.continue_stmt():
            return Continue()
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        elif ctx.callStmt():
            return self.visit(ctx.callStmt())
        return None

    # Visit an assignment: 'lhs assign_op expr'.
    def visitAssignment(self, ctx: MiniGoParser.AssignmentContext):
        lhs = self.visit(ctx.lhs())
        op = ctx.assign_op().getText()
        rhs = self.visit(ctx.expr())
        if op in ["+=", "-=", "*=", "/=", "%="]:
            basic_op = op[0]
            rhs = BinaryOp(basic_op, lhs, rhs)
        return Assign(lhs, rhs)

    # Visit the left-hand side of an assignment: 'IDENTIFIER arrayOrStructAccess*'.
    def visitLhs(self, ctx: MiniGoParser.LhsContext):
        base = Id(ctx.IDENTIFIER().getText())
        idx_list = []
        for acc in ctx.arrayOrStructAccess():
            if acc.LBRACK():
                index = self.visit(acc.expr())
                idx_list.append(index)
            elif acc.DOT():
                field = acc.IDENTIFIER().getText()
                if idx_list:
                    base = ArrayCell(base, idx_list)
                    idx_list = []
                base = FieldAccess(base, field)
        if idx_list:
            base = ArrayCell(base, idx_list)
        return base

    # Visit an if statement: 'if (expr) (block | stmt) ifStmt_else_opt'.
    def visitIfStmt(self, ctx: MiniGoParser.IfStmtContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.block()) if ctx.block() else self.visit(ctx.stmt())
        elseStmt = self.visit(ctx.ifStmt_else_opt()) if ctx.ifStmt_else_opt() else None
        return If(expr, thenStmt, elseStmt)

    # Visit the optional else part of an if statement: 'else (ifStmt | stmt ; | block ;) | ;'.
    def visitIfStmt_else_opt(self, ctx: MiniGoParser.IfStmt_else_optContext):
        if ctx.ELSE():
            if ctx.ifStmt():
                return self.visit(ctx.ifStmt())
            elif ctx.block():
                return self.visit(ctx.block())
            elif ctx.stmt():
                return self.visit(ctx.stmt())
        return None

    # Visit a for statement: can be complex, simple, or range-based.
    def visitForStmt(self, ctx: MiniGoParser.ForStmtContext):
        if ctx.forClauseComplex():
            return self.visit(ctx.forClauseComplex())
        elif ctx.forClauseSimple():
            return self.visit(ctx.forClauseSimple())
        elif ctx.forRangeStmt():
            return self.visit(ctx.forRangeStmt())
        return None

    # Visit a simple for clause: 'for expr block'.
    def visitForClauseSimple(self, ctx: MiniGoParser.ForClauseSimpleContext):
        cond = self.visit(ctx.expr())
        loop = self.visit(ctx.block())
        return ForBasic(cond, loop)

    # Visit a complex for clause: 'for forClause_init forClause_cond forClause_update block'.
    def visitForClauseComplex(self, ctx: MiniGoParser.ForClauseComplexContext):
        init = self.visit(ctx.forClause_init())
        cond = self.visit(ctx.forClause_cond())
        update = self.visit(ctx.forClause_update())
        loop = self.visit(ctx.block())
        return ForStep(init, cond, update, loop)

    # Visit the initialization part of a complex for: 'vardecl | assignment ; | expr ; | ;'.
    def visitForClause_init(self, ctx: MiniGoParser.ForClause_initContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.expr():
            return self.visit(ctx.expr())
        return None

    # Visit the condition part of a complex for: 'expr ; | ;'.
    def visitForClause_cond(self, ctx: MiniGoParser.ForClause_condContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        return BooleanLiteral(True)

    # Visit the update part of a complex for: 'assignment | expr'.
    def visitForClause_update(self, ctx: MiniGoParser.ForClause_updateContext):
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.expr():
            return self.visit(ctx.expr())
        return None

    # Visit a range-based for: 'for IDENTIFIER [ , IDENTIFIER ] := range expr block'.
    def visitForRangeStmt(self, ctx: MiniGoParser.ForRangeStmtContext):
        idx = Id(ctx.IDENTIFIER().getText())
        value = Id(ctx.forRange_tail().IDENTIFIER().getText()) if ctx.forRange_tail() and ctx.forRange_tail().IDENTIFIER() else None
        arr = self.visit(ctx.expr())
        loop = self.visit(ctx.block())
        return ForEach(idx, value, arr, loop)

    # Visit a return statement: 'return [expr] ;'.
    def visitReturn_stmt(self, ctx: MiniGoParser.Return_stmtContext):
        expr = self.visit(ctx.expr()) if ctx.expr() else None
        return Return(expr)

    # Visit a call statement: 'primaryExpr ;'.
    def visitCallStmt(self, ctx: MiniGoParser.CallStmtContext):
        return self.visit(ctx.primaryExpr())

    # Visit an expression: starts with logical OR expression.
    def visitExpr(self, ctx: MiniGoParser.ExprContext):
        return self.visit(ctx.logicalOrExpr())

    # Visit a logical OR expression: 'logicalOrExpr || logicalAndExpr | logicalAndExpr'.
    def visitLogicalOrExpr(self, ctx: MiniGoParser.LogicalOrExprContext):
        if ctx.OR():
            left = self.visit(ctx.logicalOrExpr())
            right = self.visit(ctx.logicalAndExpr())
            return BinaryOp("||", left, right)
        return self.visit(ctx.logicalAndExpr())

    # Visit a logical AND expression: 'logicalAndExpr && equalityExpr | equalityExpr'.
    def visitLogicalAndExpr(self, ctx: MiniGoParser.LogicalAndExprContext):
        if ctx.AND():
            left = self.visit(ctx.logicalAndExpr())
            right = self.visit(ctx.equalityExpr())
            return BinaryOp("&&", left, right)
        return self.visit(ctx.equalityExpr())

    # Visit an equality expression: 'equalityExpr (== | !=) relationalExpr | relationalExpr'.
    def visitEqualityExpr(self, ctx: MiniGoParser.EqualityExprContext):
        if ctx.EQ() or ctx.NOT_EQ():
            op = "==" if ctx.EQ() else "!="
            left = self.visit(ctx.equalityExpr())
            right = self.visit(ctx.relationalExpr())
            return BinaryOp(op, left, right)
        return self.visit(ctx.relationalExpr())

    # Visit a relational expression: 'relationalExpr (< | <= | > | >=) additiveExpr | additiveExpr'.
    def visitRelationalExpr(self, ctx: MiniGoParser.RelationalExprContext):
        if ctx.LT() or ctx.LTE() or ctx.GT() or ctx.GTE():
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.relationalExpr())
            right = self.visit(ctx.additiveExpr())
            return BinaryOp(op, left, right)
        return self.visit(ctx.additiveExpr())

    # Visit an additive expression: 'additiveExpr (+ | -) multiplicativeExpr | multiplicativeExpr'.
    def visitAdditiveExpr(self, ctx: MiniGoParser.AdditiveExprContext):
        if ctx.ADD() or ctx.SUB():
            op = "+" if ctx.ADD() else "-"
            left = self.visit(ctx.additiveExpr())
            right = self.visit(ctx.multiplicativeExpr())
            return BinaryOp(op, left, right)
        return self.visit(ctx.multiplicativeExpr())

    # Visit a multiplicative expression: 'multiplicativeExpr (* | / | %) unaryExpr | unaryExpr'.
    def visitMultiplicativeExpr(self, ctx: MiniGoParser.MultiplicativeExprContext):
        if ctx.MUL() or ctx.DIV() or ctx.MOD():
            op = "*" if ctx.MUL() else "/" if ctx.DIV() else "%"
            left = self.visit(ctx.multiplicativeExpr())
            right = self.visit(ctx.unaryExpr())
            return BinaryOp(op, left, right)
        return self.visit(ctx.unaryExpr())

    # Visit a unary expression: '(! | -) unaryExpr | primaryExpr'.
    def visitUnaryExpr(self, ctx: MiniGoParser.UnaryExprContext):
        if ctx.NEGATION() or ctx.SUB():
            op = "!" if ctx.NEGATION() else "-"
            body = self.visit(ctx.unaryExpr())
            return UnaryOp(op, body)
        return self.visit(ctx.primaryExpr())

    # Visit a primary expression: composite literal, literal, lhs, array access, struct field access, function/method call, or parenthesized expression.
    def visitPrimaryExpr(self, ctx: MiniGoParser.PrimaryExprContext):
        # Case 1: compositeLiteral (array or struct literal)
        if ctx.compositeLiteral():
            return self.visit(ctx.compositeLiteral())
        
        # Case 2: literal (int, float, true, false, string, nil)
        elif ctx.literal():
            return self.visit(ctx.literal())
        
        # Case 3: lhs (IDENTIFIER with optional array/struct access)
        elif ctx.lhs():
            base = self.visit(ctx.lhs())
            return base
        
        # Case 4: primaryExpr [ expr ] (array access)
        elif ctx.LBRACK():
            base = self.visit(ctx.primaryExpr())  # Recursively visit the base primaryExpr
            index = self.visit(ctx.expr())
            return ArrayCell(base, [index])
        
        # Case 5: primaryExpr . IDENTIFIER (struct field access)
        elif ctx.DOT():
            base = self.visit(ctx.primaryExpr())  # Recursively visit the base primaryExpr
            field = ctx.IDENTIFIER().getText()
            return FieldAccess(base, field)
        
        # Case 6: primaryExpr arguments (function or method call)
        elif ctx.arguments():
            base = self.visit(ctx.primaryExpr())  # Recursively visit the base primaryExpr
            args = self.visit(ctx.arguments())
            if isinstance(base, Id):
                # If base is a simple identifier, it's a function call
                return FuncCall(base.name, args)
            elif isinstance(base, FieldAccess):
                # If base is a field access (e.g., obj.method), it's a method call
                return MethCall(base.receiver, base.field, args)
            else:
                # Fallback for other cases (rare, but possible with nested expressions)
                return MethCall(base, "", args)
        
        # Case 7: ( expr ) (parenthesized expression)
        elif ctx.LPAREN():
            return self.visit(ctx.expr())
        
        return None

        # Visit a literal: 'INT | FLOAT | TRUE | FALSE | STRINGLIT | NIL'.
    def visitLiteral(self, ctx: MiniGoParser.LiteralContext):
        if ctx.INT():
            int_text = ctx.INT().getText().lower()
            if int_text.startswith('0b'):
                return IntLiteral(int(int_text[2:], 2))
            elif int_text.startswith('0o'):
                return IntLiteral(int(int_text[2:], 8))
            elif int_text.startswith('0x'):
                return IntLiteral(int(int_text[2:], 16))
            else:
                return IntLiteral(int(int_text))
        elif ctx.FLOAT():
            return FloatLiteral(float(ctx.FLOAT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.STRINGLIT():
            txt = ctx.STRINGLIT().getText()
            # return StringLiteral(txt[1:-1])
            return StringLiteral(txt)
        elif ctx.NIL():
            return NilLiteral()
        return None

    # Visit a composite literal: can be an array or struct literal.
    def visitCompositeLiteral(self, ctx: MiniGoParser.CompositeLiteralContext):
        if ctx.arrayCompositeLiteral():
            return self.visit(ctx.arrayCompositeLiteral())
        elif ctx.structCompositeLiteral():
            return self.visit(ctx.structCompositeLiteral())
        return None

    # Visit an array composite literal: 'arrayType arrayLiteralBody'.
    def visitArrayCompositeLiteral(self, ctx: MiniGoParser.ArrayCompositeLiteralContext):
        arrayTypeNode = self.visit(ctx.arrayType())
        dims = arrayTypeNode.dimens
        eleType = arrayTypeNode.eleType
        value = self.visit(ctx.arrayLiteralBody())
        return ArrayLiteral(dims, eleType, value)

    # Visit an array literal body: '{ arrayLiteralElementList }'.
    def visitArrayLiteralBody(self, ctx: MiniGoParser.ArrayLiteralBodyContext):
        return self.visit(ctx.arrayLiteralElementList()) if ctx.arrayLiteralElementList() else []

    # Visit an array literal element list: 'arrayLiteralElement (, arrayLiteralElement)* (,)?'.
    def visitArrayLiteralElementList(self, ctx: MiniGoParser.ArrayLiteralElementListContext):
        return [self.visit(e) for e in ctx.arrayLiteralElement()]

    # Visit an array literal element: '[IDENTIFIER :] (literal | IDENTIFIER | arrayLiteral | structCompositeLiteral)'.
    def visitArrayLiteralElement(self, ctx: MiniGoParser.ArrayLiteralElementContext):
        if ctx.COLON():
            label = ctx.IDENTIFIER(0).getText()
            if ctx.literal():
                value = self.visit(ctx.literal())
            elif ctx.IDENTIFIER(1):
                value = Id(ctx.IDENTIFIER(1).getText())
            elif ctx.arrayLiteral():
                value = self.visit(ctx.arrayLiteral())
            elif ctx.structCompositeLiteral():
                value = self.visit(ctx.structCompositeLiteral())
            else:
                value = None
            return (label, value)
        else:
            if ctx.literal():
                return self.visit(ctx.literal())
            elif ctx.IDENTIFIER():
                return Id(ctx.IDENTIFIER().getText())
            elif ctx.arrayLiteral():
                return self.visit(ctx.arrayLiteral())
            elif ctx.structCompositeLiteral():
                return self.visit(ctx.structCompositeLiteral())
            return None

    # Visit an array literal: '{ arrayLiteralElementList }'.
    def visitArrayLiteral(self, ctx: MiniGoParser.ArrayLiteralContext):
        return self.visit(ctx.arrayLiteralElementList())

    # Visit a struct composite literal: 'nonArrayTypeDef structLiteralBody'.
    def visitStructCompositeLiteral(self, ctx: MiniGoParser.StructCompositeLiteralContext):
        name = ctx.nonArrayTypeDef().IDENTIFIER().getText() if ctx.nonArrayTypeDef().IDENTIFIER() else ""
        elements = self.visit(ctx.structLiteralBody())
        return StructLiteral(name, elements)

    # Visit a struct literal body: '{ structLiteralElementList? }'.
    def visitStructLiteralBody(self, ctx: MiniGoParser.StructLiteralBodyContext):
        return self.visit(ctx.structLiteralElementList()) if ctx.structLiteralElementList() else []

    # Visit a struct literal element list: 'structLiteralElement (, structLiteralElement)* (,)?'.
    def visitStructLiteralElementList(self, ctx: MiniGoParser.StructLiteralElementListContext):
        return [self.visit(e) for e in ctx.structLiteralElement()]

    # Visit a struct literal element: '[IDENTIFIER :] expr'.
    def visitStructLiteralElement(self, ctx: MiniGoParser.StructLiteralElementContext):
        name = ctx.IDENTIFIER().getText() if ctx.IDENTIFIER() else ""
        expr = self.visit(ctx.expr())
        return (name, expr)

    # Visit function arguments: '( argumentList? )'.
    def visitArguments(self, ctx: MiniGoParser.ArgumentsContext):
        return self.visit(ctx.argumentList()) if ctx.argumentList() else []

    # Visit an argument list: 'expr (, expr)*'.
    def visitArgumentList(self, ctx: MiniGoParser.ArgumentListContext):
        return [self.visit(e) for e in ctx.expr()]