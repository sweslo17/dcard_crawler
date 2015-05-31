CREATE TABLE `posts` (
		`id` varchar(50) NOT NULL,
		`forum_alias` varchar(50) DEFAULT NULL,
		`excerpt` varchar(500) DEFAULT NULL,
		`pinned` tinyint(1) DEFAULT NULL,
		`anonymousDepartment` tinyint(1) DEFAULT NULL,
		`anonymousSchool` tinyint(1) DEFAULT NULL,
		`reply` int(11) DEFAULT NULL,
		`updatedAt` datetime DEFAULT NULL,
		`createdAt` datetime DEFAULT NULL,
		`follow` tinyint(1) DEFAULT NULL,
		`commentCount` int(11) DEFAULT NULL,
		`likeCount` int(11) DEFAULT NULL,
		`like` int(11) DEFAULT NULL,
		`title` varchar(1000) DEFAULT NULL,
		`content` mediumtext,
		`author_gender` varchar(10) DEFAULT NULL,
		`author_school` varchar(100) DEFAULT NULL,
		`author_department` varchar(500) DEFAULT NULL,
		`isLiked` tinyint(1) DEFAULT NULL,
		`currentUser` tinyint(1) DEFAULT NULL,
		`precious` tinyint(1) DEFAULT NULL,
		`update_time` datetime DEFAULT NULL,
		PRIMARY KEY (`id`),
		KEY `form_alias` (`forum_alias`),
		KEY `createdAt` (`createdAt`),
		KEY `updatedAt` (`updatedAt`),
		KEY `author_gender` (`author_gender`),
		KEY `author_school` (`author_school`),
		KEY `author_department` (`author_department`(333))
	) ENGINE=MyISAM DEFAULT CHARSET=utf8;