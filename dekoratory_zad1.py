# dekoratory - opakowanie jedej funkcji dodatkowymi cechami
def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew


@dekor  # uzycie dekoratora na naszej funkcji
def hej():
    print("Hej")


hej()
