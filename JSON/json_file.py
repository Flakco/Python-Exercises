import json

with open("JSON\states.json") as f:
  state_data= json.load(f)

for state in state_data['states']:
  del state["abbreviation"]

with open('JSON\new_states.json', 'w') as f:
  json.dump(state_data, f, indent=2)