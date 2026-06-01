# 云南央企国企招聘 - Git推送命令
# 注意：请先在 GitHub 上创建空仓库，然后将下方 YOUR_USERNAME 和 YOUR_REPO_NAME 替换为你的实际用户名和仓库名

# 1. 初始化 Git 仓库
cd J:/yunnan-enterprise
git init

# 2. 配置 Git 用户信息（如果尚未配置）
git config --local user.email "your.email@example.com"
git config --local user.name "Your Name"

# 3. 添加所有文件到暂存区
git add .

# 4. 提交所有文件
git commit -m "Initial commit: 云南央企国企招聘查询系统"

# 5. 添加远程仓库（请替换为你自己的 GitHub 仓库地址）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 6. 重命名分支为 main
git branch -M main

# 7. 推送到 GitHub（首次推送需要输入 GitHub 用户名和密码/令牌）
git push -u origin main

#==============================================================
# 辅助命令：
#--------------------------------------------------------------

# 查看当前状态
git status

# 查看提交历史
git log --oneline

# 查看远程仓库地址
git remote -v

# 如果推送失败提示需要认证，请使用 GitHub Personal Access Token：
# 在 GitHub → Settings → Developer settings → Personal access tokens → Generate new token
# 然后用以下命令添加认证：
# git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 后续推送命令（首次推送后使用）
git push origin main