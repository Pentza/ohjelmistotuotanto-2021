from pelitehdas import PeliTehdas

def main():
    pelitehdas = PeliTehdas()
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        peli = pelitehdas.anna_peli(vastaus)

        if peli:
            peli.pelaa()
        else:
            break

if __name__ == "__main__":
    main()
