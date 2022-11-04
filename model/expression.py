from model import provider as pr

def __normalize_expression_str(expr_str: str):
    normolized_str = ''.join(expr_str.split()).replace(',','.')
    for symb in pr.expression_valid_symbols():
        normolized_str = normolized_str.replace(symb, f' {symb} ')
    return normolized_str



def __normalized_expression_string_to_list(normalized_expr_str:str):
    def to_suitable_value(x):
        try:
            return float(x)
        except ValueError:
            return x  

    expr_lst = normalized_expr_str.split()
    expr_lst = list(map(to_suitable_value, expr_lst))
    return expr_lst

def __first_occurence_index(lst: list,value,from_index=0, backward=False):
    last_index = len(lst) - 1

    enumer = lst
    start_index = from_index
    if backward:
        enumer = reversed(lst)
        start_index = last_index - from_index
    enumer = enumerate(enumer) 
    found_index = next((i for i, v in enumer 
                        if i >= start_index and v == value),None) 
    if backward and found_index:
        return last_index - found_index
    return found_index    

def __wrap_subexpressions(expr_lst):
    fo_close_idx = __first_occurence_index(expr_lst, ')')
    if fo_close_idx is None:
        return expr_lst

    if fo_close_idx == 0:
        expr_lst.pop(0)
        return __wrap_subexpressions(expr_lst)

    bo_open_idx = __first_occurence_index(
        expr_lst, '(', fo_close_idx -1, backward=True)  

    if bo_open_idx is None:
        del expr_lst[fo_close_idx]
        return __wrap_subexpressions(expr_lst)

    subexpr_lst = expr_lst[bo_open_idx + 1: fo_close_idx]
    for _ in range(fo_close_idx-bo_open_idx):
        del expr_lst[bo_open_idx]

    expr_lst[bo_open_idx] = subexpr_lst
    return __wrap_subexpressions(expr_lst)        


def init(expression_str:str):
    pass


def calc() -> float:
    pass
