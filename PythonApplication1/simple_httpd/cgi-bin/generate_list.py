
import athletemodel
import yate
import glob

data_files = glob.glob("data/*.txt")
atheletes = athletemodel.put_to_store(data_files)

print(yate.start_response())

print(yate.include_header("Coach kelly's list of Athletes"))
print(yate.start_form("generate_timing_data.py"))

print(yate.para("Select an athlete from the list to work with:"))

for each_ath in atheletes:
    print(yate.radio_button("which_athlete", atheletes[each_ath].name))

print(yate.end_form("Select"))

print(yate.include_footer({"Home": "/index.html"}))
