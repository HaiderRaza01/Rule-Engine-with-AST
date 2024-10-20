class RuleEngine:
    def __init__(self):
        self.rules = {}  # Dictionary to store rule_name -> AST mapping

    def create_rule(self, rule_name, rule_string):
        try:
            ast = self.parse_rule_string(rule_string)  # Convert rule_string to AST
            self.rules[rule_name] = ast
            return {
                "message": f"Rule '{rule_name}' created successfully.",
                "ast": str(ast),
                "status": "success"
            }
        except Exception as e:
            return {
                "message": f"Error creating rule: {str(e)}",
                "status": "error"
            }

    def combine_rules(self, rule_names):
        try:
            combined_ast = None
            for rule_name in rule_names:
                if rule_name in self.rules:
                    rule_ast = self.rules[rule_name]
                    if combined_ast is None:
                        combined_ast = rule_ast
                    else:
                        # Combine the current AST with the combined AST using AND operator
                        combined_ast = self.combine_ast(combined_ast, rule_ast, 'AND')
                else:
                    raise ValueError(f"Rule '{rule_name}' not found")

            return {
                "message": "Rules combined successfully.",
                "combined_ast": str(combined_ast),
                "status": "success"
            }
        except Exception as e:
            return {
                "message": f"Error combining rules: {str(e)}",
                "status": "error"
            }

    def evaluate_rule(self, rule_ast, user_data):
        try:
            result = self.evaluate_ast(rule_ast, user_data)
            return result
        except Exception as e:
            return {
                "message": f"Error during rule evaluation: {str(e)}",
                "status": "error"
            }

    def parse_rule_string(self, rule_string):
        # Parse the rule_string into an AST (This is a placeholder, replace with actual parsing)
        # For example, you can implement this using `ast.literal_eval` or custom logic.
        # Returning the rule string for simplicity, in practice, return AST.
        return rule_string

    def combine_ast(self, ast1, ast2, operator):
        # Combine two ASTs using the operator (e.g., 'AND', 'OR')
        return f"({ast1} {operator} {ast2})"

    def evaluate_ast(self, rule_ast, user_data):
        # Evaluate the AST against the user data. Placeholder logic:
        # Here, you would traverse the AST and apply the conditions to the user_data.
        return eval(rule_ast, {}, user_data)
