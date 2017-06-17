import argparse


def get_entities(file_contents):
    print(file_contents[:20])
    

def main():
    parser = argparse.ArgumentParser(description='Give me the text of a novel')
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as f:
        get_entities(f.read())
    print(args)


if __name__ == '__main__':
    main()
