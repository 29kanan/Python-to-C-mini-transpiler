from sympy import symbols, Add, Pow, Symbol, Integer, Mul, parse_expr
#x, y = symbols('x y')
expr = parse_expr(input("Enter the expression: "))
def to_C_code(expr):
    if isinstance(expr, Add):
        c_code = [to_C_code(t) for t in expr.args]
        return ' + '.join(c_code)
    if isinstance(expr, Mul):
        c_code = [to_C_code(t) for t in expr.args]
        return ' * '.join(c_code)
    elif isinstance(expr, Pow):
        c_code = [to_C_code(t) for t in expr.args]
        return 'pow(' + ', '.join(c_code) + ')'
    elif isinstance(expr, Symbol):
        return str(expr)
    elif isinstance(expr, Integer):
        return str(expr)
    return str(expr)

print(to_C_code(expr))