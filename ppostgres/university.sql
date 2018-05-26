--- 6.1.1.1 The Select Operation  σ
select * from instructor where dept_name='Physics';
-- find all instructors with salary greater than $90,000 by writing 
select * from instructor where salary>90000;
-- find the instructors in Physics with a salary greater than $90,000
select * from instructor where salary>90000 and dept_name='Physics';
-- find all departments whose name is the same as their building name
select * from department where dept_name=building;


--- project operation π
select id, name, salary from instructor;

-- Find the name of all instructors in the Physics department.
select name from instructor where dept_name='Physics'; 


-- Union operation ∪
-- find the set of all courses taught in the Fall 2009 semester, the Spring 2010 semester, or both
select course_id from section where semester='Fall' and year=2009 union select course_id from section where semester='Spring' and year=2010;


-- set difference −
-- find all the courses taught in the Fall 2009 semester but not in Spring 2010 semester
select course_id from section where semester='Fall' and year=2009 except select course_id from section where semester='Spring' and year=2010;


-- The Cartesian-Product ×