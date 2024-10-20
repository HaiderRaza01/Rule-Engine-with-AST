from flask import Flask, request, jsonify
from rule_engine import RuleEngine

app = Flask(__name__)
engine = RuleEngine()

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Rule Engine API!"}), 200
    
@app.route('/create_rule', methods=['POST'])
def create_rule():
    data = request.get_json()
    rule_name = data.get('rule_name')
    rule_string = data.get('rule_string')

    if not rule_name or not rule_string:
        return jsonify({
            "message": "Both 'rule_name' and 'rule_string' are required",
            "status": "error"
        }), 400

    result = engine.create_rule(rule_name, rule_string)
    return jsonify(result), 200 if result["status"] == "success" else 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    data = request.get_json()
    rule_names = data.get('rule_names')

    if not rule_names:
        return jsonify({
            "message": "'rule_names' is required",
            "status": "error"
        }), 400

    result = engine.combine_rules(rule_names)
    return jsonify(result), 200 if result["status"] == "success" else 400

def ast_to_string(node):
    """ Recursively converts the AST nodes into a string representation. """
    if node['type'] == 'operand':
        return node['value']
    elif node['type'] == 'operator':
        left_expr = ast_to_string(node['left'])
        right_expr = ast_to_string(node['right'])
        return f"({left_expr} {node['value']} {right_expr})"
    else:
        raise ValueError(f"Unknown node type: {node['type']}")
    

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule(rule_ast, user_data):
    try:
        # Convert AST to a valid Python expression
        rule_expression = ast_to_string(rule_ast)
        
        # Now evaluate the rule expression with user data
        result = eval(rule_expression, {}, user_data)
        
        return jsonify({
            "message": "Evaluation completed.",
            "result": result,
            "status": "success"
        })
    except Exception as e:
        return jsonify({
            "message": f"Error during rule evaluation: {str(e)}",
            "status": "error"
        })


if __name__ == '__main__':
    app.run(debug=True)
