GROUP BY DATE(order_submit_dt_tm);

select o.* from orders o WHERE o.status <> 'OPEN' AND o.order_id NOT IN (select distinct os.order_id from order_status os WHERE os.status_cd = 'Shipped')
AND o.order_submit_dt_tm >= ( DATE_SUB(NOW(), INTERVAL 1 WEEK));

select o.* from orders o WHERE o.status <> 'OPEN' AND o.order_id NOT IN (select distinct os.order_id from order_status os WHERE os.status_cd = 'Shipped')
AND o.order_submit_dt_tm >= ( CURDATE() - INTERVAL 1 MONTH) GROUP BY DATE(order_submit_dt_tm);

select COUNT(order_id) as 'No Of Orders', DATE(order_submit_dt_tm) as Date, DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' from ecomm.orders 
where orders.order_submit_dt_tm >= ( DATE_SUB(NOW(), INTERVAL 30 DAY)) GROUP BY DATE(order_submit_dt_tm);

SELECT COUNT(order_id) as 'No of orders', order_id, DATE(order_submit_dt_tm) as Date, DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' FROM ecomm.orders 
WHERE MONTH(order_submit_dt_tm) = MONTH(CURDATE()) GROUP BY DATE(order_submit_dt_tm); 

select count(order_id) as 'No Of Orders' from ecomm.orders where orders.coupon_applied <> 'NoCoupon';

