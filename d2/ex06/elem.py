#!/usr/bin/python3


class Text(str):
    def __str__(self):
        # Önce tehlikeli karakterleri değiştiriyoruz
        # Not: Önce & değiştirilmeli ki diğerlerinin içindeki & bozulmasın
        content = super().__str__()
        content = content.replace('&', '&amp;')
        content = content.replace('<', '&lt;')
        content = content.replace('>', '&gt;')
        content = content.replace('"', '&quot;')
        
        # Sonra senin kodundaki o meşhur \n -> <br /> dönüşümü
        return content.replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        pass

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type
        self.content = []
        if content is not None: 
            self.add_content(content)

    def __str__(self):
        attr_str = self.__make_attr()
        if self.tag_type == 'simple':
            return f"<{self.tag}{attr_str} />"
        str_content = self.__make_content()
        return f"<{self.tag}{attr_str}>{str_content}</{self.tag}>"

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            res = str(elem)
            # BURASI KRİTİK: Her satırın başına 2 boşluk ekle
            # replace('\n', '\n  ') her alt satırı sağa iter
            result += '  ' + res.replace('\n', '\n  ') + '\n'
        return result
    
    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError()
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    # 1. En içteki elemanları oluşturuyoruz
    title = Elem(tag='title', content=Text('"Hello ground!"'))

    head = Elem(tag='head', content=title)
    
    # 2. Body içindeki elemanları oluşturuyoruz
    h1 = Elem(tag='h1', content=Text('"Oh no, not again!"'))
    # img etiketi ödevde 'simple' (tekli) tipte istenmişti
    img = Elem(tag='img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
    
    # 3. Body'yi oluşturup h1 ve img'yi içine liste olarak atıyoruz
    body = Elem(tag='body', content=[h1, img])
    
    # 4. En dış katman olan html'i oluşturup head ve body'yi içine koyuyoruz
    html = Elem(tag='html', content=[head, body])
    
    # 5. Ve hepsini tek seferde ekrana basıyoruz
    print(html)