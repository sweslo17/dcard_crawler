CREATE TABLE `comments` (
		`id` varchar(50) NOT NULL,
		`author_gender` varchar(10) DEFAULT NULL,
		`author_school` varchar(100) DEFAULT NULL,
		`author_department` varchar(500) DEFAULT NULL,
		`content` mediumtext,
		`createdAt` datetime DEFAULT NULL,
		`like` int(11) DEFAULT NULL,
		`hidden` tinyint(1) DEFAULT NULL,
		`anonymous` tinyint(1) DEFAULT NULL,
		`host` tinyint(1) DEFAULT NULL,
		`num` int(11) DEFAULT NULL,
		`currentUser` tinyint(1) DEFAULT NULL,
		`isLiked` tinyint(1) DEFAULT NULL,
		`post_id` varchar(50) DEFAULT NULL,
		`update_time` datetime DEFAULT NULL,
		PRIMARY KEY (`id`),
		KEY `post_id` (`post_id`),
		KEY `author_gender` (`author_gender`),
		KEY `author_school` (`author_school`),
		KEY `author_department` (`author_department`(333)),
		KEY `createdAt` (`createdAt`)
	) ENGINE=MyISAM DEFAULT CHARSET=utf8;

