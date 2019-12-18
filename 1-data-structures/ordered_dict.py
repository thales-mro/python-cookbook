from collections import OrderedDict
import json
# an ordered dict keeps the original order of insertion in a iteration
# implemented with a doubled linked list (2x regular dict storage!)

def main():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])

    print(json.dumps(d))

if __name__ == "__main__":
    main()