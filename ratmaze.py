  #Problem Function
  def pathing(mat, n, row, col, curr, ans, visited):
        dirs = {'D':(1,0), 'U':(-1,0), 'L':(0,-1), 'R':(0,1)}   #Value key pair for various directions
        for d in dirs:
            r, c = row+dirs[d][0], col+dirs[d][1]
            if r==n-1 and c==n-1:
                ans+=[curr+d]
            elif r>=0 and c>=0 and r<n and c<n and mat[r][c]==1 and (r,c) not in visited:
                visited_c = visited.copy()
                visited_c.add((r, c))
                pathing(mat, n, r, c, curr+d, ans, visited_c)
    ans = []
    visited = {(0,0)}
    pathing(arr, n, 0, 0, '', ans, visited)
    ans.sort()
    return ' '.join(ans)

# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        print(findPath(matrix, n[0]))
