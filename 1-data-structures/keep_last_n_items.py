from collections import deque
# deque(maxlen=N) retorna uma lista de tamanho fixo

def search(lines, pattern, history=4):
    prev_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)

def keep_last_n():
    with open('example.txt') as f:
        for line, prevlines in search(f, 'Thales'):
            for p_l in prevlines:
                print(p_l, end='')
            print(line)
            print('-'*20)


if __name__ == "__main__":
    keep_last_n()