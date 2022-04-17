#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int row = 0, col = 0;
//往右边跳到不能跳为止
//void right(vector<vector<char>>& nums, int n, int m)
void right(vector<string>& nums, int n, int m)
{
	while (col < m-2)
	{
		col += 2;
		if (nums[row][col] == '*')//如果是海.就不能跳，如果是陆地*就能跳
		{
			nums[row][col] = '.';
		}
		else
		{
			break;
		}
	}
}
//往下边跳到不能跳为止
//void down(vector<vector<char>>& nums, int n, int m)
void down(vector<string>& nums, int n, int m)
{
	while (row < n - 2)
	{
		row += 2;
		if (nums[row][col] == '*')//如果是海.就不能跳，如果是陆地*就能跳
		{
			nums[row][col] = '.';
		}
		else
		{
			break;
		}
	}
}
//往左边跳到不能跳为止
//void left(vector<vector<char>>& nums, int n, int m)
void left(vector<string>& nums, int n, int m)
{
	while (col > 1)
	{
		col -= 2;
		if (nums[row][col] == '*')//如果是海.就不能跳，如果是陆地*就能跳
		{
			nums[row][col] = '.';
		}
		else
		{
			break;
		}
	}
}
//往上边跳到不能跳为止
//void up(vector<vector<char>>& nums, int n, int m)
void up(vector<string>& nums, int n, int m)
{
	while (row > 1)
	{
		row -= 2;
		if (nums[row][col] == '*')//如果是海.就不能跳，如果是陆地*就能跳
		{
			nums[row][col] = '.';
		}
		else
		{
			break;
		}
	}
}


int main()
{
	//深度优先搜索
	int n, m;
	cin >> n >> m;

	vector<string> nums(n);
	for (int i = 0; i < n; i++)
	{
		cin >> nums[i];
	}

	int result = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (nums[i][j] == '*')
			{
				row = i, col = j;
				result++;
				right(nums, n, m);
				down(nums, n, m);
				left(nums, n, m);
				up(nums, n, m);

			}
		}
	}

	cout << "result:" << result << endl;
	

	return 0;
}