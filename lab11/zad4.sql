select boroname, sum(popn_total) as "Population" from nyc_census_blocks
where (boroname = 'The Bronx'
	   or boroname = 'Manhattan'
	   or boroname = 'Queens')
group by boroname