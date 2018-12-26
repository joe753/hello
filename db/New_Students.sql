select * from Test;

insert  into Test(id, name) values (3, 'aaa');

truncate Test;
select * from Club;

select * from Student;

ALTER TABLE New_Student AUTO_INCREMENT = 1;



update Club set leader = null where id > 0;

create temporary table Temp_Subject(name varchar(31));

insert into Temp_Subject(name) select name from Subject order by name;
select group_concat(name) from Temp_Subject;

select count(*) from Student where phone like '010-5%' or phone like '010-2%' or phone like '010-6%' or phone like '010-4%' or phone like '010-8%';


select min(sub.name) as '과목' , (case s.gender when 1 then '남' else '여' end) as '성별', count(*) as '학생수'
from Enroll en inner join New_Student s on en.student = s.id 
			   inner join Subject sub on en.subject = sub.id
where s.addr = '서울'
  group by s.gender, sub.id	
  order by sub.name, s.gender desc ;
  
