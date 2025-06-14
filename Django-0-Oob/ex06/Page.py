from elem import *
from elements import *

class Page():


    def __init__(self, elem):
        if not isinstance(elem, Elem):
            raise ValueError("Validation Error")
        self.elem = elem


    def is_valid(self) -> bool:
        return self.checkForValid(self.elem)

    def display(self) -> None:

        result = ""
        if isinstance(self.elem, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.elem)
        print(result)


    def write_to_file(self, file_name):

        self.file_name = file_name
        result = ""
        if isinstance(self.elem, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.elem)

        with open(file_name, "a") as f:
            f.write(result)


    def checkForValid(self, elem) -> bool:

        if not isinstance(self.elem, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text)):
            return False


        if isinstance(elem, Html):

            if len(elem.content) == 2 and isinstance(elem.content[0], Head) and isinstance(elem.content[1], Body):
                return all(self.checkForValid(el) for el in elem.content)


        if isinstance(elem, Head): 

            if not elem.content:
                return True
            if len(elem.content) == 1 and isinstance(elem.content[0], Title):
                return self.checkForValid(elem.content[0])


        if isinstance(elem, Body) or isinstance(elem, Div):
            
            if not elem.content:
                return True
            for el in elem.content:
                if not isinstance(el, (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                    return False
            return all(self.checkForValid(el) for el in elem.content)


        if isinstance(elem, (Title, H1, H2, Li, Th, Td)):
            
            if not elem.content:
                return True
            if len(elem.content) == 1 and isinstance(elem.content[0], Text):
                return True


        if isinstance(elem, P):

            if not elem.content:
                return True
            return all(isinstance(el,Text) for el in elem.content)
           

        if isinstance(elem, Span):

            if not elem.content:
                return True
            if all(isinstance(el,(Text,P)) for el in elem.content):
                return all(self.checkForValid(el) for el in elem.content)


        if isinstance(elem, Ul) or isinstance(elem, Ol):
            
            if len(elem.content) > 0:
                if all(isinstance(el,Li) for el in elem.content):
                    return all(self.checkForValid(el) for el in elem.content)


        if isinstance(elem, Tr):
            
            if len(elem.content) > 0:
                if all(isinstance(el, (Th,Td)) for el in elem.content):
                        el_list = [el.__class__.__name__ for el in elem.content]
                        if all([el == el_list[0] for el in el_list]):
                            return all(self.checkForValid(el) for el in elem.content)


        if isinstance(elem, Table):

            if not elem.content:
                return True
            if all(isinstance(el,Tr) for el in elem.content):
                return all(self.checkForValid(el) for el in elem.content)


        if isinstance(elem, (Meta, Img, Hr, Br, Text)):
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
    page_html.display()
    print("\nRESULT =", page_html.is_valid())
    start_end("END", "HTML")

    # -----------------TEST2--------------------------

    print("\n"*2)
    start_end("START", "HTML")
    page_html = Page(Html([Head()]))
    page_html.display()
    print("\nRESULT =", page_html.is_valid())
    start_end("END", "HTML")

    # -----------------TEST3--------------------------

    print("\n"*2)
    start_end("START", "HTML")
    page_html = Page(Html([Head(), Body(), Body()]))
    page_html.display()
    print("\nRESULT =", page_html.is_valid())
    start_end("END", "HTML")
    print("\n")

    # -----------------TEST4--------------------------

    print("\n"*2)
    start_end("START", "HTML")
    page_html = Page(Html())
    page_html.display()
    print("\nRESULT =", page_html.is_valid())
    start_end("END", "HTML")
    print("\n")

def test_head():

    # -----------------TEST1--------------------------

    start_end("START", "HEAD")
    page_head = Page(Head())
    page_head.display()
    print("\nRESULT =", page_head.is_valid())
    start_end("END", "HEAD")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "HEAD")
    page_head = Page(Head(Title()))
    page_head.display()
    print("\nRESULT =", page_head.is_valid())
    start_end("END", "HEAD")
    print("\n")

    # -----------------TEST3--------------------------

    start_end("START", "HEAD")
    page_head = Page(Html([Head(Title()), Body()]))
    page_head.display()
    print("\nRESULT =", page_head.is_valid())
    start_end("END", "HEAD")
    print("\n")

    # -----------------TEST4--------------------------

    start_end("START", "HEAD")
    page_head = Page(Html([Head([Title(), Title()]), Body()]))
    page_head.display()
    print("\nRESULT =", page_head.is_valid())
    start_end("END", "HEAD")
    print("\n")



def test_body_div():

    # -----------------TEST1--------------------------

    start_end("START", "BODY-DIV")
    page_div_body = Page(Div([]))
    page_div_body.display()
    print("\nRESULT =", page_div_body.is_valid())
    start_end("END", "BODY-DIV")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "BODY-DIV")
    page_div_body = Page(Html([Head(Title([])), Body(Div())]))
    page_div_body.display()
    print("\nRESULT =", page_div_body.is_valid())
    start_end("END", "BODY-DIV")
    print("\n")

    # -----------------TEST3--------------------------

    start_end("START", "BODY-DIV")
    page_div_body = Page(Div([H1(),H2()]))
    page_div_body.display()
    print("\nRESULT =", page_div_body.is_valid())
    start_end("END", "BODY-DIV")
    print("\n")

    # -----------------TEST4--------------------------

    start_end("START", "BODY-DIV")
    page_div_body = Page(Html([Head(Title([])), Body(Div([H1(), Li(), Div([Td(), Title()])]))]))
    page_div_body.display()
    print("\nRESULT =", page_div_body.is_valid())
    start_end("END", "BODY-DIV")
    print("\n")

    # -----------------TEST5--------------------------

    start_end("START", "BODY-DIV")
    page_div_body = Page(Html([Head(Title([])), Body(Div([H1(), Span(), Div([Span(), Text("Hello World")])]))]))
    page_div_body.display()
    print("\nRESULT =", page_div_body.is_valid())
    start_end("END", "BODY-DIV")
    print("\n")



