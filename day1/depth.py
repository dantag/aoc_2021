import urllib.request
import sys

def get_compare(a_list, count, window):
    """The window will cancel out all but the first and last element
    """
    if len(a_list) < (1 + window): 
        return count
    
    if a_list[0] < a_list[window]:
        count += 1
    return get_compare(a_list[1:], count, window)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <AOC sessionID>")
        return

    data = list()
    link = "https://adventofcode.com/2021/day/1/input" 
    req = urllib.request.Request(link)
    req.add_header("cookie", f"session={sys.argv[1]}")
    with urllib.request.urlopen(req) as site_data:
        data = list(map(lambda a: int(a.decode('utf-8').strip('\n')), site_data))

    sys.setrecursionlimit(len(data) + 10) 
    print(len(data))
    print(data[-3:])

    window = 1
    print(f"part 1: {get_compare(data, 0, window)}")
    window = 3
    print(f"part 2: {get_compare(data, 0, window)}")


if __name__ == '__main__':
    main()
