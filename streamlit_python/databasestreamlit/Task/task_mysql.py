import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "swapna2021",
    database = "ecomm"
)

getOrderStatusDf = "SELECT * FROM ecomm.order_status"

filterOrderStatusDf = "SElECT order_id, status_cd, estimated_time FROM ecomm.order_status"

ordersCount = "SELECT COUNT(order_id) as 'No Of Orders', DATE(order_submit_dt_tm) as 'Date', DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' FROM ecomm.orders GROUP BY DATE(order_submit_dt_tm)" 

currentMonthOrders = "SELECT COUNT(order_id) as 'No Of Orders', order_id, coupon_applied, DATE(order_submit_dt_tm) as 'Date', DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' FROM ecomm.orders WHERE MONTH(order_submit_dt_tm) = MONTH(CURDATE()) GROUP BY DATE(order_submit_dt_tm)"

unShippedordersWeekCount = "select order_id, COUNT(order_id) as 'No Of Orders', DATE(order_submit_dt_tm) as Date, DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' from orders o WHERE o.status <> 'OPEN' AND o.order_id NOT IN (select distinct os.order_id from order_status os WHERE os.status_cd = 'Shipped') AND o.order_submit_dt_tm >= ( DATE_SUB(NOW(), INTERVAL 1 WEEK)) GROUP BY DATE(order_submit_dt_tm)"

unShippedordersByDaysCount = "select DATE(order_submit_dt_tm) as 'Date', order_id, COUNT(order_id) as 'No Of Orders' from orders o WHERE o.status <> 'OPEN' AND o.order_id NOT IN (select distinct os.order_id from order_status os WHERE os.status_cd = 'Shipped') AND o.order_submit_dt_tm >= ( CURDATE() - INTERVAL 11 DAY ) GROUP BY order_id"

ordersLastMonthCountDf = "select order_id, COUNT(order_id) as 'No Of Orders', DATE(order_submit_dt_tm) as 'Date', DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' from ecomm.orders where orders.order_submit_dt_tm >= ( CURDATE() - INTERVAL 1 MONTH) GROUP BY DATE(order_submit_dt_tm)"

ordersLastdaysCount = "select order_id, COUNT(order_id) as 'No Of Orders', DATE(order_submit_dt_tm) as 'Date', DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' from ecomm.orders where orders.order_submit_dt_tm >= ( DATE_SUB(NOW(), INTERVAL 10 DAY)) GROUP BY DATE(order_submit_dt_tm)"

ordersCountByCoupon = "select count(order_id) as 'No Of Orders', coupon_applied from ecomm.orders where orders.coupon_applied <> '0' GROUP BY coupon_applied"

unShippedordersMonthCount = "select order_id, COUNT(order_id) as 'No Of Orders', DATE(order_submit_dt_tm) as Date, DAY (order_submit_dt_tm) as 'Day', DAYNAME(order_submit_dt_tm) as 'Day Name', MONTHNAME(order_submit_dt_tm) as 'Month Name', YEAR(order_submit_dt_tm) as 'Year' from orders o WHERE o.status <> 'OPEN' AND o.order_id NOT IN (select distinct os.order_id from order_status os WHERE os.status_cd = 'Shipped') AND o.order_submit_dt_tm >= ( DATE_SUB(NOW(), INTERVAL 1 MONTH)) GROUP BY DATE(order_submit_dt_tm)"