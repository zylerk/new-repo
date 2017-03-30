import cgi
import athletemodel
import yate

import cgitb
cgitb.enable()

athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
ath_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))

print(yate.header("Athlete:" + ath_name + ", DOB:" + athletes[ath_name].dob + "."))

print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes[ath_name].top3))

print(yate.include_footer({"Home": "/index.html", "Select another athlete" : "generate_list.py"}))
