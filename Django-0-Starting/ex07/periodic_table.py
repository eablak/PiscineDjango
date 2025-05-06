
def get_values(periodic_table) -> list:
    
    table_elements = []

    for line in periodic_table:
        name, attributes = line.split("=")
        dict_element = dict(att.strip().split(":") for att in attributes.split(","))
        dict_element["name"] = name.strip()
        table_elements.append(dict_element)

    return table_elements


def table_positioning(elements) -> list:
    
    table = []

    for row in range(7):
        table.append(["" for column in range(18)])


    for element in elements:

        position = int(element["position"])
        number = int(element["number"])

        if number == 1 or number == 2:
            row = 0
        elif 3 <= number <= 10:
            row = 1
        elif 11 <= number <= 18:
            row = 2
        elif 19 <= number <= 36:
            row = 3
        elif 37 <= number <= 54:
            row = 4
        elif 55 <= number <= 86:
            row = 5
        else:
            row = 6 

        table[row][position] = element

    return table


def generate_html(table, html_file):

    html = ['<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<title>Periodic Table</title>\n</head>\n<body>']
    html.append('\t<h1>Periodic Table</h1>')
    html.append('<table style="border-collapse: collapse;">')

    for row in table:
        html.append('<tr>')

        for cell in row:      
            if cell == "":
                html.append('<td></td>')
            else:
                name = cell["name"]
                number = cell["number"]
                small = cell["small"]
                molar = cell.get("molar","N/A")
                electron = cell["electron"]
                html.append('<td style="border: 1px solid black; padding:10px">')
                html.append(f'''<h4>{name}</h4><ul>
                    <li>No {number}</li>
                    <li>{small}</li>
                    <li>{molar}</li>
                    <li>{electron} electron</li>
                    </ul></td>''')
        html.append('</tr>')
                
    html.append('</table></body></html>')

    html_file.write("\n".join(html))


def main():

    try:
        with open ("periodic_table.txt","r") as f_periodic:
            f_html = open("periodic_table.html","w")
            elements = get_values(f_periodic)
            table = table_positioning(elements)
            generate_html(table, f_html)
    except FileNotFoundError:
        print("File not exist")
        return

    
if __name__ == "__main__":
    main()