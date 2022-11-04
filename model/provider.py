from model import addition, substraction, multiplication,division

__operations= {
    addition.operation_mark:addition,
    substraction.operation_mark:substraction,
    multiplication.operation_mark:multiplication,
    division.operation_mark: division
}

__operation_marks = list(__operations.keys())  #[+,-,*,/]

__expression_valid_symbols = __operation_marks + ['(',')']

__operation_marks_by_priority =[
    {multiplication.operation_mark, division.operation_mark},
    {addition.operation_mark, substraction.operation_mark}
]

def get_operations_marks() -> list[str]:
    return __operation_marks

def operation_marks_by_priority():
    return __operation_marks_by_priority

def expression_valid_symbols():
    return __expression_valid_symbols 

def get_operation_by_mark(mark):
    return __operations[mark]        








