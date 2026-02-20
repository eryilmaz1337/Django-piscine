from elem import Elem, Text
from elements import *



# ağaç modeli var html de buna bak eva da lazım olur
class Page:
    def __init__(self, elem):
        if not isinstance(elem, Elem):
            raise TypeError("Page must be initialized with an Elem")
        self.root = elem

    def __str__(self):
        html = str(self.root)
        if self.root.tag == 'html':
            return "<!DOCTYPE html>\n" + html
        return html

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

    # ================= VALIDATION =================

    def is_valid(self):
        try:
            self._check_tree(self.root)
            self._check_rules(self.root)
            return True
        except Exception:
            return False

    def _check_tree(self, elem):
        allowed = {
            'html','head','body','title','meta','img','table','th','tr','td',
            'ul','ol','li','h1','h2','p','div','span','hr','br'
        }

        if isinstance(elem, Text):
            return

        if elem.tag not in allowed:
            raise Exception("Invalid tag")

        for c in elem.content:
            self._check_tree(c)

    def _check_rules(self, elem):
        if isinstance(elem, Text):
            return

        rules = {
            'html': self._html_rule,
            'head': self._head_rule,
            'body': self._body_rule,
            'div': self._body_rule,
            'title': self._single_text_rule,
            'h1': self._single_text_rule,
            'h2': self._single_text_rule,
            'li': self._single_text_rule,
            'th': self._single_text_rule,
            'td': self._single_text_rule,
            'p': self._p_rule,
            'span': self._span_rule,
            'ul': self._ul_ol_rule,
            'ol': self._ul_ol_rule,
            'tr': self._tr_rule,
            'table': self._table_rule
        }

        if elem.tag in rules:
            rules[elem.tag](elem)

        for c in elem.content:
            self._check_rules(c)

    # ================= RULES =================

    def _html_rule(self, elem):
        if len(elem.content) != 2:
            raise Exception
        if elem.content[0].tag != 'head' or elem.content[1].tag != 'body':
            raise Exception

    def _head_rule(self, elem):
        titles = [c for c in elem.content if c.tag == 'title']
        if len(titles) != 1 or len(elem.content) != 1:
            raise Exception

    def _body_rule(self, elem):
        allowed = {'h1','h2','div','table','ul','ol','span'}
        for c in elem.content:
            if isinstance(c, Text):
                continue
            if c.tag not in allowed:
                raise Exception

    def _single_text_rule(self, elem):
        if len(elem.content) != 1 or not isinstance(elem.content[0], Text):
            raise Exception

    def _p_rule(self, elem):
        for c in elem.content:
            if not isinstance(c, Text):
                raise Exception

    def _span_rule(self, elem):
        for c in elem.content:
            if not isinstance(c, Text) and c.tag != 'p':
                raise Exception

    def _ul_ol_rule(self, elem):
        if len(elem.content) == 0:
            raise Exception
        for c in elem.content:
            if c.tag != 'li':
                raise Exception

    def _tr_rule(self, elem):
        if len(elem.content) == 0:
            raise Exception
        tags = {c.tag for c in elem.content}
        if not tags.issubset({'th','td'}):
            raise Exception
        if 'th' in tags and 'td' in tags:
            raise Exception

    def _table_rule(self, elem):
        for c in elem.content:
            if c.tag != 'tr':
                raise Exception



def main():
    page = Page(
        Html([
            Head(
                Title(Text("Hello"))
            ),
            Body([
                H1(Text("Hi")),
                Div([
                    P(Text("paragraph")),
                    Span(Text("span text"))
                ])
            ])
        ])
    )

    print("Is valid:", page.is_valid())
    print("\nHTML OUTPUT:\n")
    print(page)

    page.write_to_file("test.html")
    print("\nHTML written to test.html")

if __name__ == "__main__":
    main()