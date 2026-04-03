create table data_quality_check(
	check_id serial primary key,
	table_name text, 
	check_type text,
	check_result text, 
	check_time timestamp 
);

create table data_pipeline_runs(
	run_id serial primary key,
	run_time timestamp,
	status text,
	records_processed int, 
	errors_detected int
);
	

select * from data_quality_check 

select * from data_pipeline_runs 

