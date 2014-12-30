CREATE TABLE `db_user` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `email` varchar(50) NOT NULL COMMENT '注册邮箱',
  `password` varchar(150)  comment '密码加密',
  `nickname` varchar(50) COMMENT '昵称',
  `is_nickname` tinyint(1) NOT NULL default 0 comment '是否昵称',
  `company_id` int(11) NOT NULL comment '公司id',
  `position_id` decimal(10,2) NOT NULL comment '职位id',
  `check_sign` varchar(50) NOT NULL comment '注册验证',
  `register_date` datetime NOT NULL comment '注册时间',
  `is_check_email` tinyint(1)  NOT NULL default 0 comment '是否匿名',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `company_nick` (`company_id`,`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '用户表';

CREATE TABLE `db_company` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `name` varchar(50) NOT NULL COMMENT '公司名称',
  `email` varchar(50) NOT NULL COMMENT '公司邮箱后缀',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司表';

CREATE TABLE `db_position` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `company_id` int(11) NOT NULL COMMENT '公司id',
  `name` varchar(50)  NOT NULL default 'public' comment '职位',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `company_id_name` (`company_id`,`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='职位表';

CREATE TABLE `db_ridicule` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `user_id` int(11) NOT NULL COMMENT '吐槽人id',
  `content` varchar(150)  NOT NULL  comment '吐槽内容',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 comment='吐槽内容表';

CREATE TABLE `db_comment` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `user_id` int(11) NOT NULL COMMENT '评论人id',
  `ridicule_id` int(11)  NOT NULL  comment '评论的吐槽id',
  `content` varchar(50) COMMENT '评论内容',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='评论表';

CREATE TABLE `db_like` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `user_id` int(11) NOT NULL COMMENT 'like人id',
  `ridicule_id` int(11)  NOT NULL  comment 'like的吐槽id',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='like表';

CREATE TABLE `db_friend` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `main_user_id` int(11) NOT NULL COMMENT '当事人id',
  `related_user_id` int(11)  NOT NULL  comment '关系人id',
  `is_open` tinyint(1) not null default 0 comment '是否能看关系人吐槽',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `relationship` (`main_user_id`,`related_user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='用户关系表';

---- reminder----
CREATE TABLE `db_reminder_friend` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `is_read` tinyint(1) NOT NULL default 0 comment '是否阅读',
  `user_id` int(11) NOT NULL COMMENT '当事人id',
  `request_user_id` int(11)  NOT NULL  comment '请求人id',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `relationship` (`user_id`,`request_user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='用户请求提醒表';

CREATE TABLE `db_reminder_like` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `is_read` tinyint(1) NOT NULL default 0 comment '是否阅读',
  `user_id` int(11) NOT NULL COMMENT '当事人id',
  `like_user_id` int(11)  NOT NULL  comment 'like人id',
  `like_ridicule_id` int(11)  NOT NULL  comment 'the ridicule id of like for',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `like_relation` (`like_user_id`,`like_ridicule_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='like提醒表';

CREATE TABLE `db_reminder_comment` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `is_read` tinyint(1) NOT NULL default 0 comment '是否阅读',
  `user_id` int(11) NOT NULL COMMENT '当事人id',
  `comment_user_id` int(11)  NOT NULL  comment 'comment人id',
  `comment_id` int(11)  NOT NULL  comment 'comment id',
  `comment_ridicule_id` int(11)  NOT NULL  comment 'the ridicule id of comment for',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `comment_id` (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='comment提醒表';
------ reminder----

---------boycott------------
CREATE TABLE `db_boycott` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `user_id` int(11) NOT NULL COMMENT 'id of user who start the boycott',
  `content` int(11)  NOT NULL  comment 'content of the boycott',
  `status` int(11)  NOT NULL  comment 'status of boycott(start,end)',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='boycott';

CREATE TABLE `db_boycott_like` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `user_id` tinyint(1) NOT NULL default 0 comment 'id of user who like the boycott',
  `boycott_id` int(11) NOT NULL COMMENT 'id of boycott',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id_boycott_id` (`user_id`,`boycott_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='like of boycott_id';

CREATE TABLE `db_boycott_comment` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `user_id` tinyint(1) NOT NULL default 0 comment 'id of user who comment the boycott',
  `boycott_id` int(11) NOT NULL COMMENT 'id of the boycott',
  `content` int(11)  NOT NULL  comment 'content of the comment',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='comment of boycott';

CREATE TABLE `db_boycott_result` (
  `id` int(11) NOT NULL auto_increment,
  `is_delete` tinyint(1) NOT NULL default 0 comment '是否删除',
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `user_id` tinyint(1) NOT NULL default 0 comment 'id of user who send result',
  `boycott_id` int(11) NOT NULL COMMENT 'id of the boycott',
  `content` int(11)  NOT NULL  comment 'content of boycott result'
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='result of boycott';
----- boycott---




