if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        ip = input().split()
        if ip[0] == 'append':
            arr.append(int(ip[1]))
        elif ip[0] =='insert':
            arr.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == 'remove':
            arr.remove(int(ip[1]))
        elif ip[0] =='pop':
            arr.pop()
        elif ip[0]=='sort':
            arr.sort()
        elif ip[0] == 'reverse':
            arr.reverse()
        elif ip[0] == 'print':
            print(arr)
