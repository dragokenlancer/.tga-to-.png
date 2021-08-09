from PIL import Image
import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='convert a tga to png recursivly or per file provided ',
                                    epilog='--Dragoken\'s stupid projects--')
parser.add_argument("-r", help="recursivly go down current folders tree and convert all ", action='store_true')
parser.add_argument("-f", "--file", type=str, help="file name to convert a signle file")
args = parser.parse_args()

if args.file != None and args.r == True:
    print("please only select -f or -r not both")
    exit()
elif args.file != None:
    print("converting", args.file, "to {}.png".format(args.file))
    test = str(args.file)
    if test.lower().endswith('.tga'):
        Image.open(args.file).save(args.file+".png")
    else:
        Image.open(args.file+".tga").save(args.file+".png")
elif args.r == True:
    result = list(Path(".").rglob("*.[tT][gG][aA]"))
    print(len(result), "items to convert")
    for i in result:
        Image.open(i).save("{}.png".format(i))
else:
    parser.parse_args(['-h'])
