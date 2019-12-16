
import sys


def main():
    children = input()

    ret = {i: 0 for i in range(len(children))}

    previous_L = -1
    loop_flag = True
    for i, child in enumerate(children):
        if loop_flag:
            if child == 'L':
                ret[i] = (i - previous_L + 1) // 2
                ret[i - 1] = (i - previous_L) // 2
                loop_flag = False
                previous_L = i
                        
        else:
            if child == 'L':
                if (i - previous_L) % 2:
                    ret[previous_L - 1] += 1
                else:
                    ret[previous_L] += 1
            else:
                loop_flag = True
                previous_L = i - 1

    ret = [str(value) for value in ret.values()]       
    ret = ' '.join(ret)
    print(ret)
    
if __name__=="__main__":
    main()
