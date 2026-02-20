from elem import Elem , Text

class Html(Elem):
    def __init__(self, content=None, attr={}):
        # Html her zaman 'html' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='html', attr=attr, content=content, tag_type='double')

class Head(Elem):
    def __init__(self, content=None, attr={}):
        # Head her zaman 'head' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='head', attr=attr, content=content, tag_type='double')

class Body(Elem):
    def __init__(self, content=None, attr={}):
        # Body her zaman 'body' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='body', attr=attr, content=content, tag_type='double')

class Title(Elem):
    def __init__(self, content=None, attr={}):
        # Title her zaman 'title' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='title', attr=attr, content=content, tag_type='double')

class Meta(Elem):
    def __init__(self, attr={}):
        # Meta her zaman 'meta' tagine sahiptir ve 'simple' tiptedir.
        super().__init__(tag='meta', attr=attr, content=None, tag_type='simple')

class Img(Elem):
    def __init__(self, attr={}):
        # Img her zaman 'img' tagine sahiptir ve 'simple' tiptedir.
        super().__init__(tag='img', attr=attr, content=None, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        # Table her zaman 'table' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='table', attr=attr, content=content, tag_type='double')

class Th(Elem):
    def __init__(self, content=None, attr={}):
        # Th her zaman 'th' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='th', attr=attr, content=content, tag_type='double')

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        # Tr her zaman 'tr' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='tr', attr=attr, content=content, tag_type='double')

class Td(Elem):
    def __init__(self, content=None, attr={}):
        # Td her zaman 'td' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='td', attr=attr, content=content, tag_type='double')

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        # Ul her zaman 'ul' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='ul', attr=attr, content=content, tag_type='double')

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        # Ol her zaman 'ol' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='ol', attr=attr, content=content, tag_type='double')

class Li(Elem):
    def __init__(self, content=None, attr={}):
        # Li her zaman 'li' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='li', attr=attr, content=content, tag_type='double')

class H1(Elem):
    def __init__(self, content=None, attr={}):
        # H1 her zaman 'h1' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='h1', attr=attr, content=content, tag_type='double')

class H2(Elem):
    def __init__(self, content=None, attr={}):
        # H2 her zaman 'h2' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='h2', attr=attr, content=content, tag_type='double')

class P(Elem):
    def __init__(self, content=None, attr={}):
        # P her zaman 'p' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='p', attr=attr, content=content, tag_type='double')

class Div(Elem):
    def __init__(self, content=None, attr={}):
        # Div her zaman 'div' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='div', attr=attr, content=content, tag_type='double')

class Span(Elem):
    def __init__(self, content=None, attr={}):
        # Span her zaman 'span' tagine sahiptir ve 'double' tiptedir.
        super().__init__(tag='span', attr=attr, content=content, tag_type='double')

class Hr(Elem):
    def __init__(self, attr={}):
        # Hr her zaman 'hr' tagine sahiptir ve 'simple' tiptedir.
        super().__init__(tag='hr', attr=attr, content=None, tag_type='simple')

class Br(Elem):
    def __init__(self, attr={}):
        # Br her zaman 'br' tagine sahiptir ve 'simple' tiptedir.
        super().__init__(tag='br', attr=attr, content=None, tag_type='simple')


if __name__ == '__main__':
    # 1. Miras aldığımız yeni sınıflarla yapıyı kuruyoruz
    # Dikkat: Artık Elem() yok, Html(), Body() var.
    html_page = Html([
        Head(
            Title(Text('"Hello ground!"'))
        ),
        Body([
            H1(Text('"Oh no, not again!"')),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])

    # 2. Sonucu ekrana basıyoruz
    print(html_page)