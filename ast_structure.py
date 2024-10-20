# Node class for AST representation
# ast_structure.py

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

    def to_dict(self):
        node_dict = {
            "type": self.type,
            "value": self.value
        }
        if self.left is not None:
            node_dict["left"] = self.left.to_dict()
        if self.right is not None:
            node_dict["right"] = self.right.to_dict()
        return node_dict

# Add any additional functions here for creating and evaluating the AST.


# Custom exception for rule engine errors
class RuleEngineError(Exception):
    pass

# Predefined valid attributes for validation
VALID_ATTRIBUTES = {'age', 'department', 'salary', 'experience'}

# Catalog-based validation: ensure attributes used in rules are valid
def validate_rule_ast(ast_node):
    if ast_node.type == "operand":
        attribute = ast_node.value.split()[0]  # Get attribute part of operand (e.g., 'age')
        if attribute not in VALID_ATTRIBUTES:
            raise RuleEngineError(f"Invalid attribute: {attribute}")
    
    if ast_node.left:
        validate_rule_ast(ast_node.left)
    if ast_node.right:
        validate_rule_ast(ast_node.right)

# User data validation
def validate_user_data(user_data, required_fields):
    for field in required_fields:
        if field not in user_data:
            raise RuleEngineError(f"Missing required attribute: {field}")

# Helper function to create AST from rule string (mock function for simplicity)
def parse_rule_string(rule_string):
    # Mockup AST parsing logic (you would use a real parser for production)
    # Example: This function should turn rule_string into an AST.
    return Node("operator", "AND", 
                Node("operand", "age > 30"),
                Node("operator", "OR",
                     Node("operand", "salary > 50000"),
                     Node("operand", "experience > 5")))