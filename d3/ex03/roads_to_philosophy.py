import sys
import requests
from bs4 import BeautifulSoup

def get_first_valid_link(soup):
    content = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    
    # Sadece paragrafları al (tabloları vs atla)
    for paragraph in content.find_all("p", recursive=False):
        # Parantez sayacı
        parenthesis_count = 0
        
        # Paragrafın metnini ve linklerini sırayla taramak zorundayız.
        # BeautifulSoup'un .descendants özelliği tüm alt elemanları (nested dahil) sırayla verir.
        # Ancak bu hem text hem tag döndürür.
        
        # Daha kontrollü bir döngü:
        # Linkleri bul, ama konumlarına göre ele (parantez içi mi?)
        # Bunu yapmak için paragrafın ham metnini (text) tarayıp parantez saymak en kolayıdır
        # ama linkin tam konumunu metin içinde bulmak zordur.
        
        # En sağlam ve basit yöntem:
        # Paragraf içindeki her şeyi metin olarak birleştirirken, 
        # karşılaştığımız <a> etiketlerini kontrol etmek.
        
        def is_valid_link(tag):
            if tag.name != 'a': return False
            href = tag.get('href')
            if not href or not href.startswith('/wiki/') or ':' in href: return False
            # İtalik içindeyse atla (örneğin bitki adları vs)
            if tag.find_parent(['i', 'em']): return False
            return True

        # Paragrafın içindeki tüm 'string'leri ve 'a' taglerini sırayla gezelim.
        # .contents sadece ilk seviyeyi verir. .descendants hepsini verir.
        
        # Pratik Çözüm:
        # Paragrafı string'e çevirmeden parça parça işleyelim.
        # Basitlik adına: Sadece ana paragraf akışındaki linkleri alalım.
        
        # Tekrar baştan: Basit ve etkili bir recursive gezici
        
        found_link = None
        
        def traverse(element):
            nonlocal parenthesis_count, found_link
            if found_link: return
            
            # Element bir Tag ise (örneğin <a>, <b>, <i> vs)
            if element.name:
                # 1. Eğer Link ise
                if element.name == 'a':
                    if is_valid_link(element):
                        if parenthesis_count == 0:
                            found_link = element['href']
                            # Link bulundu!
                        else:
                            # Debug: Link parantez içinde olduğu için atlandı
                            pass
                    return # Linkin içine (çocuklarına) tekrar girme, linki bütün olarak ele al

                # 2. Eğer özel bir tag ise ve içine girmemiz gerekirse
                # (Zaten aşağıda children ile gezeceğiz)
                pass

            # Element bir NavigableString ise (Sadece yazı)
            if element.name is None:
                text = str(element)
                # Parantez sayımı
                open_p = text.count('(')
                close_p = text.count(')')
                parenthesis_count += (open_p - close_p)
                # Güvenlik önlemi: Sayaç negatife düşerse 0'la (fazla kapama parantezi varsa)
                if parenthesis_count < 0: parenthesis_count = 0
                return

            # Çocukları gez
            if hasattr(element, 'children'):
                for child in element.children:
                    traverse(child)

        traverse(paragraph)
        
        if found_link:
            return found_link
            
    return None

def roads_to_philosophy(start_term):
    visited_pages = [] # Sonsuz döngü kontrolü için
    current_url = "https://en.wikipedia.org/wiki/" + start_term
    
    # Wikipedia API requires a User-Agent
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; RoadToPhilosophy/1.0)"
    }
    
    while True:
        # 1. İstek at
        try:
            response = requests.get(current_url, headers=headers)
            response.raise_for_status()
        except Exception as e:
            if response.status_code == 404:
                print("It leads to a dead end !")
            else:
                print(f"Hata: Bağlantı sorunu. ({e})")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 2. Başlığı bul ve yazdır
        title = soup.find(id="firstHeading").text
        
        # Sonsuz döngü kontrolü
        if title in visited_pages:
            print("It leads to an infinite loop !")
            return
        
        visited_pages.append(title)
        print(title)

        # 3. Hedefe ulaştık mı?
        if title == "Philosophy":
            print(f"{len(visited_pages)} roads from {sys.argv[1]} to philosophy !")
            return

        # 4. Bir sonraki linki bul
        next_link = get_first_valid_link(soup)
        
        if not next_link:
            print("It leads to a dead end !")
            return
            
        current_url = "https://en.wikipedia.org" + next_link

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Hata: Bir arama terimi girin.")
    else:
        roads_to_philosophy(sys.argv[1])