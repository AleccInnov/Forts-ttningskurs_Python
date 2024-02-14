Olika sätt att få färdigsorterade resultat från en databas:

SELECT * FROM my_table ORDER BY column_name ASC;

SELECT * FROM users ORDER BY age DESC;

SELECT * FROM users ORDER BY age ASC, name ASC;

SELECT * FROM highscore ORDER BY score DESC LIMIT 10;


Om du vill ha slumpa vilken information som du hämtar ur databasen:

SELECT name FROM users ORDER BY RANDOM() LIMIT 1;



Man kan också lägga till flera krav i en sql-sats:
AND - kan användas om två saker ska gälla samtidigt:
SELECT * FROM my_table WHERE column1=2 AND column2=5;
SELECT * FROM employees WHERE department = 'IT' AND salary > 50000;

OR - kan användas istället om det ena eller det andra gäller
SELECT * FROM employees WHERE department = 'IT' OR salary > 50000;
SELECT * FROM employees WHERE department = 'HR' OR department = 'Finance';

NOT - kan användas om man vill utesluta särskilda resultat
SELECT * FROM students WHERE NOT grade = 'F';

Och alla dessa kan förstås kombineras:
SELECT * FROM employees WHERE department = 'IT' AND (salary > 50000 OR NOT experience = 'Senior');





