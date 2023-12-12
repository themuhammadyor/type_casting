
def type_casting(to_upper, to_lower, to_split):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if to_upper == 'True':
                to_lower == 'False'
                result = result.upper()
                return result
            if to_lower == 'True':
                to_upper == 'False'
                result = result.lower()
                return result
            if to_split == 'True':
                result = result.split()
                return result
            # if to_split == 'True' and to_upper == 'True':
            #     result = result.split()
            #     result_split = []
            #     for i in result:
            #         i = i.upper()
            #         result_split.append(i)
            #     return result_split
            # if to_split == 'True' and to_lower == 'True':
            #     result = result.split()
            #     result_split = []
            #     for i in result:
            #         i = i.lower()
            #         result_split.append(i)
            #     return result_split

                # if to_upper == 'True':
                #     result = result.upper()
                #     result = result.split()
                # if to_lower == 'True':
                #     result = result.lower()
                #     result = result.split()
                # return result
        return inner
    return wrapper

@type_casting(to_upper='', to_lower='', to_split='True')
def printer(string: str) -> str:
    return string

if __name__ == '__main__':
    print(printer("HEllo, HOw are you"))