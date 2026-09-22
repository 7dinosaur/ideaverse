#！/bin/bash

current_date=$(date +%Y%m%d)

git pull

git add .

# 提交
git commit -m 'updated${current_date}_xk'

git push