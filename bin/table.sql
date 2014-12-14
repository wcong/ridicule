CREATE TABLE `db_users` (
  `id` int(11) NOT NULL auto_increment,
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `email` varchar(50) NOT NULL COMMENT '注册邮箱',
  `password` varchar(150)  NOT NULL  comment '密码加密',
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
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `name` varchar(50) NOT NULL COMMENT '公司名称',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司表';

CREATE TABLE `db_position` (
  `id` int(11) NOT NULL auto_increment,
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `company_id` int(11) NOT NULL COMMENT '公司id',
  `name` varchar(50)  NOT NULL  comment '职位',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `company_id_name` (`company_id`,`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='职位表';

CREATE TABLE `db_redicule` (
  `id` int(11) NOT NULL auto_increment,
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `user_id` int(11) NOT NULL COMMENT '吐槽人id',
  `content` varchar(150)  NOT NULL  comment '吐槽内容',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 comment='吐槽内容表';

CREATE TABLE `db_comment` (
  `id` int(11) NOT NULL auto_increment,
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `user_id` int(11) NOT NULL COMMENT '评论人id',
  `redicule_id` int(11)  NOT NULL  comment '评论的吐槽id',
  `content` varchar(50) COMMENT '评论内容',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='评论表';

CREATE TABLE `db_like` (
  `id` int(11) NOT NULL auto_increment,
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `user_id` int(11) NOT NULL COMMENT 'like人id',
  `redicule_id` int(11)  NOT NULL  comment 'like的吐槽id',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='like表';

CREATE TABLE `db_relationship` (
  `id` int(11) NOT NULL auto_increment,
  `create_time` datetime NOT NULL,
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `main_user_id` int(11) NOT NULL COMMENT '当事人id',
  `related_user_id` int(11)  NOT NULL  comment '关系人id',
  `is_readable` tinyint(1) not null default 0 comment '是否能看关系人吐槽',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `relationship` (`main_user_id`,`related_user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  comment='用户关系表';