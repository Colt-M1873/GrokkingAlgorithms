// https://leetcode.com/problems/valid-sudoku/
// 2022年07月22日 14:32:52

import "fmt"
func isValidSudoku(board [][]byte) bool {
    // check within row and column
    for i:=0;i<9;i++{ 
        mRow:=make(map[byte]int)
        mCol:=make(map[byte]int)
        for j:=0;j<9;j++{
            if board[i][j]!=byte('.'){                
                if _,ok:=mRow[board[i][j]];!ok{ // check i th row
                    mRow[board[i][j]]=0
                }else{
                    return false
                }
            }
            if board[j][i]!=byte('.'){                
                if _,ok:=mCol[board[j][i]];!ok{ // check i th column
                    mCol[board[j][i]]=0
                }else{
                    return false
                }
            }
        }
    }
    // check within 3x3 boxes
    for i:=0;i<9;i+=3{
        for j:=0;j<9;j+=3{
            mBox:=make(map[byte]int)
            for k:=0;k<3;k++{
                for l:=0;l<3;l++{
                    if board[i+k][j+l]!=byte('.'){
                        if _,ok:=mBox[board[i+k][j+l]];ok{
                            return false
                        }
                        mBox[board[i+k][j+l]]=0
                    }
                }
            }
        }
    }
    return true
}