import sys
# Python'a "local_lib klasörüne de bak" diyoruz.
sys.path.insert(0, './local_lib')

# Artık path kütüphanesini import edebiliriz.
from path import Path

def main():
    try:
        # 1. Bir klasör oluştur (mkdir_p: varsa hata vermez, yoksa oluşturur)
        folder_path = Path("test_folder")
        folder_path.mkdir_p()

        # 2. O klasörün içinde bir dosya tanımla
        # path kütüphanesinde '/' operatörü dizin birleştirmek için kullanılır.
        file_path = folder_path / "test_file.txt"

        # 3. Dosyaya yaz
        file_path.write_text("Hello, Path library!")

        # 4. Dosyayı oku ve ekrana bas
        content = file_path.read_text()
        print(f"Dosya icerigi: {content}")

    except Exception as e:
        print(f"Hata: {e}")

if __name__ == '__main__':
    main()