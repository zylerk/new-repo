import json
import athletemodel
import yate
import cgi

import sys


athletes = athletemodel.get_from_store()
form_data = cgi.FieldStorage()
ath_name = form_data['which_athlete'].value

print(yate.start_response('application/json'))
print(json.dumps(athletes[ath_name].as_dict))

#print(json.dumps(athletes[ath_name].as_dict), file = sys.stderr)






