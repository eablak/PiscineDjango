from elem import *
from elements import *

class Page():


    def __init__(self, elem):
        if not isinstance(elem, Elem):
            raise ValueError("Validation Error")
        self.elem = elem
    

    def is_valid(self) -> bool:
        return self.checkForValid(self.elem)


    def checkForValid(self, elem) -> bool:

        if not isinstance(self.elem, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)):
            return False
        
        if isinstance(elem, Html) and len(elem.content) == 2 and isinstance(elem.content[0], Head) and isinstance(elem.content[1], Body):
            returns = [self.checkForValid(el) for el in elem.content]
            if False in returns:
                return False
            return True

        if isinstance(elem, Head):
            if len(elem.content) == 1 and isinstance(elem.content[0], Title):
                returns = [self.checkForValid(elem.content[0])]
                if False in returns:
                    return False
            else:
                return False
            return True

        if isinstance(elem, (Title, H1, H2, Li, Th, Td)):
            if len(elem.content) > 0:
                if len(elem.content) > 1 or not isinstance(elem.content[0], Text):
                    return False
                return True
            return True

        if isinstance(elem, Body) or isinstance(elem, Div):
            if len(elem.content) == 0:
                if not isinstance(elem, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                    return True
            else:
                returns = [self.checkForValid(el) for el in elem.content]
                if False in returns:
                    return False
            return True
        

        if isinstance(elem, P):
            if len(elem.content) > 0:
                for el in elem.content:
                    if not isinstance(el, Text):
                        return False
                returns = [self.checkForValid(el) for el in elem.content]
                if False in returns:
                    return False
            return True


        if isinstance(elem, Span):
            if len(elem.content) > 0:
                for el in elem.content:
                    if not isinstance(el, Text) and not isinstance(el, P):
                        return False
                returns = [self.checkForValid(el) for el in elem.content]
                if False in returns:
                    return False
            else:
                results = [self.checkForValid(el) for el in elem.content]
                if False in results:
                    return False
            return True


        if isinstance(elem, Text):
            return True

        if isinstance(elem, Ul) or isinstance(elem, Ol):
            if not len(elem.content) > 0:
                return False
            for el in elem.content:
                if not isinstance(el, Li):
                    return False
            returns = [self.checkForValid(el) for el in elem.content]
            if False in returns:
                return False
            return True


        if isinstance(elem, Tr):
            if len(elem.content) > 0:
                for el in elem.content:
                    if not isinstance(el, Th) and not isinstance(el, Td):
                        return False
                returns = [self.checkForValid(el) for el in elem.content]
                if False in returns:
                    return False

                el_list = [el.__class__.__name__ for el in elem.content]
                return(all([el == el_list[0] for el in el_list]))

            return True


        if isinstance(elem, Table):
            if len(elem.content) > 0:
                for el in elem.content:
                    if not isinstance(el, Tr):
                        return False
                returns = [self.checkForValid(el) for el in elem.content]
                if False in returns:
                    return False
            return True



        return False







def start_end(flag, class_name):
    
    if flag == "START":
        print("-" * 20, flag, class_name, "-" * 20)
    else:
        print("-" * 20, flag, class_name, "-" * 20)


def test_html():

    # -----------------TEST1--------------------------

    start_end("START", "HTML")
    page_html = Page(Html([Head(), Body()]))
    print(page_html.elem)
    print("\nRESULT =", page_html.is_valid())
    start_end("END", "HTML")

    # -----------------TEST2--------------------------

    print("\n"*2)
    start_end("START", "HTML")
    page_html = Page(Html([Head()]))
    print(page_html.elem)
    print("\nRESULT =", page_html.is_valid())
    start_end("END", "HTML")

    # -----------------TEST3--------------------------

    print("\n"*2)
    start_end("START", "HTML")
    page_html = Page(Html([Head(), Body(), Body()]))
    print(page_html.elem)
    print("\nRESULT =", page_html.is_valid())
    start_end("END", "HTML")
    print("\n")


def test_head():
    
    # -----------------TEST1--------------------------

    start_end("START", "HEAD")
    page_head = Page(Head())
    print(page_head.elem)
    print("\nRESULT =", page_head.is_valid())
    start_end("END", "HEAD")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "HEAD")
    page_head = Page(Head(Title()))
    print(page_head.elem)
    print("\nRESULT =", page_head.is_valid())
    start_end("END", "HEAD")
    print("\n")

    # -----------------TEST3--------------------------

    start_end("START", "HEAD")
    page_head = Page(Html([Head(Title()), Body()]))
    print(page_head.elem)
    print("\nRESULT =", page_head.is_valid())
    start_end("END", "HEAD")
    print("\n")

    # -----------------TEST4--------------------------

    start_end("START", "HEAD")
    page_head = Page(Html([Head([Title(), Title()]), Body()]))
    print(page_head.elem)
    print("\nRESULT =", page_head.is_valid())
    start_end("END", "HEAD")
    print("\n")



