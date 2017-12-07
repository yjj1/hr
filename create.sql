-- auto-generated definition
CREATE TABLE resume_base_info
(
  resumeId         VARCHAR(50)             NOT NULL
    PRIMARY KEY,
  resumeCode       VARCHAR(50) DEFAULT ''  NULL,
  name             VARCHAR(50) DEFAULT ''  NULL,
  sex              VARCHAR(50) DEFAULT ''  NULL,
  birthday         VARCHAR(50) DEFAULT ''  NULL,
  eduBack          VARCHAR(50) DEFAULT ''  NULL,
  eduDegree        VARCHAR(50) DEFAULT ''  NULL,
  school           VARCHAR(50) DEFAULT ''  NULL,
  phone            VARCHAR(50) DEFAULT ''  NULL,
  homePhone        VARCHAR(50) DEFAULT ''  NULL,
  resumePath       VARCHAR(100) DEFAULT '' NULL,
  politicsStatus   VARCHAR(50) DEFAULT ''  NULL,
  nativePlace      VARCHAR(50) DEFAULT ''  NULL,
  address          VARCHAR(100) DEFAULT '' NULL,
  bigBang          VARCHAR(200) DEFAULT '' NULL,
  height           VARCHAR(50) DEFAULT ''  NULL,
  healthy          VARCHAR(50) DEFAULT ''  NULL,
  marriage         VARCHAR(50) DEFAULT ''  NULL,
  idcard           VARCHAR(50) DEFAULT ''  NULL,
  job              VARCHAR(50) DEFAULT ''  NULL,
  isAddressControl VARCHAR(50) DEFAULT ''  NULL
)ENGINE =InnoDb DEFAULT CHARSET =utf8;

-- auto-generated definition
CREATE TABLE edu
(
  eduId      VARCHAR(50)             NOT NULL
    PRIMARY KEY,
  resumeId   VARCHAR(50) DEFAULT ''  NULL,
  eduType    VARCHAR(50) DEFAULT ''  NULL,
  schoolName VARCHAR(100) DEFAULT '' NULL,
  eduDate    VARCHAR(50) DEFAULT ''  NULL,
  eduPro     VARCHAR(50) DEFAULT ''  NULL
)ENGINE =InnoDb DEFAULT CHARSET =utf8;

-- auto-generated definition
CREATE TABLE family
(
  familyId       VARCHAR(50)            NOT NULL
    PRIMARY KEY,
  resumeId       VARCHAR(50) DEFAULT '' NULL,
  relationShip   VARCHAR(50) DEFAULT '' NULL,
  name           VARCHAR(50) DEFAULT '' NULL,
  politicsStatus VARCHAR(50) DEFAULT '' NULL,
  company        VARCHAR(50) DEFAULT '' NULL,
  job            VARCHAR(50)            NULL
)ENGINE =InnoDb DEFAULT CHARSET =utf8;

-- auto-generated definition
CREATE TABLE resume_apply
(
  applyId   VARCHAR(50)            NOT NULL
    PRIMARY KEY,
  applier   VARCHAR(50) DEFAULT '' NULL,
  resumeId  VARCHAR(50) DEFAULT '' NULL,
  applyDate VARCHAR(50) DEFAULT '' NULL,
  emailId   VARCHAR(50) DEFAULT '' NULL,
  status    VARCHAR(50) DEFAULT '' NULL
)ENGINE =InnoDb DEFAULT CHARSET =utf8;

-- auto-generated definition
CREATE TABLE origin_email
(
  emailId     VARCHAR(50)             NOT NULL
    PRIMARY KEY,
  emailName   VARCHAR(200) DEFAULT '' NULL,
  `from`      VARCHAR(50) DEFAULT ''  NULL,
  `to`        VARCHAR(50) DEFAULT ''  NULL,
  size        VARCHAR(50) DEFAULT ''  NULL,
  report      VARCHAR(50) DEFAULT ''  NULL,
  isRead      VARCHAR(50) DEFAULT ''  NULL,
  sendDate    VARCHAR(50) DEFAULT ''  NULL,
  receiveDate VARCHAR(50) DEFAULT ''  NULL,
  priority    VARCHAR(50) DEFAULT ''  NULL
)ENGINE =InnoDb DEFAULT CHARSET =utf8;

-- auto-generated definition
CREATE TABLE temp_email
(
  emailId   VARCHAR(50)             NOT NULL
    PRIMARY KEY,
  emailName VARCHAR(200) DEFAULT '' NULL
)ENGINE =InnoDb DEFAULT CHARSET =utf8;

create table accessory
(
	accessoryId varchar(50) not null
		primary key,
	accessoryName varchar(100) default '' null,
	emailId varchar(50) null,
	resumeId varchar(50) null,
	path varchar(100) default '' null
)ENGINE =InnoDb DEFAULT CHARSET =utf8;


