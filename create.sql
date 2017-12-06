create table resume_base_info (resumeId VARCHAR(50) PRIMARY KEY
  , resumeCode VARCHAR(50) DEFAULT '',
name VARCHAR(50) DEFAULT '', sex VARCHAR(50) DEFAULT '',
birthday VARCHAR(50) DEFAULT '', eduBack VARCHAR(50) DEFAULT '',
eduDegree VARCHAR(50) DEFAULT '', school VARCHAR(50) DEFAULT '',
phone VARCHAR(50) DEFAULT '', homePhone VARCHAR(50) DEFAULT '',
resumePath VARCHAR(100) DEFAULT '',politicsStatus VARCHAR(50) DEFAULT '',
nativePlace VARCHAR(50) DEFAULT '', address VARCHAR(100) DEFAULT '',
bigBang VARCHAR(200) DEFAULT '',height VARCHAR(50) DEFAULT '',
  healtht VARCHAR(50) DEFAULT '',marriage VARCHAR(50) DEFAULT ''
,idcard VARCHAR(50) DEFAULT '')ENGINE =InnoDb DEFAULT CHARSET =utf8;

create table edu(eduId VARCHAR(50) PRIMARY KEY ,
resumeId VARCHAR(50) DEFAULT '', eduType VARCHAR(50) DEFAULT '',
schoolName VARCHAR(100) DEFAULT '', eduDate VARCHAR(50) DEFAULT '',
eduPro VARCHAR(50) DEFAULT '')ENGINE =InnoDb DEFAULT CHARSET =utf8;

create table family(familyId VARCHAR(50) PRIMARY KEY ,
resumeId VARCHAR(50) DEFAULT '', relationShip VARCHAR(50) DEFAULT '',
name VARCHAR(50) DEFAULT '', politicsStatus VARCHAR(50) DEFAULT '',
company VARCHAR(50) DEFAULT '', job VARCHAR(50))ENGINE =InnoDb DEFAULT CHARSET =utf8;