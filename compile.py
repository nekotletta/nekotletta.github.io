# skribilo --target=html contribution.skb -o contribution.html
import argparse, os, glob
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-path", "--filepath", help="The path to the file you wish to compile from Skribilo to HTML (without .skb)")
parser.add_argument("-out", "--outfile", help="Name of the HTML file (if different from the Skribilo file). Ensure same path.")
args = parser.parse_args()

if args.filepath:
    
    if not os.path.exists(f"{args.filepath}.skb"):
        print(f"File {args.filepath}.skb does not exist.")
        exit(1)

    if args.outfile:
        os.system(f"skribilo --target=html {args.filepath}.skb -o {args.outfile}.html")
    else:
        os.system(f"skribilo --target=html {args.filepath}.skb -o {args.filepath}.html")
else:

    files = [f.resolve() for f in Path(".").rglob("*.skb")]

    root = os.getcwd()
    for file in files:
        try:
            os.chdir(file.parent)
            os.system(f"skribilo --target=html {file.name} -o {file.with_suffix('.html').name}")

        except Exception as e:
            print(f"Error occured: {e}, in {file}")

        finally:
            os.chdir(root)