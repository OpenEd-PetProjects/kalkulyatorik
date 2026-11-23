import ast
import operator
import re


_BINARY = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.floordiv,
}
_UNARY = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def evaluate(expression: str) -> int | float:
    """Evaluate arithmetic without executing Python code."""
    expression = expression.strip()
    # Reject syntax the parser discards, such as comments and line continuations.
    if not re.fullmatch(r"[0-9.eE+*/()\s-]+", expression):
        raise ValueError("Invalid arithmetic expression")
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ValueError("Invalid arithmetic expression") from exc
    return _evaluate_node(tree.body)


def _evaluate_node(node: ast.expr) -> int | float:
    match node:
        case ast.Constant(value=value) if type(value) in (int, float):
            return value
        case ast.BinOp(left, op, right) if type(op) in _BINARY:
            return _BINARY[type(op)](_evaluate_node(left), _evaluate_node(right))
        case ast.UnaryOp(op, operand) if type(op) in _UNARY:
            return _UNARY[type(op)](_evaluate_node(operand))
        case _:
            raise ValueError("Unsupported arithmetic expression")
