import argparse
import spacy

def get_entities(file_contents):
    print(file_contents[:20])
    nlp = spacy.load('en')
    doc = nlp(file_contents)
    for ent in doc.ents:
            print(ent.label_, ent.text)


def main():
    parser = argparse.ArgumentParser(description='Give me the text of a novel')
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as f:
        get_entities(f.read())


if __name__ == '__main__':
    main()
