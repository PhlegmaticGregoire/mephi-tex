from itertools import chain
from pathlib import Path


def get_mds(md_roots):
    roots = (Path.cwd() / root for root in md_roots)
    return chain(*(root.glob("**/*.md") for root in roots))


MACROS = "<!-- Macros: {} -->"
START = MACROS.format("start")
END = MACROS.format("end")


def get_macros_pos(string):
    s = string.find(START)
    e = string.find(END, s)

    if s != -1 and e != -1:
        return s + len(START), e
    return 0, 0


def get_preamble():
    text = Path("./preamble.sty").read_text("utf-8")
    s, e = get_macros_pos(text)
    lines = (
        f"${line}$"
        for line in text[s:e].split("\n")
        if line and not line.startswith("%")
    )
    return "\n" + "\n".join(lines) + "\n"


def fix_preambles(md_roots):
    prompt = "fixing preambles..."
    print(prompt, end="\r")

    preamble = get_preamble()

    last_size = 0
    for file in get_mds(md_roots):
        text = file.read_text("utf-8")

        s, e = get_macros_pos(text)
        macros = text[s:e]

        if macros:
            if macros != preamble:
                print(prompt, "Updating preamble in", file, " " * last_size, end="\r")
            else:
                print(prompt, "Skipping preamble in", file, " " * last_size, end="\r")
            text = text[:s] + preamble + text[e:]
        else:
            print(prompt, "Creating preamble in", file, " " * last_size, end="\r")
            text = START + preamble + END + "\n" + text

        file.write_text(text, "utf-8")
        last_size = len(str(file))

    print(prompt, "done", " " * (last_size + 20))


def fix_line_endings(md_roots):
    prompt = "fixing line endings..."
    print(prompt, end="\r")

    last_size = 0
    for file in get_mds(md_roots):
        text = file.read_text("utf-8")

        result = ""
        for line in text.split("\n"):
            if line:
                if not line.endswith("  "):
                    line += "  "
            result += line + "\n"
        result = result[:-1]

        print(prompt, file, " " * last_size, end="\r")

        file.write_text(result, "utf-8")
        last_size = len(str(file))

    print(prompt, "done", " " * (last_size + 20))


USUAL_MAP = {
    "<=": r"\leq",
    ">=": r"\geq",
    "-->": chr(0),
    "<->": r"\leftrightarrow",
    "->": r"\rightarrow",
    "<-": r"\leftarrow",
    "<=>": r"\ident",
    chr(0): "-->",
}


def fix_usual_repr(md_roots):
    prompt = "fixing susual representations..."
    print(prompt, end="\r")

    last_size = 0
    for file in get_mds(md_roots):
        text = file.read_text("utf-8")

        for pattern, repl in USUAL_MAP.items():
            text = text.replace(pattern, repl)

        print(prompt, file, " " * last_size, end="\r")

        file.write_text(text, "utf-8")
        last_size = len(str(file))

    print(prompt, "done", " " * (last_size + 20))


LITERATURE = """# {name}

Веб-просмотр:

<a href="https://github.com/0dminnimda/mephi-docs/blob/main/docs/_static/literature/{name}.pdf">Здесь</a> можно найти запасной веб-просмотр, на случай, если этот не работает <br>
Также можно <a href="../_static/literature/{name}.pdf">скачать PDF</a>

object
<object data="../_static/literature/{name}.pdf" type="application/pdf" style="width:150%; height:1000px;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</object>

iframe
<iframe src="../_static/literature/{name}.pdf" style="width:150%; height:1000px; border: none;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>

gh object
<object data="https://github.com/0dminnimda/mephi-docs/blob/main/docs/_static/literature/{name}.pdf" type="application/pdf" style="width:150%; height:1000px;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</object>

gh iframe
<iframe src="https://github.com/0dminnimda/mephi-docs/blob/main/docs/_static/literature/{name}.pdf" style="width:150%; height:1000px; border: none;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>

rtd object
<object data="https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf" type="application/pdf" style="width:150%; height:1000px;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</object>

rtd iframe
<iframe src="https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf" style="width:150%; height:1000px; border: none;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>

google object
<object data="http://docs.google.com/gview?url=https://github.com/mephi-tex/mephi-tex/blob/main/docs/_static/literature/{name}.pdf?raw=true&embedded=true" type="application/pdf" style="width:150%; height:1000px;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</object>

google iframe
<iframe src="http://docs.google.com/gview?url=https://github.com/mephi-tex/mephi-tex/blob/main/docs/_static/literature/{name}.pdf?raw=true&embedded=true" style="width:150%; height:1000px;" frameborder="0">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>

google rtd object
<object data="http://docs.google.com/gview?url=https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf&embedded=true" type="application/pdf" style="width:150%; height:1000px;">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</object>

google rtd iframe
<iframe src="http://docs.google.com/gview?url=https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf&embedded=true" style="width:150%; height:1000px;" frameborder="0">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>

pdfobject
<div id="example1" style="width:150%; height:1000px;" frameborder="0">hello?</div>
<script src="../_static/javascript/pdfobject.js"></script>
<script>PDFObject.embed("../_static/literature/{name}.pdf", "#example1", {{
   fallbackLink: 'У-упс, этот браузер не поддерживает встроенные PDF 😅'
}});</script>

.
<iframe src="http://docs.google.com/gview?url=https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf" style="width:150%; height:1000px;" frameborder="0">
    У-упс, этот браузер не поддерживает встроенные PDF 😅
</iframe>
"""
"""
https://github.com/afragen/embed-pdf-viewer
    <iframe src="../_static/literature/{name}.pdf" style="width:150%; height:1000px; border: none;">
        У-упс, этот браузер не поддерживает встроенные PDF 😅
    </iframe>
    <object data="../_static/literature/{name}.pdf" type="application/pdf" style="width:150%; height:1000px;">
        У-упс, этот браузер не поддерживает встроенные PDF 😅
    </object>

<iframe src="http://docs.google.com/gview?url=https://mephi-tex.rtfd.io/ru/latest/_static/literature/{name}.pdf&embedded=true" style="width:100%; height:1000px;" frameborder="0"></iframe>
"""


def generate_literature():
    gen_path = Path("literature")

    for file in Path.cwd().glob("./_static/literature/*.pdf"):
        gen_file = gen_path / file.with_suffix(".md").name
        gen_file.write_text(LITERATURE.format(name=file.stem), "utf-8")


def run_all(md_roots):
    fix_line_endings(md_roots)
    fix_preambles(md_roots)
    fix_usual_repr(md_roots)
    # generate_literature()


if __name__ == "__main__":
    run_all(["IVT", "IVT_evening"])
