echo on
cd /d d:
cd Git_repos/GrokkingAlgorithms

echo %date% %time%>> a.txt
echo ping baidu.com >> a.txt
echo %date% %time%>> gitbatlog.txt

@REM echo git diff >>gitbatlog.txt
@REM git diff >>gitbatlog.txt

echo git status >> gitbatlog.txt
git status >> gitbatlog.txt

echo git add --all >> gitbatlog.txt
git add --all >> gitbatlog.txt

echo git commit -m 'mostly Leetcode problems solved, commited and pushed by bat' >> gitbatlog.txt
git commit -m "mostly Leetcode problems solved, commited and pushed by bat" >> gitbatlog.txt

echo git push origin master >> gitbatlog.txt
git push origin master >> gitbatlog.txt

echo.>>gitbatlog.txt