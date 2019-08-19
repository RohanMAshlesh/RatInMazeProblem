# RatInMazeProblem
Consider a rat placed at (0, 0) in a square matrix m[][] of order n and has to reach the destination at (n-1, n-1). Your task is to complete the function printPath() which returns a sorted array of strings denoting all the possible directions which the rat can take to reach the destination at (n-1, n-1). The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right).

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line contains an integer n denoting the size of the square matrix. The next line contains n*n space separated values of the matrix m where 0's represents blocked paths and 1 represent valid paths.

Output:
For each test case output will be space separated sorted strings denoting all directions, which the rat could take to reach the destination.

User Task:
Since this is functional problem you don't have to worry about input, you just have to complete the function printPath()

Example
Input:
2
4
1 0 0 0 1 1 0 1 0 1 0 0 0 1 1 1
4
1 0 0 0 1 1 0 1 1 1 0 0 0 1 1 1

Output:
DRDDRR
DDRDRR DRDDRR
