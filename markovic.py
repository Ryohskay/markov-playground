from sys import argv
import markovify

def main():
    # Use run.sh to preprocess the input Japanese text
    file = 
    text = file.read()

    # default state_size is 2
    model = markovify.NewlineText(text, state_size=2)

    print(model.make_sentence())


if __name__ == "__main__":
    main()
