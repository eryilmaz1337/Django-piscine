def my_sort():
    # Given dictionary
    d = {
        'Hendrix': '1942',
        'Allman': '1946',
        'King': '1925',
        'Clapton': '1945',
        'Johnson': '1911',
        'Berry': '1926',
        'Vaughan': '1954',
        'Cooder': '1947',
        'Page': '1944',
        'Richards': '1943',
        'Hammett': '1962',
        'Cobain': '1967',
        'Garcia': '1942',
        'Beck': '1944',
        'Santana': '1947',
        'Ramone': '1948',
        'White': '1975',
        'Frusciante': '1970',
        'Thompson': '1949',
        'Burton': '1939',
    }

    # Convert the dictionary to a list of tuples (name, year)
    musicians = [(name, int(year)) for name, year in d.items()]

    # Sort the list first by year, and then by name for equal years
    musicians.sort(key=lambda x: (x[1], x[0]))

    # Print musician names along with the "Yaz" for each year
    for musician in musicians:
        print(f"{musician[0]} : {musician[1]}")

# Call the function to test it
if __name__ == '__main__':
    my_sort()
#     # Test cases