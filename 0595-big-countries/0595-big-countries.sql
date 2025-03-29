# Write your MySQL query statement below

select name,population,area as 'area' from World w where w.area>=3000000 or w.population>=25000000 #order by name