def test_Title_H1_H2_Li_Th_Td():

    # -----------------TEST1--------------------------

    start_end("START", "title_etc")
    page_title_etc = Page(Html([Head(Title([Text("Title Text")])), Body(Div([H1(Text("H1 Text")), Div([H2()])]))]))
    page_title_etc.display()
    print("\nRESULT =", page_title_etc.is_valid())
    start_end("END", "title_etc")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "title_etc")
    page_title_etc = Page(Html([Head(Title([Text("Title Text")])), Body(Div([H1([Text("H1 Text"), Text("H1 second text")]), Div([Td(), Title()])]))]))
    page_title_etc.display()
    print("\nRESULT =", page_title_etc.is_valid())
    start_end("END", "title_etc")
    print("\n")


def test_p():

    # -----------------TEST1--------------------------

    start_end("START", "p")
    page_p = Page(P(P()))
    page_p.display()
    print("\nRESULT =", page_p.is_valid())
    start_end("END", "p")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "p")
    page_p = Page(P([Text("xxx"), Text("yyy")]))
    page_p.display()
    print("\nRESULT =", page_p.is_valid())
    start_end("END", "p")
    print("\n")



def test_span():

    # -----------------TEST1--------------------------

    start_end("START", "SPAN")
    page_span = Page(Html([Head(Title([Text("Title Text")])), Body(Div([Span([Text("H1 Text"), P(Text("p text"))]), Div([H2(), Text("heloğ")])]))]))
    page_span.display()
    print("\nRESULT =", page_span.is_valid())
    start_end("END", "SPAN")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "SPAN")
    page_span = Page(Html([Head(Title([Text("Title Text")])), Body(Div([Span([Text("H1 Text"), H2(Text("p text"))]), Div([H2(), Text("heloğ")])]))]))
    page_span.display()
    print("\nRESULT =", page_span.is_valid())
    start_end("END", "SPAN")
    print("\n")


