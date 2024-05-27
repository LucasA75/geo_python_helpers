import requests
import json
import time

# /Login
def login(user, password):
  url = "https://customerapi.geovictoria.com/api/v1/Login"

  payload = json.dumps({
    "User": user,
    "Password": password
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  token = json.loads(str(response.text))

  return token

token_prod = login("", "")
token_test = login("", "")

# /Shift/List
def shift_list(token):
  url = "https://customerapi.geovictoria.com/api/v1/Shift/List"

  payload = {}
  headers = {
    'Authorization': f'Bearer {token["token"]}'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  shifts = json.loads(str(response.text))

  return shifts

# /Punch/AddArtificial
def punch_addartificial(token, user_identifier, punch_date, punch_type):
  url = "https://customerapi.geovictoria.com/api/v1/punch/AddArtificial"

  payload = json.dumps({
    "Date": punch_date,
    "UserIdentifier": user_identifier,
    "Type": punch_type
  })
  headers = {
    'Authorization': f'{token["token"]}',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)

# /Punch/AddMultiple
def punch_addmultiple(token, punch_bsn, punch_date, user_identifier, punch_type):
    url = "https://customerapi.geovictoria.com/api/v1/Punch/AddMultiple"

    payload = json.dumps([
    {
        "ReferenceIdentifier": "",
        "BoxSerialNumber": punch_bsn,
        "Date": punch_date,
        "UserIdentifier": user_identifier,
        "Type": punch_type
    }
    ])
    headers = {
        'Authorization': f'{token["token"]}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)



# turnos = shift_list(token_prod)

# for turno in turnos:
#   # print(turno["Id"])
#   # shift = {
#   #     "StartHour": turno["StartTime"],
#   #     "MaxStartHour": turno["MaxStartTime"],
#   #     "EndHour": turno["ExitTime"],
#   #     "BreakStart": turno["BreakStart"],
#   #     "BreakEnd": turno["BreakEnd"],
#   #     "BreakMinutes": turno["BreakMinutes"],
#   #     "ShiftHours": turno["FixedShiftHours"],
#   #     "Custom": turno["Custom"]
#   # }
#   print(turno)

punches = []

for punch in punches :

    fecha = punch["Date"]
    hora = punch["Hora"]

    hora_dividida = hora.split(":")
    mes, dia, año = fecha.split("-")

    # Reconstruir la fecha en formato año mes día
    fecha_nueva = f"{año}{mes}{dia}"
    
    fecha_invertida = ''.join(fecha_nueva) + ''.join(hora_dividida)
 
    print(fecha_invertida) 
    punch_addartificial(token_test, punch["UserIdentifier"], fecha_invertida, punch["Type"])
    time.sleep(0.3)