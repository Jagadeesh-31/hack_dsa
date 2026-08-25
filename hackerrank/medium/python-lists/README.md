# Lists

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Consider a list (`list = []`). You can perform the following commands:   

1. `insert i e`: Insert integer $e$ at position $i$.
2. `print`: Print the list.
3. `remove e`: Delete the first occurrence of integer $e$.
4. `append e`: Insert integer $e$ at the end of the list.  
5. `sort`: Sort the list.
6. `pop`: Pop the last element from the list.
7. `reverse`: Reverse the list.

Initialize your list and read in the value of $n$ followed by $n$ lines of commands where each command will be of the $7$ types listed above. Iterate through each command in order and perform the corresponding operation on your list.  

**Example**  
$N = 4$  
$\text{append 1}$  
$\text{append 2}$  
$\text{insert 1 3}$  
$\text{print}$   
</br >
</br >
   
- $\text{append 1}$: Append $1$ to the list, $arr = [1]$.  
- $\text{append 2}$: Append $2$ to the list, $arr = [1, 2]$.  
- $\text{insert 1 3}$: Insert $3$ at index $1$, $arr = [1, 3, 2]$.  
- $\text{print}$: Print the array.  
</br >
Output:
<pre>
[1, 3, 2]
</pre>

**Input Format**

The first line contains an integer, $n$, denoting the number of commands.	
Each line $i$ of the $n$ subsequent lines contains one of the commands described above.


**Constraints**

- The elements added to the list must be *integers*.

**Output Format**

For each command of type `print`, print the list on a new line.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T17:08:20.958Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/python-lists/problem)