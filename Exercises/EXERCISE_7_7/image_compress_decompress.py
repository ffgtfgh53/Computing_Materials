from re import sub, Match
def read(File) -> str:
    with open(File) as f:
        return f.read()
    
def compress(colours: str):
    def sub_multiple(matchobj:Match) -> str:
        #group(0) is whole match, group(1) is only the colour
        return matchobj.group(1).rstrip() + str(int(len(matchobj.group(0)) / len(matchobj.group(1)))) + "\n"
    #Replace repeated occurences and removes \n from entire string
    with open('./images/compressedimage.txt', 'w') as f:
        f.write(sub(r"(\d{3}\n)\1+", sub_multiple, colours))

def uncompress(file:str):
    def sub_multiple(matchobj:Match):
        return (matchobj.group(1) + '\n') * int(matchobj.group(2))
    with open("./images/decompressedimage.txt", 'w') as f:
        f.write(sub(r"(\d{3})(\d)(\n)", sub_multiple, file))

def main():
    file = read(input(":File path? "))
    if 'decompress' in input('Decompress or compress? '):
        uncompress(file)
    else:
        compress(file)

main()