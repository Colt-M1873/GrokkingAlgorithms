// https://leetcode.com/problems/first-bad-version/
// 2022年07月02日 10:23:55

/** 
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad 
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

 func firstBadVersion(n int) int {
    l,h:=0,n
    for l<=h {
        mid:=(l+h)/2
        if isBadVersion(mid) {
            h=mid-1
        }else{
            l=mid+1
        }
    }
    return l
}