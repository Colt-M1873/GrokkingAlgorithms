// https://leetcode.com/problems/where-will-the-ball-fall/
// 2022年11月01日 20:16:31

class Solution {
    public int[] findBall(int[][] grid) {
        int[] ret=new int[grid[0].length];
        // Arrays.fill(ret,-1);
        for(int i=0;i<grid[0].length;i++){
            int[] initCoord={0,i};
            ret[i]=this.dfs(initCoord,grid);            
        }
        return ret;
    }
    
    private int dfs(int[] coord, int[][] grid){
        int x=coord[0];
        int y=coord[1];
        // System.out.println(x+","+y);
        // baseline case
        if(x==grid.length){ return y;}
        // recursion case
        if(grid[x][y]==1){
            if(y+1>=grid[0].length || grid[x][y+1]==-1){
                return -1; // i.e. out of boundary or stucked
            }else{
                return dfs(new int[]{x+1,y+1},grid);
            }
        }else{//-1
            if(y-1<0 || grid[x][y-1]==1){
                return -1; // i.e. out of boundary or stucked
            }else{
                return dfs(new int[]{x+1,y-1},grid);
            }
        }
    }
}
