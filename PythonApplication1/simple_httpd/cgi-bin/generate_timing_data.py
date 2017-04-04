import cgi
import athletemodel
import yate

import cgitb
cgitb.enable()

#athletes = athletemodel.get_from_store()
athletes = athletemodel.get_namesID_from_store()

form_data = cgi.FieldStorage()
ath_id = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(ath_id)

print(yate.start_response())
print(yate.include_header("NUAC's Timing Data"))

print(yate.header("Athlete:" + athlete['Name'] + ", DOB:" + athlete['DOB'] + "."))

print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athlete['top3']))

print(yate.para("The entire set of timing data is: " + str(athlete['data']) + "(duplicates removed)."))

print(yate.include_footer({"Home": "/index.html", "Select another athlete" : "generate_list.py"}))