def test_ul_ol():

    # -----------------TEST1--------------------------

    start_end("START", "UL-OL")
    page_ul_ol = Page(Html([Head(Title(Text())), Body([H1(), Ul([Li(Text("text for li")), Li(), Li()])])]))
    page_ul_ol.display()
    print("\nRESULT =", page_ul_ol.is_valid())
    start_end("END", "UL-OL")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "UL-OL")
    page_ul_ol = Page(Html([Head(Title(Text())), Body([H1(), Ol(Text("text for ol"))])]))
    page_ul_ol.display()
    print("\nRESULT =", page_ul_ol.is_valid())
    start_end("END", "UL-OL")
    print("\n")

    # -----------------TEST3--------------------------

    start_end("START", "UL-OL")
    page_ul_ol = Page(Html([Head(Title(Text())), Body([H1(), Ul([Li(Text("text inside li")), Li(), Li()])])]))
    page_ul_ol.display()
    print("\nRESULT =", page_ul_ol.is_valid())
    start_end("END", "UL-OL")
    print("\n")

    # -----------------TEST4--------------------------

    start_end("START", "UL-OL")
    page_ul_ol = Page(Html([Head(Title(Text())), Body([H1(), Ul()])]))
    page_ul_ol.display()
    print("\nRESULT =", page_ul_ol.is_valid())
    start_end("END", "UL-OL")
    print("\n")


def test_tr():

    # -----------------TEST1--------------------------

    start_end("START", "TR")
    page_tr = Page(Tr())
    page_tr.display()
    print("\nRESULT =", page_tr.is_valid())
    start_end("END", "TR")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "TR")
    page_tr = Page(Tr([Th(), Th(Text("lslsl"))]))
    page_tr.display()
    print("\nRESULT =", page_tr.is_valid())
    start_end("END", "TR")
    print("\n")

    # # -----------------TEST3--------------------------

    start_end("START", "TR")
    page_tr = Page(Tr([Td(), Th(Text("lslsl"))]))
    page_tr.display()
    print("\nRESULT =", page_tr.is_valid())
    start_end("END", "TR")
    print("\n")


def test_table():

    # -----------------TEST1--------------------------

    start_end("START", "Table")
    page_table = Page(Html([Head(Title()), Body([H1(), Span(), Table()])]))
    page_table.display()
    print("\nRESULT =", page_table.is_valid())
    start_end("END", "Table")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "Table")
    page_table = Page(Html([Head(Title()), Body([H1(), Span(), Table(Tr([Th(), Th(Text("th is ok"))]))])]))
    page_table.display()
    print("\nRESULT =", page_table.is_valid())
    start_end("END", "Table")
    print("\n")

    # # -----------------TEST3--------------------------

    start_end("START", "Table")
    page_table = Page(Html([Head(Title()), Body([H1(), Span(), Table(Tr([Th(), H1(Text("h1 is not ok"))]))])]))
    page_table.display()
    print("\nRESULT =", page_table.is_valid())
    start_end("END", "Table")
    print("\n")


def test_general():

    # -----------------TEST1--------------------------

    start_end("START", "Random")
    page_random = Page(Html([Head(Title(Text("what's up"))), Body([H1(), H2(), Div(), Div([Ol(Li(Text("ol needs li"))), Span(), Text("div text")])])]))
    page_random.display()
    print("\n",page_random.is_valid())
    start_end("END", "Random")
    print("\n")

    # -----------------TEST2--------------------------

    start_end("START", "Random")
    page_random = Page(Html([Head(Title()), Body([Table(Tr([Th(Text("th needs..")), Th(Text("..th or td"))])), H1(Text("---")), Table(Tr([Td(Text("..just one")), Td(Text("..of them"))]))])]))
    page_random.display()
    page_random.write_to_file("my_file.txt")
    print("\n",page_random.is_valid())
    start_end("END", "Random")
    print("\n")




def tests():

    # test_html()
    # test_head()
    # test_body_div()
    # test_Title_H1_H2_Li_Th_Td()
    # test_p()
    # test_span()
    # test_ul_ol()
    # test_tr()
    # test_table()
    test_general()


if __name__ == '__main__':

    tests()