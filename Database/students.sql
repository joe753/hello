PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE Student (
id integer primary key autoincrement not null,
name text not null default 'aaa',
mobile text null);
INSERT INTO Student VALUES(1,'홍길동','010-2323-4545');
INSERT INTO Student VALUES(2,'홍길순',NULL);
INSERT INTO Student VALUES(3,'aaa','010-4669-4255');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('Student',3);
COMMIT;
