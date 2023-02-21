select count(*) from nyc_streets
where (name like 'B%' 
	   or name like 'Q%'
	   or name like 'M%')