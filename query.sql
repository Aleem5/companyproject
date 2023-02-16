-- DDL Commands
CREATE TABLE employee (
  id INT,
  eName VARCHAR(30),
  managerId INT
);
INSERT INTO employee (id, eName, managerId) VALUES (1, "A", 2);
INSERT INTO employee (id, eName, managerId) VALUES (2, "B", 3);
INSERT INTO employee (id, eName, managerId) VALUES (3, "C", 4);
INSERT INTO employee (id, eName, managerId) VALUES (4, "D", 5);
INSERT INTO employee (id, eName, managerId) VALUES (5, "E", 2);
INSERT INTO employee (id, eName, managerId) VALUES (6, "CEO", 0);


-- Query Commands
select 
	e.id as emp_id,
    e.eName as emp_name,
    -- e.managerId as managerId,
	m.eName as manager_name
FROM employee e
LEFT JOIN  employee m ON e.managerId = m.id
ORDER BY e.id;
