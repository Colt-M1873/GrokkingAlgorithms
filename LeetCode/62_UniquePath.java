// https://leetcode.com/problems/unique-paths/
// 2023年08月29日 10:55:43

// v1 12ms 40.9MB time O(mn) space O(mn)
class Solution {
    public int uniquePaths(int m, int n) {
        int[] row=new int[n];
        Arrays.fill(row,1);
        ArrayList<List<Integer>> grid=new ArrayList<List<Integer>>();
        for(int i=0;i<m;i++){
            grid.add(Arrays.stream(row).boxed().collect(Collectors.toList()));
        }
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                System.out.println(grid.get(i).get(j));
                grid.get(i).set(j,grid.get(i).get(j-1)+grid.get(i-1).get(j));
            }
        }
        for(int i=0;i<m;i++){
            System.out.println(grid.get(i));
        }
        
        return grid.get(m-1).get(n-1);
    }
}


// v2 0ms 39.5MB time O(mn) space O(n)
class Solution {
    public int uniquePaths(int m, int n) {
        // 两行交替进行
        if(m<2||n<2){return 1;}
        int[] oldrow=new int[n];
        Arrays.fill(oldrow,1);
        int[] newrow=new int[n];
        for(int i=1;i<m;i++){
            newrow[0]=1;
            for(int j=1;j<n;j++){
                newrow[j] = newrow[j-1] + oldrow[j];
            }
            oldrow=newrow.clone();
        }
        return newrow[n-1];
    }
}


// v3 0ms 38.9MB time O(mn) space O(n)
class Solution {
    public int uniquePaths(int m, int n) {
        // 一行自身迭代
        if(m<2||n<2){return 1;}
        int[] row=new int[n];
        Arrays.fill(row,1);
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                row[j] = row[j-1] + row[j];
            }
        }
        return row[n-1];
    }
}

// 数学公式
