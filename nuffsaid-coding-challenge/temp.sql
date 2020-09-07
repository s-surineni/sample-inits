INSERT INTO Worker
	(WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES
		(017, 'Monika', 'Arora', 100000, '14-02-20 09.00.00', 'Account'),
		(018, 'Niharika', 'Verma', 80000, '14-06-11 09.00.00', 'Admin'),
		(019, 'Vishal', 'Singhal', 300000, '14-02-20 09.00.00', 'Account'),
		(020, 'Amitabh', 'Singh', 500000, '14-02-20 09.00.00', 'Admin'),
		(021, 'Vivek', 'Bhati', 500000, '14-06-11 09.00.00', 'Admin'),
		(022, 'Vipul', 'Diwan', 200000, '14-06-11 09.00.00', 'Admin'),
		(023, 'Satish', 'Kumar', 75000, '14-01-20 09.00.00', 'Admin'),
		(024, 'Geetika', 'Chauhan', 90000, '14-04-11 09.00.00', 'Admin');

SELECT W.FIRST_NAME, T.WORKER_TITLE FROM Worker W INNER JOIN Title T ON W.WORKER_ID = T.WORKER_REF_ID AND T.WORKER_TITLE in ('Manager');
