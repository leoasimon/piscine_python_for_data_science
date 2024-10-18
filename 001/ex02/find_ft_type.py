def all_thing_is_obj(object: any) -> int:
    # Define a mapping of types to labels
    type_mapping = {
        list: 'List',
        dict: 'Dict',
        set: 'Set',
        tuple: 'Tuple',
        str: 'String',
        bool: 'Boolean',
        # Add other types as needed
    }

    # Get the type of the object
    obj_type = type(object)

    # Get the corresponding label, defaulting to 'Unknown' if not found
    label = type_mapping.get(obj_type, 'Type not found')
    if label == 'String':
        label = f'{object} is in the kitchen'

    # Formatting the output
    if label == 'Type not found':
        formatted_output = label
    else:
        formatted_output = f"{label} : {obj_type}"

    print(formatted_output)

    return 42
