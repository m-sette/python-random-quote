def main():

    quote = input("Enter a quote: ")
    f = open("quotes.txt", "a")
    f.write(quote + "\n")
    f.close()


if __name__ == "__main__":
    main()
