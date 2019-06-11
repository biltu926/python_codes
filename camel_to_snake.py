import re
import sys

def string_convert(in_):
    def replace(m):
        r = m.group(0)[0] + '_' + m.group(0)[1]
        return r.lower()

    result = re.sub(r'[a-z][A-Z]', replace, in_)
    print(in_)
    print(result)

if __name__ == '__main__':
    input_ = sys.argv[1]
    string_convert(input_)
