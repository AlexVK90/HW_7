import view
from model import provider as pr


def calc_expression(inp: str) -> float:
    try:
        f_num = float(inp)
        return f_num
    except ValueError:
        pass

    # calculate expression:
    pass


def start():

    inp = view.get_expression()
    result = calc_expression(inp)

    while True:
        op_mark = view.get_operation_mark()
        if op_mark == '=':
            break

        inp = view.get_expression()
        value_b = calc_expression(inp)

        op_model = pr.get_operation_by_mark(op_mark)

        op_model.init(result, value_b)
        result = op_model.calc()

        if result:
            view.print_result(result)
        else:
            view.print_zerodivision_error()

    view.print_result(result, True)
