# dcard_crawler
-------------------

Dcard 文章/推文爬蟲

* 抓取Dcard文章及推文，儲存至Mysql資料庫

# 安裝說明
-------------------
* 安裝MySQL資料庫
* 執行`database/dcard.sql`、`database/dcard_posts.sql`、`database/dcard_comments.sql`
* 
```
git clone https://github.com/sweslo17/chinese_sentiment.git
pip install -r requirements.txt
```
* 修改config.py.template

# 使用說明
-------------------
* `python crawler.py new [N]`回溯更新2小時資料，並新增最新N個post ID資料（往max ID後掃描至max ID+N。default: N=100）
* `python crawler.py last [N]`回溯更新N天資料。（default: N=7）
