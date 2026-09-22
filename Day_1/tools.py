import ast
import operator
from config import COURSE_FEES


# Tool 1: Get the fee of a course
def get_course_fee(course_code):
    course_code = course_code.upper()

    if course_code not in COURSE_FEES:
        return f"Unknown course code: {course_code}"

    return COURSE_FEES[course_code]


# Allowed mathematical operations
ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


# Tool 2: Safe calculator
def calculator(expression):
    try:
        tree = ast.parse(expression, mode="eval")

        def evaluate(node):
            if isinstance(node, ast.Expression):
                return evaluate(node.body)

            if isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value

            if isinstance(node, ast.BinOp):
                operation = ALLOWED_OPERATORS.get(type(node.op))

                if operation is None:
                    raise ValueError("Operation not allowed")

                return operation(
                    evaluate(node.left),
                    evaluate(node.right)
                )

            raise ValueError("Invalid expression")

        return evaluate(tree)

    except Exception as e:
        return f"Calculator error: {e}"


# Python functions available to the agent
TOOL_FUNCTIONS = {
    "get_course_fee": get_course_fee,
    "calculator": calculator,
}


# Tool descriptions given to the LLM
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the official fee for a course.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "Course code such as CS101, AI202, or DS303"
                    }
                },
                "required": ["course_code"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform arithmetic calculations safely.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A mathematical expression such as (12000+18000)*0.9"
                    }
                },
                "required": ["expression"],
            },
        },
    },
]