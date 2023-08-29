// https://leetcode.com/problems/unique-paths-ii/description/
// 2023年08月29日 11:47:17

// 遇到障碍就把障碍格子设置为0，因为各条路径都不能到达障碍格，即能到达障碍格的路径数是0，然后把这个障碍等于0的条件直接加入到 62题中 当前格=左格+上格 的递推公式就可以了
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // if obstacle grid=1 ,then grid=0
        for(int i=0;i<obstacleGrid.length;i++){
            for(int j=0;j<obstacleGrid[0].length;j++){
                if(obstacleGrid[i][j]==1){ // obstacle  grid
                    obstacleGrid[i][j]=0;
                }else{
                    if(i==0 && j==0){
                        obstacleGrid[0][0]=1;
                    }else if(i==0){
                        obstacleGrid[i][j]=obstacleGrid[i][j-1];
                    }else if(j==0){
                        obstacleGrid[i][j]=obstacleGrid[i-1][j];
                    }else{
                        obstacleGrid[i][j]=obstacleGrid[i][j-1]+obstacleGrid[i-1][j];
                    }
                }
            }
        }
        return obstacleGrid[obstacleGrid.length-1][obstacleGrid[0].length-1];
    }
}
