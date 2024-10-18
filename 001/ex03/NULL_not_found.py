def is_nan(n) -> bool:
    return n != n

def test_nb(nb) -> str:
    if is_nan(nb):
        return f'Cheese: {nb}'
    if nb == 0:
        return f'Zero: {nb}'
    return 'Type not Found'

def test_bool(b: bool) -> str:
    if not b:
        return f'Fake: {b}'
    return 'Type not Found'

def test_str(s: str) -> str:
    if s == '':
        return 'Empty:'
    return 'Type not Found'

def NULL_not_found(object: any) -> int:
    obj_type = type(object)

    label = 'Type not Found'
    if object is None:
        label = f'Nothing: {object}'
    elif obj_type == int or obj_type == float:
       label = test_nb(object)
    elif obj_type == str:
        label = test_str(object)
    elif obj_type == bool:
        label = test_bool(object)

    if label == 'Type not Found':
        print(label)
        return 1

    print(label, obj_type)
    return 0
