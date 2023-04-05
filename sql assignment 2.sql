/* Five Extra Business Rules 
1) One store can have multiple staff and one staff can manage multiple stores.
2) One city can have multiple staff and one staff can have one and only one address. 
3) A store can have one or more customers. 
4) One inventory can have one or more rentals. 
5) One store can have one or more inventories. 


/* 5a) Tell MySQL Workbench which schema to use*/
use sakila; 
/* 5b) Create a SQL program to get an aggregate count of the number of films in this
database */
Select  count(*)
from film ;

/* 5c)Create a SQL program to determine the count of films that include actor Nick
Wahlberg. */
Select count(film_id) AS "No. of Films"
from actor, film_actor
where actor.last_name = 'Wahlberg' and actor.first_name = "Nick"
and film_actor.actor_id = actor.actor_id;  

select count(film_id) AS "No. of Films"
from film_actor
where actor_id in (select actor_id from actor where actor.last_name = 'Wahlberg' and actor.first_name = "Nick");


/* 5d) Write another program that lists 
the films are that have a PG rating. */
Select film.film_id, rating,title
from film 
where rating = 'PG'
group by film_id;

/*5e) Create a SQL program to extract the total
 amount of revenue received (payment
amount) per store manager (staff). Sort by store manager id.*/
SELECT sum(PAYMENT.AMOUNT) as 'Total amonut of revenue', staff_id
from payment 
group by staff_id
order by staff_id; 


/* 5f)Write a SQL program to display the average revenue 
grouped by store. Format the
results to two decimal places and 
sort by the results by average revenue in
descending order.*/

SELECT ROUND(avg(amount),2) as AvgRevenue, store.store_id
FROM payment INNER JOIN (store inner join staff on store.store_id = staff.store_id) 
ON payment.staff_id = staff.staff_id 
group by store.store_id
order by avg(amount) desc;


/* 5g) Create a SQL program which extracts and groups the 
total count of films by rating
and the ORDER BY clause to 
sort the results in descending order by film count. After
running the program, which rating had the highest film count?*/
SELECT rating, count(rating) AS 'Number of films based on Rating'
from film 
GROUP BY rating
order by count(rating) desc;

/* 5h) Display the count of all films grouped by rating. Use a subquery (inner query) to
calculate the total count for all films. */
SELECT temp_table.rating, temp_table.count_rating as 'Number of films based on Rating'
from (SELECT rating, count(rating) AS count_rating
from film 
GROUP BY rating) as temp_table
order by count_rating DESC;


/* 5i) Create a program that selects all films whose title begins with “a” and has a fourth
letter “d”. */
select film_id, title
from film 
where title like 'A___d%';

/* 5j) Use a regular expression with the [] symbols 
to display all film titles having a k or q in
them. */
SELECT title
from film
where TITLE REGEXP '[kq]';

/* 5k) Use the sample solution below to write a query to show overdue film rentals. Search
for films with a return date that is NULL and where the rental date is farther in the past
than the rental duration specified in the film table. If so, the film is overdue, and the
query should produce the name of the overdue film rental, along with the customer
name, phone number, and how many days the rental is overdue. Use CONCAT to
concatenate the last and first names of the customer, the CURRENT_DATE()
function to determine the current date, ISNULL to find the movies where the rental
return date is null, DATEDIFF and INTERVAL to calculate the days overdue, ORDER
BY to sort the results by title. Limit the results to five rows.*/


SELECT CONCAT(CUSTOMER.LAST_NAME, ',', Customer.first_name) as customer,
address.phone, film.title, rental_date,film.rental_duration, current_date(),
datediff(current_date(), rental_date + Interval film.rental_duration DAY) as daysoverdue
from rental inner join customer on rental.customer_id = customer.customer_id
inner join address on customer.address_id = address.address_id
inner join inventory on rental.inventory_id = inventory.inventory_id
inner join film on inventory.film_id = film.film_id
where rental.return_date IS NULL 
AND rental_date + Interval film.rental_duration DAY < CURRENT_DATE()
ORDER BY TITLE 
LIMIT 5;


/* 5l ) Create a SQL program using GROUP BY to show customers 
who owe more than
$200 with ROLLUP */
SELECT customer_id, SUM(amount) AS total_amt
FROM payment 
GROUP BY customer_id
WITH ROLLUP
HAVING total_amt > 200;


/* 5m)Create a SQL program using PARTITION to show payment amounts by rentals
partitioned over customer. For each rental, include customer first name, last name,
payment amount, and payment date. Show the Total Payment Amount as the
partitioned column.*/
SELECT payment.amount,customer.first_name, customer.last_name, payment.payment_date,
SUM(amount) OVER(PARTITION BY payment.rental_id) as sum_amount
from payment, customer
where payment.customer_id = customer.customer_id;


