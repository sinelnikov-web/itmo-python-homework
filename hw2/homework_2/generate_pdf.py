from latex_generator import generate_table


def create_full_document():
    data = [
        ["Название", "Количество", "Цена"],
        ["Яблоки", 10, 15],
        ["Бананы", 5, 20],
        ["Апельсины", 8, 25],
    ]

    table_code = generate_table(data)

    document = r"""
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[russian]{babel}
\usepackage{graphicx}
\begin{document}

%s

\end{document}
    """ % (table_code)

    with open("document.tex", "w", encoding="utf-8") as f:
        f.write(document)


if __name__ == "__main__":
    create_full_document()
