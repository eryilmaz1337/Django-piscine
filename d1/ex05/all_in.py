import sys

def capital_city(name):
    # Başkent ve eyalet eşlemeleri
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    orjName = name
    # Girişin küçük/büyük harf farkını göz ardı etmek için
    name = name.strip().lower()  # Tüm harfleri küçük yapıyoruz ve baştaki/sondaki boşlukları kaldırıyoruz

    # Eğer giriş bir başkentse
    for code, city in capital_cities.items():
        if name == city.lower():
            # Eğer şehir, başkentse, o zaman hangi eyalete ait olduğunu bulalım
            state = next(key for key, value in states.items() if value == code)
            return f"{city.capitalize()} is the capital of {state}"

    # Eğer giriş bir eyaletse
    for state, code in states.items():
        if name == state.lower():
            return f"{capital_cities[code]} is the capital of {state}"

    return f"{orjName} is neither a capital city nor a state"

if __name__ == '__main__':
    if len(sys.argv) == 2:
        expressions = sys.argv[1].split(',')  # Giriş string'ini virgülle ayır

        # Virgülleri ayırırken gereksiz boşlukları temizliyoruz
        expressions = [expr.strip() for expr in expressions if expr.strip() != ""]

        if len(expressions) == 0:
            sys.exit(0)  # Eğer parametre boşsa hiçbir şey yazdırma

        for expr in expressions:
            print(capital_city(expr))  # Şehir ya da eyaletle ilgili sonucu yazdır
