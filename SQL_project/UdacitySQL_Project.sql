/**question set 1 */
/*question#1 */
select
f.title as film_tile,
c.name as category_name,
count(r.rental_id) as count_rental
from film f
inner join film_category fc
on f.film_id=fc.film_id
inner join category c
on fc.category_id=c.category_id
inner join inventory i
on f.film_id=i.film_id
inner join rental r
on i.inventory_id=r.inventory_id
group by 1,2
having c.name in ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
order by 1,2;

/*question#2 */
select distinct *
from (select
f.title as movie_tile,
c.name as category_name,
f.rental_duration,
ntile(4)over(partition by f.rental_duration order by f.title, c.name, f.rental_duration) as standard_quartile
from film f
inner join film_category fc
on fc.film_id=f.film_id
inner join category c
on c.category_id=fc.category_id) sub;

/*question#3 */
with tab1 as (
select
f.title as film_name,
c.name as category_name,
f.rental_duration,
ntile(4)over(partition by c.name,f.rental_duration order by c.name, f.rental_duration) as standard_quartile
from  category c
inner join film_category fc
on c.category_id=fc.category_id
inner join film f
on f.film_id=fc.film_id)
select 
category_name,
standard_quartile,
count(film_name) as count
from tab1
group by 1, 2
order by 1, 2;

/**question set 2**/
/*question #1 **/
select
date_part('month',r.rental_date) as rental_month,
date_part('year',r.rental_date) as rental_year,
s.store_id as store_id,
count(rental_id) as count_rentals
from store s
inner join staff f
on s.store_id=f.store_id
inner join rental r
on f.staff_id = r.staff_id
group by 1,2,3
order by 4 desc;

/*question#2 */
select 
pay_mon,
fullname,
pay_countpermon,
total_amount as pay_amount
from (
select
date_trunc('month',p.payment_date) as pay_mon,
concat(c.first_name,' ',c.last_name) as fullname,
count(payment_id) as pay_countpermon,
sum(p.amount) as total_amount,
rank()over(partition by date_trunc('month',p.payment_date) order by sum(p.amount) desc) as rank
from payment p
inner join customer c
on p.customer_id = c.customer_id
group by 1,2) t1
where rank <=10
order by 1, 4

/*question#3 */
with prevous_table as(
select fullname from 
(select 
pay_mon,
fullname,
pay_countpermon,
total_amount as pay_amount
from (
select
date_trunc('month',p.payment_date) as pay_mon,
concat(c.first_name,' ',c.last_name) as fullname,
count(payment_id) as pay_countpermon,
sum(p.amount) as total_amount,
rank()over(partition by date_trunc('month',p.payment_date) order by sum(p.amount) desc) as rank
from payment p
inner join customer c
on p.customer_id = c.customer_id
group by 1,2) sub1
where rank <=10
order by 1, 4) sub2
)
select 
concat(c.first_name,' ',c.last_name) as fullname,
date_trunc('month', payment_date) as pay_month,
sum(amount) as pay_amount,
lead(sum(amount))over(partition by date_trunc('month',p.payment_date) order by date_trunc('month',p.payment_date) ) as lead,
lead(sum(amount))over(partition by date_trunc('month',p.payment_date) order by date_trunc('month',p.payment_date) ) - sum(amount) as difference
from payment p
inner join customer c
on p.customer_id = c.customer_id 
where date_part('year', payment_date) = '2007'
and concat(c.first_name,' ',c.last_name) in (select * from prevous_table)
group by 1,2
order by 2, 1;


