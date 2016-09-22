"""
    For strings, return its length.
    For None return string 'no value'
    For booleans return the boolean
    For integers return a string showing how it compares to hundred e.g.
    For 67 return 'less than 100' for 4034 return 'more than 100' or
    equal to 100 as the case may be


    For lists return the 3rd item, or None if it doesn't exist


    """

def data_type(datatype):    
    if datatype is None:
        return 'no value'
    elif isinstance(datatype, str):
        return len(datatype)
    elif isinstance(datatype, bool):
        return datatype
    elif isinstance(datatype, int):
            if datatype < 100:
                return 'less than 100'
            return 'more than 100'
    elif isinstance(datatype, list):
            if len(datatype) > 2:
                return datatype[2]
            else:
                return None
