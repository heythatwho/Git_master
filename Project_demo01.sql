#assumption: 
#assuming each user ID mean one user found the app, each device_ID means one login in a unique device
select count(*) from testing.attribution; #5271 records show in total
Select count(*) from (select distinct device_id from testing.attribution) as a; 
# 3750 different device IDs less than the total records above, assume some device IDs login multiple times

# check if any device_id in attribution not show in device table
select device_id as id from testing.attribution a 
where a.device_id not in (
 select id from testing.device); # 0 rows returned

select count(*) from (select distinct id from testing.user) as user_id; 
#3496 user id issued, assume that 3496 user found that app

select count(*) from (select distinct user_id from testing.user_device) as a; 
#3491 different user_id found in the user_device table (5 users less than user table), assume that 5 users used unknow device to sign up.

select count(*) from (select distinct user_id from testing.sale) as a; 
# 2546 different user_id returned, assume 2546 users make purchase in the app


#create a allrecord table to contain everything
create table testing.allrecords as(
select 
#a.id
#there is no attribution ID, unlike the attachment picture (schema.png) shows, however, it doesnt impact the process
a.created_on
,a.device_id
,a.campaign
,b.created_on as device_date
,b.device_type
,b.operating_system
,c.user_id
,d.name user_name
,d.created_on usr_crtd_dt
,e.created_on sale_crtd_date
,e.amount
,e.date sale_dt
,e.weekday
,f.item_id
from testing.attribution a
left join testing.device b 
	on b.id = a.device_id
left join testing.user_device c
	on b.id = c.device_id
left join testing.user d
	on d.id = c.user_id
left join testing.sale e
	on e.user_id = d.id
left join testing.item f
	on f.sale_id = e.id
);

#check occurrence frequency of each compaign
select campaign, count(campaign) as occurrence_freq
from testing.allrecords
group by 1 order by 2 desc;
#range from the minimum 292 (ZBW0OM) to maximum 1382 (ZDNTT7)


# check how many users brought by each campaign
select campaign, count(user_name) as user_crtd_per_campaign
from testing.allrecords
group by 1 order by 2 desc; #range from ZDNTT7 (1362 users) to ZBW0OM (281 users)

#check # of the sales issued by each campaign
select campaign, count(amount) as sales_per_campaign
from testing.allrecords
group by 1 order by 2 desc;# rang from ZDNTT7 (1358) to ZBW0OM (265)

#check the efficiencies for each campaign
#created_on to timestamps, use the usr_crtd_date (user created date) instead(for later use).    
alter table testing.allrecords
	change usr_crtd_dt usr_crtd_dt  timestamp ;
#and the sale_crtd_date too;
alter table testing.allrecords
	change sale_crtd_date sale_crtd_date  timestamp ;
#Due to data format issue, unable to change attribution.created_on to timestamp (error 1292 incorrect date value), this step would be completed in Excel
#calculate the difference between the user signup and campaign created_on, the result comes up with some negative value which mean some users signup in the past, ignore these registered users and filter the results to positive value. I only take the rows with users found app after the campaigns created
#import the table allrecords_time_diff from excel, count the user name and then group by campaign
select 
campaign, 
count(user_name) 
from testing.allrecords_time_diff
group by 1 order by 2;





    


