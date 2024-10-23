import ast
from flask import Flask, request, jsonify

app = Flask(__name__)

class RuleEngine:
    def __init__(self, context):
        """
        Initialize the rule engine with a context.
        :param context: dict - A dictionary of variables that will be available for rules.
        """
        self.context = context

    def eval_expr(self, rule):
        """
        Evaluate an expression using AST safely.
        :param rule: str - The rule as a string.
        :return: bool - Result of evaluating the rule.
        """
        try:
            # Parse the rule into an AST
            tree = ast.parse(rule, mode='eval')

            # Validate and ensure the tree is safe to evaluate
            self._validate_ast(tree)

            # Compile and evaluate the AST within the context
            compiled_expr = compile(tree, filename="<ast>", mode="eval")
            return eval(compiled_expr, {}, self.context)

        except Exception as e:
            print(f"Error evaluating rule: {e}")
            return str(e)

    def _validate_ast(self, tree):
        """
        Validate the AST to ensure no unsafe operations.
        Raise an error if an unsafe operation is detected.
        :param tree: ast.AST - The AST to validate.
        """
        for node in ast.walk(tree):
            if isinstance(node, (ast.Call, ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef)):
                raise ValueError(f"Unsafe operation detected in the rule: {node}")
            if isinstance(node, ast.Attribute):
                raise ValueError(f"Attribute access is not allowed: {node.attr}")

@app.route('/evaluate_rule', methods=['POST', 'GET'])
def evaluate_rule():
    """
    API endpoint to evaluate a rule.
    Expects JSON input with 'rule' and 'context'.
    """
    data = request.json
    rule = data.get("rule")
    context = data.get("context")

    # Initialize rule engine with provided context
    engine = RuleEngine(context)

    # Evaluate the rule
    result = engine.eval_expr(rule)
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
