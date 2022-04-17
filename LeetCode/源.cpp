#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int row = 0, col = 0;
//���ұ�����������Ϊֹ
//void right(vector<vector<char>>& nums, int n, int m)
void right(vector<string>& nums, int n, int m)
{
	while (col < m-2)
	{
		col += 2;
		if (nums[row][col] == '*')//����Ǻ�.�Ͳ������������½��*������
		{
			nums[row][col] = '.';
		}
		else
		{
			break;
		}
	}
}
//���±�����������Ϊֹ
//void down(vector<vector<char>>& nums, int n, int m)
void down(vector<string>& nums, int n, int m)
{
	while (row < n - 2)
	{
		row += 2;
		if (nums[row][col] == '*')//����Ǻ�.�Ͳ������������½��*������
		{
			nums[row][col] = '.';
		}
		else
		{
			break;
		}
	}
}
//���������������Ϊֹ
//void left(vector<vector<char>>& nums, int n, int m)
void left(vector<string>& nums, int n, int m)
{
	while (col > 1)
	{
		col -= 2;
		if (nums[row][col] == '*')//����Ǻ�.�Ͳ������������½��*������
		{
			nums[row][col] = '.';
		}
		else
		{
			break;
		}
	}
}
//���ϱ�����������Ϊֹ
//void up(vector<vector<char>>& nums, int n, int m)
void up(vector<string>& nums, int n, int m)
{
	while (row > 1)
	{
		row -= 2;
		if (nums[row][col] == '*')//����Ǻ�.�Ͳ������������½��*������
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
	//�����������
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