from elem import *
from elements import *

class Page():


    def __init__(self, elem):
        if not isinstance(elem, Elem):
            raise ValueError("Validation Error")
        self.elem = elem
    

    def is_valid(self) -> bool:
        return self.__recursive_check(self.elem)


    def __recursive_check(self, elem) -> bool:

        if not isinstance(self.elem, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)):
            return False
        
        if isinstance(elem, Html) and len(elem.content) == 2 \
                and type(elem.content[0]) == Head and type(elem.content[1]) == Body:
            print("first")
            if (all(self.__recursive_check(el) for el in elem.content)):
                print("here",elem.content)
                return True
        if isinstance(elem, Head) and len(elem.content)==1:
            print("x",elem.content)
            return True

        if isinstance(elem, Body):
            return True

        return False






if __name__ == '__main__':
    a = Page(
        Html([Head([Title()]), Body()])
    )
    print(a.is_valid())