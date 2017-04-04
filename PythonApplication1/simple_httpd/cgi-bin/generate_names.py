
import json
import athletemodel
import yate

import cgitb
cgitb.enable()


#names = athletemodel.get_names_from_store()
names = athletemodel.get_namesID_from_store()

print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))