def test_body_div():
    
    # -----------------TEST1--------------------------

    start_end("START", "BODY-DIV")
    page_div_body = Page(Div([]))
    print(page_div_body.elem)
    print("\nRESULT =", page_div_body.is_valid())
    start_end("END", "BODY-DIV")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "BODY-DIV")
    page_div_body = Page(Html([Head(Title([])), Body(Div())]))
    print(page_div_body.elem)
    print("\nRESULT =", page_div_body.is_valid())
    start_end("END", "BODY-DIV")
    print("\n")

    # -----------------TEST3--------------------------

    start_end("START", "BODY-DIV")
    page_div_body = Page(Html([Head(Title([])), Body(Div([H1(), Th()]))]))
    print(page_div_body.elem)
    print("\nRESULT =", page_div_body.is_valid())
    start_end("END", "BODY-DIV")
    print("\n")

    # -----------------TEST4--------------------------

    start_end("START", "BODY-DIV")
    page_div_body = Page(Html([Head(Title([])), Body(Div([H1(), Li(), Div([Td(), Title()])]))]))
    print(page_div_body.elem)
    print("\nRESULT =", page_div_body.is_valid())
    start_end("END", "BODY-DIV")
    print("\n")

    # -----------------TEST5--------------------------

    start_end("START", "BODY-DIV")
    page_div_body = Page(Html([Head(Title([])), Body(Div([H1(), Ol(), Div([P(), Text("Hello World")])]))]))
    print(page_div_body.elem)
    print("\nRESULT =", page_div_body.is_valid())
    start_end("END", "BODY-DIV")
    print("\n")



def test_Title_H1_H2_Li_Th_Td():
    
    # -----------------TEST1--------------------------

    start_end("START", "title_etc")
    page_title_etc = Page(Html([Head(Title([Text("Title Text")])), Body(Div([H1(Text("H1 Text")), Li(), Div([Td(), Title()])]))]))
    print(page_title_etc.elem)
    print("\nRESULT =", page_title_etc.is_valid())
    start_end("END", "title_etc")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "title_etc")
    page_title_etc = Page(Html([Head(Title([Text("Title Text")])), Body(Div([H1([Text("H1 Text"), Text("H1 second text")]), Li(), Div([Td(), Title()])]))]))
    print(page_title_etc.elem)
    print("\nRESULT =", page_title_etc.is_valid())
    start_end("END", "title_etc")
    print("\n")


def test_p():

    # -----------------TEST1--------------------------

    start_end("START", "p")
    page_p = Page(Html([Head(Title([Text("Title Text")])), Body(Div([P([Text("H1 Text"), Text("h1 testtt")]), Li(), Div([Td(), Title()])]))]))
    print(page_p.elem)
    print("\nRESULT =", page_p.is_valid())
    start_end("END", "p")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "p")
    page_p = Page(Html([Head(Title([Text("Title Text")])), Body(Div([P([Text("H1 Text"), H1()]), Li(), Div([Td(), Title()])]))]))
    print(page_p.elem)
    print("\nRESULT =", page_p.is_valid())
    start_end("END", "p")
    print("\n")



