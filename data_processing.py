import os
import data
import json

def write_json():
  if not os.path.isfile('goals.json'):
    with open('goals.json', 'w', encoding='utf-8') as f:
      json.dump(data.goals, f, ensure_ascii=False)

  if not os.path.isfile('teachers.json'):
      with open('teachers.json', 'w', encoding='utf-8') as f:      
        json.dump(data.teachers,
                  f,
                  ensure_ascii=False,
                  indent=4,
                  separators=(',', ': '))

      
def get_json_teachers():
  try:
    with open('teachers.json', 'r') as teachers_json:
      teachers = json.load(teachers_json)
    return teachers
  except FileNotFoundError:
    return 'File not found'


def get_json_goals():
  try:
    with open('goals.json', 'r') as goals_json:
      goals = json.load(goals_json)
    return goals
  except FileNotFoundError:
    return 'File not found'