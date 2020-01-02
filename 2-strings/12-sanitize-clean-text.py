import unicodedata
import sys

def main():
    s = 'ṕŷtĥôǹ\fis\tawesome\r\n'
    print(s)
    remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\r'): None
    }
    a = s.translate(remap)
    print(a)
    cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
    b = unicodedata.normalize('NFD', a)
    print(b)
    print(b.translate(cmb_chrs))

    print("Other way:")
    print(b.encode('ascii', 'ignore').decode('ascii'))


if __name__ == "__main__":
    main()