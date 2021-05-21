import random
from data_processing import write_json, get_json_teachers, get_json_goals
from flask import Flask, render_template, redirect


app = Flask(__name__)

write_json()
teachers = get_json_teachers()
goals = get_json_goals()


WEEK = {"mon": "Понедельник",
        "tue": "Вторник",
        "wed": "Среда",
        "thu": "Четверг",
        "fri": "Пятница",
        "sat": "Суббота",
        "sun": "Воскресенье"
      }


@app.route('/')
def render_main():
  return render_template('index.html')


@app.route('/all')
def render_all():
  return render_template('all.html')


@app.route('/goals/<string:goal>')
def render_goal(goal):
  return render_template('goal.html')


@app.route('/profiles/<int:id>')
def render_profiles(id):
  try:
    teacher_profile = teachers[id]
  except (IndexError, TypeError):
    redirect('render_main', code=302)

  teach_goals  = {}
  for goal_eng in teacher_profile.get('goals'):
    for name_goal_eng, name_goal_ru in goals.items():
        if goal_eng in name_goal_eng:            
            teach_goals[goal_eng] = name_goal_ru
  
  # teach_goals = {goal_eng: name_goal_ru for goal_eng in teacher_profile.get('goals') for name_goal_eng, name_goal_ru in goals.items() if goal_eng in name_goal_eng}
  # goals_ru = [name_goal_ru for goal_eng in teacher_profile.get('goals') for name_goal_eng, name_goal_ru in goals.items() if goal_eng in name_goal_eng]

  timetable = {}
  for week_eng, shaldues in teacher_profile['free'].items():
      plans = []      
      for time, busy in shaldues.items():
          if busy:
              plans.append(time)
      timetable[WEEK[week_eng]] = plans

  print(timetable)
  
  return render_template('profile.html', teacher_profile=teacher_profile, teach_goals=teach_goals, timetable=timetable)


@app.route('/request')
def render_request():
  return render_template('request.html')


@app.route('/request_done')
def render_request_done():
  return render_template('request_done.html')


@app.route('/booking/<int:id>/<string:week>/<int:time>')
def render_booking(id, week, time):
  return render_template('booking.html')


@app.route('/booking_done')
def render_booking_done():
  return render_template('booking_done.html')


if __name__ == "__main__": 
  app.run(host='0.0.0.0', port=random.randint(2000, 9000), debug=True)

