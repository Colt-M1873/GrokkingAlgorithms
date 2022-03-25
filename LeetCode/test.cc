
#include <iostream>
#include <string>
#include <vector>
using namespace std;


char inverse_letter(char temp)
{
 if (temp >= 'A' && temp <= 'Z')
  return temp + 32;
 else
  return temp - 32;
}

int main()
{
 int n = 0, m = 0, q = 0;
 cin >> n;
 cin >> m;
 cin >> q;
 vector<string> matrix(n);
 for (int i = 0; i < n; i++)
 {
  cin >> matrix[i];
  getchar(); 
 }
 vector<vector<int>> oper(q, vector<int>(4,0));
 for (int i = 0; i < q; i++)
 {
  for (int j = 0; j < 4; j++)
  {
   cin >> oper[i][j];
  }
 }
 
 for (int i = 0; i < q; i++)
 {
  int x1 = oper[i][0]-1;
  int y1 = oper[i][1]-1;
  int x2 = oper[i][2]-1;
  int y2 = oper[i][3]-1;
  for (int j = x1; j <= x2; j++)
  {
   for (int k = y1; k <= y2; k++)
   {
    matrix[j][k] = inverse_letter(matrix[j][k]);
   }
  }
 }
 for (int i = 0; i < n; i++)
 {
  cout << matrix[i] << endl; 
 }
 return 0;
}
第四题示例跑出来了 但不知道题目的输入坐标是否都是合法的，没处理这个问题





























//
int main()
{
 int k = 3;
 //cin >> k;
 string s;
 cin >> s;
 int left = 0, right = 0;
 int len = s.size();
 map<char, int> map;
 int count = 0;
 int result = 0;
 while (right < len)
 {
  //取出右边的
  char high = s[right];
  if (map.find(high) == map.end())
  {
   count++;//如果是新的就++
  }
  map[high]++;
  right++;
  if (count > k)//就要移动左边的
  {
   char low = s[left];
   //如果那个l的大于1，那就不要count--
   if (map[low] > 1) map[low]--;
   else count--;
   left++;
  }
  //这里记录一下数值
  result = max(result, right - left + 1);
 }
 cout << "result:" << result << endl;

 return 0;
}