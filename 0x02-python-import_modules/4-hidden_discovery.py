#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for ade in dir(hidden_4):
        if ade[0] != '_' and ade[1] != '_':
            print(ade)
