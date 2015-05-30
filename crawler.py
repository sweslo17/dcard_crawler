# coding=utf-8
import requests
import json
import time
import mysql.connector
import config
import datetime
from dateutil import parser

cnx = mysql.connector.connect(host=config.db_host, user=config.db_user, passwd=config.db_password, database=config.db_database)
cur = cnx.cursor()

def crawl(id_list,update_time):
	for post_id in id_list:
		while True:
			try:
				result = requests.get('https://www.dcard.tw/api/post/all/' + str(post_id)).json()
				print 'https://www.dcard.tw/api/post/all/' + str(post_id)
				parse_result(post_id,result,update_time)
				break
			except requests.exceptions.ConnectionError:
				print str(post_id) + ' error: ' + 'connection error.'
				time.sleep(5)
				continue

def parse_result(post_id,raw_data,update_time):
	#print raw_data
	if 'error' in raw_data and raw_data['error'] is True:
		print str(post_id) + ' error: ' + raw_data['msg']
		return
	write_post(post_id,raw_data,update_time)
	for comment in raw_data['comment']:
		write_comment(post_id,comment,update_time)


def write_post(post_id,post_data,update_time):
	#print post_data.keys()
	sql = '''REPLACE INTO `dcard`.`posts` 
(`id`, 
`forum_alias`, 
`excerpt`, 
`pinned`, 
`anonymousDepartment`, 
`anonymousSchool`, 
`reply`, 
`updatedAt`, 
`createdAt`, 
`follow`, 
`commentCount`, 
`likeCount`, 
`like`, 
`title`, 
`content`, 
`author_gender`, 
`author_school`, 
`author_department`, 
`isLiked`, 
`currentUser`, 
`precious`,
`update_time`
)
VALUES
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
	id = post_id
	forum_alias = post_data['forum_alias']
	excerpt = post_data['excerpt']# if 'excerpt' in post_data else None
	pinned = post_data['pinned']# if 'pinned' in post_data else None
	anonymousDepartment = post_data['anonymousDepartment'] if 'anonymousDepartment' in post_data else None
	anonymousSchool = post_data['anonymousSchool'] if 'anonymousSchool' in post_data else None
	reply = post_data['reply']# if 'reply' in post_data else None
	updatedAt = parse_datetime(post_data['updatedAt'])
	createdAt = parse_datetime(post_data['createdAt'])# if 'createdAt' in post_data else None
	follow = post_data['follow']# if 'follow' in post_data else None
	commentCount = post_data['commentCount']# if 'commentCount' in post_data else None
	likeCount = post_data['likeCount']# if 'likeCount' in post_data else None
	like = post_data['like']# if 'like' in post_data else None
	title = post_data['version'][0]['title']# if 'title' in post_data['version'][0] else None
	content = post_data['version'][0]['content']# if 'content' in post_data['version'][0] else None
	author_gender = post_data['member']['gender']# if 'gender' in post_data['member'] else None
	author_school = post_data['member']['school']# if 'school' in post_data['member'] else None
	author_department = post_data['member']['department']# if 'department' in post_data['member'] else None
	isLiked = post_data['isLiked']# if 'isLiked' in post_data else None
	currentUser = post_data['currentUser']# if 'currentUser' in post_data else None
	precious = post_data['precious']# if 'precious' in post_data else None
	cur.execute(sql,(id, forum_alias, excerpt, pinned, anonymousDepartment, anonymousSchool, reply, updatedAt, createdAt, follow, commentCount, likeCount, like, title, content, author_gender, author_school, author_department, isLiked, currentUser,precious,update_time))
	cnx.commit()


def write_comment(post_id,comment_data,update_time):
	sql = '''REPLACE INTO `dcard`.`comments` 
(`id`, 
`author_gender`, 
`author_school`, 
`author_department`, 
`content`, 
`createdAt`, 
`like`, 
`hidden`, 
`anonymous`, 
`host`, 
`num`, 
`currentUser`, 
`isLiked`, 
`post_id`, 
`update_time`
)
VALUES
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
	id = comment_data['_id']
	author_gender = comment_data['member']['gender'] if 'member' in comment_data else None
	author_school = comment_data['member']['school'] if 'member' in comment_data else None
	author_department = comment_data['member']['department'] if 'member' in comment_data else None
	content = comment_data['version'][0]['content']
	createdAt = parse_datetime(comment_data['version'][0]['createdAt'])
	like = comment_data['like']
	if not isinstance(like,int):
		like = len(like)
	hidden = comment_data['hidden']
	anonymous = comment_data['anonymous'] if 'anonymous' in comment_data else None
	host = comment_data['host'] if 'host' in comment_data else None
	num = comment_data['num'] if 'num' in comment_data else None
	currentUser = comment_data['currentUser'] if 'currentUser' in comment_data else None
	isLiked = comment_data['isLiked'] if 'isLiked' in comment_data else None
	cur.execute(sql,(id,author_gender, author_school, author_department, content, createdAt, like, hidden, anonymous, host, num, currentUser, isLiked, post_id, update_time))
	cnx.commit()

def parse_datetime(input_time):
	locale = datetime.timedelta(hours=8)
	if isinstance(input_time,int):
		return datetime.datetime.fromtimestamp(input_time/1000) + locale
	else:
		return parser.parse(input_time) + locale


if __name__ == '__main__':
	update_time = datetime.datetime.now()
	page_list = range(25212, 300000)
	crawl(page_list,update_time)
