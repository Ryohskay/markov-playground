from sys import argv
import markovify

def main():
    fName = argv[1]
    with open(fName, "r") as file:
        text = file.read()
        # this file must be parsed by mecab and accordingly separated 

    # default state_size is 2
    model = markovify.NewlineText(text, state_size=2)

    print(model.make_sentence())


if __name__ == "__main__":
    main()
