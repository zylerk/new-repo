import json
import athletemodel
import yate
import cgi

import sys


#athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage()
ath_id = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(ath_id)

print(yate.start_response('application/json'))
#print(json.dumps(athletes[ath_name].as_dict))
print(json.dumps(athlete))

#print(json.dumps(athletes[ath_name].as_dict), file = sys.stderr)






