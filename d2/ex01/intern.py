class Intern:
    name: str
    def __init__(self, name: str = "My name? I’m nobody, an intern, I have no name."):
        self.name = name
    def __str__(self):
       return self.name
    def work(self):
       raise Exception("I can't do much... I'm just an intern.")
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
    
    def make_coffee(self):
        return Intern.Coffee()


if __name__ == "__main__":
    # 1. İsimsiz stajyer
    nobody = Intern()
    
    # 2. İsmi "Mark" olan stajyer
    mark = Intern("Mark")

    # 3. İsimleri yazdır
    print(nobody)  # My name? I’m nobody, an intern, I have no name.
    print(mark)    # Mark

    # 4. Mark kahve yapıyor
    print(mark.make_coffee())  # This is the worst coffee you ever tasted.

    # 5. İsimsiz intern çalışıyor → exception handle
    try:
        nobody.work()
    except Exception as e:
        print(e)  # I’m just an intern, I can’t do that...