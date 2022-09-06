
--count all users
select count(id) as "Users Count" from auth_user;
--count all users joined today
select count(id) as "Users Count" from auth_user u where date_joined >= current_date;
--count all users joined this month
select count(id) as "Users count" from auth_user u where date_part('month', u.date_joined)=  date_part('month', (SELECT current_timestamp));
--count all users joined this year
select count(id) as "Users count" from auth_user u where date_part('year', u.date_joined)=  date_part('year', (SELECT current_timestamp));






--count all accounts
 select count(id) as "Accounts Count" from internshipcash_account;
--count all accounts created today
select count(id) as "Accounts Count" from internshipcash_account a where a.created_at>= current_date;
--count all accounts created this month
 select count(id) as "Accounts count" from internshipcash_account a where date_part('month', a.created_at)=  date_part('month', (SELECT current_timestamp));
--count all accounts created this year
 select count(id) as "Accounts count" from internshipcash_account a where date_part('year', a.created_at)=  date_part('year', (SELECT current_timestamp));










--count all transactions
select count(id) as "Transactions count" from internshipcash_transaction
--count all transactions happednd today
select count(id) as "Transactions count" from internshipcash_transaction t where t.transaction_time = current_date;
--count all transactions happednd this month
select count(id) as "Transactions count" from internshipcash_transaction t where date_part('month', t.transaction_time)=  date_part('month', (SELECT current_timestamp));
--count all transactions happednd this year
 select count(id) as "Transactions count" from internshipcash_transaction t where date_part('year', t.transaction_time)=  date_part('year', (SELECT current_timestamp));






--count all gain
 select sum(fee) as "Gain" from internshipcash_transaction;
--count all gain for today
 select sum(fee) as "Gain" from internshipcash_transaction t where t.transaction_time >= current_date;
--count all gain for this month
select sum(fee) as "Gain" from internshipcash_transaction t where date_part('month', t.transaction_time)=  date_part('month', (SELECT current_timestamp));
--count all gain for this year
select sum(fee) as "Gain" from internshipcash_transaction t where date_part('year', t.transaction_time)=  date_part('year', (SELECT current_timestamp));





--join user & account (to get the users data and their related accounts)
select username,first_name, last_name,email ,account_number, balance, created_at "Account date created" from auth_user cross join internshipcash_account;




--join account& transaction (to get transactions with receiver and sender accounts information)
 select type "Transaction type", amount, fee,transaction_time , balance "Sender Balance", account_number "Sender Account number", "receiverAccNumber" "Reciever Account number"  from internshipcash_transaction cross join internshipcash_account;