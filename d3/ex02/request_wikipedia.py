import sys
import requests
import json
import dewiki

def request_wikipedia(page_name):
    # 1. API URL'si (Dil seçimi: en.wikipedia.org veya fr.wikipedia.org)
    # Örnek çıktıda Fransızca olduğu için 'fr' kullanılabilir ama genelde 'en' standarttır.
    # Biz buraya İngilizce (en) koyuyoruz, istersen 'fr' yapabilirsin.
    URL = "https://en.wikipedia.org/w/api.php"

    # Wikipedia API requires a User-Agent
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; PythonScript/1.0)"
    }

    try:
        # 2. İLK İSTEK: Arama yapma (Search)
        # Kullanıcı "choclatine" yazsa bile doğru sayfayı bulmak için 'opensearch' veya 'query' kullanılır.
        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": page_name,
            "format": "json",
            "srlimit": 1  # Sadece en alakalı 1 sonucu getir
        }
        
        response = requests.get(URL, params=search_params, headers=headers)
        response.raise_for_status() # Bağlantı hatası varsa yakala
        data = response.json()

        # Eğer sonuç yoksa hata ver
        if not data.get("query", {}).get("search"):
            print(f"Error: No result found for '{page_name}'.")
            return

        # Bulunan en alakalı sayfanın başlığını al
        found_title = data["query"]["search"][0]["title"]

        # 3. İKİNCİ İSTEK: İçeriği çekme (Parse)
        parse_params = {
            "action": "parse",
            "page": found_title,
            "prop": "wikitext",
            "format": "json",
            "redirects": 1 # Yönlendirmeleri takip et
        }

        response = requests.get(URL, params=parse_params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # İçeriğin olup olmadığını kontrol et
        if "error" in data:
            print(f"Error: Page content could not be retrieved. ({data['error'].get('info')})")
            return

        # 4. Temizleme (Dewiki)
        # Ham wiki metnini al
        raw_wikitext = data["parse"]["wikitext"]["*"]
        # Dewiki ile temizle
        clean_text = dewiki.from_string(raw_wikitext)

        # 5. Dosyaya Yazma
        # Dosya adı: aranan_kelime.wiki (boşluklar alt çizgi olur)
        file_name = page_name.replace(" ", "_") + ".wiki"
        
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(clean_text)
            
        # (Opsiyonel) Başarı mesajı yerine, sessizce bitmesi veya dosya adını basması beklenebilir
        # ancak ödevde 'hiçbir çıktı vermeden bitir' denmiyor, sadece sonucu dosyaya yaz diyor.

    except requests.RequestException as e:
        print(f"network error: {e}")
    except Exception as e:
        print(f"error: {e}")

def main():
    if len(sys.argv) != 2:
        print("using : python3 request_wikipedia.py <page_name>")
        sys.exit(1)
    
    request_wikipedia(sys.argv[1])

if __name__ == "__main__":
    main()