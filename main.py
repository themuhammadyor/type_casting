
def date_formate(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if ' ' in result:
            day = result.split()[0]
            month = result.split()[1]
            year = result.split()[2]
            print(f"{day} - {month} - {year}")
        if '/' in result:
            day = result.split('/')[0]
            month = result.split('/')[1]
            year = result.split('/')[2]
            print(f"{day} - {month} - {year}")
        return result
    return inner


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

@date_formate
def formater(string: str):
    return string

@type_casting(to_upper='', to_lower='', to_split='True')
def printer(string: str) -> str:
    return string

if __name__ == '__main__':
    print(printer("HEllo, HOw are you"))
    print(formater("6th Oct 2025"))
    print(formater("6/11/2025"))
