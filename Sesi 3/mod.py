s = "Nama Kalian2"
a = 123

def foo():
    return "bar"

class Foo:
    pass

import argparse

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--echo", "-e", help="echo the string you use here")
    parser.add_argument("--file", "-f", help="specify file")
    
    args = parser.parse_args()
    print(args.echo)
    print(args.file)