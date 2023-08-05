import ast

from fastest.code_assets.naive_case_detector import get_test_from_example_passage



def get_functions_from_node(node):
    return [{
        'name': n.name,
        'tests': get_test_from_example_passage(ast.get_docstring(n))
    } for n in node.body if isinstance(n, ast.FunctionDef)]


def get_functions(page):
    """
    ------
    examples:
    @let
    page = 'def f(): return 1'
    @end

    1) get_functions(page) -> [{'name': 'f', 'tests': None}]
    ------
    :param page:
    :return:
    """
    node = ast.parse(page)
    functions = get_functions_from_node(node)
    classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
    methods = [get_functions_from_node(class_) for class_ in classes]
    return functions + methods
