
import json
import athletemodel
import yate

import cgitb
cgitb.enable()




print(yate.start_response('application/json'))

names = athletemodel.get_names_from_store()
print(json.dumps(sorted(names)))

