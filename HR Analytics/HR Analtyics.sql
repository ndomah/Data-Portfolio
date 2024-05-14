--create a join table
select * from Absenteeism_at_work a
left join compensation b
on a.ID = b.ID
left join Reasons r on
a.Reason_for_absence = r.Number;

--find the healthiest employees for the bonus
select * from Absenteeism_at_work
where Social_drinker = 0 and 
	  Social_smoker = 0 and 
	  Body_mass_index < 25 and 
	  Absenteeism_time_in_hours < (select avg(Absenteeism_time_in_hours) from Absenteeism_at_work);

--compensation rate increase for non-smokers
select count(*) as nonsmokers from Absenteeism_at_work
where Social_smoker = 0;
-- 686 nonsmokers
-- 5 working days x 8 hours per day x 52 weeks in a year = 2080 hours worked x 686 employees = 1,426,880 hours worked total per year by nonsmokers
-- compensation increase for nonsmokers: budget: $986,221 / 1,426,880 hours per year = $0.69 per hour
-- compensation increase for nonsmokers per year: 2080 hours worked per year x $0.69 per hour = $1,414.4 salary bonus

--optimize this query
select
a.ID,
r.Reason,
Month_of_absence,
Body_mass_index,
case when Body_mass_index < 18.5 then 'Underweight'
	 when Body_mass_index between 18.5 and 25 then 'Healthy Weight'
	 when Body_mass_index between 25 and 30 then 'Overweight'
	 when Body_mass_index > 30 then 'Obese'
	 else 'Unknown' end as BMI_category,
case when Month_of_absence in (12,1,2) then 'Winter'
	 when Month_of_absence in (3,4,5) then 'Spring'
	 when Month_of_absence in (6,7,8) then 'Summer'
	 when Month_of_absence in (9,10,11) then 'Fall'
	 else 'Unknown' end as Season_names,
Month_of_absence,
Day_of_the_week,
Transportation_expense,
Education,
Son,
Social_drinker,
Social_smoker,
Pet,
Disciplinary_failure,
Age,
Work_load_Average_day,
Absenteeism_time_in_hours
from Absenteeism_at_work a
left join compensation b
on a.ID = b.ID
left join Reasons r on
a.Reason_for_absence = r.Number;