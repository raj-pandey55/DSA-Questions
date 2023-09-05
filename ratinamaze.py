def searchMaze(arr,n):
  

  ans=[]
  vis = [[False for j in range(n)]for i in range(n)]

  def search(arr,n,row,col,s,ans,vis):
    if(row==n-1 and col==n-1):
      ans.append(s)
      return

    #downward
    if(row+1<n and not vis[row+1][col] and arr[row+1][col]==1):
      vis[row][col]=True   
      search(arr,n,row+1,col,s+'D',ans,vis)
      vis[row][col]=False
                  
    #left
    if(col-1>=0 and not vis[row][col-1] and arr[row][col-1]==1):
      vis[row][col]=True    
      search(arr,n,row,col-1,s+'L',ans,vis)
      vis[row][col]=False

    #right
    if(col+1<n and not vis[row][col+1] and arr[row][col+1]==1):
      vis[row][col]=True   
      search(arr,n,row,col+1,s+'R',ans,vis)
      vis[row][col]=False

    #upward
    if(row-1>=0 and not vis[row-1][col] and arr[row-1][col]==1):
      vis[row][col]=True 
      search(arr,n,row-1,col,s+'U',ans,vis)
      vis[row][col]=False

  # n=4
  # arr = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]

  # ans=[]
  # vis = [[False for j in range(n)]for i in range(n)]
  search(arr,n,0,0,"",ans,vis)

  return (ans)
n=4
arr = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
print(searchMaze(arr,n))