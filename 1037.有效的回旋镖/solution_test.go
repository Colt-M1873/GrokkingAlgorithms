package leetcode
import (
	"reflect"
	"testing"
)
// 1037.有效的回旋镖
// https://leetcode-cn.com/problems/valid-boomerang
func isBoomerang(points [][]int) bool {

}
func TestSolution(t *testing.T) {
	testCases := []struct {
		desc string
		want 
	}{
		{
            want: ,
		},
	}
	for _, tC := range testCases {
		t.Run(tC.desc, func(t *testing.T) {
			get := 
			if !reflect.DeepEqual(tC.want,get){
				t.Errorf("input: %+v get: %v\n",tC,get)
			}
		})
	}
}
