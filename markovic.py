from sys import argv
import markovify

def main():
    # Use run.sh to preprocess the input Japanese text
    fName = "parsed_out.txt"

    with open(fName, "r") as file:
        text = file.read() # file must be preprocessed with MeCab -O wakati

    # default state_size is 2
    model = markovify.NewlineText(text, state_size=2)

    print(model.make_sentence())


if __name__ == "__main__":
    main()
