
import athletemodel
import yate
#import glob

#data_files = glob.glob("data/*.txt")
#atheletes = athletemodel.put_to_store(data_files)
athletes = athletemodel.get_namesID_from_store()


print(yate.start_response())

print(yate.include_header("NUAC's list of Athletes"))
print(yate.start_form("generate_timing_data.py"))

print(yate.para("Select an athlete from the list to work with:"))

for each_ath in athletes:
    print(yate.radio_button_id("which_athlete", each_ath[0], each_ath[1]))

print(yate.end_form("Select"))

print(yate.include_footer({"Home": "/index.html"}))
