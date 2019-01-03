CREATE TABLE run_Board (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    description text
);
CREATE TABLE run_Post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author text,
    title text,
    description text
);

CREATE TABLE hala_Board (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    description text
);

CREATE TABLE hala_Post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author text,
    title text,
    description text
);

CREATE TABLE sex_Board (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    description text
);

CREATE TABLE sex_Post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author text,
    title text,
    description text
);

CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    picture text,
    username text,
    password text,
    coin INTEGER,
    login_count INTEGER,
    is_admin BOOLEAN,
    is_active BOOLEAN,
    profile text
);

-- board新增
insert into run_Board (name, description) values ('run', '約跑');
insert into hala_Board (name, description) values ('hala','哈龜');
insert into sex_Board (name, description) values ('sex', '做愛');
-- 使用者新增
insert into User (username, password, login_count, is_admin, is_active, profile) values (
    '鐘良軒', 'iam30cm', 0, 0, 1, "我ㄉGG有30公分");
insert into User (username, password, login_count, is_admin, is_active, profile) values (
    'milli', 'GGstinky', 0, 0, 1, "我有stinkyGG");
insert into User (username, password, login_count, is_admin, is_active, profile) values (
    'yochang', 'localsmoke', 0, 0, 1, "同學，遠端抽煙嗎？");
--run_post新增
insert into run_Post(author,title,description) values(
     '鐘良軒','鍋鍋鍋鍋鍋鍋鍋鍋郭家雞肉飯','現在是誰在被我約跑啊？(　･`ω･´)');
insert into run_Post(author,title,description) values(
     'milli','約跑','男 台北 處女 20y 晚上6點約嗎？(ฅ`ω´ฅ)');
insert into run_Post(author,title,description) values(
     'yochang','你以為我要約跑嗎？','我不只約還要約 Icloud Smoke (´･ω･`)');
--hala_post新增
insert into hala_Post(author,title,description) values(
     '鐘良軒','你知道嗎？','窮的時候，賺點錢就不窮了');
insert into hala_Post(author,title,description) values(
     'milli','太酷了吧','台北市改民國市，中華台北就變中華民國了呢！');
insert into hala_Post(author,title,description) values(
     'yochang','我有個大膽的想法','人類的避孕藥，猩猩也可以用。');
--sex_post新增
insert into sex_Post(author,title,description) values(
     '鐘良軒','NYKD-54','嘔嘔嘔嘔嘔嘔嘔');
insert into sex_Post(author,title,description) values(
     'milli','200GANA-1200','好文推推推');
insert into sex_Post(author,title,description) values(
     'yochang','SSNI-205','好文推推推');