def test_span():
    
    # -----------------TEST1--------------------------

    start_end("START", "SPAN")
    page_span = Page(Html([Head(Title([Text("Title Text")])), Body(Div([Span([Text("H1 Text"), P()]), Li(), Div([Td(), Title()])]))]))
    print(page_span.elem)
    print("\nRESULT =", page_span.is_valid())
    start_end("END", "SPAN")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "SPAN")
    page_span = Page(Html([Head(Title([Text("Title Text")])), Body(Div([Span([Text("H1 Text"), H1()]), Li(), Div([Td(), Title()])]))]))
    print(page_span.elem)
    print("\nRESULT =", page_span.is_valid())
    start_end("END", "SPAN")
    print("\n")


def test_ul_ol():

    # -----------------TEST1--------------------------

    start_end("START", "UL-OL")
    page_ul_ol = Page(Html([Head(Title(Text())), Body([H1(), Ul([Li(Text("text for li")), Li(), Li()])])]))
    print(page_ul_ol.elem)
    print("\nRESULT =", page_ul_ol.is_valid())
    start_end("END", "UL-OL")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "UL-OL")
    page_ul_ol = Page(Html([Head(Title(Text())), Body([H1(), Ol(Text("text for ol"))])]))
    print(page_ul_ol.elem)
    print("\nRESULT =", page_ul_ol.is_valid())
    start_end("END", "UL-OL")
    print("\n")

    # -----------------TEST3--------------------------

    start_end("START", "UL-OL")
    page_ul_ol = Page(Html([Head(Title(Text())), Body([H1(), Ul([Li(Text("text inside li")), Li(), Li()])])]))
    print(page_ul_ol.elem)
    print("\nRESULT =", page_ul_ol.is_valid())
    start_end("END", "UL-OL")
    print("\n")

    # -----------------TEST4--------------------------

    start_end("START", "UL-OL")
    page_ul_ol = Page(Html([Head(Title(Text())), Body([H1(), Ul([Li(P()), Li(), Li()])])]))
    print(page_ul_ol.elem)
    print("\nRESULT =", page_ul_ol.is_valid())
    start_end("END", "UL-OL")
    print("\n")


def test_tr():

    # -----------------TEST1--------------------------

    start_end("START", "TR")
    page_tr = Page(Html([Head(Title()), Body([H1(), Li(), Tr([Td()])])]))
    print(page_tr.elem)
    print("\nRESULT =", page_tr.is_valid())
    start_end("END", "TR")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "TR")
    page_tr = Page(Html([Head(Title()), Body([H1(), Li(), Tr([Th(), Th(Text("hello"))])])]))
    print(page_tr.elem)
    print("\nRESULT =", page_tr.is_valid())
    start_end("END", "TR")
    print("\n")
    
    # -----------------TEST3--------------------------

    start_end("START", "TR")
    page_tr = Page(Html([Head(Title()), Body([H1(), Li(), Tr([Td(), Th()])])]))
    print(page_tr.elem)
    print("\nRESULT =", page_tr.is_valid())
    start_end("END", "TR")
    print("\n")


def test_table():

    # -----------------TEST1--------------------------

    start_end("START", "Table")
    page_table = Page(Html([Head(Title()), Body([H1(), Li(), Table()])]))
    print(page_table.elem)
    print("\nRESULT =", page_table.is_valid())
    start_end("END", "Table")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "Table")
    page_table = Page(Html([Head(Title()), Body([H1(), Li(), Table([Tr(), Tr([Td()])])])]))
    print(page_table.elem)
    print("\nRESULT =", page_table.is_valid())
    start_end("END", "Table")
    print("\n")

    # -----------------TEST3--------------------------

    start_end("START", "Table")
    page_table = Page(Html([Head(Title()), Body([H1(), Li(), Table([Tr(), Tr(), Text("table text")])])]))
    print(page_table.elem)
    print("\nRESULT =", page_table.is_valid())
    start_end("END", "Table")
    print("\n")


def tests():
    
    test_html()
    test_head()
    test_body_div()
    test_Title_H1_H2_Li_Th_Td()
    test_p()
    test_span()
    test_ul_ol()
    test_tr()
    test_table()


if __name__ == '__main__':
    
    tests()
    
    # a = Page(Html([Head(Title()), Body(Ol(), H1(Text("asdasd")))]))
    # print(a.is_valid())