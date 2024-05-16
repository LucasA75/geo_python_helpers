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

"""
CIAL Producción
  "User": bd02cb
  "Password": b69fcaf5

CIAL Test
  "User": f0e1c0
  "Password": 1c1fc4e5
  
CEVA Test
"User":"10d36a"
"Pass":"3ddd2e85"
  
"""
token_prod = login("bd02cb", "b69fcaf5")
token_test = login("10d36a", "3ddd2e85")

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

punchesCeva = [
 {
  "UserIdentifier": 129666455,
  "Date": "03-22-2024",
  "Hora": "01:11:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "03-22-2024",
  "Hora": "12:49:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "03-22-2024",
  "Hora": "21:39:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "03-25-2024",
  "Hora": "12:52:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "03-25-2024",
  "Hora": "22:15:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "03-26-2024",
  "Hora": "12:50:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "03-26-2024",
  "Hora": "22:12:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "03-27-2024",
  "Hora": "12:51:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "03-27-2024",
  "Hora": "22:10:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "03-28-2024",
  "Hora": "12:50:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "03-28-2024",
  "Hora": "21:52:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-01-2024",
  "Hora": "15:36:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-02-2024",
  "Hora": "01:31:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-02-2024",
  "Hora": "15:56:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-03-2024",
  "Hora": "01:27:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-03-2024",
  "Hora": "15:39:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-04-2024",
  "Hora": "01:13:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-04-2024",
  "Hora": "15:41:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-05-2024",
  "Hora": "01:15:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-08-2024",
  "Hora": "12:51:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-08-2024",
  "Hora": "22:12:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-09-2024",
  "Hora": "12:50:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-09-2024",
  "Hora": "22:02:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-10-2024",
  "Hora": "12:51:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-10-2024",
  "Hora": "22:14:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-11-2024",
  "Hora": "12:47:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-11-2024",
  "Hora": "22:09:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-13-2024",
  "Hora": "21:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129666455,
  "Date": "04-15-2024",
  "Hora": "15:37:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-16-2024",
  "Hora": "00:12:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-18-2024",
  "Hora": "15:58:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-19-2024",
  "Hora": "01:11:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-19-2024",
  "Hora": "15:55:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-20-2024",
  "Hora": "01:02:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-20-2024",
  "Hora": "16:08:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-21-2024",
  "Hora": "01:11:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-21-2024",
  "Hora": "15:56:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-22-2024",
  "Hora": "01:11:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-22-2024",
  "Hora": "16:06:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-23-2024",
  "Hora": "00:13:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-25-2024",
  "Hora": "15:46:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-26-2024",
  "Hora": "01:23:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-26-2024",
  "Hora": "15:54:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-27-2024",
  "Hora": "01:00:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-27-2024",
  "Hora": "15:47:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-28-2024",
  "Hora": "01:05:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-28-2024",
  "Hora": "15:28:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "03-28-2024",
  "Hora": "23:52:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-01-2024",
  "Hora": "15:59:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-02-2024",
  "Hora": "01:36:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-02-2024",
  "Hora": "15:28:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-03-2024",
  "Hora": "01:35:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-03-2024",
  "Hora": "15:58:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-04-2024",
  "Hora": "01:11:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-04-2024",
  "Hora": "15:56:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-05-2024",
  "Hora": "01:13:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-05-2024",
  "Hora": "16:11:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-05-2024",
  "Hora": "23:53:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-08-2024",
  "Hora": "15:31:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-09-2024",
  "Hora": "01:15:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-09-2024",
  "Hora": "15:31:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-10-2024",
  "Hora": "01:01:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-10-2024",
  "Hora": "15:25:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-11-2024",
  "Hora": "01:08:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-11-2024",
  "Hora": "15:33:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-12-2024",
  "Hora": "01:00:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-12-2024",
  "Hora": "15:30:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-13-2024",
  "Hora": "00:05:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211949538,
  "Date": "04-15-2024",
  "Hora": "15:35:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-16-2024",
  "Hora": "04:17:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-16-2024",
  "Hora": "12:02:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-18-2024",
  "Hora": "01:48:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-18-2024",
  "Hora": "10:14:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-19-2024",
  "Hora": "02:00:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-19-2024",
  "Hora": "10:24:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-20-2024",
  "Hora": "01:55:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-20-2024",
  "Hora": "10:21:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-21-2024",
  "Hora": "01:56:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-21-2024",
  "Hora": "10:23:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-22-2024",
  "Hora": "01:42:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-22-2024",
  "Hora": "10:19:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-23-2024",
  "Hora": "01:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-23-2024",
  "Hora": "10:14:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-25-2024",
  "Hora": "04:06:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-25-2024",
  "Hora": "11:36:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-26-2024",
  "Hora": "03:31:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-26-2024",
  "Hora": "12:06:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-27-2024",
  "Hora": "03:56:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-27-2024",
  "Hora": "12:02:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-28-2024",
  "Hora": "04:06:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "03-28-2024",
  "Hora": "12:12:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-01-2024",
  "Hora": "04:00:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-01-2024",
  "Hora": "12:12:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-02-2024",
  "Hora": "05:04:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-02-2024",
  "Hora": "12:19:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-03-2024",
  "Hora": "04:03:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-03-2024",
  "Hora": "14:18:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-04-2024",
  "Hora": "03:58:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-04-2024",
  "Hora": "12:09:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-05-2024",
  "Hora": "04:01:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-05-2024",
  "Hora": "12:07:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-06-2024",
  "Hora": "04:05:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-06-2024",
  "Hora": "12:03:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-08-2024",
  "Hora": "04:05:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-08-2024",
  "Hora": "09:04:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-09-2024",
  "Hora": "04:08:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-09-2024",
  "Hora": "12:09:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-10-2024",
  "Hora": "03:45:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-10-2024",
  "Hora": "11:46:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-11-2024",
  "Hora": "03:38:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-11-2024",
  "Hora": "11:49:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-12-2024",
  "Hora": "03:49:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-12-2024",
  "Hora": "11:44:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-13-2024",
  "Hora": "03:49:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-13-2024",
  "Hora": "11:48:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-15-2024",
  "Hora": "02:06:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-15-2024",
  "Hora": "10:13:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 186625404,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "03-16-2024",
  "Hora": "03:39:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "03-25-2024",
  "Hora": "18:08:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "03-26-2024",
  "Hora": "03:26:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "03-26-2024",
  "Hora": "18:17:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "03-27-2024",
  "Hora": "03:54:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "03-27-2024",
  "Hora": "18:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "03-28-2024",
  "Hora": "04:02:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "03-28-2024",
  "Hora": "18:02:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "03-29-2024",
  "Hora": "00:01:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-01-2024",
  "Hora": "18:04:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-02-2024",
  "Hora": "04:03:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-02-2024",
  "Hora": "18:36:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-03-2024",
  "Hora": "04:02:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-03-2024",
  "Hora": "18:20:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-04-2024",
  "Hora": "03:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-04-2024",
  "Hora": "18:10:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-05-2024",
  "Hora": "03:28:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-05-2024",
  "Hora": "18:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-06-2024",
  "Hora": "03:26:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-08-2024",
  "Hora": "18:19:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-09-2024",
  "Hora": "03:36:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-09-2024",
  "Hora": "18:16:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-10-2024",
  "Hora": "03:46:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-10-2024",
  "Hora": "18:10:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-11-2024",
  "Hora": "03:41:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-12-2024",
  "Hora": "18:54:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-13-2024",
  "Hora": "03:08:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198853690,
  "Date": "04-15-2024",
  "Hora": "17:47:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 264968518,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-16-2024",
  "Hora": "05:07:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-16-2024",
  "Hora": "13:07:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-18-2024",
  "Hora": "06:04:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-18-2024",
  "Hora": "13:29:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-19-2024",
  "Hora": "05:05:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-19-2024",
  "Hora": "13:01:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-20-2024",
  "Hora": "05:12:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-20-2024",
  "Hora": "12:57:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-21-2024",
  "Hora": "05:03:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-21-2024",
  "Hora": "13:05:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-22-2024",
  "Hora": "05:15:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-22-2024",
  "Hora": "13:07:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-23-2024",
  "Hora": "05:09:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-23-2024",
  "Hora": "05:09:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-23-2024",
  "Hora": "05:09:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-23-2024",
  "Hora": "05:09:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-23-2024",
  "Hora": "05:09:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-23-2024",
  "Hora": "05:09:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-23-2024",
  "Hora": "05:09:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-23-2024",
  "Hora": "05:09:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-23-2024",
  "Hora": "05:09:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-23-2024",
  "Hora": "05:09:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-23-2024",
  "Hora": "13:01:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-25-2024",
  "Hora": "06:08:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-25-2024",
  "Hora": "14:00:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-26-2024",
  "Hora": "05:09:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-26-2024",
  "Hora": "13:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-27-2024",
  "Hora": "05:11:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "03-27-2024",
  "Hora": "13:00:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-01-2024",
  "Hora": "06:14:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-01-2024",
  "Hora": "14:05:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-02-2024",
  "Hora": "05:03:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-02-2024",
  "Hora": "13:05:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-03-2024",
  "Hora": "05:05:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-03-2024",
  "Hora": "13:04:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-04-2024",
  "Hora": "05:12:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-04-2024",
  "Hora": "13:03:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-05-2024",
  "Hora": "05:13:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-05-2024",
  "Hora": "13:07:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-06-2024",
  "Hora": "05:13:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-06-2024",
  "Hora": "12:57:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-08-2024",
  "Hora": "06:03:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-08-2024",
  "Hora": "14:01:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-09-2024",
  "Hora": "05:07:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-09-2024",
  "Hora": "13:04:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-10-2024",
  "Hora": "05:10:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-10-2024",
  "Hora": "13:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-11-2024",
  "Hora": "05:08:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-11-2024",
  "Hora": "13:02:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-12-2024",
  "Hora": "05:04:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-12-2024",
  "Hora": "12:59:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-13-2024",
  "Hora": "05:12:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-13-2024",
  "Hora": "13:00:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-15-2024",
  "Hora": "06:04:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 164772160,
  "Date": "04-15-2024",
  "Hora": "13:59:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-16-2024",
  "Hora": "04:49:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-16-2024",
  "Hora": "14:00:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-18-2024",
  "Hora": "04:43:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-18-2024",
  "Hora": "14:31:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-19-2024",
  "Hora": "04:52:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-19-2024",
  "Hora": "14:30:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-20-2024",
  "Hora": "04:49:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-20-2024",
  "Hora": "14:31:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-21-2024",
  "Hora": "04:48:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-21-2024",
  "Hora": "14:31:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-22-2024",
  "Hora": "04:47:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-22-2024",
  "Hora": "14:30:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-27-2024",
  "Hora": "04:48:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-27-2024",
  "Hora": "14:32:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-28-2024",
  "Hora": "04:46:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "03-28-2024",
  "Hora": "14:31:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-01-2024",
  "Hora": "04:49:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-01-2024",
  "Hora": "14:31:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-03-2024",
  "Hora": "04:51:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-03-2024",
  "Hora": "14:31:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-04-2024",
  "Hora": "04:51:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-04-2024",
  "Hora": "14:31:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-05-2024",
  "Hora": "04:48:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-05-2024",
  "Hora": "14:30:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-06-2024",
  "Hora": "04:47:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-06-2024",
  "Hora": "14:30:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-09-2024",
  "Hora": "04:50:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-09-2024",
  "Hora": "14:30:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-10-2024",
  "Hora": "04:47:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-10-2024",
  "Hora": "14:30:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-11-2024",
  "Hora": "04:48:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-11-2024",
  "Hora": "14:31:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-12-2024",
  "Hora": "05:29:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-12-2024",
  "Hora": "14:30:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-15-2024",
  "Hora": "04:41:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 156503053,
  "Date": "04-15-2024",
  "Hora": "14:31:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 169366926,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-16-2024",
  "Hora": "03:42:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-16-2024",
  "Hora": "10:56:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-18-2024",
  "Hora": "04:00:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-18-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-19-2024",
  "Hora": "03:50:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-19-2024",
  "Hora": "12:14:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-20-2024",
  "Hora": "03:51:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-20-2024",
  "Hora": "12:03:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-21-2024",
  "Hora": "03:46:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-21-2024",
  "Hora": "12:05:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-22-2024",
  "Hora": "03:43:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-22-2024",
  "Hora": "12:11:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-23-2024",
  "Hora": "03:43:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-23-2024",
  "Hora": "12:02:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-25-2024",
  "Hora": "02:33:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-25-2024",
  "Hora": "11:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-25-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-26-2024",
  "Hora": "02:58:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-26-2024",
  "Hora": "11:00:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-27-2024",
  "Hora": "03:07:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-27-2024",
  "Hora": "11:00:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-28-2024",
  "Hora": "02:50:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "03-28-2024",
  "Hora": "11:05:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-01-2024",
  "Hora": "04:02:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-01-2024",
  "Hora": "13:06:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-02-2024",
  "Hora": "04:05:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-02-2024",
  "Hora": "12:10:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-03-2024",
  "Hora": "03:45:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-03-2024",
  "Hora": "12:13:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-04-2024",
  "Hora": "03:38:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-04-2024",
  "Hora": "12:04:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-05-2024",
  "Hora": "03:37:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-05-2024",
  "Hora": "08:57:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-06-2024",
  "Hora": "03:35:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-06-2024",
  "Hora": "11:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-08-2024",
  "Hora": "03:38:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-08-2024",
  "Hora": "12:02:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-09-2024",
  "Hora": "03:30:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-09-2024",
  "Hora": "12:00:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-10-2024",
  "Hora": "03:31:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-10-2024",
  "Hora": "12:00:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-11-2024",
  "Hora": "03:27:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-11-2024",
  "Hora": "11:56:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-12-2024",
  "Hora": "03:34:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-12-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-13-2024",
  "Hora": "03:24:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-13-2024",
  "Hora": "11:01:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-15-2024",
  "Hora": "04:31:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 155061995,
  "Date": "04-15-2024",
  "Hora": "12:02:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-16-2024",
  "Hora": "05:43:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-16-2024",
  "Hora": "13:45:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-18-2024",
  "Hora": "05:43:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-18-2024",
  "Hora": "14:00:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-19-2024",
  "Hora": "05:43:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-19-2024",
  "Hora": "13:47:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-20-2024",
  "Hora": "05:49:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-20-2024",
  "Hora": "13:46:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-21-2024",
  "Hora": "05:39:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-21-2024",
  "Hora": "13:46:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-22-2024",
  "Hora": "05:41:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-22-2024",
  "Hora": "13:46:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-23-2024",
  "Hora": "05:42:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-23-2024",
  "Hora": "13:46:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-25-2024",
  "Hora": "05:50:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-25-2024",
  "Hora": "14:02:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-26-2024",
  "Hora": "05:44:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-26-2024",
  "Hora": "13:50:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-27-2024",
  "Hora": "05:43:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-27-2024",
  "Hora": "13:45:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-28-2024",
  "Hora": "05:39:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "03-28-2024",
  "Hora": "13:45:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-01-2024",
  "Hora": "05:59:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-01-2024",
  "Hora": "14:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-02-2024",
  "Hora": "05:41:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-02-2024",
  "Hora": "13:46:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-03-2024",
  "Hora": "05:40:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-03-2024",
  "Hora": "13:49:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-04-2024",
  "Hora": "05:44:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-04-2024",
  "Hora": "13:45:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-05-2024",
  "Hora": "05:42:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-05-2024",
  "Hora": "13:46:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-06-2024",
  "Hora": "05:40:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-06-2024",
  "Hora": "13:45:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-08-2024",
  "Hora": "05:56:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-08-2024",
  "Hora": "14:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-09-2024",
  "Hora": "05:46:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-09-2024",
  "Hora": "13:45:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-10-2024",
  "Hora": "05:44:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-10-2024",
  "Hora": "13:46:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-11-2024",
  "Hora": "05:40:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-11-2024",
  "Hora": "13:45:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-12-2024",
  "Hora": "05:44:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-12-2024",
  "Hora": "13:45:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-13-2024",
  "Hora": "05:42:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-13-2024",
  "Hora": "13:55:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-15-2024",
  "Hora": "05:52:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178116037,
  "Date": "04-15-2024",
  "Hora": "14:00:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-16-2024",
  "Hora": "02:28:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-16-2024",
  "Hora": "09:13:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-18-2024",
  "Hora": "04:50:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-18-2024",
  "Hora": "11:01:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-19-2024",
  "Hora": "02:54:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-19-2024",
  "Hora": "11:04:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-20-2024",
  "Hora": "02:39:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-20-2024",
  "Hora": "11:05:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-21-2024",
  "Hora": "02:20:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-21-2024",
  "Hora": "11:13:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-22-2024",
  "Hora": "02:30:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-22-2024",
  "Hora": "11:04:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-23-2024",
  "Hora": "02:21:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-23-2024",
  "Hora": "12:09:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-25-2024",
  "Hora": "02:07:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-25-2024",
  "Hora": "12:06:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-26-2024",
  "Hora": "02:29:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-26-2024",
  "Hora": "12:11:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-27-2024",
  "Hora": "03:19:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-27-2024",
  "Hora": "12:12:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-28-2024",
  "Hora": "02:55:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "03-28-2024",
  "Hora": "11:10:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-01-2024",
  "Hora": "02:46:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-01-2024",
  "Hora": "11:05:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-02-2024",
  "Hora": "02:55:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-02-2024",
  "Hora": "11:06:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-03-2024",
  "Hora": "03:48:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-03-2024",
  "Hora": "11:08:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-04-2024",
  "Hora": "02:42:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-04-2024",
  "Hora": "11:58:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-05-2024",
  "Hora": "02:34:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-05-2024",
  "Hora": "11:00:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-06-2024",
  "Hora": "02:54:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-06-2024",
  "Hora": "11:00:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-08-2024",
  "Hora": "03:19:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-08-2024",
  "Hora": "12:10:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-09-2024",
  "Hora": "03:33:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-09-2024",
  "Hora": "12:05:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-10-2024",
  "Hora": "03:52:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-10-2024",
  "Hora": "12:02:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-11-2024",
  "Hora": "03:23:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-11-2024",
  "Hora": "12:02:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-12-2024",
  "Hora": "03:25:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-12-2024",
  "Hora": "12:15:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-13-2024",
  "Hora": "03:23:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-13-2024",
  "Hora": "10:58:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-15-2024",
  "Hora": "02:34:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215327590,
  "Date": "04-15-2024",
  "Hora": "11:02:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-18-2024",
  "Hora": "08:00:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-18-2024",
  "Hora": "17:30:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-19-2024",
  "Hora": "08:00:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-19-2024",
  "Hora": "17:30:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-20-2024",
  "Hora": "08:00:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-20-2024",
  "Hora": "17:30:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-21-2024",
  "Hora": "08:00:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-21-2024",
  "Hora": "17:31:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-22-2024",
  "Hora": "08:00:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-22-2024",
  "Hora": "17:32:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-25-2024",
  "Hora": "08:00:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-25-2024",
  "Hora": "17:30:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-26-2024",
  "Hora": "08:00:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-26-2024",
  "Hora": "17:31:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-27-2024",
  "Hora": "08:00:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-27-2024",
  "Hora": "17:35:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-28-2024",
  "Hora": "08:00:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-28-2024",
  "Hora": "17:35:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-29-2024",
  "Hora": "08:00:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-29-2024",
  "Hora": "18:20:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-30-2024",
  "Hora": "08:00:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-30-2024",
  "Hora": "18:02:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-31-2024",
  "Hora": "08:00:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "03-31-2024",
  "Hora": "18:45:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-01-2024",
  "Hora": "08:00:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-01-2024",
  "Hora": "17:30:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-02-2024",
  "Hora": "08:00:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-02-2024",
  "Hora": "17:30:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-04-2024",
  "Hora": "08:00:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-04-2024",
  "Hora": "17:31:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-05-2024",
  "Hora": "08:00:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-05-2024",
  "Hora": "17:30:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-05-2024",
  "Hora": "17:30:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-08-2024",
  "Hora": "08:00:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-08-2024",
  "Hora": "17:30:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-09-2024",
  "Hora": "08:00:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-09-2024",
  "Hora": "17:30:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-10-2024",
  "Hora": "08:00:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-10-2024",
  "Hora": "17:31:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-11-2024",
  "Hora": "08:00:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-11-2024",
  "Hora": "17:30:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-12-2024",
  "Hora": "08:00:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-12-2024",
  "Hora": "17:30:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-15-2024",
  "Hora": "08:00:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270570291,
  "Date": "04-15-2024",
  "Hora": "17:31:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-16-2024",
  "Hora": "07:55:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-16-2024",
  "Hora": "14:00:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-18-2024",
  "Hora": "08:01:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-18-2024",
  "Hora": "15:50:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-19-2024",
  "Hora": "11:30:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-19-2024",
  "Hora": "18:01:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-20-2024",
  "Hora": "08:06:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-20-2024",
  "Hora": "20:01:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-21-2024",
  "Hora": "08:00:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-21-2024",
  "Hora": "20:01:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-22-2024",
  "Hora": "07:59:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-22-2024",
  "Hora": "17:02:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-23-2024",
  "Hora": "07:58:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-23-2024",
  "Hora": "07:58:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-23-2024",
  "Hora": "07:58:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-23-2024",
  "Hora": "07:58:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-23-2024",
  "Hora": "07:58:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-23-2024",
  "Hora": "07:58:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-23-2024",
  "Hora": "07:58:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-23-2024",
  "Hora": "07:58:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-23-2024",
  "Hora": "07:58:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-23-2024",
  "Hora": "07:58:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-23-2024",
  "Hora": "14:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-26-2024",
  "Hora": "08:01:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-26-2024",
  "Hora": "20:03:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-27-2024",
  "Hora": "08:01:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-27-2024",
  "Hora": "18:00:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-28-2024",
  "Hora": "08:03:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "03-28-2024",
  "Hora": "23:28:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-01-2024",
  "Hora": "08:10:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-01-2024",
  "Hora": "18:00:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-02-2024",
  "Hora": "08:03:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-02-2024",
  "Hora": "18:03:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-03-2024",
  "Hora": "07:55:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-03-2024",
  "Hora": "18:01:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-04-2024",
  "Hora": "08:00:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-04-2024",
  "Hora": "18:02:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-05-2024",
  "Hora": "07:57:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-05-2024",
  "Hora": "17:00:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-06-2024",
  "Hora": "07:52:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-06-2024",
  "Hora": "14:01:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-08-2024",
  "Hora": "08:22:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-08-2024",
  "Hora": "18:01:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-09-2024",
  "Hora": "08:04:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-09-2024",
  "Hora": "18:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-10-2024",
  "Hora": "07:57:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-10-2024",
  "Hora": "17:54:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-11-2024",
  "Hora": "07:58:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-11-2024",
  "Hora": "22:00:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-12-2024",
  "Hora": "07:55:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-12-2024",
  "Hora": "17:00:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-15-2024",
  "Hora": "08:02:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182436461,
  "Date": "04-15-2024",
  "Hora": "18:01:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-16-2024",
  "Hora": "05:24:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-16-2024",
  "Hora": "11:47:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-18-2024",
  "Hora": "05:55:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-18-2024",
  "Hora": "13:03:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-19-2024",
  "Hora": "05:21:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-19-2024",
  "Hora": "13:33:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-20-2024",
  "Hora": "05:33:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-20-2024",
  "Hora": "13:32:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-21-2024",
  "Hora": "05:22:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-21-2024",
  "Hora": "13:33:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-22-2024",
  "Hora": "05:25:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-22-2024",
  "Hora": "13:33:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-23-2024",
  "Hora": "05:23:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-23-2024",
  "Hora": "05:23:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-23-2024",
  "Hora": "05:23:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-23-2024",
  "Hora": "05:23:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-23-2024",
  "Hora": "05:23:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-23-2024",
  "Hora": "05:23:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-23-2024",
  "Hora": "05:23:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-23-2024",
  "Hora": "05:23:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-23-2024",
  "Hora": "05:23:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-23-2024",
  "Hora": "05:23:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-23-2024",
  "Hora": "11:11:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-25-2024",
  "Hora": "05:57:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-25-2024",
  "Hora": "13:04:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-26-2024",
  "Hora": "05:20:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-26-2024",
  "Hora": "13:34:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-27-2024",
  "Hora": "05:21:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-27-2024",
  "Hora": "13:33:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-28-2024",
  "Hora": "05:24:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "03-28-2024",
  "Hora": "13:32:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-01-2024",
  "Hora": "05:57:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-01-2024",
  "Hora": "14:03:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-02-2024",
  "Hora": "05:18:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-02-2024",
  "Hora": "13:33:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-03-2024",
  "Hora": "05:25:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-03-2024",
  "Hora": "13:36:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-04-2024",
  "Hora": "05:24:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-04-2024",
  "Hora": "13:35:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-05-2024",
  "Hora": "05:19:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-05-2024",
  "Hora": "13:33:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-06-2024",
  "Hora": "05:49:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-06-2024",
  "Hora": "12:33:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-08-2024",
  "Hora": "05:54:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-08-2024",
  "Hora": "14:02:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-09-2024",
  "Hora": "05:17:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-09-2024",
  "Hora": "13:35:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-10-2024",
  "Hora": "05:23:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-10-2024",
  "Hora": "13:32:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-11-2024",
  "Hora": "05:15:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-11-2024",
  "Hora": "13:32:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-12-2024",
  "Hora": "05:17:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-12-2024",
  "Hora": "13:34:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-13-2024",
  "Hora": "05:23:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-13-2024",
  "Hora": "12:02:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-15-2024",
  "Hora": "05:45:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195115125,
  "Date": "04-15-2024",
  "Hora": "13:02:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-18-2024",
  "Hora": "08:00:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-18-2024",
  "Hora": "20:01:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-19-2024",
  "Hora": "07:47:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-19-2024",
  "Hora": "18:01:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-20-2024",
  "Hora": "07:50:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-20-2024",
  "Hora": "20:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-21-2024",
  "Hora": "07:47:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-21-2024",
  "Hora": "18:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-22-2024",
  "Hora": "07:52:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-22-2024",
  "Hora": "16:58:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-23-2024",
  "Hora": "07:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-23-2024",
  "Hora": "07:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-23-2024",
  "Hora": "07:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-23-2024",
  "Hora": "07:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-23-2024",
  "Hora": "07:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-23-2024",
  "Hora": "07:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-23-2024",
  "Hora": "07:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-23-2024",
  "Hora": "07:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-23-2024",
  "Hora": "07:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-23-2024",
  "Hora": "07:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-23-2024",
  "Hora": "14:05:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-25-2024",
  "Hora": "07:55:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-25-2024",
  "Hora": "14:30:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-26-2024",
  "Hora": "07:57:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-26-2024",
  "Hora": "18:00:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-27-2024",
  "Hora": "07:53:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-27-2024",
  "Hora": "17:56:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-28-2024",
  "Hora": "07:58:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "03-28-2024",
  "Hora": "18:00:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-02-2024",
  "Hora": "08:09:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-02-2024",
  "Hora": "18:01:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-03-2024",
  "Hora": "07:51:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-03-2024",
  "Hora": "18:01:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-04-2024",
  "Hora": "07:48:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-04-2024",
  "Hora": "18:02:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-05-2024",
  "Hora": "07:55:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-05-2024",
  "Hora": "16:56:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-08-2024",
  "Hora": "11:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-08-2024",
  "Hora": "18:01:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-09-2024",
  "Hora": "07:46:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-09-2024",
  "Hora": "18:01:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-10-2024",
  "Hora": "07:45:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-10-2024",
  "Hora": "18:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-11-2024",
  "Hora": "07:47:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-11-2024",
  "Hora": "20:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-12-2024",
  "Hora": "07:51:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-12-2024",
  "Hora": "16:57:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-15-2024",
  "Hora": "07:55:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173047274,
  "Date": "04-15-2024",
  "Hora": "17:55:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-16-2024",
  "Hora": "05:50:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-16-2024",
  "Hora": "11:25:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-18-2024",
  "Hora": "05:52:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-18-2024",
  "Hora": "13:16:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-19-2024",
  "Hora": "05:53:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-19-2024",
  "Hora": "12:45:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-20-2024",
  "Hora": "05:57:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-20-2024",
  "Hora": "14:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-21-2024",
  "Hora": "05:56:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-21-2024",
  "Hora": "14:00:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-22-2024",
  "Hora": "05:53:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-22-2024",
  "Hora": "14:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-23-2024",
  "Hora": "06:00:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-23-2024",
  "Hora": "12:02:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-25-2024",
  "Hora": "05:53:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-25-2024",
  "Hora": "12:30:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-26-2024",
  "Hora": "05:52:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-26-2024",
  "Hora": "14:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-27-2024",
  "Hora": "05:55:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-27-2024",
  "Hora": "14:02:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-28-2024",
  "Hora": "05:53:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "03-28-2024",
  "Hora": "14:01:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-01-2024",
  "Hora": "05:57:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-01-2024",
  "Hora": "14:05:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-02-2024",
  "Hora": "05:56:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-02-2024",
  "Hora": "14:02:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-03-2024",
  "Hora": "05:48:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-03-2024",
  "Hora": "14:01:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-04-2024",
  "Hora": "05:55:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-04-2024",
  "Hora": "12:09:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-05-2024",
  "Hora": "05:56:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-05-2024",
  "Hora": "14:00:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-06-2024",
  "Hora": "05:50:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-06-2024",
  "Hora": "12:34:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-08-2024",
  "Hora": "05:44:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-08-2024",
  "Hora": "14:01:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-09-2024",
  "Hora": "05:54:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-09-2024",
  "Hora": "14:01:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-10-2024",
  "Hora": "05:51:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-10-2024",
  "Hora": "14:17:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-11-2024",
  "Hora": "05:47:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-11-2024",
  "Hora": "14:01:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-12-2024",
  "Hora": "05:53:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-12-2024",
  "Hora": "14:01:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-13-2024",
  "Hora": "05:48:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-13-2024",
  "Hora": "14:00:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-15-2024",
  "Hora": "05:51:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203214774,
  "Date": "04-15-2024",
  "Hora": "13:01:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181719141,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-16-2024",
  "Hora": "04:58:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-16-2024",
  "Hora": "13:05:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-18-2024",
  "Hora": "05:58:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-18-2024",
  "Hora": "14:00:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-19-2024",
  "Hora": "04:56:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-19-2024",
  "Hora": "13:02:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-20-2024",
  "Hora": "05:00:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-20-2024",
  "Hora": "13:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-21-2024",
  "Hora": "05:04:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-21-2024",
  "Hora": "13:07:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-22-2024",
  "Hora": "05:00:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-22-2024",
  "Hora": "13:09:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-23-2024",
  "Hora": "05:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-23-2024",
  "Hora": "05:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-23-2024",
  "Hora": "05:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-23-2024",
  "Hora": "05:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-23-2024",
  "Hora": "05:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-23-2024",
  "Hora": "05:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-23-2024",
  "Hora": "05:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-23-2024",
  "Hora": "05:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-23-2024",
  "Hora": "05:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-23-2024",
  "Hora": "05:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "03-23-2024",
  "Hora": "13:02:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-02-2024",
  "Hora": "04:59:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-02-2024",
  "Hora": "13:07:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-04-2024",
  "Hora": "04:58:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-04-2024",
  "Hora": "13:06:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-05-2024",
  "Hora": "05:02:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-05-2024",
  "Hora": "13:05:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-06-2024",
  "Hora": "04:56:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-06-2024",
  "Hora": "13:00:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-08-2024",
  "Hora": "06:01:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-08-2024",
  "Hora": "09:35:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-13-2024",
  "Hora": "05:02:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-13-2024",
  "Hora": "13:00:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-15-2024",
  "Hora": "06:01:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214475103,
  "Date": "04-15-2024",
  "Hora": "14:00:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17383764k",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "03-18-2024",
  "Hora": "08:23:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "03-18-2024",
  "Hora": "17:54:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "03-19-2024",
  "Hora": "12:16:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "03-19-2024",
  "Hora": "17:54:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "03-20-2024",
  "Hora": "08:32:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "03-20-2024",
  "Hora": "17:50:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "03-21-2024",
  "Hora": "08:26:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "03-21-2024",
  "Hora": "20:00:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "03-22-2024",
  "Hora": "08:38:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "03-22-2024",
  "Hora": "19:51:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-02-2024",
  "Hora": "08:21:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-02-2024",
  "Hora": "17:50:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-03-2024",
  "Hora": "08:25:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-03-2024",
  "Hora": "17:55:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-04-2024",
  "Hora": "08:27:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-04-2024",
  "Hora": "17:52:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-05-2024",
  "Hora": "08:28:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-05-2024",
  "Hora": "17:53:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-08-2024",
  "Hora": "09:22:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-08-2024",
  "Hora": "18:51:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-09-2024",
  "Hora": "09:25:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-09-2024",
  "Hora": "18:54:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-10-2024",
  "Hora": "09:27:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-10-2024",
  "Hora": "18:52:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-11-2024",
  "Hora": "09:25:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-11-2024",
  "Hora": "18:52:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-15-2024",
  "Hora": "09:25:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 121618435,
  "Date": "04-15-2024",
  "Hora": "17:54:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-16-2024",
  "Hora": "00:22:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-18-2024",
  "Hora": "15:36:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-19-2024",
  "Hora": "01:26:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-19-2024",
  "Hora": "15:40:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-20-2024",
  "Hora": "01:17:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-20-2024",
  "Hora": "15:19:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-21-2024",
  "Hora": "01:19:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-21-2024",
  "Hora": "15:40:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-22-2024",
  "Hora": "01:18:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-22-2024",
  "Hora": "15:45:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-23-2024",
  "Hora": "00:15:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-25-2024",
  "Hora": "15:25:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-26-2024",
  "Hora": "01:26:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-26-2024",
  "Hora": "15:30:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-27-2024",
  "Hora": "01:20:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-27-2024",
  "Hora": "15:44:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-28-2024",
  "Hora": "01:17:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-28-2024",
  "Hora": "15:57:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "03-29-2024",
  "Hora": "00:00:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-01-2024",
  "Hora": "15:25:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-02-2024",
  "Hora": "01:33:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-02-2024",
  "Hora": "15:52:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-03-2024",
  "Hora": "02:30:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-03-2024",
  "Hora": "16:02:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-04-2024",
  "Hora": "01:24:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-04-2024",
  "Hora": "16:02:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-05-2024",
  "Hora": "01:24:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-05-2024",
  "Hora": "15:42:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-05-2024",
  "Hora": "23:55:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-08-2024",
  "Hora": "15:48:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-09-2024",
  "Hora": "01:22:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-09-2024",
  "Hora": "15:57:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-10-2024",
  "Hora": "01:25:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-10-2024",
  "Hora": "15:47:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-11-2024",
  "Hora": "01:16:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-11-2024",
  "Hora": "16:00:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-12-2024",
  "Hora": "01:15:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-12-2024",
  "Hora": "15:32:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-13-2024",
  "Hora": "00:17:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254146315,
  "Date": "04-15-2024",
  "Hora": "15:25:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-16-2024",
  "Hora": "05:24:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-16-2024",
  "Hora": "09:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-18-2024",
  "Hora": "05:55:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-18-2024",
  "Hora": "13:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-19-2024",
  "Hora": "05:22:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-19-2024",
  "Hora": "13:32:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-20-2024",
  "Hora": "05:34:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-20-2024",
  "Hora": "13:31:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-21-2024",
  "Hora": "05:23:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-21-2024",
  "Hora": "13:32:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-22-2024",
  "Hora": "05:24:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-22-2024",
  "Hora": "13:30:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-23-2024",
  "Hora": "05:24:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-23-2024",
  "Hora": "05:24:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-23-2024",
  "Hora": "05:24:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-23-2024",
  "Hora": "05:24:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-23-2024",
  "Hora": "05:24:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-23-2024",
  "Hora": "05:24:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-23-2024",
  "Hora": "05:24:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-23-2024",
  "Hora": "05:24:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-23-2024",
  "Hora": "05:24:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-23-2024",
  "Hora": "05:24:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-23-2024",
  "Hora": "11:08:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-25-2024",
  "Hora": "05:57:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-25-2024",
  "Hora": "13:01:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-26-2024",
  "Hora": "05:20:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-26-2024",
  "Hora": "13:31:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-27-2024",
  "Hora": "05:22:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-27-2024",
  "Hora": "13:31:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-28-2024",
  "Hora": "05:25:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "03-28-2024",
  "Hora": "13:32:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-01-2024",
  "Hora": "05:57:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-01-2024",
  "Hora": "14:02:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-02-2024",
  "Hora": "05:18:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-02-2024",
  "Hora": "13:31:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-03-2024",
  "Hora": "05:24:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-03-2024",
  "Hora": "13:39:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-04-2024",
  "Hora": "05:24:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-04-2024",
  "Hora": "13:36:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-05-2024",
  "Hora": "05:19:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-05-2024",
  "Hora": "13:32:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-06-2024",
  "Hora": "05:28:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-06-2024",
  "Hora": "12:32:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-08-2024",
  "Hora": "05:55:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-08-2024",
  "Hora": "14:00:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-09-2024",
  "Hora": "05:18:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-09-2024",
  "Hora": "13:32:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-10-2024",
  "Hora": "05:22:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-10-2024",
  "Hora": "13:32:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-11-2024",
  "Hora": "05:15:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-11-2024",
  "Hora": "13:32:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-12-2024",
  "Hora": "05:18:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-12-2024",
  "Hora": "13:32:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-13-2024",
  "Hora": "05:24:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-13-2024",
  "Hora": "12:01:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-15-2024",
  "Hora": "05:46:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187627842,
  "Date": "04-15-2024",
  "Hora": "13:01:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-16-2024",
  "Hora": "04:46:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-16-2024",
  "Hora": "14:01:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-20-2024",
  "Hora": "04:45:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-20-2024",
  "Hora": "14:30:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-21-2024",
  "Hora": "04:46:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-21-2024",
  "Hora": "14:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-22-2024",
  "Hora": "04:45:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-22-2024",
  "Hora": "14:30:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-25-2024",
  "Hora": "04:43:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-25-2024",
  "Hora": "14:30:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-26-2024",
  "Hora": "04:57:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-26-2024",
  "Hora": "14:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-27-2024",
  "Hora": "04:44:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-27-2024",
  "Hora": "14:31:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-28-2024",
  "Hora": "04:46:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "03-28-2024",
  "Hora": "14:30:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-01-2024",
  "Hora": "04:49:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-01-2024",
  "Hora": "14:30:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-03-2024",
  "Hora": "04:47:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-03-2024",
  "Hora": "14:30:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-04-2024",
  "Hora": "04:41:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-04-2024",
  "Hora": "14:30:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-05-2024",
  "Hora": "04:44:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-05-2024",
  "Hora": "14:31:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-06-2024",
  "Hora": "04:50:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-06-2024",
  "Hora": "14:30:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-08-2024",
  "Hora": "04:45:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-08-2024",
  "Hora": "14:31:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-10-2024",
  "Hora": "04:44:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-10-2024",
  "Hora": "14:30:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-11-2024",
  "Hora": "04:42:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-11-2024",
  "Hora": "14:30:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-12-2024",
  "Hora": "04:44:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-12-2024",
  "Hora": "14:30:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-13-2024",
  "Hora": "04:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-13-2024",
  "Hora": "14:30:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-15-2024",
  "Hora": "04:43:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193669298,
  "Date": "04-15-2024",
  "Hora": "14:30:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-18-2024",
  "Hora": "03:51:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-18-2024",
  "Hora": "12:12:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-19-2024",
  "Hora": "04:07:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-19-2024",
  "Hora": "12:19:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-20-2024",
  "Hora": "04:07:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-20-2024",
  "Hora": "12:20:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-21-2024",
  "Hora": "03:56:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-21-2024",
  "Hora": "12:20:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-22-2024",
  "Hora": "03:55:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-22-2024",
  "Hora": "12:18:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-23-2024",
  "Hora": "03:58:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-23-2024",
  "Hora": "11:13:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-25-2024",
  "Hora": "16:08:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-26-2024",
  "Hora": "01:25:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-26-2024",
  "Hora": "16:32:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-27-2024",
  "Hora": "01:15:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-27-2024",
  "Hora": "16:20:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-28-2024",
  "Hora": "01:18:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-28-2024",
  "Hora": "16:04:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "03-28-2024",
  "Hora": "23:56:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-01-2024",
  "Hora": "03:33:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-01-2024",
  "Hora": "12:10:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-02-2024",
  "Hora": "03:58:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-02-2024",
  "Hora": "12:16:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-03-2024",
  "Hora": "03:52:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-03-2024",
  "Hora": "12:16:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-04-2024",
  "Hora": "03:38:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-04-2024",
  "Hora": "12:02:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-05-2024",
  "Hora": "03:40:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-05-2024",
  "Hora": "12:02:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-06-2024",
  "Hora": "03:42:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-06-2024",
  "Hora": "11:49:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-08-2024",
  "Hora": "12:56:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-08-2024",
  "Hora": "22:31:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-09-2024",
  "Hora": "13:06:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-09-2024",
  "Hora": "22:32:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-10-2024",
  "Hora": "13:14:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-10-2024",
  "Hora": "22:34:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-11-2024",
  "Hora": "12:56:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-11-2024",
  "Hora": "21:59:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-12-2024",
  "Hora": "12:57:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-12-2024",
  "Hora": "21:25:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-15-2024",
  "Hora": "03:48:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 146946194,
  "Date": "04-15-2024",
  "Hora": "11:53:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-16-2024",
  "Hora": "03:39:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-16-2024",
  "Hora": "11:59:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-18-2024",
  "Hora": "03:56:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-18-2024",
  "Hora": "12:27:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-19-2024",
  "Hora": "04:08:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-19-2024",
  "Hora": "12:15:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-20-2024",
  "Hora": "04:10:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-20-2024",
  "Hora": "12:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-21-2024",
  "Hora": "01:41:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-21-2024",
  "Hora": "12:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-22-2024",
  "Hora": "04:11:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-22-2024",
  "Hora": "11:57:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-23-2024",
  "Hora": "04:01:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-23-2024",
  "Hora": "10:58:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-25-2024",
  "Hora": "04:07:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-25-2024",
  "Hora": "11:55:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-26-2024",
  "Hora": "03:44:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-26-2024",
  "Hora": "12:03:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-27-2024",
  "Hora": "03:55:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-27-2024",
  "Hora": "12:04:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-28-2024",
  "Hora": "04:06:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "03-28-2024",
  "Hora": "12:06:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-01-2024",
  "Hora": "04:03:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-01-2024",
  "Hora": "12:07:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-02-2024",
  "Hora": "01:46:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-02-2024",
  "Hora": "12:10:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-03-2024",
  "Hora": "01:43:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-03-2024",
  "Hora": "12:09:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-04-2024",
  "Hora": "01:44:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-04-2024",
  "Hora": "10:08:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-05-2024",
  "Hora": "02:08:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-05-2024",
  "Hora": "10:04:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-06-2024",
  "Hora": "01:50:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-06-2024",
  "Hora": "10:02:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-08-2024",
  "Hora": "04:10:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-08-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-09-2024",
  "Hora": "04:08:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-09-2024",
  "Hora": "12:13:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-10-2024",
  "Hora": "03:38:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-10-2024",
  "Hora": "12:03:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-11-2024",
  "Hora": "03:40:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-11-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-12-2024",
  "Hora": "04:04:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-12-2024",
  "Hora": "11:55:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-13-2024",
  "Hora": "03:36:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-13-2024",
  "Hora": "11:47:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-15-2024",
  "Hora": "03:55:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209014769,
  "Date": "04-15-2024",
  "Hora": "11:46:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-16-2024",
  "Hora": "03:42:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-16-2024",
  "Hora": "11:03:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-18-2024",
  "Hora": "02:42:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-18-2024",
  "Hora": "11:06:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-19-2024",
  "Hora": "02:40:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-19-2024",
  "Hora": "11:08:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-20-2024",
  "Hora": "03:15:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-20-2024",
  "Hora": "11:09:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-21-2024",
  "Hora": "02:32:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-21-2024",
  "Hora": "11:08:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-22-2024",
  "Hora": "02:49:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-22-2024",
  "Hora": "11:08:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-23-2024",
  "Hora": "02:44:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-23-2024",
  "Hora": "11:10:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-25-2024",
  "Hora": "03:50:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-25-2024",
  "Hora": "12:06:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-26-2024",
  "Hora": "03:58:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-26-2024",
  "Hora": "12:08:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-27-2024",
  "Hora": "04:10:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-27-2024",
  "Hora": "12:09:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-28-2024",
  "Hora": "03:34:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-28-2024",
  "Hora": "12:00:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "03-31-2024",
  "Hora": "21:45:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-01-2024",
  "Hora": "02:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-01-2024",
  "Hora": "11:15:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-02-2024",
  "Hora": "06:07:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-02-2024",
  "Hora": "11:05:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-03-2024",
  "Hora": "03:02:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-03-2024",
  "Hora": "11:03:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-04-2024",
  "Hora": "02:47:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-04-2024",
  "Hora": "11:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-05-2024",
  "Hora": "02:37:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-05-2024",
  "Hora": "11:38:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-06-2024",
  "Hora": "02:39:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-06-2024",
  "Hora": "11:04:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-08-2024",
  "Hora": "03:54:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-08-2024",
  "Hora": "12:04:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-09-2024",
  "Hora": "03:55:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-09-2024",
  "Hora": "12:06:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-10-2024",
  "Hora": "03:51:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-10-2024",
  "Hora": "12:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-11-2024",
  "Hora": "03:46:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-11-2024",
  "Hora": "12:01:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-12-2024",
  "Hora": "03:56:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-12-2024",
  "Hora": "12:03:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-13-2024",
  "Hora": "03:51:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-13-2024",
  "Hora": "10:56:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-15-2024",
  "Hora": "02:08:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 238355664,
  "Date": "04-15-2024",
  "Hora": "11:17:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-18-2024",
  "Hora": "07:38:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-18-2024",
  "Hora": "18:06:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-19-2024",
  "Hora": "07:27:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-19-2024",
  "Hora": "18:03:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-20-2024",
  "Hora": "07:20:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-20-2024",
  "Hora": "18:01:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-21-2024",
  "Hora": "07:26:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-21-2024",
  "Hora": "18:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-22-2024",
  "Hora": "07:33:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-22-2024",
  "Hora": "17:03:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-22-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-22-2024",
  "Hora": "19:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-25-2024",
  "Hora": "07:29:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-25-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-26-2024",
  "Hora": "07:33:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-26-2024",
  "Hora": "18:17:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-27-2024",
  "Hora": "07:28:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-27-2024",
  "Hora": "18:08:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-28-2024",
  "Hora": "07:30:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "03-28-2024",
  "Hora": "18:28:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-01-2024",
  "Hora": "07:31:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-01-2024",
  "Hora": "18:03:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-02-2024",
  "Hora": "07:27:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-02-2024",
  "Hora": "18:02:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-03-2024",
  "Hora": "07:33:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-03-2024",
  "Hora": "18:02:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-03-2024",
  "Hora": "19:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-04-2024",
  "Hora": "07:35:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-04-2024",
  "Hora": "18:02:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-05-2024",
  "Hora": "06:59:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-05-2024",
  "Hora": "07:41:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-05-2024",
  "Hora": "17:02:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-06-2024",
  "Hora": "12:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-06-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-08-2024",
  "Hora": "07:40:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-08-2024",
  "Hora": "18:03:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-09-2024",
  "Hora": "07:32:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-09-2024",
  "Hora": "18:02:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-10-2024",
  "Hora": "07:26:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-10-2024",
  "Hora": "18:00:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-11-2024",
  "Hora": "08:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-11-2024",
  "Hora": "18:02:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-12-2024",
  "Hora": "07:29:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-12-2024",
  "Hora": "17:03:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-12-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-15-2024",
  "Hora": "07:40:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18538263K",
  "Date": "04-15-2024",
  "Hora": "18:04:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-16-2024",
  "Hora": "04:03:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-16-2024",
  "Hora": "11:52:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-18-2024",
  "Hora": "04:05:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-18-2024",
  "Hora": "12:20:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-19-2024",
  "Hora": "03:59:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-19-2024",
  "Hora": "12:14:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-20-2024",
  "Hora": "04:06:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-20-2024",
  "Hora": "11:59:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-21-2024",
  "Hora": "04:07:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-21-2024",
  "Hora": "12:02:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-22-2024",
  "Hora": "04:14:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-22-2024",
  "Hora": "11:40:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-23-2024",
  "Hora": "04:05:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-23-2024",
  "Hora": "11:08:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-25-2024",
  "Hora": "03:39:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-25-2024",
  "Hora": "12:01:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-26-2024",
  "Hora": "03:50:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-26-2024",
  "Hora": "11:57:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-27-2024",
  "Hora": "03:55:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-27-2024",
  "Hora": "11:58:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-28-2024",
  "Hora": "04:01:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "03-28-2024",
  "Hora": "12:01:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-01-2024",
  "Hora": "01:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-01-2024",
  "Hora": "04:10:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-01-2024",
  "Hora": "10:19:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-02-2024",
  "Hora": "04:24:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-02-2024",
  "Hora": "12:26:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-03-2024",
  "Hora": "03:56:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-03-2024",
  "Hora": "12:13:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-04-2024",
  "Hora": "03:26:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-04-2024",
  "Hora": "12:12:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-05-2024",
  "Hora": "03:45:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-05-2024",
  "Hora": "12:05:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-06-2024",
  "Hora": "04:05:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-06-2024",
  "Hora": "11:59:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-07-2024",
  "Hora": "22:13:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-08-2024",
  "Hora": "10:23:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-09-2024",
  "Hora": "04:02:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-09-2024",
  "Hora": "12:19:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-10-2024",
  "Hora": "04:07:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-10-2024",
  "Hora": "11:43:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-11-2024",
  "Hora": "04:14:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-11-2024",
  "Hora": "11:53:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-12-2024",
  "Hora": "04:12:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-12-2024",
  "Hora": "11:59:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-13-2024",
  "Hora": "04:11:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-13-2024",
  "Hora": "11:45:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-15-2024",
  "Hora": "04:13:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211801603,
  "Date": "04-15-2024",
  "Hora": "11:40:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-18-2024",
  "Hora": "08:30:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-18-2024",
  "Hora": "17:55:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-19-2024",
  "Hora": "08:34:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-19-2024",
  "Hora": "17:50:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-20-2024",
  "Hora": "08:44:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-20-2024",
  "Hora": "17:51:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-21-2024",
  "Hora": "08:44:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-21-2024",
  "Hora": "17:48:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-22-2024",
  "Hora": "08:22:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-22-2024",
  "Hora": "17:48:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-25-2024",
  "Hora": "08:27:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-25-2024",
  "Hora": "17:56:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-26-2024",
  "Hora": "08:20:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-26-2024",
  "Hora": "17:51:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-27-2024",
  "Hora": "08:13:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-27-2024",
  "Hora": "17:57:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-28-2024",
  "Hora": "08:27:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "03-28-2024",
  "Hora": "17:57:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-01-2024",
  "Hora": "08:11:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-01-2024",
  "Hora": "17:53:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-02-2024",
  "Hora": "08:11:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-02-2024",
  "Hora": "17:51:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-03-2024",
  "Hora": "08:21:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-03-2024",
  "Hora": "17:47:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-04-2024",
  "Hora": "08:15:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-04-2024",
  "Hora": "17:47:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-05-2024",
  "Hora": "08:18:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-05-2024",
  "Hora": "17:48:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-08-2024",
  "Hora": "09:25:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-08-2024",
  "Hora": "18:54:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-09-2024",
  "Hora": "09:21:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-09-2024",
  "Hora": "18:49:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-10-2024",
  "Hora": "09:30:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-10-2024",
  "Hora": "19:07:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-11-2024",
  "Hora": "09:16:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-11-2024",
  "Hora": "18:53:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-12-2024",
  "Hora": "09:16:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-12-2024",
  "Hora": "21:16:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-15-2024",
  "Hora": "09:14:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 143836835,
  "Date": "04-15-2024",
  "Hora": "17:57:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-16-2024",
  "Hora": "04:52:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-16-2024",
  "Hora": "12:01:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-18-2024",
  "Hora": "05:54:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-18-2024",
  "Hora": "14:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-19-2024",
  "Hora": "04:55:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-19-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-20-2024",
  "Hora": "04:53:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-20-2024",
  "Hora": "13:02:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-21-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-21-2024",
  "Hora": "13:00:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-22-2024",
  "Hora": "04:52:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-22-2024",
  "Hora": "13:01:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-23-2024",
  "Hora": "04:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-23-2024",
  "Hora": "04:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-23-2024",
  "Hora": "04:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-23-2024",
  "Hora": "04:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-23-2024",
  "Hora": "04:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-23-2024",
  "Hora": "04:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-23-2024",
  "Hora": "04:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-23-2024",
  "Hora": "04:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-23-2024",
  "Hora": "04:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-23-2024",
  "Hora": "04:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-23-2024",
  "Hora": "13:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-25-2024",
  "Hora": "05:51:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-25-2024",
  "Hora": "14:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-26-2024",
  "Hora": "04:52:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-26-2024",
  "Hora": "13:02:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-27-2024",
  "Hora": "04:52:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-27-2024",
  "Hora": "13:00:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-28-2024",
  "Hora": "04:53:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "03-28-2024",
  "Hora": "13:02:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-01-2024",
  "Hora": "04:48:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-01-2024",
  "Hora": "13:02:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-02-2024",
  "Hora": "03:52:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-02-2024",
  "Hora": "12:00:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-03-2024",
  "Hora": "03:52:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-03-2024",
  "Hora": "12:02:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-04-2024",
  "Hora": "04:52:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-04-2024",
  "Hora": "12:02:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-05-2024",
  "Hora": "04:52:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-05-2024",
  "Hora": "12:02:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-06-2024",
  "Hora": "04:52:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-06-2024",
  "Hora": "12:00:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-08-2024",
  "Hora": "05:52:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-08-2024",
  "Hora": "14:00:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-09-2024",
  "Hora": "03:48:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-09-2024",
  "Hora": "12:00:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-10-2024",
  "Hora": "04:51:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-10-2024",
  "Hora": "12:05:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-11-2024",
  "Hora": "04:52:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-11-2024",
  "Hora": "12:58:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-12-2024",
  "Hora": "04:51:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-12-2024",
  "Hora": "13:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-13-2024",
  "Hora": "04:53:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-13-2024",
  "Hora": "13:00:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-15-2024",
  "Hora": "05:51:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 129943149,
  "Date": "04-15-2024",
  "Hora": "14:00:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-16-2024",
  "Hora": "06:43:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-16-2024",
  "Hora": "13:00:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-18-2024",
  "Hora": "06:52:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-18-2024",
  "Hora": "15:00:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-19-2024",
  "Hora": "06:41:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-19-2024",
  "Hora": "15:00:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-20-2024",
  "Hora": "06:55:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-20-2024",
  "Hora": "15:00:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-21-2024",
  "Hora": "06:54:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-21-2024",
  "Hora": "15:00:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-22-2024",
  "Hora": "06:53:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-22-2024",
  "Hora": "15:00:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-23-2024",
  "Hora": "06:43:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-23-2024",
  "Hora": "13:35:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-25-2024",
  "Hora": "06:57:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-25-2024",
  "Hora": "15:01:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-26-2024",
  "Hora": "06:43:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-26-2024",
  "Hora": "15:01:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-27-2024",
  "Hora": "06:48:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-27-2024",
  "Hora": "13:07:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-28-2024",
  "Hora": "06:56:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "03-28-2024",
  "Hora": "15:00:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-01-2024",
  "Hora": "06:40:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-01-2024",
  "Hora": "15:02:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-02-2024",
  "Hora": "06:42:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-02-2024",
  "Hora": "15:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-03-2024",
  "Hora": "06:45:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-03-2024",
  "Hora": "15:01:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-04-2024",
  "Hora": "06:39:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-04-2024",
  "Hora": "15:02:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-05-2024",
  "Hora": "06:59:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-05-2024",
  "Hora": "15:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-06-2024",
  "Hora": "07:00:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-06-2024",
  "Hora": "14:40:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-08-2024",
  "Hora": "06:55:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-08-2024",
  "Hora": "15:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-09-2024",
  "Hora": "06:44:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-09-2024",
  "Hora": "15:00:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-10-2024",
  "Hora": "06:53:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-10-2024",
  "Hora": "15:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-11-2024",
  "Hora": "06:53:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-11-2024",
  "Hora": "15:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-12-2024",
  "Hora": "06:52:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-12-2024",
  "Hora": "15:00:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-13-2024",
  "Hora": "06:44:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-13-2024",
  "Hora": "14:30:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-15-2024",
  "Hora": "06:50:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 139639294,
  "Date": "04-15-2024",
  "Hora": "15:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-16-2024",
  "Hora": "00:17:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-18-2024",
  "Hora": "15:53:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-19-2024",
  "Hora": "01:10:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-19-2024",
  "Hora": "15:44:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-20-2024",
  "Hora": "00:51:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-20-2024",
  "Hora": "15:53:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-21-2024",
  "Hora": "00:59:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-21-2024",
  "Hora": "15:54:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-22-2024",
  "Hora": "01:07:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-22-2024",
  "Hora": "15:59:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-23-2024",
  "Hora": "00:08:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-25-2024",
  "Hora": "15:54:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-26-2024",
  "Hora": "01:15:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-27-2024",
  "Hora": "15:58:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-28-2024",
  "Hora": "00:57:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-28-2024",
  "Hora": "16:00:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "03-28-2024",
  "Hora": "23:49:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-01-2024",
  "Hora": "15:54:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-02-2024",
  "Hora": "01:43:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-02-2024",
  "Hora": "17:47:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-03-2024",
  "Hora": "02:29:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-03-2024",
  "Hora": "16:02:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-04-2024",
  "Hora": "01:12:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-04-2024",
  "Hora": "15:59:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-05-2024",
  "Hora": "01:12:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-05-2024",
  "Hora": "15:53:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-06-2024",
  "Hora": "00:09:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-08-2024",
  "Hora": "15:58:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-09-2024",
  "Hora": "01:04:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-09-2024",
  "Hora": "15:58:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-10-2024",
  "Hora": "00:53:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-10-2024",
  "Hora": "15:42:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-11-2024",
  "Hora": "01:04:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-11-2024",
  "Hora": "15:58:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-12-2024",
  "Hora": "00:56:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-12-2024",
  "Hora": "15:52:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-13-2024",
  "Hora": "00:15:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188371248,
  "Date": "04-15-2024",
  "Hora": "15:37:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-18-2024",
  "Hora": "04:41:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-18-2024",
  "Hora": "14:29:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-20-2024",
  "Hora": "04:46:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-20-2024",
  "Hora": "14:30:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-21-2024",
  "Hora": "04:48:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-21-2024",
  "Hora": "14:31:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-22-2024",
  "Hora": "04:49:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-22-2024",
  "Hora": "14:29:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-23-2024",
  "Hora": "04:55:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-23-2024",
  "Hora": "13:23:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-25-2024",
  "Hora": "04:43:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-25-2024",
  "Hora": "14:32:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-27-2024",
  "Hora": "04:44:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-27-2024",
  "Hora": "14:39:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-28-2024",
  "Hora": "04:47:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "03-28-2024",
  "Hora": "14:36:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-01-2024",
  "Hora": "04:45:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-01-2024",
  "Hora": "14:36:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-02-2024",
  "Hora": "04:50:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-02-2024",
  "Hora": "12:00:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-03-2024",
  "Hora": "04:48:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-03-2024",
  "Hora": "14:31:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-04-2024",
  "Hora": "04:49:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-04-2024",
  "Hora": "14:30:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-05-2024",
  "Hora": "04:51:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-05-2024",
  "Hora": "14:29:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-08-2024",
  "Hora": "04:46:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-08-2024",
  "Hora": "14:32:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-10-2024",
  "Hora": "04:41:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-10-2024",
  "Hora": "14:35:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-11-2024",
  "Hora": "04:39:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-11-2024",
  "Hora": "14:30:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-12-2024",
  "Hora": "04:43:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-12-2024",
  "Hora": "14:35:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-13-2024",
  "Hora": "04:49:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-13-2024",
  "Hora": "14:29:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-15-2024",
  "Hora": "04:43:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26271599K",
  "Date": "04-15-2024",
  "Hora": "14:29:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-16-2024",
  "Hora": "04:55:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-16-2024",
  "Hora": "14:01:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-18-2024",
  "Hora": "04:44:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-18-2024",
  "Hora": "14:31:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-20-2024",
  "Hora": "04:55:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-20-2024",
  "Hora": "14:30:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-21-2024",
  "Hora": "04:48:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-21-2024",
  "Hora": "14:30:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-22-2024",
  "Hora": "04:54:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-22-2024",
  "Hora": "14:32:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-23-2024",
  "Hora": "04:47:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-23-2024",
  "Hora": "13:16:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-25-2024",
  "Hora": "04:47:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-25-2024",
  "Hora": "14:30:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-26-2024",
  "Hora": "04:47:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-26-2024",
  "Hora": "14:30:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-27-2024",
  "Hora": "04:49:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-27-2024",
  "Hora": "14:31:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-28-2024",
  "Hora": "04:53:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "03-28-2024",
  "Hora": "14:31:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-01-2024",
  "Hora": "04:54:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-01-2024",
  "Hora": "14:30:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-03-2024",
  "Hora": "04:52:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-03-2024",
  "Hora": "14:30:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-04-2024",
  "Hora": "04:52:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-04-2024",
  "Hora": "14:30:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-05-2024",
  "Hora": "04:48:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-05-2024",
  "Hora": "14:30:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-06-2024",
  "Hora": "04:53:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-06-2024",
  "Hora": "14:32:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-08-2024",
  "Hora": "04:49:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-08-2024",
  "Hora": "14:31:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-10-2024",
  "Hora": "04:52:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-10-2024",
  "Hora": "14:35:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-11-2024",
  "Hora": "04:48:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-11-2024",
  "Hora": "14:30:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-12-2024",
  "Hora": "04:53:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-12-2024",
  "Hora": "14:30:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-13-2024",
  "Hora": "04:55:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-13-2024",
  "Hora": "14:30:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-15-2024",
  "Hora": "04:41:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178888226,
  "Date": "04-15-2024",
  "Hora": "14:30:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 144200071,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-16-2024",
  "Hora": "05:32:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-16-2024",
  "Hora": "14:25:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-18-2024",
  "Hora": "06:23:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-18-2024",
  "Hora": "13:01:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-19-2024",
  "Hora": "05:20:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-19-2024",
  "Hora": "13:31:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-20-2024",
  "Hora": "05:23:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-20-2024",
  "Hora": "13:31:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-21-2024",
  "Hora": "05:19:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-21-2024",
  "Hora": "13:31:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-22-2024",
  "Hora": "05:24:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-22-2024",
  "Hora": "13:30:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-23-2024",
  "Hora": "05:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-23-2024",
  "Hora": "13:31:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-25-2024",
  "Hora": "05:51:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-25-2024",
  "Hora": "13:05:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-26-2024",
  "Hora": "05:17:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-26-2024",
  "Hora": "13:31:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-27-2024",
  "Hora": "05:18:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "03-27-2024",
  "Hora": "13:30:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-01-2024",
  "Hora": "05:46:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-01-2024",
  "Hora": "14:11:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-02-2024",
  "Hora": "05:17:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-02-2024",
  "Hora": "13:32:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-03-2024",
  "Hora": "05:17:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-03-2024",
  "Hora": "13:33:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-04-2024",
  "Hora": "05:18:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-04-2024",
  "Hora": "13:35:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-05-2024",
  "Hora": "05:21:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-05-2024",
  "Hora": "13:37:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-06-2024",
  "Hora": "05:31:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-06-2024",
  "Hora": "13:43:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-08-2024",
  "Hora": "05:49:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-08-2024",
  "Hora": "14:01:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-09-2024",
  "Hora": "05:15:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-09-2024",
  "Hora": "13:32:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-10-2024",
  "Hora": "05:24:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-10-2024",
  "Hora": "13:31:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-11-2024",
  "Hora": "05:18:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-11-2024",
  "Hora": "13:31:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-12-2024",
  "Hora": "05:18:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-12-2024",
  "Hora": "13:32:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-13-2024",
  "Hora": "05:19:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-13-2024",
  "Hora": "14:02:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-15-2024",
  "Hora": "05:49:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 106846626,
  "Date": "04-15-2024",
  "Hora": "13:02:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-18-2024",
  "Hora": "08:46:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-18-2024",
  "Hora": "18:01:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-19-2024",
  "Hora": "08:50:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-19-2024",
  "Hora": "18:01:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-20-2024",
  "Hora": "08:55:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-20-2024",
  "Hora": "18:00:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-21-2024",
  "Hora": "08:44:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-21-2024",
  "Hora": "18:00:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-22-2024",
  "Hora": "08:56:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-22-2024",
  "Hora": "18:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-25-2024",
  "Hora": "08:42:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-25-2024",
  "Hora": "18:01:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-26-2024",
  "Hora": "08:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-26-2024",
  "Hora": "18:01:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-27-2024",
  "Hora": "08:22:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-27-2024",
  "Hora": "18:00:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-28-2024",
  "Hora": "08:24:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-28-2024",
  "Hora": "08:26:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "03-28-2024",
  "Hora": "18:01:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-01-2024",
  "Hora": "08:28:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-01-2024",
  "Hora": "18:02:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-02-2024",
  "Hora": "08:35:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-02-2024",
  "Hora": "18:06:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-03-2024",
  "Hora": "08:26:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-03-2024",
  "Hora": "18:02:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-04-2024",
  "Hora": "08:28:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-04-2024",
  "Hora": "18:00:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-05-2024",
  "Hora": "08:33:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-05-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-08-2024",
  "Hora": "08:22:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-08-2024",
  "Hora": "18:03:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-09-2024",
  "Hora": "08:21:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-09-2024",
  "Hora": "20:13:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-10-2024",
  "Hora": "08:30:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-10-2024",
  "Hora": "18:04:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-11-2024",
  "Hora": "08:26:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-11-2024",
  "Hora": "18:06:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-12-2024",
  "Hora": "08:16:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-12-2024",
  "Hora": "18:11:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-15-2024",
  "Hora": "08:33:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 141623176,
  "Date": "04-15-2024",
  "Hora": "18:06:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-18-2024",
  "Hora": "08:32:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-18-2024",
  "Hora": "17:54:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-19-2024",
  "Hora": "08:35:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-19-2024",
  "Hora": "18:00:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-20-2024",
  "Hora": "08:50:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-20-2024",
  "Hora": "17:56:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-21-2024",
  "Hora": "08:37:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-21-2024",
  "Hora": "17:58:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-22-2024",
  "Hora": "08:32:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-22-2024",
  "Hora": "17:54:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "06:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "07:12:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "07:12:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "07:12:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "07:12:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "07:12:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "07:12:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "07:12:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "07:12:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "07:12:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "07:12:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-23-2024",
  "Hora": "16:02:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-25-2024",
  "Hora": "08:39:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-25-2024",
  "Hora": "17:59:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-26-2024",
  "Hora": "08:33:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-26-2024",
  "Hora": "18:27:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-27-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-27-2024",
  "Hora": "17:58:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-28-2024",
  "Hora": "08:40:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "03-28-2024",
  "Hora": "17:51:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-01-2024",
  "Hora": "08:30:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-01-2024",
  "Hora": "17:56:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-02-2024",
  "Hora": "08:35:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-02-2024",
  "Hora": "18:03:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-03-2024",
  "Hora": "08:36:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-03-2024",
  "Hora": "17:58:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-04-2024",
  "Hora": "08:38:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-04-2024",
  "Hora": "17:54:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-05-2024",
  "Hora": "08:37:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-05-2024",
  "Hora": "17:55:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-09-2024",
  "Hora": "08:37:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-09-2024",
  "Hora": "18:55:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-10-2024",
  "Hora": "09:36:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-10-2024",
  "Hora": "18:47:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-11-2024",
  "Hora": "09:31:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-11-2024",
  "Hora": "18:48:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-12-2024",
  "Hora": "09:37:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-12-2024",
  "Hora": "17:49:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-15-2024",
  "Hora": "12:59:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174202036,
  "Date": "04-15-2024",
  "Hora": "18:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-16-2024",
  "Hora": "00:14:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-18-2024",
  "Hora": "15:26:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-19-2024",
  "Hora": "01:11:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-19-2024",
  "Hora": "15:24:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-20-2024",
  "Hora": "01:01:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-20-2024",
  "Hora": "15:19:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-21-2024",
  "Hora": "01:05:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-21-2024",
  "Hora": "15:33:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-22-2024",
  "Hora": "01:06:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-22-2024",
  "Hora": "15:34:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-23-2024",
  "Hora": "00:13:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-25-2024",
  "Hora": "15:36:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-26-2024",
  "Hora": "01:18:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-26-2024",
  "Hora": "15:13:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-27-2024",
  "Hora": "01:24:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-27-2024",
  "Hora": "15:23:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-28-2024",
  "Hora": "01:04:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-28-2024",
  "Hora": "15:34:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "03-28-2024",
  "Hora": "23:48:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-01-2024",
  "Hora": "15:30:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-02-2024",
  "Hora": "01:31:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-02-2024",
  "Hora": "15:41:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-03-2024",
  "Hora": "02:39:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-03-2024",
  "Hora": "15:26:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-04-2024",
  "Hora": "01:09:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-04-2024",
  "Hora": "15:28:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-05-2024",
  "Hora": "01:21:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-05-2024",
  "Hora": "15:41:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-05-2024",
  "Hora": "23:54:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-08-2024",
  "Hora": "15:27:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-09-2024",
  "Hora": "01:21:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-09-2024",
  "Hora": "15:22:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-10-2024",
  "Hora": "01:01:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-10-2024",
  "Hora": "15:13:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-11-2024",
  "Hora": "01:04:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-11-2024",
  "Hora": "15:30:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-12-2024",
  "Hora": "00:55:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-12-2024",
  "Hora": "16:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-13-2024",
  "Hora": "00:08:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145610028,
  "Date": "04-15-2024",
  "Hora": "15:32:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-16-2024",
  "Hora": "03:41:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-16-2024",
  "Hora": "10:58:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-18-2024",
  "Hora": "03:54:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-18-2024",
  "Hora": "12:02:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-19-2024",
  "Hora": "04:07:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-19-2024",
  "Hora": "12:18:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-20-2024",
  "Hora": "04:05:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-20-2024",
  "Hora": "12:10:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-21-2024",
  "Hora": "04:04:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-21-2024",
  "Hora": "12:07:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-22-2024",
  "Hora": "03:52:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-22-2024",
  "Hora": "12:15:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-23-2024",
  "Hora": "03:53:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-23-2024",
  "Hora": "12:15:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-25-2024",
  "Hora": "05:10:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-25-2024",
  "Hora": "12:05:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-26-2024",
  "Hora": "03:52:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-26-2024",
  "Hora": "12:02:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-27-2024",
  "Hora": "04:07:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-27-2024",
  "Hora": "12:05:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-28-2024",
  "Hora": "03:48:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "03-28-2024",
  "Hora": "12:00:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-02-2024",
  "Hora": "03:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-02-2024",
  "Hora": "13:18:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-03-2024",
  "Hora": "03:59:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-03-2024",
  "Hora": "12:14:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-04-2024",
  "Hora": "04:01:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-04-2024",
  "Hora": "11:59:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-05-2024",
  "Hora": "03:42:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-05-2024",
  "Hora": "12:10:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-06-2024",
  "Hora": "03:43:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-06-2024",
  "Hora": "11:04:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-08-2024",
  "Hora": "03:39:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-08-2024",
  "Hora": "12:05:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-09-2024",
  "Hora": "03:36:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-09-2024",
  "Hora": "12:10:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-10-2024",
  "Hora": "02:57:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-10-2024",
  "Hora": "11:03:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-11-2024",
  "Hora": "03:28:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-11-2024",
  "Hora": "11:02:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-12-2024",
  "Hora": "03:27:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-12-2024",
  "Hora": "11:01:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-13-2024",
  "Hora": "03:25:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-13-2024",
  "Hora": "11:00:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-15-2024",
  "Hora": "03:55:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21008682K",
  "Date": "04-15-2024",
  "Hora": "11:58:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-16-2024",
  "Hora": "03:38:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-16-2024",
  "Hora": "03:38:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-16-2024",
  "Hora": "10:58:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-16-2024",
  "Hora": "10:58:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-18-2024",
  "Hora": "03:43:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-18-2024",
  "Hora": "03:43:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-18-2024",
  "Hora": "12:08:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-19-2024",
  "Hora": "03:45:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-19-2024",
  "Hora": "03:45:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-19-2024",
  "Hora": "12:20:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-19-2024",
  "Hora": "12:20:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-20-2024",
  "Hora": "04:03:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-20-2024",
  "Hora": "04:03:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-20-2024",
  "Hora": "12:09:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-21-2024",
  "Hora": "03:47:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-21-2024",
  "Hora": "03:47:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-21-2024",
  "Hora": "12:05:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-21-2024",
  "Hora": "12:05:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-22-2024",
  "Hora": "03:46:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-22-2024",
  "Hora": "03:46:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-22-2024",
  "Hora": "12:12:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-22-2024",
  "Hora": "12:12:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-23-2024",
  "Hora": "03:49:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-23-2024",
  "Hora": "03:49:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-23-2024",
  "Hora": "12:06:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-23-2024",
  "Hora": "12:06:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-25-2024",
  "Hora": "02:58:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-25-2024",
  "Hora": "02:58:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-25-2024",
  "Hora": "11:02:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-25-2024",
  "Hora": "11:02:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-26-2024",
  "Hora": "02:29:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-26-2024",
  "Hora": "02:29:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-26-2024",
  "Hora": "11:10:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-26-2024",
  "Hora": "11:10:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-27-2024",
  "Hora": "03:19:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-27-2024",
  "Hora": "03:19:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-27-2024",
  "Hora": "11:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-27-2024",
  "Hora": "11:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-28-2024",
  "Hora": "02:55:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-28-2024",
  "Hora": "02:55:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-28-2024",
  "Hora": "11:03:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "03-28-2024",
  "Hora": "11:03:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-01-2024",
  "Hora": "04:19:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-01-2024",
  "Hora": "04:19:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-01-2024",
  "Hora": "13:05:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-01-2024",
  "Hora": "13:05:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-02-2024",
  "Hora": "03:48:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-02-2024",
  "Hora": "03:48:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-02-2024",
  "Hora": "11:35:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-02-2024",
  "Hora": "11:35:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-03-2024",
  "Hora": "03:35:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-03-2024",
  "Hora": "03:35:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-03-2024",
  "Hora": "12:12:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-03-2024",
  "Hora": "12:12:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-04-2024",
  "Hora": "03:26:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-04-2024",
  "Hora": "03:26:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-04-2024",
  "Hora": "12:05:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-04-2024",
  "Hora": "12:05:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-05-2024",
  "Hora": "03:24:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-05-2024",
  "Hora": "03:24:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-05-2024",
  "Hora": "12:09:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-05-2024",
  "Hora": "12:09:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-06-2024",
  "Hora": "03:24:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-06-2024",
  "Hora": "03:24:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-06-2024",
  "Hora": "11:03:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-06-2024",
  "Hora": "11:03:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-09-2024",
  "Hora": "03:34:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-09-2024",
  "Hora": "03:34:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-09-2024",
  "Hora": "12:07:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-09-2024",
  "Hora": "12:07:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-10-2024",
  "Hora": "03:24:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-10-2024",
  "Hora": "03:24:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-10-2024",
  "Hora": "12:01:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-10-2024",
  "Hora": "12:01:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-11-2024",
  "Hora": "03:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-11-2024",
  "Hora": "03:23:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-11-2024",
  "Hora": "12:03:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-11-2024",
  "Hora": "12:04:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-12-2024",
  "Hora": "03:25:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-12-2024",
  "Hora": "03:26:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-12-2024",
  "Hora": "12:05:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-12-2024",
  "Hora": "12:05:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-13-2024",
  "Hora": "03:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-13-2024",
  "Hora": "03:23:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-13-2024",
  "Hora": "10:57:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-13-2024",
  "Hora": "10:57:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-15-2024",
  "Hora": "02:34:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-15-2024",
  "Hora": "02:34:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-15-2024",
  "Hora": "11:07:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245989849,
  "Date": "04-15-2024",
  "Hora": "11:07:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-16-2024",
  "Hora": "05:43:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-16-2024",
  "Hora": "13:45:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-18-2024",
  "Hora": "05:43:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-18-2024",
  "Hora": "13:58:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-19-2024",
  "Hora": "05:44:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-19-2024",
  "Hora": "13:44:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-20-2024",
  "Hora": "05:48:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-20-2024",
  "Hora": "13:45:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-21-2024",
  "Hora": "05:40:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-21-2024",
  "Hora": "13:47:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-22-2024",
  "Hora": "05:41:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-22-2024",
  "Hora": "13:44:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-22-2024",
  "Hora": "22:31:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-23-2024",
  "Hora": "05:43:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-23-2024",
  "Hora": "13:44:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-25-2024",
  "Hora": "05:50:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-25-2024",
  "Hora": "13:58:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-26-2024",
  "Hora": "05:37:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-26-2024",
  "Hora": "13:44:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-27-2024",
  "Hora": "05:43:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-27-2024",
  "Hora": "13:43:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-28-2024",
  "Hora": "05:39:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "03-28-2024",
  "Hora": "13:44:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-01-2024",
  "Hora": "06:00:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-01-2024",
  "Hora": "13:59:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-02-2024",
  "Hora": "05:41:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-02-2024",
  "Hora": "13:46:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-03-2024",
  "Hora": "05:39:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-03-2024",
  "Hora": "13:48:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-04-2024",
  "Hora": "05:43:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-04-2024",
  "Hora": "13:45:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-08-2024",
  "Hora": "05:59:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-08-2024",
  "Hora": "13:59:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-09-2024",
  "Hora": "05:46:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-09-2024",
  "Hora": "13:45:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-10-2024",
  "Hora": "05:45:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-10-2024",
  "Hora": "13:44:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-11-2024",
  "Hora": "05:40:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-11-2024",
  "Hora": "13:44:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-12-2024",
  "Hora": "06:10:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-12-2024",
  "Hora": "13:45:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-13-2024",
  "Hora": "05:41:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-13-2024",
  "Hora": "13:53:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-15-2024",
  "Hora": "05:52:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167008178,
  "Date": "04-15-2024",
  "Hora": "13:59:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "03-24-2024",
  "Hora": "20:01:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "03-25-2024",
  "Hora": "02:12:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "03-25-2024",
  "Hora": "17:59:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "03-26-2024",
  "Hora": "03:27:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "03-26-2024",
  "Hora": "18:00:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "03-27-2024",
  "Hora": "03:38:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "03-27-2024",
  "Hora": "18:01:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "03-28-2024",
  "Hora": "03:34:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-01-2024",
  "Hora": "18:01:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-02-2024",
  "Hora": "03:44:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-02-2024",
  "Hora": "17:57:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-03-2024",
  "Hora": "03:38:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-03-2024",
  "Hora": "18:00:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-04-2024",
  "Hora": "03:20:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-04-2024",
  "Hora": "18:00:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-05-2024",
  "Hora": "03:19:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-05-2024",
  "Hora": "18:59:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-06-2024",
  "Hora": "03:18:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-08-2024",
  "Hora": "17:55:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-09-2024",
  "Hora": "03:36:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-09-2024",
  "Hora": "17:58:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-10-2024",
  "Hora": "03:19:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-10-2024",
  "Hora": "18:00:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-11-2024",
  "Hora": "03:34:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-11-2024",
  "Hora": "17:59:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-12-2024",
  "Hora": "03:14:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-12-2024",
  "Hora": "18:49:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-13-2024",
  "Hora": "03:05:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-14-2024",
  "Hora": "11:59:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199302582,
  "Date": "04-15-2024",
  "Hora": "18:06:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-16-2024",
  "Hora": "04:49:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-16-2024",
  "Hora": "11:31:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-18-2024",
  "Hora": "05:55:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-18-2024",
  "Hora": "14:00:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-19-2024",
  "Hora": "04:43:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-19-2024",
  "Hora": "13:03:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-20-2024",
  "Hora": "04:44:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-20-2024",
  "Hora": "13:00:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-21-2024",
  "Hora": "04:50:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-21-2024",
  "Hora": "13:01:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-22-2024",
  "Hora": "04:49:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-22-2024",
  "Hora": "13:01:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-23-2024",
  "Hora": "04:55:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-23-2024",
  "Hora": "12:00:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-25-2024",
  "Hora": "05:48:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-25-2024",
  "Hora": "14:01:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-26-2024",
  "Hora": "04:48:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-26-2024",
  "Hora": "13:00:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-27-2024",
  "Hora": "04:43:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "03-27-2024",
  "Hora": "13:01:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-01-2024",
  "Hora": "05:48:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-01-2024",
  "Hora": "13:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-02-2024",
  "Hora": "04:51:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-02-2024",
  "Hora": "13:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-03-2024",
  "Hora": "04:42:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-03-2024",
  "Hora": "13:01:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-04-2024",
  "Hora": "04:47:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-04-2024",
  "Hora": "13:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-05-2024",
  "Hora": "04:47:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-05-2024",
  "Hora": "13:00:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-06-2024",
  "Hora": "04:48:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-06-2024",
  "Hora": "12:30:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-08-2024",
  "Hora": "05:41:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-08-2024",
  "Hora": "14:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-09-2024",
  "Hora": "04:49:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-09-2024",
  "Hora": "13:00:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-10-2024",
  "Hora": "04:52:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-10-2024",
  "Hora": "13:02:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-11-2024",
  "Hora": "04:48:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-11-2024",
  "Hora": "13:01:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-12-2024",
  "Hora": "04:48:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-12-2024",
  "Hora": "13:00:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-13-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-13-2024",
  "Hora": "13:01:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-15-2024",
  "Hora": "05:40:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206279958,
  "Date": "04-15-2024",
  "Hora": "14:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-18-2024",
  "Hora": "11:19:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-18-2024",
  "Hora": "22:17:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-19-2024",
  "Hora": "10:52:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-19-2024",
  "Hora": "22:18:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-20-2024",
  "Hora": "10:35:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-20-2024",
  "Hora": "22:22:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-21-2024",
  "Hora": "10:29:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-21-2024",
  "Hora": "22:17:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-23-2024",
  "Hora": "12:34:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-23-2024",
  "Hora": "20:21:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-25-2024",
  "Hora": "14:51:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-26-2024",
  "Hora": "01:26:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-26-2024",
  "Hora": "15:04:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-27-2024",
  "Hora": "01:19:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-27-2024",
  "Hora": "14:47:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-28-2024",
  "Hora": "01:21:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-28-2024",
  "Hora": "15:17:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "03-28-2024",
  "Hora": "23:54:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-01-2024",
  "Hora": "10:57:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-01-2024",
  "Hora": "22:29:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-02-2024",
  "Hora": "11:04:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-02-2024",
  "Hora": "22:32:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-03-2024",
  "Hora": "11:09:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-03-2024",
  "Hora": "22:23:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-04-2024",
  "Hora": "11:10:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-04-2024",
  "Hora": "22:24:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-06-2024",
  "Hora": "12:31:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-06-2024",
  "Hora": "20:45:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-08-2024",
  "Hora": "15:21:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-09-2024",
  "Hora": "01:24:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-09-2024",
  "Hora": "15:14:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-10-2024",
  "Hora": "01:24:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-10-2024",
  "Hora": "15:02:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-11-2024",
  "Hora": "01:12:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-11-2024",
  "Hora": "15:08:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-12-2024",
  "Hora": "01:16:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-12-2024",
  "Hora": "11:23:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-12-2024",
  "Hora": "21:54:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-15-2024",
  "Hora": "12:07:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268568921,
  "Date": "04-15-2024",
  "Hora": "22:27:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206374543,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-16-2024",
  "Hora": "07:01:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-16-2024",
  "Hora": "13:07:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-18-2024",
  "Hora": "06:52:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-18-2024",
  "Hora": "15:04:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-19-2024",
  "Hora": "06:56:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-19-2024",
  "Hora": "15:04:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-20-2024",
  "Hora": "06:57:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-20-2024",
  "Hora": "15:01:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-21-2024",
  "Hora": "06:54:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-21-2024",
  "Hora": "15:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-22-2024",
  "Hora": "06:54:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-22-2024",
  "Hora": "15:00:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-23-2024",
  "Hora": "07:08:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-23-2024",
  "Hora": "15:01:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-25-2024",
  "Hora": "06:58:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-25-2024",
  "Hora": "15:01:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-26-2024",
  "Hora": "07:00:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-26-2024",
  "Hora": "15:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-27-2024",
  "Hora": "06:48:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-27-2024",
  "Hora": "13:08:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-28-2024",
  "Hora": "06:56:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "03-28-2024",
  "Hora": "15:01:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-01-2024",
  "Hora": "07:10:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-01-2024",
  "Hora": "15:16:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-02-2024",
  "Hora": "07:07:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-02-2024",
  "Hora": "15:04:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-03-2024",
  "Hora": "06:57:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-03-2024",
  "Hora": "15:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-04-2024",
  "Hora": "07:01:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-04-2024",
  "Hora": "15:03:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-05-2024",
  "Hora": "06:59:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-05-2024",
  "Hora": "15:01:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-06-2024",
  "Hora": "07:06:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-06-2024",
  "Hora": "14:40:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-08-2024",
  "Hora": "06:55:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-08-2024",
  "Hora": "15:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-09-2024",
  "Hora": "07:04:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-09-2024",
  "Hora": "15:01:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-10-2024",
  "Hora": "06:53:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-10-2024",
  "Hora": "15:01:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-11-2024",
  "Hora": "06:53:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-11-2024",
  "Hora": "15:00:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-12-2024",
  "Hora": "06:52:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-12-2024",
  "Hora": "15:02:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-13-2024",
  "Hora": "06:50:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-13-2024",
  "Hora": "14:30:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-15-2024",
  "Hora": "06:50:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163193159,
  "Date": "04-15-2024",
  "Hora": "15:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-18-2024",
  "Hora": "08:04:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-18-2024",
  "Hora": "17:50:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-19-2024",
  "Hora": "07:53:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-19-2024",
  "Hora": "17:53:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-20-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-20-2024",
  "Hora": "16:47:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-21-2024",
  "Hora": "08:04:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-21-2024",
  "Hora": "14:02:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-22-2024",
  "Hora": "08:03:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-22-2024",
  "Hora": "18:00:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-23-2024",
  "Hora": "06:01:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-23-2024",
  "Hora": "14:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-25-2024",
  "Hora": "08:05:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-25-2024",
  "Hora": "17:59:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-26-2024",
  "Hora": "08:06:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-26-2024",
  "Hora": "17:55:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-27-2024",
  "Hora": "07:59:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-27-2024",
  "Hora": "17:53:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-28-2024",
  "Hora": "07:57:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "03-28-2024",
  "Hora": "17:55:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-01-2024",
  "Hora": "08:04:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-01-2024",
  "Hora": "17:58:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-02-2024",
  "Hora": "07:55:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-02-2024",
  "Hora": "17:54:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-04-2024",
  "Hora": "08:02:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-04-2024",
  "Hora": "17:53:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-05-2024",
  "Hora": "08:27:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-05-2024",
  "Hora": "17:48:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-08-2024",
  "Hora": "09:00:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-08-2024",
  "Hora": "18:49:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-09-2024",
  "Hora": "09:00:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-09-2024",
  "Hora": "18:54:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-10-2024",
  "Hora": "09:04:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-10-2024",
  "Hora": "18:49:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-15-2024",
  "Hora": "09:02:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 137361345,
  "Date": "04-15-2024",
  "Hora": "17:57:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-19-2024",
  "Hora": "04:53:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-19-2024",
  "Hora": "14:30:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-20-2024",
  "Hora": "04:52:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-20-2024",
  "Hora": "14:31:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-21-2024",
  "Hora": "04:55:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-21-2024",
  "Hora": "14:30:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-22-2024",
  "Hora": "04:55:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-22-2024",
  "Hora": "14:30:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-25-2024",
  "Hora": "04:59:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-25-2024",
  "Hora": "14:33:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-27-2024",
  "Hora": "05:00:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-27-2024",
  "Hora": "14:32:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-28-2024",
  "Hora": "04:56:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "03-28-2024",
  "Hora": "14:30:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-01-2024",
  "Hora": "04:58:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-01-2024",
  "Hora": "14:31:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-03-2024",
  "Hora": "04:59:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-03-2024",
  "Hora": "14:30:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-04-2024",
  "Hora": "04:59:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-04-2024",
  "Hora": "14:31:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-05-2024",
  "Hora": "04:58:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-05-2024",
  "Hora": "14:31:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-06-2024",
  "Hora": "04:55:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-06-2024",
  "Hora": "14:30:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-08-2024",
  "Hora": "04:51:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-08-2024",
  "Hora": "14:32:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-09-2024",
  "Hora": "05:00:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-09-2024",
  "Hora": "14:30:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-10-2024",
  "Hora": "04:58:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-10-2024",
  "Hora": "14:30:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-11-2024",
  "Hora": "04:57:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-11-2024",
  "Hora": "14:31:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-12-2024",
  "Hora": "04:59:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-12-2024",
  "Hora": "14:31:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-15-2024",
  "Hora": "04:58:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187526833,
  "Date": "04-15-2024",
  "Hora": "14:31:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-16-2024",
  "Hora": "04:51:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-16-2024",
  "Hora": "12:15:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-18-2024",
  "Hora": "05:48:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-18-2024",
  "Hora": "14:05:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-19-2024",
  "Hora": "04:47:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-19-2024",
  "Hora": "13:06:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-19-2024",
  "Hora": "18:46:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-20-2024",
  "Hora": "13:08:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-21-2024",
  "Hora": "04:53:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-21-2024",
  "Hora": "13:05:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-22-2024",
  "Hora": "04:49:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-22-2024",
  "Hora": "13:09:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-23-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-23-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-23-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-23-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-23-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-23-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-23-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-23-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-23-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-23-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-23-2024",
  "Hora": "11:04:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-25-2024",
  "Hora": "05:49:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-25-2024",
  "Hora": "11:32:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-26-2024",
  "Hora": "04:50:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-26-2024",
  "Hora": "13:06:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-27-2024",
  "Hora": "04:49:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-27-2024",
  "Hora": "13:07:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-28-2024",
  "Hora": "04:56:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "03-28-2024",
  "Hora": "13:01:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-01-2024",
  "Hora": "05:52:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-01-2024",
  "Hora": "14:03:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-02-2024",
  "Hora": "04:50:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-02-2024",
  "Hora": "13:07:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-03-2024",
  "Hora": "04:49:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-03-2024",
  "Hora": "13:21:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-04-2024",
  "Hora": "04:50:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-04-2024",
  "Hora": "13:07:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-05-2024",
  "Hora": "04:49:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-05-2024",
  "Hora": "13:01:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-06-2024",
  "Hora": "04:49:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-06-2024",
  "Hora": "13:00:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-08-2024",
  "Hora": "05:50:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-08-2024",
  "Hora": "14:04:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-09-2024",
  "Hora": "04:55:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-09-2024",
  "Hora": "13:04:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-10-2024",
  "Hora": "04:48:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-10-2024",
  "Hora": "13:12:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-12-2024",
  "Hora": "04:51:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-12-2024",
  "Hora": "13:06:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-13-2024",
  "Hora": "04:49:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-13-2024",
  "Hora": "13:04:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-15-2024",
  "Hora": "05:48:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200704002,
  "Date": "04-15-2024",
  "Hora": "14:07:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-16-2024",
  "Hora": "08:08:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-16-2024",
  "Hora": "08:08:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-16-2024",
  "Hora": "14:03:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-18-2024",
  "Hora": "08:08:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-18-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-19-2024",
  "Hora": "07:42:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-19-2024",
  "Hora": "18:03:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-20-2024",
  "Hora": "08:05:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-20-2024",
  "Hora": "18:01:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-21-2024",
  "Hora": "07:50:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-21-2024",
  "Hora": "20:01:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-22-2024",
  "Hora": "07:28:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-22-2024",
  "Hora": "17:02:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-23-2024",
  "Hora": "08:01:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-23-2024",
  "Hora": "14:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-25-2024",
  "Hora": "08:13:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-25-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-26-2024",
  "Hora": "07:41:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-26-2024",
  "Hora": "20:01:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-27-2024",
  "Hora": "07:50:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-27-2024",
  "Hora": "18:02:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-28-2024",
  "Hora": "08:20:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-28-2024",
  "Hora": "23:38:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "03-28-2024",
  "Hora": "23:38:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-08-2024",
  "Hora": "07:27:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-08-2024",
  "Hora": "18:03:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-09-2024",
  "Hora": "07:26:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-09-2024",
  "Hora": "07:26:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-09-2024",
  "Hora": "18:02:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-10-2024",
  "Hora": "07:51:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-10-2024",
  "Hora": "18:00:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-11-2024",
  "Hora": "07:39:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-11-2024",
  "Hora": "18:01:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-12-2024",
  "Hora": "07:35:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-12-2024",
  "Hora": "17:02:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-13-2024",
  "Hora": "07:35:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-13-2024",
  "Hora": "14:02:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-13-2024",
  "Hora": "14:02:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-15-2024",
  "Hora": "07:38:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204684405,
  "Date": "04-15-2024",
  "Hora": "18:01:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-16-2024",
  "Hora": "08:43:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-16-2024",
  "Hora": "14:01:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-18-2024",
  "Hora": "08:23:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-18-2024",
  "Hora": "08:23:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-18-2024",
  "Hora": "18:05:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-19-2024",
  "Hora": "08:06:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-19-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-20-2024",
  "Hora": "08:07:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-20-2024",
  "Hora": "20:05:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-21-2024",
  "Hora": "08:02:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-21-2024",
  "Hora": "20:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-22-2024",
  "Hora": "08:28:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-22-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-23-2024",
  "Hora": "08:22:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-23-2024",
  "Hora": "14:03:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-25-2024",
  "Hora": "08:33:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-25-2024",
  "Hora": "20:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-26-2024",
  "Hora": "07:53:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-26-2024",
  "Hora": "20:02:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-27-2024",
  "Hora": "07:56:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-27-2024",
  "Hora": "18:01:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-28-2024",
  "Hora": "08:02:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-28-2024",
  "Hora": "08:02:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "03-28-2024",
  "Hora": "18:02:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-01-2024",
  "Hora": "08:07:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-01-2024",
  "Hora": "18:04:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-02-2024",
  "Hora": "08:08:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-02-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-03-2024",
  "Hora": "08:26:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-03-2024",
  "Hora": "18:05:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-04-2024",
  "Hora": "08:15:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-04-2024",
  "Hora": "18:09:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-05-2024",
  "Hora": "08:17:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-05-2024",
  "Hora": "17:05:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-06-2024",
  "Hora": "08:04:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-06-2024",
  "Hora": "14:01:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-08-2024",
  "Hora": "08:21:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-08-2024",
  "Hora": "18:03:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-09-2024",
  "Hora": "08:10:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-09-2024",
  "Hora": "08:10:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-09-2024",
  "Hora": "18:01:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-10-2024",
  "Hora": "07:54:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-10-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-11-2024",
  "Hora": "08:04:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-11-2024",
  "Hora": "18:04:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-12-2024",
  "Hora": "08:16:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-12-2024",
  "Hora": "17:04:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-15-2024",
  "Hora": "08:00:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195138400,
  "Date": "04-15-2024",
  "Hora": "18:03:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118419340,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-18-2024",
  "Hora": "12:51:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-18-2024",
  "Hora": "18:29:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-19-2024",
  "Hora": "13:25:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-19-2024",
  "Hora": "18:08:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-20-2024",
  "Hora": "12:50:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-20-2024",
  "Hora": "17:47:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-21-2024",
  "Hora": "12:49:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-21-2024",
  "Hora": "17:25:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-22-2024",
  "Hora": "13:04:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-22-2024",
  "Hora": "17:25:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-25-2024",
  "Hora": "13:05:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-25-2024",
  "Hora": "19:13:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-26-2024",
  "Hora": "13:08:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-26-2024",
  "Hora": "18:44:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-27-2024",
  "Hora": "12:56:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-27-2024",
  "Hora": "18:49:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-28-2024",
  "Hora": "13:46:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "03-28-2024",
  "Hora": "17:54:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-01-2024",
  "Hora": "12:56:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-01-2024",
  "Hora": "19:29:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-02-2024",
  "Hora": "13:02:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-02-2024",
  "Hora": "18:50:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-03-2024",
  "Hora": "12:55:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-03-2024",
  "Hora": "18:22:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-04-2024",
  "Hora": "12:58:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-04-2024",
  "Hora": "18:24:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-05-2024",
  "Hora": "13:07:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-05-2024",
  "Hora": "19:20:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-08-2024",
  "Hora": "13:08:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-08-2024",
  "Hora": "19:03:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-09-2024",
  "Hora": "12:56:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-09-2024",
  "Hora": "18:32:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-10-2024",
  "Hora": "12:55:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-10-2024",
  "Hora": "18:07:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-11-2024",
  "Hora": "13:00:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-11-2024",
  "Hora": "17:57:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-12-2024",
  "Hora": "12:55:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-12-2024",
  "Hora": "18:24:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-15-2024",
  "Hora": "13:00:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175015868,
  "Date": "04-15-2024",
  "Hora": "18:36:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-19-2024",
  "Hora": "07:42:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-19-2024",
  "Hora": "18:02:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-20-2024",
  "Hora": "07:26:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-20-2024",
  "Hora": "20:00:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-20-2024",
  "Hora": "20:00:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-21-2024",
  "Hora": "07:35:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-21-2024",
  "Hora": "20:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-22-2024",
  "Hora": "07:35:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-22-2024",
  "Hora": "17:01:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-23-2024",
  "Hora": "07:51:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-23-2024",
  "Hora": "14:01:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-25-2024",
  "Hora": "07:53:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-25-2024",
  "Hora": "18:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-26-2024",
  "Hora": "07:47:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-26-2024",
  "Hora": "20:00:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-27-2024",
  "Hora": "07:53:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-27-2024",
  "Hora": "18:43:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-27-2024",
  "Hora": "18:43:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-28-2024",
  "Hora": "07:32:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "03-28-2024",
  "Hora": "23:29:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-01-2024",
  "Hora": "10:44:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-01-2024",
  "Hora": "10:44:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-01-2024",
  "Hora": "18:01:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-02-2024",
  "Hora": "07:49:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-02-2024",
  "Hora": "18:01:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-03-2024",
  "Hora": "07:31:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-03-2024",
  "Hora": "07:31:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-03-2024",
  "Hora": "18:00:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-04-2024",
  "Hora": "07:36:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-04-2024",
  "Hora": "18:01:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-08-2024",
  "Hora": "07:50:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-08-2024",
  "Hora": "18:01:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-09-2024",
  "Hora": "07:26:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-09-2024",
  "Hora": "18:02:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-10-2024",
  "Hora": "07:45:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-10-2024",
  "Hora": "18:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-11-2024",
  "Hora": "07:47:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-11-2024",
  "Hora": "18:00:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-11-2024",
  "Hora": "18:00:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-12-2024",
  "Hora": "11:38:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-12-2024",
  "Hora": "17:01:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-12-2024",
  "Hora": "17:01:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-13-2024",
  "Hora": "07:36:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-13-2024",
  "Hora": "14:01:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-15-2024",
  "Hora": "07:56:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-15-2024",
  "Hora": "18:01:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204947090,
  "Date": "04-15-2024",
  "Hora": "18:01:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-16-2024",
  "Hora": "04:50:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-16-2024",
  "Hora": "11:30:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-18-2024",
  "Hora": "05:45:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-18-2024",
  "Hora": "14:00:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-19-2024",
  "Hora": "04:43:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-19-2024",
  "Hora": "13:03:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-20-2024",
  "Hora": "04:43:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-20-2024",
  "Hora": "13:01:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-21-2024",
  "Hora": "04:48:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-21-2024",
  "Hora": "13:00:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-22-2024",
  "Hora": "04:48:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-22-2024",
  "Hora": "13:00:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-23-2024",
  "Hora": "04:49:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-23-2024",
  "Hora": "12:00:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-25-2024",
  "Hora": "05:47:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-25-2024",
  "Hora": "12:23:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-25-2024",
  "Hora": "12:23:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-27-2024",
  "Hora": "04:43:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-27-2024",
  "Hora": "11:14:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-28-2024",
  "Hora": "04:59:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "03-28-2024",
  "Hora": "13:00:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-01-2024",
  "Hora": "05:44:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-01-2024",
  "Hora": "13:01:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-02-2024",
  "Hora": "05:11:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-02-2024",
  "Hora": "13:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-03-2024",
  "Hora": "04:43:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-03-2024",
  "Hora": "13:00:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-04-2024",
  "Hora": "04:45:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-04-2024",
  "Hora": "13:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-05-2024",
  "Hora": "04:46:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-05-2024",
  "Hora": "13:01:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-06-2024",
  "Hora": "04:48:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-06-2024",
  "Hora": "12:30:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-08-2024",
  "Hora": "05:41:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-08-2024",
  "Hora": "14:01:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-09-2024",
  "Hora": "04:47:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-09-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-10-2024",
  "Hora": "04:47:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-10-2024",
  "Hora": "13:01:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-11-2024",
  "Hora": "04:45:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-11-2024",
  "Hora": "13:00:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-12-2024",
  "Hora": "04:54:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-12-2024",
  "Hora": "13:00:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-13-2024",
  "Hora": "04:45:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-13-2024",
  "Hora": "13:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-15-2024",
  "Hora": "05:41:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 168197640,
  "Date": "04-15-2024",
  "Hora": "14:00:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-18-2024",
  "Hora": "12:40:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-18-2024",
  "Hora": "22:19:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-19-2024",
  "Hora": "12:47:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-19-2024",
  "Hora": "22:17:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-20-2024",
  "Hora": "13:51:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-20-2024",
  "Hora": "22:12:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-21-2024",
  "Hora": "12:30:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-21-2024",
  "Hora": "22:10:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-23-2024",
  "Hora": "12:26:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-23-2024",
  "Hora": "20:16:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-25-2024",
  "Hora": "14:52:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-26-2024",
  "Hora": "01:20:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-26-2024",
  "Hora": "14:40:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-27-2024",
  "Hora": "01:10:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-27-2024",
  "Hora": "15:51:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-28-2024",
  "Hora": "01:17:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-28-2024",
  "Hora": "15:52:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "03-28-2024",
  "Hora": "23:41:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-01-2024",
  "Hora": "12:58:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-01-2024",
  "Hora": "22:21:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-02-2024",
  "Hora": "12:43:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-02-2024",
  "Hora": "22:30:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-03-2024",
  "Hora": "12:41:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-03-2024",
  "Hora": "22:20:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-04-2024",
  "Hora": "12:37:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-04-2024",
  "Hora": "22:22:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-06-2024",
  "Hora": "12:40:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-06-2024",
  "Hora": "20:33:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-08-2024",
  "Hora": "15:45:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-09-2024",
  "Hora": "01:17:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-09-2024",
  "Hora": "15:44:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-10-2024",
  "Hora": "01:14:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-10-2024",
  "Hora": "15:58:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-11-2024",
  "Hora": "01:11:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-11-2024",
  "Hora": "15:48:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-12-2024",
  "Hora": "01:14:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-12-2024",
  "Hora": "12:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-12-2024",
  "Hora": "21:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-15-2024",
  "Hora": "08:19:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-15-2024",
  "Hora": "12:40:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176239166,
  "Date": "04-15-2024",
  "Hora": "22:16:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-16-2024",
  "Hora": "00:08:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-18-2024",
  "Hora": "15:46:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-19-2024",
  "Hora": "01:04:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-19-2024",
  "Hora": "15:37:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-20-2024",
  "Hora": "01:00:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-20-2024",
  "Hora": "15:38:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-21-2024",
  "Hora": "01:02:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-21-2024",
  "Hora": "15:38:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-22-2024",
  "Hora": "01:01:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-22-2024",
  "Hora": "16:23:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-23-2024",
  "Hora": "00:08:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-25-2024",
  "Hora": "15:58:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-26-2024",
  "Hora": "01:10:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-26-2024",
  "Hora": "15:56:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-27-2024",
  "Hora": "01:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-27-2024",
  "Hora": "15:41:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-28-2024",
  "Hora": "01:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-28-2024",
  "Hora": "15:56:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "03-28-2024",
  "Hora": "23:50:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-01-2024",
  "Hora": "15:53:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-02-2024",
  "Hora": "01:28:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-02-2024",
  "Hora": "16:06:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-03-2024",
  "Hora": "01:26:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-03-2024",
  "Hora": "16:00:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-04-2024",
  "Hora": "01:01:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-04-2024",
  "Hora": "15:59:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-05-2024",
  "Hora": "01:03:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-05-2024",
  "Hora": "15:51:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-05-2024",
  "Hora": "23:44:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-08-2024",
  "Hora": "15:47:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-09-2024",
  "Hora": "01:00:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-09-2024",
  "Hora": "15:43:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-10-2024",
  "Hora": "00:52:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-10-2024",
  "Hora": "15:54:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-11-2024",
  "Hora": "00:59:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180735372,
  "Date": "04-15-2024",
  "Hora": "15:32:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-16-2024",
  "Hora": "04:01:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-16-2024",
  "Hora": "12:45:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-18-2024",
  "Hora": "03:49:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-18-2024",
  "Hora": "12:59:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-18-2024",
  "Hora": "13:30:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-19-2024",
  "Hora": "03:19:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-19-2024",
  "Hora": "13:05:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-20-2024",
  "Hora": "03:50:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-20-2024",
  "Hora": "14:45:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-21-2024",
  "Hora": "03:29:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-21-2024",
  "Hora": "13:42:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-22-2024",
  "Hora": "03:44:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-22-2024",
  "Hora": "12:45:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-23-2024",
  "Hora": "03:56:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-23-2024",
  "Hora": "11:47:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-25-2024",
  "Hora": "03:22:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-25-2024",
  "Hora": "12:24:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-26-2024",
  "Hora": "03:38:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-26-2024",
  "Hora": "14:23:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-27-2024",
  "Hora": "03:42:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-27-2024",
  "Hora": "12:59:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-28-2024",
  "Hora": "03:37:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "03-28-2024",
  "Hora": "13:02:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-01-2024",
  "Hora": "02:09:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-01-2024",
  "Hora": "16:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-02-2024",
  "Hora": "02:47:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-02-2024",
  "Hora": "13:16:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-03-2024",
  "Hora": "03:37:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-03-2024",
  "Hora": "14:49:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-04-2024",
  "Hora": "03:21:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-04-2024",
  "Hora": "13:32:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-05-2024",
  "Hora": "03:24:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-05-2024",
  "Hora": "14:37:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-06-2024",
  "Hora": "03:49:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-06-2024",
  "Hora": "12:57:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-08-2024",
  "Hora": "03:22:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-08-2024",
  "Hora": "13:06:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-09-2024",
  "Hora": "03:06:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-09-2024",
  "Hora": "13:10:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-10-2024",
  "Hora": "04:04:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-10-2024",
  "Hora": "12:34:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-11-2024",
  "Hora": "03:45:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-11-2024",
  "Hora": "13:23:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-12-2024",
  "Hora": "03:40:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-12-2024",
  "Hora": "14:04:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-13-2024",
  "Hora": "04:08:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-13-2024",
  "Hora": "12:46:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "13881145K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-18-2024",
  "Hora": "08:29:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-18-2024",
  "Hora": "18:01:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-19-2024",
  "Hora": "08:05:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-19-2024",
  "Hora": "18:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-20-2024",
  "Hora": "08:33:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-20-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-21-2024",
  "Hora": "08:30:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-21-2024",
  "Hora": "18:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-22-2024",
  "Hora": "08:37:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-22-2024",
  "Hora": "18:00:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-25-2024",
  "Hora": "08:30:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-25-2024",
  "Hora": "18:00:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-26-2024",
  "Hora": "08:31:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-26-2024",
  "Hora": "18:01:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-27-2024",
  "Hora": "08:30:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-27-2024",
  "Hora": "18:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-28-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "03-28-2024",
  "Hora": "18:00:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-01-2024",
  "Hora": "08:29:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-01-2024",
  "Hora": "18:01:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-02-2024",
  "Hora": "09:15:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-02-2024",
  "Hora": "18:56:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-03-2024",
  "Hora": "08:29:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-03-2024",
  "Hora": "18:00:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-04-2024",
  "Hora": "08:29:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-04-2024",
  "Hora": "18:00:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-05-2024",
  "Hora": "08:26:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-05-2024",
  "Hora": "18:18:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-08-2024",
  "Hora": "08:32:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-08-2024",
  "Hora": "18:04:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-09-2024",
  "Hora": "08:31:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-09-2024",
  "Hora": "18:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-10-2024",
  "Hora": "08:31:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-10-2024",
  "Hora": "18:02:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-11-2024",
  "Hora": "08:28:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-11-2024",
  "Hora": "18:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-12-2024",
  "Hora": "08:30:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-12-2024",
  "Hora": "18:01:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 163400081,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-16-2024",
  "Hora": "08:02:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-16-2024",
  "Hora": "14:02:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-18-2024",
  "Hora": "08:17:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-18-2024",
  "Hora": "19:50:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-19-2024",
  "Hora": "08:08:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-19-2024",
  "Hora": "18:06:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-20-2024",
  "Hora": "08:10:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-20-2024",
  "Hora": "20:02:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-21-2024",
  "Hora": "08:21:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-21-2024",
  "Hora": "18:04:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-22-2024",
  "Hora": "08:18:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-22-2024",
  "Hora": "17:02:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-23-2024",
  "Hora": "07:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-23-2024",
  "Hora": "07:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-23-2024",
  "Hora": "07:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-23-2024",
  "Hora": "07:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-23-2024",
  "Hora": "07:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-23-2024",
  "Hora": "07:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-23-2024",
  "Hora": "07:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-23-2024",
  "Hora": "07:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-23-2024",
  "Hora": "07:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-23-2024",
  "Hora": "07:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-23-2024",
  "Hora": "14:01:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-25-2024",
  "Hora": "08:19:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-25-2024",
  "Hora": "19:09:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-26-2024",
  "Hora": "08:17:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-26-2024",
  "Hora": "17:59:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-28-2024",
  "Hora": "08:24:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "03-28-2024",
  "Hora": "23:40:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-02-2024",
  "Hora": "08:04:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-02-2024",
  "Hora": "18:02:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-03-2024",
  "Hora": "08:15:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-03-2024",
  "Hora": "18:02:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-04-2024",
  "Hora": "08:19:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-04-2024",
  "Hora": "18:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-05-2024",
  "Hora": "08:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-05-2024",
  "Hora": "17:01:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-06-2024",
  "Hora": "08:03:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-06-2024",
  "Hora": "14:02:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-08-2024",
  "Hora": "08:31:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-08-2024",
  "Hora": "18:02:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-09-2024",
  "Hora": "08:15:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-09-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-10-2024",
  "Hora": "08:08:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-10-2024",
  "Hora": "18:03:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-11-2024",
  "Hora": "08:07:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-11-2024",
  "Hora": "18:17:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-12-2024",
  "Hora": "08:28:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-12-2024",
  "Hora": "17:02:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-15-2024",
  "Hora": "08:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178752510,
  "Date": "04-15-2024",
  "Hora": "18:02:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-16-2024",
  "Hora": "05:55:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-16-2024",
  "Hora": "14:00:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-18-2024",
  "Hora": "08:33:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-18-2024",
  "Hora": "17:59:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-19-2024",
  "Hora": "08:34:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-19-2024",
  "Hora": "17:59:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-20-2024",
  "Hora": "08:34:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-20-2024",
  "Hora": "14:20:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-21-2024",
  "Hora": "08:49:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-21-2024",
  "Hora": "14:24:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-23-2024",
  "Hora": "06:00:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-23-2024",
  "Hora": "14:06:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-25-2024",
  "Hora": "08:51:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-25-2024",
  "Hora": "18:00:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-26-2024",
  "Hora": "06:00:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-26-2024",
  "Hora": "17:59:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-27-2024",
  "Hora": "06:10:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "03-27-2024",
  "Hora": "17:59:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-01-2024",
  "Hora": "08:48:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-01-2024",
  "Hora": "17:59:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-02-2024",
  "Hora": "08:40:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-02-2024",
  "Hora": "17:59:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-04-2024",
  "Hora": "08:20:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-04-2024",
  "Hora": "17:59:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-05-2024",
  "Hora": "08:28:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-05-2024",
  "Hora": "17:59:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-06-2024",
  "Hora": "06:11:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-06-2024",
  "Hora": "14:03:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-08-2024",
  "Hora": "08:40:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-08-2024",
  "Hora": "17:58:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-09-2024",
  "Hora": "08:35:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-09-2024",
  "Hora": "17:59:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-10-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-10-2024",
  "Hora": "17:59:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-15-2024",
  "Hora": "08:40:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189269617,
  "Date": "04-15-2024",
  "Hora": "17:59:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260072153,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-18-2024",
  "Hora": "15:25:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-19-2024",
  "Hora": "01:19:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-19-2024",
  "Hora": "15:15:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-20-2024",
  "Hora": "01:05:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-20-2024",
  "Hora": "15:13:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-21-2024",
  "Hora": "01:06:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-21-2024",
  "Hora": "15:21:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-22-2024",
  "Hora": "01:11:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-22-2024",
  "Hora": "10:54:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-22-2024",
  "Hora": "21:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-25-2024",
  "Hora": "10:47:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-25-2024",
  "Hora": "22:17:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-26-2024",
  "Hora": "11:01:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-26-2024",
  "Hora": "22:12:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-27-2024",
  "Hora": "11:09:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-27-2024",
  "Hora": "22:09:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-28-2024",
  "Hora": "10:54:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "03-28-2024",
  "Hora": "21:45:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-01-2024",
  "Hora": "14:29:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-02-2024",
  "Hora": "01:43:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-02-2024",
  "Hora": "15:20:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-03-2024",
  "Hora": "01:33:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-03-2024",
  "Hora": "15:32:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-04-2024",
  "Hora": "01:20:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-04-2024",
  "Hora": "15:27:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-05-2024",
  "Hora": "01:17:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-05-2024",
  "Hora": "10:48:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-05-2024",
  "Hora": "21:35:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-08-2024",
  "Hora": "10:39:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-08-2024",
  "Hora": "22:17:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-09-2024",
  "Hora": "10:35:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-09-2024",
  "Hora": "22:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-10-2024",
  "Hora": "10:39:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-10-2024",
  "Hora": "22:02:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-11-2024",
  "Hora": "11:12:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-11-2024",
  "Hora": "21:59:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-13-2024",
  "Hora": "21:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-15-2024",
  "Hora": "08:14:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265669883,
  "Date": "04-15-2024",
  "Hora": "18:03:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-18-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-18-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-19-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-19-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-20-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-20-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-21-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-21-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-22-2024",
  "Hora": "08:34:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-22-2024",
  "Hora": "10:27:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-22-2024",
  "Hora": "14:07:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-22-2024",
  "Hora": "15:07:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-22-2024",
  "Hora": "17:00:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-23-2024",
  "Hora": "07:54:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-23-2024",
  "Hora": "15:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-25-2024",
  "Hora": "06:50:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-25-2024",
  "Hora": "15:01:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-25-2024",
  "Hora": "16:02:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-25-2024",
  "Hora": "17:00:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-26-2024",
  "Hora": "07:09:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-26-2024",
  "Hora": "14:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-26-2024",
  "Hora": "15:29:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-26-2024",
  "Hora": "17:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-27-2024",
  "Hora": "07:08:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-27-2024",
  "Hora": "14:57:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-27-2024",
  "Hora": "15:58:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-27-2024",
  "Hora": "17:00:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-28-2024",
  "Hora": "07:00:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-28-2024",
  "Hora": "13:34:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-28-2024",
  "Hora": "14:35:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "03-28-2024",
  "Hora": "17:07:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-01-2024",
  "Hora": "06:38:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-01-2024",
  "Hora": "15:02:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-01-2024",
  "Hora": "16:03:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-01-2024",
  "Hora": "17:02:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-02-2024",
  "Hora": "07:10:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-02-2024",
  "Hora": "13:46:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-02-2024",
  "Hora": "14:49:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-02-2024",
  "Hora": "17:00:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-03-2024",
  "Hora": "06:56:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-03-2024",
  "Hora": "13:23:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-03-2024",
  "Hora": "14:23:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-03-2024",
  "Hora": "17:01:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-04-2024",
  "Hora": "07:16:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-04-2024",
  "Hora": "14:03:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-04-2024",
  "Hora": "14:48:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-04-2024",
  "Hora": "17:00:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-05-2024",
  "Hora": "07:37:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-05-2024",
  "Hora": "14:31:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-05-2024",
  "Hora": "15:29:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-05-2024",
  "Hora": "17:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-06-2024",
  "Hora": "07:46:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-06-2024",
  "Hora": "15:00:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-08-2024",
  "Hora": "06:46:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-08-2024",
  "Hora": "14:30:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-08-2024",
  "Hora": "15:32:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-08-2024",
  "Hora": "17:02:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-09-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-09-2024",
  "Hora": "07:12:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-09-2024",
  "Hora": "07:12:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-09-2024",
  "Hora": "14:11:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-09-2024",
  "Hora": "15:10:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-09-2024",
  "Hora": "17:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-10-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-10-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-15-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195847762,
  "Date": "04-15-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-16-2024",
  "Hora": "05:25:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-16-2024",
  "Hora": "11:49:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-18-2024",
  "Hora": "05:53:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-18-2024",
  "Hora": "13:00:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-19-2024",
  "Hora": "05:21:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-19-2024",
  "Hora": "13:31:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-20-2024",
  "Hora": "05:23:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-20-2024",
  "Hora": "13:30:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-21-2024",
  "Hora": "05:20:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-21-2024",
  "Hora": "13:30:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-22-2024",
  "Hora": "05:25:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-22-2024",
  "Hora": "13:31:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-23-2024",
  "Hora": "05:19:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-23-2024",
  "Hora": "05:19:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-23-2024",
  "Hora": "05:19:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-23-2024",
  "Hora": "05:19:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-23-2024",
  "Hora": "05:19:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-23-2024",
  "Hora": "05:19:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-23-2024",
  "Hora": "05:19:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-23-2024",
  "Hora": "05:19:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-23-2024",
  "Hora": "05:19:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-23-2024",
  "Hora": "05:19:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-23-2024",
  "Hora": "11:09:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-25-2024",
  "Hora": "05:51:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-25-2024",
  "Hora": "13:02:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-26-2024",
  "Hora": "05:17:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-26-2024",
  "Hora": "13:31:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-27-2024",
  "Hora": "05:19:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-27-2024",
  "Hora": "13:31:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-28-2024",
  "Hora": "05:16:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "03-28-2024",
  "Hora": "13:31:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-01-2024",
  "Hora": "05:44:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-01-2024",
  "Hora": "14:01:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-02-2024",
  "Hora": "05:17:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-02-2024",
  "Hora": "13:31:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-03-2024",
  "Hora": "05:18:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-03-2024",
  "Hora": "13:37:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-04-2024",
  "Hora": "05:17:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-04-2024",
  "Hora": "13:30:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-05-2024",
  "Hora": "05:22:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-05-2024",
  "Hora": "13:31:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-06-2024",
  "Hora": "05:18:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-06-2024",
  "Hora": "12:30:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-08-2024",
  "Hora": "05:50:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-08-2024",
  "Hora": "14:01:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-09-2024",
  "Hora": "05:16:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-09-2024",
  "Hora": "13:31:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-10-2024",
  "Hora": "05:25:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-10-2024",
  "Hora": "13:31:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-11-2024",
  "Hora": "05:19:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-11-2024",
  "Hora": "13:30:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-12-2024",
  "Hora": "05:18:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-12-2024",
  "Hora": "10:01:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-15-2024",
  "Hora": "05:49:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 194548842,
  "Date": "04-15-2024",
  "Hora": "13:01:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "03-16-2024",
  "Hora": "04:49:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "03-16-2024",
  "Hora": "12:00:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "03-18-2024",
  "Hora": "05:55:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "03-18-2024",
  "Hora": "14:00:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-01-2024",
  "Hora": "06:00:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-01-2024",
  "Hora": "13:03:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-02-2024",
  "Hora": "03:56:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-02-2024",
  "Hora": "12:02:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-03-2024",
  "Hora": "03:59:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-03-2024",
  "Hora": "12:02:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-04-2024",
  "Hora": "05:02:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-04-2024",
  "Hora": "12:01:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-05-2024",
  "Hora": "04:54:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-05-2024",
  "Hora": "12:00:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-06-2024",
  "Hora": "04:51:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-06-2024",
  "Hora": "12:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-08-2024",
  "Hora": "06:10:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-08-2024",
  "Hora": "14:00:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-09-2024",
  "Hora": "03:48:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-09-2024",
  "Hora": "12:00:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-10-2024",
  "Hora": "04:57:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-10-2024",
  "Hora": "12:06:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-11-2024",
  "Hora": "04:57:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-11-2024",
  "Hora": "12:59:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-12-2024",
  "Hora": "04:58:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-12-2024",
  "Hora": "13:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-13-2024",
  "Hora": "04:56:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-13-2024",
  "Hora": "13:01:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-15-2024",
  "Hora": "05:56:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205527516,
  "Date": "04-15-2024",
  "Hora": "14:01:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191099680,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-16-2024",
  "Hora": "05:51:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-16-2024",
  "Hora": "13:47:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-18-2024",
  "Hora": "06:11:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-18-2024",
  "Hora": "14:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-19-2024",
  "Hora": "05:48:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-19-2024",
  "Hora": "13:46:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-20-2024",
  "Hora": "05:49:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-20-2024",
  "Hora": "13:44:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-21-2024",
  "Hora": "05:46:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-21-2024",
  "Hora": "13:47:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-22-2024",
  "Hora": "05:42:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-22-2024",
  "Hora": "13:44:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-23-2024",
  "Hora": "05:42:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-23-2024",
  "Hora": "13:48:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-25-2024",
  "Hora": "05:50:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-25-2024",
  "Hora": "14:01:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-26-2024",
  "Hora": "05:37:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-26-2024",
  "Hora": "13:48:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-27-2024",
  "Hora": "05:44:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-27-2024",
  "Hora": "13:46:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-28-2024",
  "Hora": "05:58:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "03-28-2024",
  "Hora": "13:46:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "04-01-2024",
  "Hora": "06:00:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "04-01-2024",
  "Hora": "14:01:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "04-02-2024",
  "Hora": "05:46:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "04-02-2024",
  "Hora": "09:02:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "04-03-2024",
  "Hora": "06:00:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "04-03-2024",
  "Hora": "13:47:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "04-04-2024",
  "Hora": "05:44:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "04-04-2024",
  "Hora": "13:44:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184380900,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-16-2024",
  "Hora": "05:59:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-16-2024",
  "Hora": "14:01:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-18-2024",
  "Hora": "07:58:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-18-2024",
  "Hora": "18:00:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-19-2024",
  "Hora": "08:34:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-19-2024",
  "Hora": "18:00:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-20-2024",
  "Hora": "08:07:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-20-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-21-2024",
  "Hora": "08:07:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-21-2024",
  "Hora": "17:59:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-22-2024",
  "Hora": "08:08:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-22-2024",
  "Hora": "18:00:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-23-2024",
  "Hora": "06:00:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-23-2024",
  "Hora": "16:09:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-25-2024",
  "Hora": "08:06:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-25-2024",
  "Hora": "18:01:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-26-2024",
  "Hora": "08:07:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-26-2024",
  "Hora": "17:52:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-27-2024",
  "Hora": "08:34:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-27-2024",
  "Hora": "17:59:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-28-2024",
  "Hora": "07:59:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "03-28-2024",
  "Hora": "18:00:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-08-2024",
  "Hora": "08:05:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-08-2024",
  "Hora": "18:01:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-09-2024",
  "Hora": "08:03:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-09-2024",
  "Hora": "17:59:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-10-2024",
  "Hora": "08:29:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-10-2024",
  "Hora": "17:58:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-12-2024",
  "Hora": "08:08:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-12-2024",
  "Hora": "17:58:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-13-2024",
  "Hora": "05:58:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-13-2024",
  "Hora": "14:08:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-15-2024",
  "Hora": "08:04:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 152310676,
  "Date": "04-15-2024",
  "Hora": "17:59:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-16-2024",
  "Hora": "05:07:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-16-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-18-2024",
  "Hora": "06:05:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-18-2024",
  "Hora": "13:29:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-19-2024",
  "Hora": "05:06:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-19-2024",
  "Hora": "13:01:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-20-2024",
  "Hora": "05:13:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-20-2024",
  "Hora": "13:00:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-22-2024",
  "Hora": "05:15:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-22-2024",
  "Hora": "13:07:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-23-2024",
  "Hora": "05:09:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-23-2024",
  "Hora": "05:09:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-23-2024",
  "Hora": "05:09:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-23-2024",
  "Hora": "05:09:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-23-2024",
  "Hora": "05:09:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-23-2024",
  "Hora": "05:09:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-23-2024",
  "Hora": "05:09:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-23-2024",
  "Hora": "05:09:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-23-2024",
  "Hora": "05:09:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-23-2024",
  "Hora": "05:09:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-23-2024",
  "Hora": "13:00:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-25-2024",
  "Hora": "06:08:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-25-2024",
  "Hora": "14:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-26-2024",
  "Hora": "05:10:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-26-2024",
  "Hora": "13:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-27-2024",
  "Hora": "05:12:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-27-2024",
  "Hora": "12:58:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-28-2024",
  "Hora": "05:17:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "03-28-2024",
  "Hora": "11:15:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-01-2024",
  "Hora": "06:13:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-01-2024",
  "Hora": "14:04:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-02-2024",
  "Hora": "05:03:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-02-2024",
  "Hora": "13:05:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-03-2024",
  "Hora": "05:04:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-03-2024",
  "Hora": "13:04:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-04-2024",
  "Hora": "05:12:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-04-2024",
  "Hora": "13:03:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-05-2024",
  "Hora": "05:13:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-05-2024",
  "Hora": "13:06:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-06-2024",
  "Hora": "05:13:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-06-2024",
  "Hora": "12:57:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-09-2024",
  "Hora": "05:06:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-09-2024",
  "Hora": "13:05:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-10-2024",
  "Hora": "05:10:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-10-2024",
  "Hora": "13:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-11-2024",
  "Hora": "05:08:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-11-2024",
  "Hora": "13:01:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-12-2024",
  "Hora": "05:04:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-12-2024",
  "Hora": "12:59:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-13-2024",
  "Hora": "05:12:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-13-2024",
  "Hora": "13:00:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-15-2024",
  "Hora": "06:04:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177386960,
  "Date": "04-15-2024",
  "Hora": "13:58:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-16-2024",
  "Hora": "04:02:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-16-2024",
  "Hora": "11:01:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-18-2024",
  "Hora": "04:09:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-18-2024",
  "Hora": "12:03:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-19-2024",
  "Hora": "04:12:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-19-2024",
  "Hora": "12:18:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-20-2024",
  "Hora": "04:20:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-20-2024",
  "Hora": "12:01:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-21-2024",
  "Hora": "04:33:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-21-2024",
  "Hora": "12:03:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-22-2024",
  "Hora": "04:10:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-22-2024",
  "Hora": "12:18:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-23-2024",
  "Hora": "05:14:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-23-2024",
  "Hora": "12:04:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-25-2024",
  "Hora": "04:11:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-25-2024",
  "Hora": "12:02:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-26-2024",
  "Hora": "04:13:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-26-2024",
  "Hora": "12:02:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-27-2024",
  "Hora": "04:10:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-27-2024",
  "Hora": "12:08:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-28-2024",
  "Hora": "04:01:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "03-28-2024",
  "Hora": "11:55:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-01-2024",
  "Hora": "04:19:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-01-2024",
  "Hora": "13:14:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-02-2024",
  "Hora": "04:14:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-02-2024",
  "Hora": "12:09:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-04-2024",
  "Hora": "04:40:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-04-2024",
  "Hora": "12:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-05-2024",
  "Hora": "04:20:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-05-2024",
  "Hora": "12:07:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-06-2024",
  "Hora": "04:07:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-06-2024",
  "Hora": "11:04:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-08-2024",
  "Hora": "02:22:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-08-2024",
  "Hora": "11:05:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-09-2024",
  "Hora": "02:24:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-09-2024",
  "Hora": "11:06:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-10-2024",
  "Hora": "04:36:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-10-2024",
  "Hora": "11:02:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-11-2024",
  "Hora": "02:43:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-11-2024",
  "Hora": "11:03:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-12-2024",
  "Hora": "02:26:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-12-2024",
  "Hora": "11:00:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-13-2024",
  "Hora": "03:26:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-13-2024",
  "Hora": "11:00:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-15-2024",
  "Hora": "03:56:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211685441,
  "Date": "04-15-2024",
  "Hora": "11:58:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-16-2024",
  "Hora": "09:09:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-16-2024",
  "Hora": "17:57:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-18-2024",
  "Hora": "09:12:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-18-2024",
  "Hora": "16:35:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-19-2024",
  "Hora": "09:22:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-19-2024",
  "Hora": "16:51:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-20-2024",
  "Hora": "09:22:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-20-2024",
  "Hora": "17:42:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-21-2024",
  "Hora": "09:24:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-21-2024",
  "Hora": "16:53:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-22-2024",
  "Hora": "09:14:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-22-2024",
  "Hora": "17:16:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-23-2024",
  "Hora": "09:12:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-23-2024",
  "Hora": "16:12:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-25-2024",
  "Hora": "09:19:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-25-2024",
  "Hora": "17:20:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-26-2024",
  "Hora": "09:17:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-26-2024",
  "Hora": "17:12:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-27-2024",
  "Hora": "09:23:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-27-2024",
  "Hora": "16:59:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-28-2024",
  "Hora": "11:19:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "03-28-2024",
  "Hora": "16:57:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-01-2024",
  "Hora": "08:22:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-01-2024",
  "Hora": "19:03:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-02-2024",
  "Hora": "08:23:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-02-2024",
  "Hora": "18:06:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-03-2024",
  "Hora": "09:13:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-03-2024",
  "Hora": "17:53:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-04-2024",
  "Hora": "09:16:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-04-2024",
  "Hora": "17:46:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-05-2024",
  "Hora": "09:16:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-05-2024",
  "Hora": "18:06:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-06-2024",
  "Hora": "09:10:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-06-2024",
  "Hora": "16:14:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-08-2024",
  "Hora": "09:14:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-08-2024",
  "Hora": "17:03:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-09-2024",
  "Hora": "09:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-09-2024",
  "Hora": "17:07:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-10-2024",
  "Hora": "09:17:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-10-2024",
  "Hora": "18:03:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-11-2024",
  "Hora": "09:16:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-11-2024",
  "Hora": "17:50:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-12-2024",
  "Hora": "09:14:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-12-2024",
  "Hora": "16:44:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-13-2024",
  "Hora": "09:06:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-13-2024",
  "Hora": "15:52:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-15-2024",
  "Hora": "09:21:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 170512561,
  "Date": "04-15-2024",
  "Hora": "16:46:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-18-2024",
  "Hora": "16:53:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-19-2024",
  "Hora": "01:27:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-19-2024",
  "Hora": "16:53:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-20-2024",
  "Hora": "01:17:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-20-2024",
  "Hora": "16:58:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-21-2024",
  "Hora": "01:18:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-21-2024",
  "Hora": "16:55:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-22-2024",
  "Hora": "01:20:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-22-2024",
  "Hora": "17:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-23-2024",
  "Hora": "00:21:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-25-2024",
  "Hora": "16:59:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-26-2024",
  "Hora": "01:26:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-26-2024",
  "Hora": "16:57:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-27-2024",
  "Hora": "01:20:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-27-2024",
  "Hora": "16:59:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-28-2024",
  "Hora": "01:17:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-28-2024",
  "Hora": "17:07:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "03-29-2024",
  "Hora": "00:04:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-01-2024",
  "Hora": "16:47:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-02-2024",
  "Hora": "01:43:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-02-2024",
  "Hora": "16:45:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-03-2024",
  "Hora": "01:34:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-03-2024",
  "Hora": "01:34:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-03-2024",
  "Hora": "16:51:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-04-2024",
  "Hora": "01:25:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-04-2024",
  "Hora": "16:51:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-05-2024",
  "Hora": "01:24:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-05-2024",
  "Hora": "16:58:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-06-2024",
  "Hora": "00:04:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-08-2024",
  "Hora": "16:44:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-09-2024",
  "Hora": "01:25:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-09-2024",
  "Hora": "16:49:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-10-2024",
  "Hora": "01:24:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-10-2024",
  "Hora": "16:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-11-2024",
  "Hora": "01:17:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-11-2024",
  "Hora": "16:57:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-12-2024",
  "Hora": "01:16:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-12-2024",
  "Hora": "16:52:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-13-2024",
  "Hora": "00:21:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 263773845,
  "Date": "04-15-2024",
  "Hora": "16:56:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-16-2024",
  "Hora": "09:28:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-16-2024",
  "Hora": "17:57:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-18-2024",
  "Hora": "09:31:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-18-2024",
  "Hora": "16:32:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-19-2024",
  "Hora": "09:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-19-2024",
  "Hora": "16:49:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-20-2024",
  "Hora": "09:41:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-20-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-21-2024",
  "Hora": "09:20:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-21-2024",
  "Hora": "16:52:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-22-2024",
  "Hora": "08:56:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-22-2024",
  "Hora": "17:15:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-23-2024",
  "Hora": "09:25:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-23-2024",
  "Hora": "16:09:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-25-2024",
  "Hora": "09:07:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-25-2024",
  "Hora": "17:24:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-26-2024",
  "Hora": "09:32:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-26-2024",
  "Hora": "17:14:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-27-2024",
  "Hora": "09:29:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-27-2024",
  "Hora": "16:59:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-28-2024",
  "Hora": "11:29:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "03-28-2024",
  "Hora": "16:54:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-01-2024",
  "Hora": "08:14:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-01-2024",
  "Hora": "19:02:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-02-2024",
  "Hora": "08:22:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-02-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-03-2024",
  "Hora": "09:30:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-03-2024",
  "Hora": "17:53:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-04-2024",
  "Hora": "09:24:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-04-2024",
  "Hora": "17:44:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-05-2024",
  "Hora": "09:23:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-05-2024",
  "Hora": "18:04:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-06-2024",
  "Hora": "09:32:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-06-2024",
  "Hora": "16:09:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-08-2024",
  "Hora": "08:06:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-08-2024",
  "Hora": "17:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-09-2024",
  "Hora": "08:13:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-09-2024",
  "Hora": "17:04:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-10-2024",
  "Hora": "09:29:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-10-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-11-2024",
  "Hora": "09:26:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-11-2024",
  "Hora": "17:48:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-12-2024",
  "Hora": "09:29:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-12-2024",
  "Hora": "16:43:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-13-2024",
  "Hora": "09:29:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-13-2024",
  "Hora": "15:47:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-15-2024",
  "Hora": "09:36:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165732952,
  "Date": "04-15-2024",
  "Hora": "16:43:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-16-2024",
  "Hora": "00:04:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-18-2024",
  "Hora": "15:23:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-19-2024",
  "Hora": "01:08:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-19-2024",
  "Hora": "15:28:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-20-2024",
  "Hora": "00:53:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-20-2024",
  "Hora": "15:32:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-21-2024",
  "Hora": "00:55:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-21-2024",
  "Hora": "16:05:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-22-2024",
  "Hora": "00:59:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-22-2024",
  "Hora": "15:25:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-23-2024",
  "Hora": "00:04:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-25-2024",
  "Hora": "15:55:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-26-2024",
  "Hora": "01:10:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-26-2024",
  "Hora": "15:34:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-27-2024",
  "Hora": "01:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-27-2024",
  "Hora": "15:36:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-28-2024",
  "Hora": "00:58:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-28-2024",
  "Hora": "15:19:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "03-28-2024",
  "Hora": "23:46:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-01-2024",
  "Hora": "15:32:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-02-2024",
  "Hora": "01:22:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-02-2024",
  "Hora": "15:29:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-02-2024",
  "Hora": "21:26:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-03-2024",
  "Hora": "15:28:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-04-2024",
  "Hora": "01:03:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-04-2024",
  "Hora": "16:02:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-05-2024",
  "Hora": "01:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-05-2024",
  "Hora": "15:33:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-05-2024",
  "Hora": "23:44:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-08-2024",
  "Hora": "15:26:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-09-2024",
  "Hora": "01:00:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-09-2024",
  "Hora": "15:30:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-10-2024",
  "Hora": "00:53:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-10-2024",
  "Hora": "15:50:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-11-2024",
  "Hora": "00:59:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-11-2024",
  "Hora": "15:32:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-12-2024",
  "Hora": "00:32:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-12-2024",
  "Hora": "15:27:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-13-2024",
  "Hora": "00:00:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 158455161,
  "Date": "04-15-2024",
  "Hora": "15:27:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-18-2024",
  "Hora": "08:41:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-18-2024",
  "Hora": "18:13:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-19-2024",
  "Hora": "08:46:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-19-2024",
  "Hora": "18:04:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-20-2024",
  "Hora": "08:35:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-20-2024",
  "Hora": "18:17:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-21-2024",
  "Hora": "09:08:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-21-2024",
  "Hora": "18:01:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-22-2024",
  "Hora": "08:38:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-22-2024",
  "Hora": "18:12:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-25-2024",
  "Hora": "08:46:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-25-2024",
  "Hora": "18:07:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-26-2024",
  "Hora": "08:49:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-26-2024",
  "Hora": "18:05:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-27-2024",
  "Hora": "09:06:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-27-2024",
  "Hora": "18:02:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-28-2024",
  "Hora": "08:37:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "03-28-2024",
  "Hora": "18:19:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-01-2024",
  "Hora": "09:09:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-01-2024",
  "Hora": "18:12:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-02-2024",
  "Hora": "09:17:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-02-2024",
  "Hora": "18:10:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-03-2024",
  "Hora": "09:10:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-03-2024",
  "Hora": "18:12:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-04-2024",
  "Hora": "08:58:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-04-2024",
  "Hora": "18:13:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-05-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-05-2024",
  "Hora": "18:12:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-06-2024",
  "Hora": "09:02:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-06-2024",
  "Hora": "18:58:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-08-2024",
  "Hora": "08:59:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-08-2024",
  "Hora": "18:15:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-09-2024",
  "Hora": "09:05:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-09-2024",
  "Hora": "18:18:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-10-2024",
  "Hora": "08:50:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-10-2024",
  "Hora": "20:09:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-11-2024",
  "Hora": "08:45:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-11-2024",
  "Hora": "18:15:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-11-2024",
  "Hora": "18:15:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-12-2024",
  "Hora": "08:44:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-12-2024",
  "Hora": "18:21:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-15-2024",
  "Hora": "08:15:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271576188,
  "Date": "04-15-2024",
  "Hora": "18:09:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-18-2024",
  "Hora": "08:14:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-18-2024",
  "Hora": "17:50:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-19-2024",
  "Hora": "08:14:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-19-2024",
  "Hora": "17:50:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-20-2024",
  "Hora": "08:21:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-20-2024",
  "Hora": "17:50:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-21-2024",
  "Hora": "08:20:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-21-2024",
  "Hora": "17:50:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-22-2024",
  "Hora": "08:21:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-22-2024",
  "Hora": "17:50:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-23-2024",
  "Hora": "07:12:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-23-2024",
  "Hora": "07:12:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-23-2024",
  "Hora": "07:12:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-23-2024",
  "Hora": "07:12:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-23-2024",
  "Hora": "07:12:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-23-2024",
  "Hora": "07:12:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-23-2024",
  "Hora": "07:12:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-23-2024",
  "Hora": "07:12:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-23-2024",
  "Hora": "07:12:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-23-2024",
  "Hora": "07:12:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-23-2024",
  "Hora": "14:53:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-25-2024",
  "Hora": "08:22:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-25-2024",
  "Hora": "14:05:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-26-2024",
  "Hora": "08:19:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-26-2024",
  "Hora": "17:51:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-27-2024",
  "Hora": "08:15:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-27-2024",
  "Hora": "17:50:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-28-2024",
  "Hora": "08:14:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "03-28-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-01-2024",
  "Hora": "08:17:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-01-2024",
  "Hora": "17:50:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-02-2024",
  "Hora": "08:12:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-02-2024",
  "Hora": "17:50:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-03-2024",
  "Hora": "08:07:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-03-2024",
  "Hora": "17:50:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-04-2024",
  "Hora": "08:02:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-04-2024",
  "Hora": "17:50:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-05-2024",
  "Hora": "11:51:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-05-2024",
  "Hora": "17:50:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-08-2024",
  "Hora": "09:14:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-08-2024",
  "Hora": "18:50:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-09-2024",
  "Hora": "09:16:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-09-2024",
  "Hora": "18:50:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-10-2024",
  "Hora": "09:17:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-10-2024",
  "Hora": "18:50:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-12-2024",
  "Hora": "09:16:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-12-2024",
  "Hora": "18:50:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-15-2024",
  "Hora": "09:14:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 181002298,
  "Date": "04-15-2024",
  "Hora": "17:55:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-16-2024",
  "Hora": "05:26:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-16-2024",
  "Hora": "11:48:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-18-2024",
  "Hora": "07:14:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-18-2024",
  "Hora": "13:03:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-19-2024",
  "Hora": "05:30:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-19-2024",
  "Hora": "13:32:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-20-2024",
  "Hora": "05:28:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-20-2024",
  "Hora": "13:31:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-21-2024",
  "Hora": "05:27:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-21-2024",
  "Hora": "13:32:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-22-2024",
  "Hora": "05:25:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-22-2024",
  "Hora": "13:33:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-23-2024",
  "Hora": "05:31:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-23-2024",
  "Hora": "11:11:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-25-2024",
  "Hora": "05:52:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-25-2024",
  "Hora": "13:02:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-26-2024",
  "Hora": "05:25:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-26-2024",
  "Hora": "13:33:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-27-2024",
  "Hora": "05:31:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-27-2024",
  "Hora": "13:33:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-28-2024",
  "Hora": "05:27:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "03-28-2024",
  "Hora": "13:32:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-01-2024",
  "Hora": "05:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-01-2024",
  "Hora": "14:03:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-02-2024",
  "Hora": "05:26:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-02-2024",
  "Hora": "13:33:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-03-2024",
  "Hora": "05:25:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-03-2024",
  "Hora": "13:36:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-04-2024",
  "Hora": "05:27:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-04-2024",
  "Hora": "13:33:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-05-2024",
  "Hora": "05:26:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-05-2024",
  "Hora": "13:32:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-06-2024",
  "Hora": "05:25:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-06-2024",
  "Hora": "12:31:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-08-2024",
  "Hora": "05:51:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-08-2024",
  "Hora": "14:02:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-09-2024",
  "Hora": "05:29:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-09-2024",
  "Hora": "13:34:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-10-2024",
  "Hora": "05:23:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-10-2024",
  "Hora": "13:33:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-12-2024",
  "Hora": "05:30:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-12-2024",
  "Hora": "13:34:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-13-2024",
  "Hora": "05:30:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-13-2024",
  "Hora": "12:02:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-15-2024",
  "Hora": "05:51:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184096064,
  "Date": "04-15-2024",
  "Hora": "13:02:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-16-2024",
  "Hora": "00:17:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-16-2024",
  "Hora": "00:18:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-18-2024",
  "Hora": "15:37:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-19-2024",
  "Hora": "01:20:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-19-2024",
  "Hora": "15:32:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-20-2024",
  "Hora": "01:17:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-20-2024",
  "Hora": "15:45:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-21-2024",
  "Hora": "01:17:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-21-2024",
  "Hora": "15:43:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-22-2024",
  "Hora": "01:19:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-22-2024",
  "Hora": "15:40:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-23-2024",
  "Hora": "00:19:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-25-2024",
  "Hora": "15:40:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-26-2024",
  "Hora": "01:26:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-26-2024",
  "Hora": "15:45:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-27-2024",
  "Hora": "01:18:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-27-2024",
  "Hora": "15:42:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-28-2024",
  "Hora": "01:17:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-28-2024",
  "Hora": "15:33:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "03-29-2024",
  "Hora": "00:03:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-01-2024",
  "Hora": "15:41:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-02-2024",
  "Hora": "01:38:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-02-2024",
  "Hora": "15:41:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-03-2024",
  "Hora": "02:35:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-03-2024",
  "Hora": "15:43:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-04-2024",
  "Hora": "01:25:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-04-2024",
  "Hora": "15:48:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-05-2024",
  "Hora": "01:24:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-05-2024",
  "Hora": "15:35:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-06-2024",
  "Hora": "00:01:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-08-2024",
  "Hora": "15:27:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-09-2024",
  "Hora": "01:25:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-09-2024",
  "Hora": "15:37:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-10-2024",
  "Hora": "01:23:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-10-2024",
  "Hora": "15:42:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-11-2024",
  "Hora": "01:17:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-11-2024",
  "Hora": "15:38:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-12-2024",
  "Hora": "01:18:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-12-2024",
  "Hora": "15:43:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-13-2024",
  "Hora": "00:21:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 115745476,
  "Date": "04-15-2024",
  "Hora": "15:40:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-18-2024",
  "Hora": "08:29:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-18-2024",
  "Hora": "18:03:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-19-2024",
  "Hora": "08:03:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-19-2024",
  "Hora": "18:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-20-2024",
  "Hora": "08:25:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-20-2024",
  "Hora": "18:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-21-2024",
  "Hora": "08:34:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-21-2024",
  "Hora": "08:38:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-21-2024",
  "Hora": "18:02:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-22-2024",
  "Hora": "08:18:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-22-2024",
  "Hora": "18:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-25-2024",
  "Hora": "08:29:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-25-2024",
  "Hora": "18:11:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-26-2024",
  "Hora": "08:08:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-26-2024",
  "Hora": "18:00:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-27-2024",
  "Hora": "08:23:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-27-2024",
  "Hora": "18:01:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-28-2024",
  "Hora": "08:07:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "03-28-2024",
  "Hora": "18:01:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-01-2024",
  "Hora": "08:08:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-01-2024",
  "Hora": "18:01:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-02-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-02-2024",
  "Hora": "18:03:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-03-2024",
  "Hora": "08:07:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-03-2024",
  "Hora": "18:02:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-04-2024",
  "Hora": "08:01:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-04-2024",
  "Hora": "18:02:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-05-2024",
  "Hora": "07:59:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-05-2024",
  "Hora": "18:03:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-08-2024",
  "Hora": "08:06:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-08-2024",
  "Hora": "18:01:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-09-2024",
  "Hora": "08:22:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-09-2024",
  "Hora": "18:05:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-10-2024",
  "Hora": "08:01:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-10-2024",
  "Hora": "18:01:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-11-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-11-2024",
  "Hora": "18:01:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-12-2024",
  "Hora": "08:20:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-12-2024",
  "Hora": "18:01:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-15-2024",
  "Hora": "08:01:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 172808220,
  "Date": "04-15-2024",
  "Hora": "18:01:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-19-2024",
  "Hora": "08:26:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-19-2024",
  "Hora": "18:05:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-20-2024",
  "Hora": "08:30:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-20-2024",
  "Hora": "18:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-21-2024",
  "Hora": "08:21:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-21-2024",
  "Hora": "18:01:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-22-2024",
  "Hora": "08:35:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-22-2024",
  "Hora": "18:03:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-25-2024",
  "Hora": "08:21:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-25-2024",
  "Hora": "18:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-26-2024",
  "Hora": "08:28:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-26-2024",
  "Hora": "18:00:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-27-2024",
  "Hora": "05:58:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-27-2024",
  "Hora": "18:02:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-28-2024",
  "Hora": "11:23:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "03-28-2024",
  "Hora": "19:21:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-01-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-01-2024",
  "Hora": "18:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-02-2024",
  "Hora": "08:30:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-02-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-03-2024",
  "Hora": "08:25:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-03-2024",
  "Hora": "18:04:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-05-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-05-2024",
  "Hora": "18:00:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-08-2024",
  "Hora": "08:27:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-08-2024",
  "Hora": "18:00:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-09-2024",
  "Hora": "08:27:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-09-2024",
  "Hora": "18:00:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-10-2024",
  "Hora": "08:27:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-10-2024",
  "Hora": "18:00:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-11-2024",
  "Hora": "08:27:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-11-2024",
  "Hora": "17:59:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-12-2024",
  "Hora": "08:27:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-12-2024",
  "Hora": "18:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-15-2024",
  "Hora": "08:21:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 112546073,
  "Date": "04-15-2024",
  "Hora": "18:01:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-18-2024",
  "Hora": "08:16:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-18-2024",
  "Hora": "18:05:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-19-2024",
  "Hora": "07:51:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-19-2024",
  "Hora": "18:03:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-20-2024",
  "Hora": "08:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-20-2024",
  "Hora": "20:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-21-2024",
  "Hora": "08:21:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-21-2024",
  "Hora": "18:02:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-22-2024",
  "Hora": "08:04:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-22-2024",
  "Hora": "17:04:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-25-2024",
  "Hora": "08:10:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-25-2024",
  "Hora": "19:18:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-26-2024",
  "Hora": "08:03:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-26-2024",
  "Hora": "19:21:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-27-2024",
  "Hora": "08:26:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-27-2024",
  "Hora": "19:12:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-28-2024",
  "Hora": "08:15:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "03-28-2024",
  "Hora": "23:32:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-01-2024",
  "Hora": "08:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-01-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-02-2024",
  "Hora": "07:53:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-02-2024",
  "Hora": "07:53:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-02-2024",
  "Hora": "18:02:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-03-2024",
  "Hora": "08:13:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-03-2024",
  "Hora": "18:02:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-04-2024",
  "Hora": "08:04:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-04-2024",
  "Hora": "18:02:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-05-2024",
  "Hora": "08:04:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-05-2024",
  "Hora": "17:02:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-08-2024",
  "Hora": "08:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-08-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-09-2024",
  "Hora": "08:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-09-2024",
  "Hora": "20:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-10-2024",
  "Hora": "08:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-10-2024",
  "Hora": "20:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-11-2024",
  "Hora": "07:50:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-11-2024",
  "Hora": "07:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-11-2024",
  "Hora": "19:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185334325,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-16-2024",
  "Hora": "00:13:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-19-2024",
  "Hora": "16:06:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-20-2024",
  "Hora": "01:01:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-20-2024",
  "Hora": "16:09:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-21-2024",
  "Hora": "01:04:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-21-2024",
  "Hora": "16:06:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-22-2024",
  "Hora": "01:09:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-22-2024",
  "Hora": "16:08:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-23-2024",
  "Hora": "00:14:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-25-2024",
  "Hora": "16:03:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-26-2024",
  "Hora": "01:21:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-26-2024",
  "Hora": "16:06:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-27-2024",
  "Hora": "01:10:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-27-2024",
  "Hora": "16:13:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-28-2024",
  "Hora": "01:02:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-28-2024",
  "Hora": "16:37:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "03-28-2024",
  "Hora": "23:46:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-01-2024",
  "Hora": "16:08:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-02-2024",
  "Hora": "01:40:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-02-2024",
  "Hora": "16:07:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-03-2024",
  "Hora": "01:34:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-03-2024",
  "Hora": "16:12:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-04-2024",
  "Hora": "01:15:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-04-2024",
  "Hora": "16:09:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-05-2024",
  "Hora": "01:10:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-05-2024",
  "Hora": "16:03:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-06-2024",
  "Hora": "00:06:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-08-2024",
  "Hora": "17:32:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-09-2024",
  "Hora": "01:15:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-09-2024",
  "Hora": "16:11:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-10-2024",
  "Hora": "01:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-10-2024",
  "Hora": "16:09:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-11-2024",
  "Hora": "01:08:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-11-2024",
  "Hora": "16:14:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-12-2024",
  "Hora": "01:00:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-12-2024",
  "Hora": "16:13:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-13-2024",
  "Hora": "00:02:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 183275976,
  "Date": "04-15-2024",
  "Hora": "16:14:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-18-2024",
  "Hora": "12:56:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-18-2024",
  "Hora": "22:30:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-19-2024",
  "Hora": "12:59:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-19-2024",
  "Hora": "21:45:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-20-2024",
  "Hora": "12:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-20-2024",
  "Hora": "21:01:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-21-2024",
  "Hora": "12:55:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-21-2024",
  "Hora": "20:47:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-22-2024",
  "Hora": "12:54:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-22-2024",
  "Hora": "20:01:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-25-2024",
  "Hora": "12:48:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-25-2024",
  "Hora": "21:45:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-26-2024",
  "Hora": "12:49:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-26-2024",
  "Hora": "22:30:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-27-2024",
  "Hora": "12:50:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-27-2024",
  "Hora": "21:30:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-28-2024",
  "Hora": "12:55:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "03-28-2024",
  "Hora": "21:07:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-01-2024",
  "Hora": "12:50:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-01-2024",
  "Hora": "22:32:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-02-2024",
  "Hora": "14:21:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-02-2024",
  "Hora": "20:50:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-03-2024",
  "Hora": "12:48:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-03-2024",
  "Hora": "20:32:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-04-2024",
  "Hora": "12:52:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-04-2024",
  "Hora": "20:41:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-05-2024",
  "Hora": "12:52:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-05-2024",
  "Hora": "20:38:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-08-2024",
  "Hora": "12:47:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-08-2024",
  "Hora": "22:25:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-09-2024",
  "Hora": "12:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-09-2024",
  "Hora": "21:34:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-10-2024",
  "Hora": "12:49:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-10-2024",
  "Hora": "21:04:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-11-2024",
  "Hora": "12:58:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-11-2024",
  "Hora": "21:36:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-12-2024",
  "Hora": "12:51:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-12-2024",
  "Hora": "21:02:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-15-2024",
  "Hora": "12:49:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213310127,
  "Date": "04-15-2024",
  "Hora": "22:30:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-16-2024",
  "Hora": "07:46:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-16-2024",
  "Hora": "14:01:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-18-2024",
  "Hora": "08:05:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-18-2024",
  "Hora": "20:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-19-2024",
  "Hora": "08:41:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-19-2024",
  "Hora": "18:02:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-20-2024",
  "Hora": "07:50:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-20-2024",
  "Hora": "20:04:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-21-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-21-2024",
  "Hora": "20:02:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-22-2024",
  "Hora": "08:32:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-22-2024",
  "Hora": "17:02:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-23-2024",
  "Hora": "10:09:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-23-2024",
  "Hora": "10:09:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-23-2024",
  "Hora": "14:03:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-25-2024",
  "Hora": "07:54:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-25-2024",
  "Hora": "07:54:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-25-2024",
  "Hora": "18:03:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-25-2024",
  "Hora": "18:03:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-26-2024",
  "Hora": "08:29:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-26-2024",
  "Hora": "20:01:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-27-2024",
  "Hora": "07:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-27-2024",
  "Hora": "18:01:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-28-2024",
  "Hora": "08:16:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-28-2024",
  "Hora": "08:16:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "03-28-2024",
  "Hora": "18:05:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-01-2024",
  "Hora": "07:54:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-01-2024",
  "Hora": "07:54:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-01-2024",
  "Hora": "18:03:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-02-2024",
  "Hora": "08:10:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-02-2024",
  "Hora": "08:10:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-02-2024",
  "Hora": "18:02:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-03-2024",
  "Hora": "08:23:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-03-2024",
  "Hora": "18:02:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-04-2024",
  "Hora": "10:15:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-04-2024",
  "Hora": "18:11:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-04-2024",
  "Hora": "18:11:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-05-2024",
  "Hora": "08:29:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-05-2024",
  "Hora": "17:02:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-05-2024",
  "Hora": "17:02:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-08-2024",
  "Hora": "07:48:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-08-2024",
  "Hora": "18:03:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-09-2024",
  "Hora": "08:12:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-09-2024",
  "Hora": "18:02:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-10-2024",
  "Hora": "08:11:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-10-2024",
  "Hora": "18:01:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-11-2024",
  "Hora": "08:09:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-11-2024",
  "Hora": "08:09:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-11-2024",
  "Hora": "08:09:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-11-2024",
  "Hora": "20:01:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-12-2024",
  "Hora": "08:27:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-12-2024",
  "Hora": "17:04:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-15-2024",
  "Hora": "08:07:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192456681,
  "Date": "04-15-2024",
  "Hora": "18:03:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-16-2024",
  "Hora": "04:50:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-16-2024",
  "Hora": "12:15:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-18-2024",
  "Hora": "05:47:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-18-2024",
  "Hora": "14:06:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-19-2024",
  "Hora": "04:47:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-19-2024",
  "Hora": "13:04:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-20-2024",
  "Hora": "04:50:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-20-2024",
  "Hora": "13:06:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-21-2024",
  "Hora": "04:56:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-21-2024",
  "Hora": "13:05:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-22-2024",
  "Hora": "04:48:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-22-2024",
  "Hora": "13:09:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-23-2024",
  "Hora": "04:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-23-2024",
  "Hora": "04:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-23-2024",
  "Hora": "04:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-23-2024",
  "Hora": "04:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-23-2024",
  "Hora": "04:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-23-2024",
  "Hora": "04:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-23-2024",
  "Hora": "04:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-23-2024",
  "Hora": "04:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-23-2024",
  "Hora": "04:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-23-2024",
  "Hora": "04:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-23-2024",
  "Hora": "11:02:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-25-2024",
  "Hora": "05:49:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-25-2024",
  "Hora": "14:01:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-26-2024",
  "Hora": "04:50:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-26-2024",
  "Hora": "13:05:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-27-2024",
  "Hora": "04:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-27-2024",
  "Hora": "13:05:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-28-2024",
  "Hora": "04:55:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "03-28-2024",
  "Hora": "13:01:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-01-2024",
  "Hora": "05:51:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-01-2024",
  "Hora": "14:02:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-02-2024",
  "Hora": "04:50:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-02-2024",
  "Hora": "13:05:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-03-2024",
  "Hora": "04:48:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-03-2024",
  "Hora": "13:16:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-04-2024",
  "Hora": "04:50:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-04-2024",
  "Hora": "13:04:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-05-2024",
  "Hora": "04:49:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-05-2024",
  "Hora": "10:30:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-06-2024",
  "Hora": "04:49:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-06-2024",
  "Hora": "13:00:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-09-2024",
  "Hora": "04:54:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-09-2024",
  "Hora": "13:03:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-10-2024",
  "Hora": "04:49:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-10-2024",
  "Hora": "13:10:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-11-2024",
  "Hora": "04:48:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-11-2024",
  "Hora": "13:04:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-12-2024",
  "Hora": "04:53:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-12-2024",
  "Hora": "13:05:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-13-2024",
  "Hora": "04:49:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-13-2024",
  "Hora": "13:01:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-15-2024",
  "Hora": "05:48:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 178792997,
  "Date": "04-15-2024",
  "Hora": "14:09:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-16-2024",
  "Hora": "04:48:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-16-2024",
  "Hora": "11:33:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-18-2024",
  "Hora": "05:45:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-18-2024",
  "Hora": "14:00:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-19-2024",
  "Hora": "04:43:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-19-2024",
  "Hora": "13:01:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-20-2024",
  "Hora": "04:43:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-20-2024",
  "Hora": "13:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-21-2024",
  "Hora": "04:48:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-21-2024",
  "Hora": "12:13:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-23-2024",
  "Hora": "04:55:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-23-2024",
  "Hora": "12:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-25-2024",
  "Hora": "05:47:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-25-2024",
  "Hora": "14:01:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-26-2024",
  "Hora": "05:00:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-26-2024",
  "Hora": "13:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-27-2024",
  "Hora": "04:55:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-27-2024",
  "Hora": "13:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-28-2024",
  "Hora": "04:54:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "03-28-2024",
  "Hora": "13:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-01-2024",
  "Hora": "05:43:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-01-2024",
  "Hora": "13:00:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-02-2024",
  "Hora": "04:51:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-02-2024",
  "Hora": "13:00:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-03-2024",
  "Hora": "04:42:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-03-2024",
  "Hora": "13:01:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-04-2024",
  "Hora": "04:45:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-04-2024",
  "Hora": "13:03:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-05-2024",
  "Hora": "04:46:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-05-2024",
  "Hora": "13:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-06-2024",
  "Hora": "04:48:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-06-2024",
  "Hora": "12:31:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-08-2024",
  "Hora": "05:40:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-08-2024",
  "Hora": "12:52:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-09-2024",
  "Hora": "04:46:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-09-2024",
  "Hora": "13:04:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-10-2024",
  "Hora": "04:46:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-10-2024",
  "Hora": "13:02:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-11-2024",
  "Hora": "04:45:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-11-2024",
  "Hora": "13:01:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-12-2024",
  "Hora": "04:47:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-12-2024",
  "Hora": "13:26:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-13-2024",
  "Hora": "04:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-13-2024",
  "Hora": "13:03:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-15-2024",
  "Hora": "05:40:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 185928705,
  "Date": "04-15-2024",
  "Hora": "14:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175237577,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-16-2024",
  "Hora": "04:36:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-16-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-18-2024",
  "Hora": "04:40:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-18-2024",
  "Hora": "12:20:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-19-2024",
  "Hora": "04:12:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-19-2024",
  "Hora": "12:08:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-20-2024",
  "Hora": "04:36:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-20-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-21-2024",
  "Hora": "04:09:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-21-2024",
  "Hora": "12:05:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-22-2024",
  "Hora": "04:13:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-22-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-23-2024",
  "Hora": "04:08:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-23-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-25-2024",
  "Hora": "04:07:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-25-2024",
  "Hora": "11:28:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-26-2024",
  "Hora": "04:12:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-26-2024",
  "Hora": "11:59:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-27-2024",
  "Hora": "04:12:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-27-2024",
  "Hora": "11:47:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-28-2024",
  "Hora": "04:14:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "03-28-2024",
  "Hora": "12:10:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-01-2024",
  "Hora": "04:18:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-01-2024",
  "Hora": "12:31:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-02-2024",
  "Hora": "04:13:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-02-2024",
  "Hora": "12:04:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-03-2024",
  "Hora": "04:14:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-03-2024",
  "Hora": "12:03:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-04-2024",
  "Hora": "04:12:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-04-2024",
  "Hora": "12:06:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-05-2024",
  "Hora": "04:15:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-05-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-06-2024",
  "Hora": "04:15:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-06-2024",
  "Hora": "11:53:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-08-2024",
  "Hora": "04:10:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-08-2024",
  "Hora": "11:43:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-09-2024",
  "Hora": "04:16:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-09-2024",
  "Hora": "12:00:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-10-2024",
  "Hora": "04:11:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-10-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-11-2024",
  "Hora": "04:38:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-11-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-12-2024",
  "Hora": "04:18:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-12-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-13-2024",
  "Hora": "04:10:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-13-2024",
  "Hora": "11:38:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-15-2024",
  "Hora": "04:13:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 202235115,
  "Date": "04-15-2024",
  "Hora": "11:33:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-18-2024",
  "Hora": "08:21:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-18-2024",
  "Hora": "17:56:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-19-2024",
  "Hora": "08:20:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-19-2024",
  "Hora": "17:54:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-20-2024",
  "Hora": "08:31:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-20-2024",
  "Hora": "17:59:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-21-2024",
  "Hora": "08:22:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-21-2024",
  "Hora": "17:51:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-22-2024",
  "Hora": "08:36:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-22-2024",
  "Hora": "17:55:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-25-2024",
  "Hora": "08:22:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-25-2024",
  "Hora": "18:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-26-2024",
  "Hora": "08:20:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-26-2024",
  "Hora": "18:02:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-27-2024",
  "Hora": "08:22:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-27-2024",
  "Hora": "17:58:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-28-2024",
  "Hora": "08:27:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "03-28-2024",
  "Hora": "18:00:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-01-2024",
  "Hora": "08:26:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-01-2024",
  "Hora": "17:59:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-02-2024",
  "Hora": "08:26:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-02-2024",
  "Hora": "18:03:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-03-2024",
  "Hora": "08:22:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-03-2024",
  "Hora": "18:02:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-04-2024",
  "Hora": "08:18:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-04-2024",
  "Hora": "17:56:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-05-2024",
  "Hora": "08:21:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-05-2024",
  "Hora": "18:01:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-08-2024",
  "Hora": "09:18:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-08-2024",
  "Hora": "18:57:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-09-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-09-2024",
  "Hora": "09:20:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-09-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-09-2024",
  "Hora": "19:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-10-2024",
  "Hora": "09:17:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-10-2024",
  "Hora": "18:52:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-11-2024",
  "Hora": "09:20:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-11-2024",
  "Hora": "18:58:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-12-2024",
  "Hora": "09:22:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-12-2024",
  "Hora": "19:01:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-15-2024",
  "Hora": "09:23:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18723431K",
  "Date": "04-15-2024",
  "Hora": "18:02:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-19-2024",
  "Hora": "07:46:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-19-2024",
  "Hora": "18:03:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-20-2024",
  "Hora": "07:50:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-20-2024",
  "Hora": "18:02:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-21-2024",
  "Hora": "07:48:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-21-2024",
  "Hora": "18:01:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-22-2024",
  "Hora": "07:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-22-2024",
  "Hora": "17:03:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-25-2024",
  "Hora": "07:50:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-25-2024",
  "Hora": "18:01:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-26-2024",
  "Hora": "07:50:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-26-2024",
  "Hora": "18:00:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-27-2024",
  "Hora": "07:48:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-27-2024",
  "Hora": "18:02:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-28-2024",
  "Hora": "07:49:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "03-28-2024",
  "Hora": "18:00:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-02-2024",
  "Hora": "07:45:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-02-2024",
  "Hora": "18:03:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-03-2024",
  "Hora": "07:49:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-03-2024",
  "Hora": "18:03:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-04-2024",
  "Hora": "07:45:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-04-2024",
  "Hora": "18:03:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-05-2024",
  "Hora": "07:47:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-05-2024",
  "Hora": "17:02:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-08-2024",
  "Hora": "07:50:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-08-2024",
  "Hora": "18:03:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-09-2024",
  "Hora": "07:44:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-09-2024",
  "Hora": "18:03:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-10-2024",
  "Hora": "07:47:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-10-2024",
  "Hora": "18:00:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-11-2024",
  "Hora": "07:45:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-11-2024",
  "Hora": "18:01:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-12-2024",
  "Hora": "07:46:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-12-2024",
  "Hora": "17:03:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-15-2024",
  "Hora": "07:46:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "8456558K",
  "Date": "04-15-2024",
  "Hora": "18:03:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-16-2024",
  "Hora": "13:35:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-16-2024",
  "Hora": "16:02:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-18-2024",
  "Hora": "11:41:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-18-2024",
  "Hora": "19:35:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-19-2024",
  "Hora": "11:41:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-19-2024",
  "Hora": "19:36:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-20-2024",
  "Hora": "11:55:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-20-2024",
  "Hora": "19:06:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-21-2024",
  "Hora": "12:04:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-21-2024",
  "Hora": "18:58:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-22-2024",
  "Hora": "11:43:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-22-2024",
  "Hora": "18:16:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-23-2024",
  "Hora": "13:35:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-23-2024",
  "Hora": "16:03:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-25-2024",
  "Hora": "11:51:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-25-2024",
  "Hora": "19:03:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-26-2024",
  "Hora": "11:43:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-26-2024",
  "Hora": "19:30:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-27-2024",
  "Hora": "11:40:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-27-2024",
  "Hora": "18:37:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-28-2024",
  "Hora": "11:43:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "03-28-2024",
  "Hora": "18:32:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-01-2024",
  "Hora": "12:03:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-01-2024",
  "Hora": "19:33:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-02-2024",
  "Hora": "11:47:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-02-2024",
  "Hora": "19:02:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-03-2024",
  "Hora": "11:41:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-03-2024",
  "Hora": "19:04:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-04-2024",
  "Hora": "11:44:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-04-2024",
  "Hora": "19:34:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-05-2024",
  "Hora": "11:38:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-05-2024",
  "Hora": "19:37:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-06-2024",
  "Hora": "13:29:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-06-2024",
  "Hora": "16:04:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-08-2024",
  "Hora": "11:34:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-08-2024",
  "Hora": "19:15:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-09-2024",
  "Hora": "11:44:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-09-2024",
  "Hora": "19:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-10-2024",
  "Hora": "11:41:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-10-2024",
  "Hora": "18:31:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-11-2024",
  "Hora": "11:41:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-11-2024",
  "Hora": "19:04:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-12-2024",
  "Hora": "11:34:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-12-2024",
  "Hora": "19:02:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-13-2024",
  "Hora": "14:01:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-13-2024",
  "Hora": "16:10:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-15-2024",
  "Hora": "11:33:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160771771,
  "Date": "04-15-2024",
  "Hora": "19:30:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-16-2024",
  "Hora": "13:00:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-16-2024",
  "Hora": "21:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-18-2024",
  "Hora": "15:53:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-19-2024",
  "Hora": "01:11:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-19-2024",
  "Hora": "02:17:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-19-2024",
  "Hora": "15:53:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-20-2024",
  "Hora": "00:55:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-20-2024",
  "Hora": "15:54:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-21-2024",
  "Hora": "01:04:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-21-2024",
  "Hora": "16:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-22-2024",
  "Hora": "01:01:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-22-2024",
  "Hora": "10:54:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-22-2024",
  "Hora": "21:39:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-25-2024",
  "Hora": "10:46:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-25-2024",
  "Hora": "22:12:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-26-2024",
  "Hora": "11:07:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-26-2024",
  "Hora": "22:06:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-27-2024",
  "Hora": "10:58:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-27-2024",
  "Hora": "22:11:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-28-2024",
  "Hora": "10:55:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "03-28-2024",
  "Hora": "21:40:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-01-2024",
  "Hora": "15:42:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-02-2024",
  "Hora": "01:26:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-02-2024",
  "Hora": "15:57:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-03-2024",
  "Hora": "01:31:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-03-2024",
  "Hora": "15:42:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-04-2024",
  "Hora": "01:09:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-04-2024",
  "Hora": "15:47:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-05-2024",
  "Hora": "01:11:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-05-2024",
  "Hora": "10:46:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-05-2024",
  "Hora": "21:31:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-08-2024",
  "Hora": "10:39:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-08-2024",
  "Hora": "22:03:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-09-2024",
  "Hora": "10:53:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-09-2024",
  "Hora": "21:58:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-10-2024",
  "Hora": "10:57:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-10-2024",
  "Hora": "22:00:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-11-2024",
  "Hora": "10:51:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-11-2024",
  "Hora": "21:52:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-13-2024",
  "Hora": "21:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 101705455,
  "Date": "04-15-2024",
  "Hora": "15:41:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-16-2024",
  "Hora": "06:01:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-16-2024",
  "Hora": "13:46:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-18-2024",
  "Hora": "05:58:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-18-2024",
  "Hora": "14:00:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-19-2024",
  "Hora": "06:08:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-19-2024",
  "Hora": "13:48:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-20-2024",
  "Hora": "05:48:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-20-2024",
  "Hora": "13:45:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-21-2024",
  "Hora": "05:39:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-21-2024",
  "Hora": "13:47:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-22-2024",
  "Hora": "22:31:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-23-2024",
  "Hora": "05:43:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-23-2024",
  "Hora": "13:45:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-25-2024",
  "Hora": "05:50:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-25-2024",
  "Hora": "14:02:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-26-2024",
  "Hora": "06:24:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-26-2024",
  "Hora": "13:45:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-27-2024",
  "Hora": "05:43:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-27-2024",
  "Hora": "13:45:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-28-2024",
  "Hora": "05:50:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-28-2024",
  "Hora": "05:50:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "03-28-2024",
  "Hora": "13:46:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-01-2024",
  "Hora": "06:29:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-01-2024",
  "Hora": "14:01:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-02-2024",
  "Hora": "05:50:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-02-2024",
  "Hora": "13:46:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-03-2024",
  "Hora": "05:39:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-03-2024",
  "Hora": "13:46:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-04-2024",
  "Hora": "05:43:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-04-2024",
  "Hora": "13:45:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-05-2024",
  "Hora": "05:41:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-05-2024",
  "Hora": "13:47:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-06-2024",
  "Hora": "05:47:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-06-2024",
  "Hora": "13:47:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-08-2024",
  "Hora": "05:56:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-08-2024",
  "Hora": "14:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-09-2024",
  "Hora": "05:45:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-09-2024",
  "Hora": "13:47:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-10-2024",
  "Hora": "06:03:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-10-2024",
  "Hora": "13:45:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-11-2024",
  "Hora": "05:50:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-11-2024",
  "Hora": "13:46:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-12-2024",
  "Hora": "05:45:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-12-2024",
  "Hora": "13:46:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-13-2024",
  "Hora": "05:41:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-13-2024",
  "Hora": "13:53:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-15-2024",
  "Hora": "05:51:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191982819,
  "Date": "04-15-2024",
  "Hora": "14:05:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-16-2024",
  "Hora": "04:48:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-16-2024",
  "Hora": "12:00:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-18-2024",
  "Hora": "05:50:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-18-2024",
  "Hora": "14:00:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-19-2024",
  "Hora": "04:53:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-19-2024",
  "Hora": "13:03:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-20-2024",
  "Hora": "04:50:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-20-2024",
  "Hora": "13:05:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-26-2024",
  "Hora": "04:55:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-26-2024",
  "Hora": "13:02:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-27-2024",
  "Hora": "04:59:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-27-2024",
  "Hora": "13:03:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-28-2024",
  "Hora": "04:59:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "03-28-2024",
  "Hora": "13:02:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-01-2024",
  "Hora": "04:49:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-01-2024",
  "Hora": "14:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-02-2024",
  "Hora": "03:56:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-02-2024",
  "Hora": "12:10:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-03-2024",
  "Hora": "03:53:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-03-2024",
  "Hora": "12:03:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-04-2024",
  "Hora": "05:00:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-04-2024",
  "Hora": "12:02:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-05-2024",
  "Hora": "04:54:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-05-2024",
  "Hora": "12:00:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-06-2024",
  "Hora": "04:51:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-06-2024",
  "Hora": "12:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-08-2024",
  "Hora": "06:10:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-08-2024",
  "Hora": "13:58:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-09-2024",
  "Hora": "03:48:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-09-2024",
  "Hora": "12:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-10-2024",
  "Hora": "04:56:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-10-2024",
  "Hora": "12:07:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-11-2024",
  "Hora": "04:57:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-11-2024",
  "Hora": "12:59:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-12-2024",
  "Hora": "04:58:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-12-2024",
  "Hora": "13:02:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-13-2024",
  "Hora": "04:28:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-13-2024",
  "Hora": "13:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-15-2024",
  "Hora": "05:26:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209420910,
  "Date": "04-15-2024",
  "Hora": "14:00:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-16-2024",
  "Hora": "04:55:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-16-2024",
  "Hora": "14:00:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-18-2024",
  "Hora": "04:55:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-18-2024",
  "Hora": "14:30:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-19-2024",
  "Hora": "04:56:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-19-2024",
  "Hora": "14:30:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-20-2024",
  "Hora": "04:55:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-20-2024",
  "Hora": "14:30:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-21-2024",
  "Hora": "04:55:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-21-2024",
  "Hora": "14:30:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-22-2024",
  "Hora": "04:58:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-22-2024",
  "Hora": "14:30:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-25-2024",
  "Hora": "04:52:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-25-2024",
  "Hora": "14:30:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-27-2024",
  "Hora": "04:53:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-27-2024",
  "Hora": "14:30:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-28-2024",
  "Hora": "04:53:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "03-28-2024",
  "Hora": "14:30:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-01-2024",
  "Hora": "04:55:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-01-2024",
  "Hora": "14:32:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-03-2024",
  "Hora": "04:55:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-03-2024",
  "Hora": "14:30:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-04-2024",
  "Hora": "04:54:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-04-2024",
  "Hora": "14:29:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-05-2024",
  "Hora": "04:57:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-05-2024",
  "Hora": "14:31:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-06-2024",
  "Hora": "04:53:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-06-2024",
  "Hora": "13:07:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-08-2024",
  "Hora": "04:54:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-08-2024",
  "Hora": "14:30:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-09-2024",
  "Hora": "04:56:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-09-2024",
  "Hora": "14:30:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-10-2024",
  "Hora": "04:52:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-10-2024",
  "Hora": "14:30:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-11-2024",
  "Hora": "04:53:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-11-2024",
  "Hora": "14:30:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-12-2024",
  "Hora": "04:53:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-12-2024",
  "Hora": "14:30:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-15-2024",
  "Hora": "04:53:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195365377,
  "Date": "04-15-2024",
  "Hora": "14:30:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "03-19-2024",
  "Hora": "09:57:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "03-19-2024",
  "Hora": "17:20:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "03-20-2024",
  "Hora": "10:02:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "03-20-2024",
  "Hora": "17:11:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "03-21-2024",
  "Hora": "10:01:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "03-21-2024",
  "Hora": "16:49:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "03-27-2024",
  "Hora": "09:57:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "03-27-2024",
  "Hora": "17:06:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "03-28-2024",
  "Hora": "10:14:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "03-28-2024",
  "Hora": "17:03:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-01-2024",
  "Hora": "10:11:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-01-2024",
  "Hora": "17:29:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-02-2024",
  "Hora": "09:53:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-02-2024",
  "Hora": "17:42:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-03-2024",
  "Hora": "09:56:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-03-2024",
  "Hora": "17:15:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-04-2024",
  "Hora": "09:59:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-04-2024",
  "Hora": "17:15:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-05-2024",
  "Hora": "10:21:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-05-2024",
  "Hora": "17:19:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-08-2024",
  "Hora": "10:13:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-08-2024",
  "Hora": "17:22:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-09-2024",
  "Hora": "09:56:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-09-2024",
  "Hora": "17:06:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-10-2024",
  "Hora": "10:06:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-10-2024",
  "Hora": "16:58:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-11-2024",
  "Hora": "10:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-11-2024",
  "Hora": "16:41:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-12-2024",
  "Hora": "09:56:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-12-2024",
  "Hora": "16:52:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-15-2024",
  "Hora": "09:56:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187804221,
  "Date": "04-15-2024",
  "Hora": "17:49:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-16-2024",
  "Hora": "01:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-16-2024",
  "Hora": "14:54:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-16-2024",
  "Hora": "22:03:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-18-2024",
  "Hora": "15:50:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-18-2024",
  "Hora": "22:26:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-19-2024",
  "Hora": "12:58:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-19-2024",
  "Hora": "22:08:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-20-2024",
  "Hora": "12:43:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-20-2024",
  "Hora": "22:05:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-21-2024",
  "Hora": "13:01:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-21-2024",
  "Hora": "22:07:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-22-2024",
  "Hora": "13:14:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-22-2024",
  "Hora": "21:24:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-26-2024",
  "Hora": "15:50:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-27-2024",
  "Hora": "00:48:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-27-2024",
  "Hora": "15:52:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-28-2024",
  "Hora": "01:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-28-2024",
  "Hora": "12:55:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "03-28-2024",
  "Hora": "16:16:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-01-2024",
  "Hora": "15:49:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-02-2024",
  "Hora": "01:42:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-02-2024",
  "Hora": "13:04:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-02-2024",
  "Hora": "22:16:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-03-2024",
  "Hora": "12:49:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-03-2024",
  "Hora": "22:23:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-04-2024",
  "Hora": "13:09:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-04-2024",
  "Hora": "22:06:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-05-2024",
  "Hora": "12:54:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-05-2024",
  "Hora": "22:15:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-09-2024",
  "Hora": "15:59:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-10-2024",
  "Hora": "00:51:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-10-2024",
  "Hora": "15:48:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-10-2024",
  "Hora": "23:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-11-2024",
  "Hora": "16:10:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-12-2024",
  "Hora": "00:42:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-12-2024",
  "Hora": "15:58:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-12-2024",
  "Hora": "22:14:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-13-2024",
  "Hora": "15:02:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-13-2024",
  "Hora": "21:56:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-15-2024",
  "Hora": "15:51:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166386756,
  "Date": "04-15-2024",
  "Hora": "23:03:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-16-2024",
  "Hora": "09:08:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-16-2024",
  "Hora": "17:57:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-18-2024",
  "Hora": "09:12:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-18-2024",
  "Hora": "16:35:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-19-2024",
  "Hora": "09:22:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-19-2024",
  "Hora": "16:50:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-20-2024",
  "Hora": "09:22:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-20-2024",
  "Hora": "17:44:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-21-2024",
  "Hora": "09:24:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-21-2024",
  "Hora": "16:50:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-22-2024",
  "Hora": "09:14:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-22-2024",
  "Hora": "17:16:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-23-2024",
  "Hora": "09:12:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-23-2024",
  "Hora": "16:11:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-25-2024",
  "Hora": "09:19:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-25-2024",
  "Hora": "17:20:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-26-2024",
  "Hora": "09:17:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-26-2024",
  "Hora": "17:12:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-27-2024",
  "Hora": "09:23:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-27-2024",
  "Hora": "16:54:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-28-2024",
  "Hora": "09:13:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "03-28-2024",
  "Hora": "16:53:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-01-2024",
  "Hora": "08:22:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-01-2024",
  "Hora": "19:01:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-02-2024",
  "Hora": "08:23:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-02-2024",
  "Hora": "18:03:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-03-2024",
  "Hora": "09:13:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-03-2024",
  "Hora": "17:50:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-04-2024",
  "Hora": "09:16:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-04-2024",
  "Hora": "17:43:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-05-2024",
  "Hora": "09:16:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-05-2024",
  "Hora": "09:29:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-05-2024",
  "Hora": "18:04:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-06-2024",
  "Hora": "09:10:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-06-2024",
  "Hora": "16:13:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-08-2024",
  "Hora": "09:14:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-08-2024",
  "Hora": "18:02:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-09-2024",
  "Hora": "09:17:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-09-2024",
  "Hora": "17:08:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-10-2024",
  "Hora": "09:17:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-10-2024",
  "Hora": "17:58:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-11-2024",
  "Hora": "09:16:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-11-2024",
  "Hora": "17:51:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-12-2024",
  "Hora": "09:13:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-12-2024",
  "Hora": "18:13:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-13-2024",
  "Hora": "09:06:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-13-2024",
  "Hora": "15:51:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-15-2024",
  "Hora": "08:54:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213493469,
  "Date": "04-15-2024",
  "Hora": "16:43:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-16-2024",
  "Hora": "03:36:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-16-2024",
  "Hora": "11:03:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-16-2024",
  "Hora": "11:03:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-18-2024",
  "Hora": "03:46:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-18-2024",
  "Hora": "03:46:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-18-2024",
  "Hora": "12:11:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-18-2024",
  "Hora": "12:11:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-19-2024",
  "Hora": "04:00:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-19-2024",
  "Hora": "04:00:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-19-2024",
  "Hora": "12:24:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-19-2024",
  "Hora": "12:24:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-20-2024",
  "Hora": "03:42:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-20-2024",
  "Hora": "12:10:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-21-2024",
  "Hora": "03:38:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-21-2024",
  "Hora": "11:59:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-21-2024",
  "Hora": "11:59:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-22-2024",
  "Hora": "03:43:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-22-2024",
  "Hora": "03:43:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-22-2024",
  "Hora": "12:22:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-22-2024",
  "Hora": "12:23:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-23-2024",
  "Hora": "03:40:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-23-2024",
  "Hora": "03:40:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-23-2024",
  "Hora": "12:09:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-23-2024",
  "Hora": "12:09:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-25-2024",
  "Hora": "03:51:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-25-2024",
  "Hora": "03:52:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-25-2024",
  "Hora": "12:05:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-26-2024",
  "Hora": "04:06:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-26-2024",
  "Hora": "12:07:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-27-2024",
  "Hora": "04:16:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-27-2024",
  "Hora": "12:18:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-28-2024",
  "Hora": "04:08:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "03-28-2024",
  "Hora": "12:03:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-02-2024",
  "Hora": "03:29:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-02-2024",
  "Hora": "11:06:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-02-2024",
  "Hora": "11:06:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-03-2024",
  "Hora": "03:02:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-03-2024",
  "Hora": "03:03:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-03-2024",
  "Hora": "11:07:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-03-2024",
  "Hora": "11:07:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-04-2024",
  "Hora": "03:37:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-04-2024",
  "Hora": "11:03:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-05-2024",
  "Hora": "03:21:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-05-2024",
  "Hora": "03:21:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-05-2024",
  "Hora": "11:14:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-06-2024",
  "Hora": "02:32:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-06-2024",
  "Hora": "11:23:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-08-2024",
  "Hora": "04:00:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-08-2024",
  "Hora": "12:04:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-09-2024",
  "Hora": "03:37:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-09-2024",
  "Hora": "12:11:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-10-2024",
  "Hora": "04:10:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-10-2024",
  "Hora": "04:10:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-10-2024",
  "Hora": "12:02:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-11-2024",
  "Hora": "03:50:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-11-2024",
  "Hora": "03:50:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-11-2024",
  "Hora": "12:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-12-2024",
  "Hora": "04:13:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-12-2024",
  "Hora": "12:05:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-12-2024",
  "Hora": "12:05:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-13-2024",
  "Hora": "03:44:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-13-2024",
  "Hora": "11:02:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-15-2024",
  "Hora": "04:05:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 213076213,
  "Date": "04-15-2024",
  "Hora": "12:03:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-16-2024",
  "Hora": "00:14:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-16-2024",
  "Hora": "16:00:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-17-2024",
  "Hora": "00:24:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-18-2024",
  "Hora": "16:00:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-19-2024",
  "Hora": "00:13:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-19-2024",
  "Hora": "16:00:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-20-2024",
  "Hora": "00:15:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-20-2024",
  "Hora": "16:00:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-21-2024",
  "Hora": "00:11:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-21-2024",
  "Hora": "15:56:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-22-2024",
  "Hora": "00:15:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-22-2024",
  "Hora": "15:59:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-23-2024",
  "Hora": "00:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-23-2024",
  "Hora": "16:00:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-23-2024",
  "Hora": "16:00:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-24-2024",
  "Hora": "00:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-25-2024",
  "Hora": "15:58:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-26-2024",
  "Hora": "00:05:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-26-2024",
  "Hora": "16:00:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-27-2024",
  "Hora": "00:21:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-27-2024",
  "Hora": "16:00:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-28-2024",
  "Hora": "00:10:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-28-2024",
  "Hora": "15:59:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "03-29-2024",
  "Hora": "00:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-01-2024",
  "Hora": "16:00:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-02-2024",
  "Hora": "00:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-02-2024",
  "Hora": "15:59:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-03-2024",
  "Hora": "00:30:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-03-2024",
  "Hora": "15:59:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-04-2024",
  "Hora": "00:04:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-04-2024",
  "Hora": "16:00:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-05-2024",
  "Hora": "00:10:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-05-2024",
  "Hora": "16:00:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-06-2024",
  "Hora": "00:02:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-06-2024",
  "Hora": "16:00:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-07-2024",
  "Hora": "00:01:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-08-2024",
  "Hora": "16:00:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-09-2024",
  "Hora": "00:02:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-09-2024",
  "Hora": "16:00:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-10-2024",
  "Hora": "00:12:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-10-2024",
  "Hora": "16:00:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-11-2024",
  "Hora": "00:08:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-11-2024",
  "Hora": "16:00:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-12-2024",
  "Hora": "00:19:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-12-2024",
  "Hora": "16:00:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-13-2024",
  "Hora": "00:06:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-13-2024",
  "Hora": "15:58:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-14-2024",
  "Hora": "00:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199117556,
  "Date": "04-15-2024",
  "Hora": "16:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-18-2024",
  "Hora": "08:36:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-18-2024",
  "Hora": "18:22:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-19-2024",
  "Hora": "08:51:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-19-2024",
  "Hora": "18:03:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-20-2024",
  "Hora": "09:31:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-20-2024",
  "Hora": "18:03:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-21-2024",
  "Hora": "08:19:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-21-2024",
  "Hora": "20:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-22-2024",
  "Hora": "08:57:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-22-2024",
  "Hora": "17:04:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-23-2024",
  "Hora": "08:19:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-23-2024",
  "Hora": "14:01:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-25-2024",
  "Hora": "08:29:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-25-2024",
  "Hora": "20:01:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-26-2024",
  "Hora": "08:04:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-26-2024",
  "Hora": "20:03:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-27-2024",
  "Hora": "08:06:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-27-2024",
  "Hora": "20:03:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-28-2024",
  "Hora": "08:15:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "03-28-2024",
  "Hora": "23:37:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-01-2024",
  "Hora": "08:18:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-01-2024",
  "Hora": "18:02:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-02-2024",
  "Hora": "08:29:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-02-2024",
  "Hora": "18:02:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-03-2024",
  "Hora": "08:30:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-03-2024",
  "Hora": "18:03:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-05-2024",
  "Hora": "08:28:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-05-2024",
  "Hora": "17:01:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-08-2024",
  "Hora": "08:10:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-08-2024",
  "Hora": "17:01:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-09-2024",
  "Hora": "08:28:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-09-2024",
  "Hora": "20:00:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-10-2024",
  "Hora": "08:09:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-10-2024",
  "Hora": "20:01:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-11-2024",
  "Hora": "08:27:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-11-2024",
  "Hora": "16:20:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-12-2024",
  "Hora": "08:37:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-12-2024",
  "Hora": "17:02:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-13-2024",
  "Hora": "08:14:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-13-2024",
  "Hora": "13:48:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-13-2024",
  "Hora": "13:49:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-15-2024",
  "Hora": "08:10:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 175749179,
  "Date": "04-15-2024",
  "Hora": "18:03:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-18-2024",
  "Hora": "08:02:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-18-2024",
  "Hora": "18:01:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-19-2024",
  "Hora": "08:17:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-19-2024",
  "Hora": "18:15:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-20-2024",
  "Hora": "08:06:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-20-2024",
  "Hora": "17:58:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-21-2024",
  "Hora": "08:09:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-21-2024",
  "Hora": "18:04:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-22-2024",
  "Hora": "08:31:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-22-2024",
  "Hora": "18:07:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-25-2024",
  "Hora": "08:26:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-25-2024",
  "Hora": "17:59:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-26-2024",
  "Hora": "08:10:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-26-2024",
  "Hora": "18:02:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-27-2024",
  "Hora": "08:38:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-27-2024",
  "Hora": "18:06:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-28-2024",
  "Hora": "08:27:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "03-28-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-01-2024",
  "Hora": "08:13:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-01-2024",
  "Hora": "18:09:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-08-2024",
  "Hora": "09:17:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-08-2024",
  "Hora": "19:04:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-09-2024",
  "Hora": "09:22:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-09-2024",
  "Hora": "19:04:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-10-2024",
  "Hora": "09:21:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-10-2024",
  "Hora": "19:08:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-11-2024",
  "Hora": "09:22:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-11-2024",
  "Hora": "18:56:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-12-2024",
  "Hora": "09:26:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-12-2024",
  "Hora": "21:29:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-15-2024",
  "Hora": "09:49:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254625302,
  "Date": "04-15-2024",
  "Hora": "18:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 141767852,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-16-2024",
  "Hora": "12:59:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-16-2024",
  "Hora": "21:03:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-18-2024",
  "Hora": "16:02:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-19-2024",
  "Hora": "01:21:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-19-2024",
  "Hora": "15:53:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-20-2024",
  "Hora": "01:09:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-20-2024",
  "Hora": "16:01:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-21-2024",
  "Hora": "01:14:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-21-2024",
  "Hora": "16:07:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-22-2024",
  "Hora": "01:22:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-22-2024",
  "Hora": "13:02:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-22-2024",
  "Hora": "21:47:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-25-2024",
  "Hora": "10:49:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-25-2024",
  "Hora": "22:18:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-26-2024",
  "Hora": "10:52:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-26-2024",
  "Hora": "22:15:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-27-2024",
  "Hora": "10:48:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-27-2024",
  "Hora": "22:15:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-28-2024",
  "Hora": "10:44:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "03-28-2024",
  "Hora": "21:52:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-01-2024",
  "Hora": "15:57:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-02-2024",
  "Hora": "01:42:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-02-2024",
  "Hora": "15:46:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-03-2024",
  "Hora": "01:35:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-03-2024",
  "Hora": "15:50:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-04-2024",
  "Hora": "01:17:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-04-2024",
  "Hora": "15:45:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-05-2024",
  "Hora": "01:13:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-05-2024",
  "Hora": "11:04:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-05-2024",
  "Hora": "21:36:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-08-2024",
  "Hora": "10:50:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-08-2024",
  "Hora": "22:19:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-09-2024",
  "Hora": "10:54:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-09-2024",
  "Hora": "22:02:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-10-2024",
  "Hora": "10:56:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-10-2024",
  "Hora": "22:17:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-11-2024",
  "Hora": "10:49:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-11-2024",
  "Hora": "21:59:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-13-2024",
  "Hora": "21:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-15-2024",
  "Hora": "08:33:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205798021,
  "Date": "04-15-2024",
  "Hora": "18:02:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-16-2024",
  "Hora": "00:20:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-18-2024",
  "Hora": "15:53:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-19-2024",
  "Hora": "01:24:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-19-2024",
  "Hora": "02:17:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-19-2024",
  "Hora": "16:03:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-20-2024",
  "Hora": "01:15:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-20-2024",
  "Hora": "15:55:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-21-2024",
  "Hora": "01:15:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-21-2024",
  "Hora": "15:53:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-22-2024",
  "Hora": "01:22:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-22-2024",
  "Hora": "16:04:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-23-2024",
  "Hora": "00:20:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-25-2024",
  "Hora": "16:09:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-26-2024",
  "Hora": "01:26:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-26-2024",
  "Hora": "16:04:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-27-2024",
  "Hora": "01:18:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-27-2024",
  "Hora": "15:51:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-28-2024",
  "Hora": "01:16:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-28-2024",
  "Hora": "16:20:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "03-29-2024",
  "Hora": "00:00:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-04-2024",
  "Hora": "15:56:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-05-2024",
  "Hora": "01:26:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-05-2024",
  "Hora": "01:26:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-05-2024",
  "Hora": "15:55:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-06-2024",
  "Hora": "00:01:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-08-2024",
  "Hora": "16:07:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-09-2024",
  "Hora": "01:22:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-09-2024",
  "Hora": "15:44:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-10-2024",
  "Hora": "01:16:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-10-2024",
  "Hora": "15:39:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-11-2024",
  "Hora": "01:16:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-11-2024",
  "Hora": "16:00:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-12-2024",
  "Hora": "01:02:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-12-2024",
  "Hora": "16:04:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-13-2024",
  "Hora": "00:23:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 142579618,
  "Date": "04-15-2024",
  "Hora": "15:43:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-16-2024",
  "Hora": "03:44:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-16-2024",
  "Hora": "10:58:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-18-2024",
  "Hora": "02:37:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-18-2024",
  "Hora": "11:06:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-19-2024",
  "Hora": "03:07:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-19-2024",
  "Hora": "11:08:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-20-2024",
  "Hora": "02:49:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-20-2024",
  "Hora": "11:02:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-21-2024",
  "Hora": "02:30:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-21-2024",
  "Hora": "11:10:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-22-2024",
  "Hora": "02:31:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-22-2024",
  "Hora": "10:59:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-23-2024",
  "Hora": "02:22:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-23-2024",
  "Hora": "11:02:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-25-2024",
  "Hora": "03:30:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-25-2024",
  "Hora": "12:04:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-26-2024",
  "Hora": "04:05:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-26-2024",
  "Hora": "12:03:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-27-2024",
  "Hora": "04:15:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-27-2024",
  "Hora": "12:08:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-28-2024",
  "Hora": "03:55:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "03-28-2024",
  "Hora": "11:58:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-01-2024",
  "Hora": "04:01:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-01-2024",
  "Hora": "12:10:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-02-2024",
  "Hora": "03:55:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-02-2024",
  "Hora": "12:09:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-03-2024",
  "Hora": "03:35:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-03-2024",
  "Hora": "12:09:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-04-2024",
  "Hora": "03:58:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-04-2024",
  "Hora": "12:04:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-05-2024",
  "Hora": "03:32:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-05-2024",
  "Hora": "12:01:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-06-2024",
  "Hora": "03:24:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-06-2024",
  "Hora": "11:02:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-08-2024",
  "Hora": "02:30:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-08-2024",
  "Hora": "11:05:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-09-2024",
  "Hora": "02:47:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-09-2024",
  "Hora": "11:07:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-10-2024",
  "Hora": "02:51:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-10-2024",
  "Hora": "11:03:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-11-2024",
  "Hora": "02:54:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-11-2024",
  "Hora": "11:02:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-12-2024",
  "Hora": "02:57:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-12-2024",
  "Hora": "11:06:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-13-2024",
  "Hora": "02:59:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-13-2024",
  "Hora": "10:56:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-15-2024",
  "Hora": "03:51:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 125141935,
  "Date": "04-15-2024",
  "Hora": "12:01:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-16-2024",
  "Hora": "06:54:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-16-2024",
  "Hora": "13:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-18-2024",
  "Hora": "06:51:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-18-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-19-2024",
  "Hora": "06:56:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-19-2024",
  "Hora": "15:00:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-20-2024",
  "Hora": "06:55:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-20-2024",
  "Hora": "15:00:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-21-2024",
  "Hora": "06:53:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-21-2024",
  "Hora": "15:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-22-2024",
  "Hora": "06:53:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-22-2024",
  "Hora": "15:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-23-2024",
  "Hora": "06:49:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-23-2024",
  "Hora": "15:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-25-2024",
  "Hora": "06:57:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-25-2024",
  "Hora": "15:00:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-26-2024",
  "Hora": "06:58:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-26-2024",
  "Hora": "15:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-27-2024",
  "Hora": "06:48:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-27-2024",
  "Hora": "13:05:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-28-2024",
  "Hora": "06:56:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "03-28-2024",
  "Hora": "15:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-03-2024",
  "Hora": "06:55:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-03-2024",
  "Hora": "15:00:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-04-2024",
  "Hora": "07:00:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-04-2024",
  "Hora": "15:01:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-05-2024",
  "Hora": "06:57:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-05-2024",
  "Hora": "15:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-06-2024",
  "Hora": "07:01:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-06-2024",
  "Hora": "14:40:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-08-2024",
  "Hora": "06:57:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-08-2024",
  "Hora": "15:00:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-09-2024",
  "Hora": "06:57:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-09-2024",
  "Hora": "15:00:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-10-2024",
  "Hora": "06:52:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-10-2024",
  "Hora": "15:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-11-2024",
  "Hora": "06:52:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-11-2024",
  "Hora": "15:00:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-12-2024",
  "Hora": "09:44:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-12-2024",
  "Hora": "15:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-13-2024",
  "Hora": "06:49:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-13-2024",
  "Hora": "14:30:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-15-2024",
  "Hora": "06:50:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 199416650,
  "Date": "04-15-2024",
  "Hora": "15:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-16-2024",
  "Hora": "05:21:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-16-2024",
  "Hora": "12:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-18-2024",
  "Hora": "03:42:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-18-2024",
  "Hora": "12:21:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-19-2024",
  "Hora": "04:00:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-19-2024",
  "Hora": "12:07:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-20-2024",
  "Hora": "03:44:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-20-2024",
  "Hora": "11:48:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-21-2024",
  "Hora": "03:40:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-21-2024",
  "Hora": "11:46:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-22-2024",
  "Hora": "03:42:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-22-2024",
  "Hora": "11:23:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-23-2024",
  "Hora": "03:41:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-23-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-25-2024",
  "Hora": "01:52:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-25-2024",
  "Hora": "10:05:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-26-2024",
  "Hora": "01:43:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-26-2024",
  "Hora": "10:06:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-27-2024",
  "Hora": "01:46:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-27-2024",
  "Hora": "10:04:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-28-2024",
  "Hora": "01:43:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "03-28-2024",
  "Hora": "10:12:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-01-2024",
  "Hora": "04:37:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-01-2024",
  "Hora": "13:06:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-02-2024",
  "Hora": "04:00:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-02-2024",
  "Hora": "12:05:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-03-2024",
  "Hora": "03:50:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-03-2024",
  "Hora": "14:43:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-04-2024",
  "Hora": "03:49:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-04-2024",
  "Hora": "12:05:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-05-2024",
  "Hora": "04:05:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-05-2024",
  "Hora": "12:00:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-06-2024",
  "Hora": "04:24:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-06-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-08-2024",
  "Hora": "01:20:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-08-2024",
  "Hora": "10:04:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-09-2024",
  "Hora": "02:57:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-09-2024",
  "Hora": "11:00:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-10-2024",
  "Hora": "02:19:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-10-2024",
  "Hora": "10:18:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-11-2024",
  "Hora": "01:46:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-11-2024",
  "Hora": "10:02:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-12-2024",
  "Hora": "01:49:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-12-2024",
  "Hora": "10:02:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-13-2024",
  "Hora": "01:40:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-13-2024",
  "Hora": "04:24:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-13-2024",
  "Hora": "10:02:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-15-2024",
  "Hora": "03:34:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 268668977,
  "Date": "04-15-2024",
  "Hora": "11:56:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-16-2024",
  "Hora": "03:26:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-17-2024",
  "Hora": "19:46:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-18-2024",
  "Hora": "02:07:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-18-2024",
  "Hora": "18:06:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-19-2024",
  "Hora": "03:39:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-19-2024",
  "Hora": "17:58:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-20-2024",
  "Hora": "03:04:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-20-2024",
  "Hora": "17:49:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-21-2024",
  "Hora": "03:43:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-21-2024",
  "Hora": "17:57:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-22-2024",
  "Hora": "03:45:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-25-2024",
  "Hora": "17:53:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-26-2024",
  "Hora": "03:25:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-26-2024",
  "Hora": "18:08:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-27-2024",
  "Hora": "03:54:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-27-2024",
  "Hora": "18:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-28-2024",
  "Hora": "03:46:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-28-2024",
  "Hora": "18:15:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "03-29-2024",
  "Hora": "02:00:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-01-2024",
  "Hora": "17:57:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-02-2024",
  "Hora": "04:04:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-03-2024",
  "Hora": "17:45:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-04-2024",
  "Hora": "03:25:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-04-2024",
  "Hora": "18:07:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-05-2024",
  "Hora": "03:24:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-05-2024",
  "Hora": "18:53:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-06-2024",
  "Hora": "03:26:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-07-2024",
  "Hora": "19:41:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-08-2024",
  "Hora": "02:02:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-08-2024",
  "Hora": "18:06:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-09-2024",
  "Hora": "03:34:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-09-2024",
  "Hora": "18:14:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-10-2024",
  "Hora": "03:38:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-10-2024",
  "Hora": "17:53:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-11-2024",
  "Hora": "03:41:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-11-2024",
  "Hora": "18:14:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-12-2024",
  "Hora": "03:35:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "27212907K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-16-2024",
  "Hora": "07:57:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-16-2024",
  "Hora": "14:00:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-18-2024",
  "Hora": "07:58:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-18-2024",
  "Hora": "18:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-19-2024",
  "Hora": "07:51:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-19-2024",
  "Hora": "18:02:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-20-2024",
  "Hora": "07:52:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-20-2024",
  "Hora": "18:01:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-21-2024",
  "Hora": "07:54:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-21-2024",
  "Hora": "18:04:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-22-2024",
  "Hora": "07:53:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-22-2024",
  "Hora": "17:02:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-25-2024",
  "Hora": "07:50:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-25-2024",
  "Hora": "18:00:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-25-2024",
  "Hora": "18:00:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-26-2024",
  "Hora": "07:54:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-26-2024",
  "Hora": "18:01:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-27-2024",
  "Hora": "07:48:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-27-2024",
  "Hora": "18:02:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-27-2024",
  "Hora": "18:02:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-27-2024",
  "Hora": "18:02:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-28-2024",
  "Hora": "08:04:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "03-28-2024",
  "Hora": "18:01:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-01-2024",
  "Hora": "07:50:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-01-2024",
  "Hora": "18:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-02-2024",
  "Hora": "07:47:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-02-2024",
  "Hora": "18:02:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-03-2024",
  "Hora": "07:55:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-03-2024",
  "Hora": "18:02:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-03-2024",
  "Hora": "18:02:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-04-2024",
  "Hora": "08:11:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-04-2024",
  "Hora": "18:04:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-05-2024",
  "Hora": "07:56:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-05-2024",
  "Hora": "17:00:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-06-2024",
  "Hora": "07:46:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-06-2024",
  "Hora": "14:01:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-08-2024",
  "Hora": "07:52:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-08-2024",
  "Hora": "18:03:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-09-2024",
  "Hora": "07:47:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-09-2024",
  "Hora": "18:02:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-10-2024",
  "Hora": "07:54:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-10-2024",
  "Hora": "18:01:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-11-2024",
  "Hora": "07:51:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-11-2024",
  "Hora": "18:01:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-12-2024",
  "Hora": "07:52:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-12-2024",
  "Hora": "07:52:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-12-2024",
  "Hora": "17:03:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-15-2024",
  "Hora": "07:51:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 259174171,
  "Date": "04-15-2024",
  "Hora": "18:02:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-16-2024",
  "Hora": "04:51:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-16-2024",
  "Hora": "12:08:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-18-2024",
  "Hora": "05:54:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-18-2024",
  "Hora": "14:09:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-19-2024",
  "Hora": "04:53:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-19-2024",
  "Hora": "13:11:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-20-2024",
  "Hora": "04:51:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-20-2024",
  "Hora": "13:13:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-21-2024",
  "Hora": "04:51:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-21-2024",
  "Hora": "13:21:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-22-2024",
  "Hora": "04:50:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-22-2024",
  "Hora": "13:11:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-23-2024",
  "Hora": "04:50:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-23-2024",
  "Hora": "04:50:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-23-2024",
  "Hora": "04:50:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-23-2024",
  "Hora": "04:50:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-23-2024",
  "Hora": "04:50:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-23-2024",
  "Hora": "04:50:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-23-2024",
  "Hora": "04:50:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-23-2024",
  "Hora": "04:50:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-23-2024",
  "Hora": "04:50:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-23-2024",
  "Hora": "04:50:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-23-2024",
  "Hora": "10:55:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-25-2024",
  "Hora": "05:53:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-25-2024",
  "Hora": "14:03:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-26-2024",
  "Hora": "04:53:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-26-2024",
  "Hora": "13:11:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-27-2024",
  "Hora": "04:53:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "03-27-2024",
  "Hora": "13:11:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-02-2024",
  "Hora": "03:42:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-02-2024",
  "Hora": "15:04:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-03-2024",
  "Hora": "03:31:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-03-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-03-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-03-2024",
  "Hora": "15:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-05-2024",
  "Hora": "04:56:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-05-2024",
  "Hora": "13:25:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-06-2024",
  "Hora": "04:55:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-06-2024",
  "Hora": "13:07:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-08-2024",
  "Hora": "05:52:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-08-2024",
  "Hora": "14:09:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-09-2024",
  "Hora": "05:00:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-09-2024",
  "Hora": "13:11:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-10-2024",
  "Hora": "04:51:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-10-2024",
  "Hora": "13:11:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-11-2024",
  "Hora": "04:51:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-11-2024",
  "Hora": "12:50:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-12-2024",
  "Hora": "04:53:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-12-2024",
  "Hora": "11:41:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-13-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-13-2024",
  "Hora": "13:11:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-15-2024",
  "Hora": "05:55:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 191053850,
  "Date": "04-15-2024",
  "Hora": "14:09:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-16-2024",
  "Hora": "00:17:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-16-2024",
  "Hora": "12:41:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-16-2024",
  "Hora": "21:00:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-18-2024",
  "Hora": "15:41:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-19-2024",
  "Hora": "01:25:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-19-2024",
  "Hora": "15:41:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-20-2024",
  "Hora": "01:17:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-20-2024",
  "Hora": "15:41:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-21-2024",
  "Hora": "01:23:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-21-2024",
  "Hora": "15:42:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-22-2024",
  "Hora": "01:28:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-22-2024",
  "Hora": "16:03:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-23-2024",
  "Hora": "00:21:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-23-2024",
  "Hora": "12:26:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-23-2024",
  "Hora": "20:19:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-25-2024",
  "Hora": "15:45:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-26-2024",
  "Hora": "01:25:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-26-2024",
  "Hora": "15:47:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-27-2024",
  "Hora": "01:19:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-27-2024",
  "Hora": "15:51:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-28-2024",
  "Hora": "01:20:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-28-2024",
  "Hora": "15:52:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "03-28-2024",
  "Hora": "23:53:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-01-2024",
  "Hora": "15:43:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-02-2024",
  "Hora": "01:43:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-02-2024",
  "Hora": "15:51:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-03-2024",
  "Hora": "01:36:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-03-2024",
  "Hora": "15:48:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-04-2024",
  "Hora": "01:21:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-04-2024",
  "Hora": "15:51:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-05-2024",
  "Hora": "01:23:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-06-2024",
  "Hora": "12:41:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-06-2024",
  "Hora": "20:45:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-08-2024",
  "Hora": "15:45:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-09-2024",
  "Hora": "01:23:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-09-2024",
  "Hora": "15:44:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-10-2024",
  "Hora": "01:25:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-10-2024",
  "Hora": "15:58:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-11-2024",
  "Hora": "01:14:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-11-2024",
  "Hora": "15:48:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-12-2024",
  "Hora": "01:15:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-12-2024",
  "Hora": "15:49:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-13-2024",
  "Hora": "00:17:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-13-2024",
  "Hora": "16:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 272387990,
  "Date": "04-15-2024",
  "Hora": "15:45:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-16-2024",
  "Hora": "12:44:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-16-2024",
  "Hora": "21:01:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-18-2024",
  "Hora": "15:08:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-19-2024",
  "Hora": "01:19:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-19-2024",
  "Hora": "15:31:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-20-2024",
  "Hora": "01:09:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-20-2024",
  "Hora": "15:18:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-21-2024",
  "Hora": "01:18:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-21-2024",
  "Hora": "15:56:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-22-2024",
  "Hora": "01:16:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-22-2024",
  "Hora": "10:54:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-22-2024",
  "Hora": "21:41:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-25-2024",
  "Hora": "10:48:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-25-2024",
  "Hora": "22:22:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-26-2024",
  "Hora": "10:51:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-26-2024",
  "Hora": "22:12:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-27-2024",
  "Hora": "10:47:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-27-2024",
  "Hora": "22:08:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-28-2024",
  "Hora": "10:44:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "03-28-2024",
  "Hora": "21:52:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-01-2024",
  "Hora": "15:21:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-02-2024",
  "Hora": "01:41:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-02-2024",
  "Hora": "15:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-03-2024",
  "Hora": "01:31:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-03-2024",
  "Hora": "15:27:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-04-2024",
  "Hora": "01:12:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-04-2024",
  "Hora": "14:33:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-05-2024",
  "Hora": "01:17:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-05-2024",
  "Hora": "11:06:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-05-2024",
  "Hora": "21:36:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-08-2024",
  "Hora": "10:50:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-08-2024",
  "Hora": "22:17:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-09-2024",
  "Hora": "10:54:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-09-2024",
  "Hora": "22:00:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-10-2024",
  "Hora": "10:56:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-10-2024",
  "Hora": "21:59:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-11-2024",
  "Hora": "10:49:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-11-2024",
  "Hora": "21:59:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-13-2024",
  "Hora": "21:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-15-2024",
  "Hora": "08:13:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-15-2024",
  "Hora": "17:57:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 171494699,
  "Date": "04-15-2024",
  "Hora": "17:57:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-18-2024",
  "Hora": "08:33:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-18-2024",
  "Hora": "19:55:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-19-2024",
  "Hora": "08:17:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-19-2024",
  "Hora": "21:53:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-20-2024",
  "Hora": "08:35:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-20-2024",
  "Hora": "22:24:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-21-2024",
  "Hora": "08:33:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-21-2024",
  "Hora": "20:01:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-22-2024",
  "Hora": "08:33:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-22-2024",
  "Hora": "19:26:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-25-2024",
  "Hora": "08:32:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-25-2024",
  "Hora": "20:35:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-26-2024",
  "Hora": "08:38:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-26-2024",
  "Hora": "20:20:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-27-2024",
  "Hora": "08:36:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-27-2024",
  "Hora": "20:06:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-28-2024",
  "Hora": "08:33:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "03-28-2024",
  "Hora": "22:11:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-01-2024",
  "Hora": "08:25:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-01-2024",
  "Hora": "19:39:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-02-2024",
  "Hora": "08:36:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-02-2024",
  "Hora": "18:02:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-03-2024",
  "Hora": "08:33:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-03-2024",
  "Hora": "18:32:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-04-2024",
  "Hora": "08:43:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-04-2024",
  "Hora": "19:31:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-05-2024",
  "Hora": "08:32:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-05-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-08-2024",
  "Hora": "08:35:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-08-2024",
  "Hora": "19:54:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-09-2024",
  "Hora": "09:52:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-09-2024",
  "Hora": "19:35:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-10-2024",
  "Hora": "08:32:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-10-2024",
  "Hora": "19:22:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-11-2024",
  "Hora": "09:43:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-11-2024",
  "Hora": "19:05:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-12-2024",
  "Hora": "09:49:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-12-2024",
  "Hora": "19:07:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-15-2024",
  "Hora": "08:35:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154848150,
  "Date": "04-15-2024",
  "Hora": "18:42:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-16-2024",
  "Hora": "00:20:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-18-2024",
  "Hora": "16:05:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-19-2024",
  "Hora": "01:25:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-19-2024",
  "Hora": "16:41:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-20-2024",
  "Hora": "01:18:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-20-2024",
  "Hora": "16:31:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-21-2024",
  "Hora": "01:23:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-21-2024",
  "Hora": "16:57:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-22-2024",
  "Hora": "01:22:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-22-2024",
  "Hora": "17:14:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-23-2024",
  "Hora": "00:24:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-25-2024",
  "Hora": "15:47:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-26-2024",
  "Hora": "01:27:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-26-2024",
  "Hora": "15:48:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-27-2024",
  "Hora": "01:24:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-27-2024",
  "Hora": "16:30:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-28-2024",
  "Hora": "01:16:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-28-2024",
  "Hora": "17:37:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "03-29-2024",
  "Hora": "00:00:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-01-2024",
  "Hora": "16:59:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-02-2024",
  "Hora": "01:44:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-02-2024",
  "Hora": "16:34:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-03-2024",
  "Hora": "02:36:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-03-2024",
  "Hora": "16:23:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-04-2024",
  "Hora": "01:24:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-04-2024",
  "Hora": "16:33:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-05-2024",
  "Hora": "01:26:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-05-2024",
  "Hora": "16:10:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-06-2024",
  "Hora": "00:01:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-08-2024",
  "Hora": "15:57:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-09-2024",
  "Hora": "01:24:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-10-2024",
  "Hora": "16:08:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-11-2024",
  "Hora": "01:18:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265705960,
  "Date": "04-15-2024",
  "Hora": "17:03:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-16-2024",
  "Hora": "02:57:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-16-2024",
  "Hora": "10:57:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-18-2024",
  "Hora": "03:59:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-18-2024",
  "Hora": "12:00:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-19-2024",
  "Hora": "03:59:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-19-2024",
  "Hora": "12:10:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-20-2024",
  "Hora": "04:08:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-20-2024",
  "Hora": "12:00:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-21-2024",
  "Hora": "04:14:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-21-2024",
  "Hora": "12:01:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-22-2024",
  "Hora": "05:20:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-22-2024",
  "Hora": "10:55:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-23-2024",
  "Hora": "04:06:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-23-2024",
  "Hora": "11:59:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-25-2024",
  "Hora": "04:14:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-25-2024",
  "Hora": "12:05:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-26-2024",
  "Hora": "04:25:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-26-2024",
  "Hora": "12:03:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-27-2024",
  "Hora": "04:06:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-27-2024",
  "Hora": "12:05:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-28-2024",
  "Hora": "04:12:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "03-28-2024",
  "Hora": "12:00:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-01-2024",
  "Hora": "04:13:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-01-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-01-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-03-2024",
  "Hora": "05:01:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-03-2024",
  "Hora": "12:04:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-04-2024",
  "Hora": "04:46:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-04-2024",
  "Hora": "11:56:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-05-2024",
  "Hora": "04:57:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-05-2024",
  "Hora": "12:10:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-06-2024",
  "Hora": "04:22:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-06-2024",
  "Hora": "11:04:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-08-2024",
  "Hora": "02:50:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-08-2024",
  "Hora": "11:06:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-09-2024",
  "Hora": "02:49:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-09-2024",
  "Hora": "11:05:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-10-2024",
  "Hora": "02:57:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-10-2024",
  "Hora": "11:03:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-11-2024",
  "Hora": "02:53:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-11-2024",
  "Hora": "11:02:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-12-2024",
  "Hora": "02:47:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-12-2024",
  "Hora": "11:01:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-15-2024",
  "Hora": "04:31:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21437451K",
  "Date": "04-15-2024",
  "Hora": "11:59:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-16-2024",
  "Hora": "08:31:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-16-2024",
  "Hora": "18:00:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-18-2024",
  "Hora": "08:25:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-18-2024",
  "Hora": "18:00:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-19-2024",
  "Hora": "08:27:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-19-2024",
  "Hora": "18:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-20-2024",
  "Hora": "08:18:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-20-2024",
  "Hora": "18:01:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-21-2024",
  "Hora": "08:29:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-21-2024",
  "Hora": "18:01:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-22-2024",
  "Hora": "08:30:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-22-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-23-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-25-2024",
  "Hora": "08:33:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-25-2024",
  "Hora": "18:06:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-26-2024",
  "Hora": "08:19:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-26-2024",
  "Hora": "18:00:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-27-2024",
  "Hora": "08:20:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-27-2024",
  "Hora": "18:08:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-28-2024",
  "Hora": "08:23:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "03-28-2024",
  "Hora": "18:04:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-01-2024",
  "Hora": "08:23:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-01-2024",
  "Hora": "17:30:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-02-2024",
  "Hora": "08:30:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-02-2024",
  "Hora": "18:00:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-03-2024",
  "Hora": "08:26:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-03-2024",
  "Hora": "18:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-04-2024",
  "Hora": "08:28:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-04-2024",
  "Hora": "18:04:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-05-2024",
  "Hora": "08:17:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-05-2024",
  "Hora": "18:00:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-06-2024",
  "Hora": "08:16:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-06-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-08-2024",
  "Hora": "08:22:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-08-2024",
  "Hora": "17:31:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-09-2024",
  "Hora": "08:30:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-09-2024",
  "Hora": "15:34:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-10-2024",
  "Hora": "08:18:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-10-2024",
  "Hora": "18:00:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-11-2024",
  "Hora": "08:22:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-11-2024",
  "Hora": "18:00:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-12-2024",
  "Hora": "08:27:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-12-2024",
  "Hora": "18:00:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-13-2024",
  "Hora": "08:14:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-13-2024",
  "Hora": "13:04:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-15-2024",
  "Hora": "08:27:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200088565,
  "Date": "04-15-2024",
  "Hora": "17:30:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-18-2024",
  "Hora": "12:53:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-18-2024",
  "Hora": "18:30:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-19-2024",
  "Hora": "12:58:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-19-2024",
  "Hora": "18:10:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-20-2024",
  "Hora": "12:50:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-20-2024",
  "Hora": "17:47:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-20-2024",
  "Hora": "22:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-20-2024",
  "Hora": "22:47:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-21-2024",
  "Hora": "12:59:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-21-2024",
  "Hora": "17:27:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-22-2024",
  "Hora": "13:00:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-22-2024",
  "Hora": "17:33:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-25-2024",
  "Hora": "13:02:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-25-2024",
  "Hora": "19:04:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-26-2024",
  "Hora": "13:02:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-26-2024",
  "Hora": "18:33:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-27-2024",
  "Hora": "12:56:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-27-2024",
  "Hora": "18:50:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-28-2024",
  "Hora": "13:14:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "03-28-2024",
  "Hora": "18:03:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "04-01-2024",
  "Hora": "13:25:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "04-01-2024",
  "Hora": "19:41:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 145637384,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-16-2024",
  "Hora": "04:52:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-16-2024",
  "Hora": "14:00:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-18-2024",
  "Hora": "04:55:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-18-2024",
  "Hora": "12:01:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-19-2024",
  "Hora": "04:51:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-19-2024",
  "Hora": "14:30:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-20-2024",
  "Hora": "04:57:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-20-2024",
  "Hora": "14:31:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-21-2024",
  "Hora": "04:53:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-21-2024",
  "Hora": "14:31:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-22-2024",
  "Hora": "04:55:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-22-2024",
  "Hora": "14:30:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-25-2024",
  "Hora": "04:59:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-25-2024",
  "Hora": "14:34:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-27-2024",
  "Hora": "04:54:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-27-2024",
  "Hora": "14:15:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-28-2024",
  "Hora": "04:53:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "03-28-2024",
  "Hora": "14:30:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-01-2024",
  "Hora": "04:55:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-01-2024",
  "Hora": "14:31:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-02-2024",
  "Hora": "04:55:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-02-2024",
  "Hora": "12:05:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-03-2024",
  "Hora": "04:53:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-03-2024",
  "Hora": "14:31:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-04-2024",
  "Hora": "04:53:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-04-2024",
  "Hora": "14:31:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-05-2024",
  "Hora": "04:53:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-05-2024",
  "Hora": "14:30:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-08-2024",
  "Hora": "05:12:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-08-2024",
  "Hora": "14:30:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-10-2024",
  "Hora": "04:54:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-10-2024",
  "Hora": "14:30:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-11-2024",
  "Hora": "04:52:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-11-2024",
  "Hora": "14:31:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-12-2024",
  "Hora": "04:51:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-12-2024",
  "Hora": "14:30:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-13-2024",
  "Hora": "04:53:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-13-2024",
  "Hora": "14:34:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-15-2024",
  "Hora": "04:51:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173018002,
  "Date": "04-15-2024",
  "Hora": "14:31:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-16-2024",
  "Hora": "07:46:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-16-2024",
  "Hora": "14:00:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-18-2024",
  "Hora": "07:52:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-18-2024",
  "Hora": "20:00:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-19-2024",
  "Hora": "07:47:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-19-2024",
  "Hora": "18:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-20-2024",
  "Hora": "08:36:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-20-2024",
  "Hora": "20:01:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-21-2024",
  "Hora": "07:49:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-21-2024",
  "Hora": "20:00:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-22-2024",
  "Hora": "07:49:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-22-2024",
  "Hora": "17:01:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-25-2024",
  "Hora": "07:49:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-25-2024",
  "Hora": "18:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-26-2024",
  "Hora": "07:51:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-26-2024",
  "Hora": "20:01:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-27-2024",
  "Hora": "07:48:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-27-2024",
  "Hora": "20:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-28-2024",
  "Hora": "07:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "03-28-2024",
  "Hora": "23:27:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-04-2024",
  "Hora": "07:50:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-04-2024",
  "Hora": "18:01:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-05-2024",
  "Hora": "07:47:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-05-2024",
  "Hora": "17:01:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-06-2024",
  "Hora": "07:52:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-06-2024",
  "Hora": "14:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-08-2024",
  "Hora": "07:48:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-08-2024",
  "Hora": "18:01:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-09-2024",
  "Hora": "07:43:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-09-2024",
  "Hora": "18:01:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-11-2024",
  "Hora": "07:45:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-11-2024",
  "Hora": "20:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-12-2024",
  "Hora": "07:44:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-12-2024",
  "Hora": "17:01:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-13-2024",
  "Hora": "07:43:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-13-2024",
  "Hora": "14:01:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-15-2024",
  "Hora": "07:45:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 273995749,
  "Date": "04-15-2024",
  "Hora": "18:00:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-16-2024",
  "Hora": "00:15:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-18-2024",
  "Hora": "16:05:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-19-2024",
  "Hora": "01:43:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-19-2024",
  "Hora": "16:03:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-20-2024",
  "Hora": "00:50:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-20-2024",
  "Hora": "16:03:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-21-2024",
  "Hora": "01:05:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-21-2024",
  "Hora": "15:59:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-22-2024",
  "Hora": "01:30:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-25-2024",
  "Hora": "16:09:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-26-2024",
  "Hora": "01:23:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-26-2024",
  "Hora": "16:08:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-27-2024",
  "Hora": "01:17:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-27-2024",
  "Hora": "16:18:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-28-2024",
  "Hora": "01:04:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-28-2024",
  "Hora": "16:14:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "03-28-2024",
  "Hora": "23:58:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-01-2024",
  "Hora": "15:58:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-02-2024",
  "Hora": "01:45:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-02-2024",
  "Hora": "16:02:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-03-2024",
  "Hora": "02:36:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-03-2024",
  "Hora": "15:55:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-04-2024",
  "Hora": "01:27:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-04-2024",
  "Hora": "15:53:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-05-2024",
  "Hora": "01:31:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-05-2024",
  "Hora": "16:07:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-06-2024",
  "Hora": "00:09:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-08-2024",
  "Hora": "16:00:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-09-2024",
  "Hora": "01:21:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-09-2024",
  "Hora": "15:55:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-10-2024",
  "Hora": "01:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-10-2024",
  "Hora": "15:46:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-11-2024",
  "Hora": "01:15:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-11-2024",
  "Hora": "16:00:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-11-2024",
  "Hora": "16:00:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-12-2024",
  "Hora": "01:02:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-12-2024",
  "Hora": "15:53:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-13-2024",
  "Hora": "00:20:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-13-2024",
  "Hora": "16:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-15-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-15-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-15-2024",
  "Hora": "16:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138995054,
  "Date": "04-15-2024",
  "Hora": "22:23:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-16-2024",
  "Hora": "03:46:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-16-2024",
  "Hora": "12:02:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-18-2024",
  "Hora": "03:46:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-18-2024",
  "Hora": "12:31:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-19-2024",
  "Hora": "03:37:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-19-2024",
  "Hora": "12:16:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-20-2024",
  "Hora": "04:37:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-20-2024",
  "Hora": "11:53:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-21-2024",
  "Hora": "04:08:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-21-2024",
  "Hora": "12:00:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-22-2024",
  "Hora": "04:03:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-22-2024",
  "Hora": "11:36:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-23-2024",
  "Hora": "04:02:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-23-2024",
  "Hora": "10:59:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-25-2024",
  "Hora": "01:57:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-25-2024",
  "Hora": "12:00:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-26-2024",
  "Hora": "01:59:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-26-2024",
  "Hora": "12:04:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-27-2024",
  "Hora": "04:27:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-27-2024",
  "Hora": "12:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-28-2024",
  "Hora": "01:56:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "03-28-2024",
  "Hora": "10:05:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-02-2024",
  "Hora": "03:21:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-02-2024",
  "Hora": "12:16:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-03-2024",
  "Hora": "04:03:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-03-2024",
  "Hora": "12:13:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-04-2024",
  "Hora": "03:27:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-04-2024",
  "Hora": "12:09:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-05-2024",
  "Hora": "03:56:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-05-2024",
  "Hora": "12:00:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-06-2024",
  "Hora": "04:05:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-06-2024",
  "Hora": "12:37:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-08-2024",
  "Hora": "04:06:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-08-2024",
  "Hora": "12:19:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-09-2024",
  "Hora": "04:01:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-09-2024",
  "Hora": "12:08:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-10-2024",
  "Hora": "03:56:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-10-2024",
  "Hora": "12:00:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-11-2024",
  "Hora": "03:38:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-11-2024",
  "Hora": "11:58:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-12-2024",
  "Hora": "03:58:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-12-2024",
  "Hora": "12:04:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-13-2024",
  "Hora": "04:02:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-13-2024",
  "Hora": "11:47:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-15-2024",
  "Hora": "02:08:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-15-2024",
  "Hora": "10:01:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154124233,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-16-2024",
  "Hora": "02:34:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-16-2024",
  "Hora": "10:58:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-18-2024",
  "Hora": "03:46:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-18-2024",
  "Hora": "12:06:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-19-2024",
  "Hora": "03:30:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-19-2024",
  "Hora": "12:19:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-20-2024",
  "Hora": "03:35:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-20-2024",
  "Hora": "12:04:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-21-2024",
  "Hora": "03:38:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-21-2024",
  "Hora": "12:01:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-22-2024",
  "Hora": "03:42:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-22-2024",
  "Hora": "11:04:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-23-2024",
  "Hora": "03:40:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-23-2024",
  "Hora": "12:04:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-25-2024",
  "Hora": "03:20:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-25-2024",
  "Hora": "12:07:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-26-2024",
  "Hora": "03:51:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-26-2024",
  "Hora": "12:05:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-27-2024",
  "Hora": "04:41:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-27-2024",
  "Hora": "12:07:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-28-2024",
  "Hora": "03:36:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "03-28-2024",
  "Hora": "12:03:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-01-2024",
  "Hora": "03:41:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-01-2024",
  "Hora": "12:13:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-01-2024",
  "Hora": "12:14:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-02-2024",
  "Hora": "04:03:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-02-2024",
  "Hora": "12:14:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-03-2024",
  "Hora": "03:46:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-03-2024",
  "Hora": "12:10:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-04-2024",
  "Hora": "03:53:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-04-2024",
  "Hora": "11:58:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-05-2024",
  "Hora": "03:44:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-05-2024",
  "Hora": "12:12:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-06-2024",
  "Hora": "04:46:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-06-2024",
  "Hora": "11:02:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-08-2024",
  "Hora": "02:29:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-08-2024",
  "Hora": "11:06:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-09-2024",
  "Hora": "02:47:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-09-2024",
  "Hora": "11:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-10-2024",
  "Hora": "02:51:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-10-2024",
  "Hora": "11:09:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-11-2024",
  "Hora": "02:54:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-11-2024",
  "Hora": "11:03:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-12-2024",
  "Hora": "02:57:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-12-2024",
  "Hora": "11:03:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-13-2024",
  "Hora": "02:59:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-13-2024",
  "Hora": "11:03:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-15-2024",
  "Hora": "03:32:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195468702,
  "Date": "04-15-2024",
  "Hora": "12:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-16-2024",
  "Hora": "05:55:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-16-2024",
  "Hora": "14:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-18-2024",
  "Hora": "08:29:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-18-2024",
  "Hora": "18:00:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-19-2024",
  "Hora": "08:28:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-19-2024",
  "Hora": "18:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-20-2024",
  "Hora": "08:29:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-20-2024",
  "Hora": "18:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-21-2024",
  "Hora": "08:30:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-21-2024",
  "Hora": "18:00:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-22-2024",
  "Hora": "08:54:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-22-2024",
  "Hora": "18:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-23-2024",
  "Hora": "06:06:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-23-2024",
  "Hora": "06:06:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-23-2024",
  "Hora": "06:06:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-23-2024",
  "Hora": "06:06:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-23-2024",
  "Hora": "06:06:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-23-2024",
  "Hora": "06:06:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-23-2024",
  "Hora": "06:06:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-23-2024",
  "Hora": "06:06:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-23-2024",
  "Hora": "06:06:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-23-2024",
  "Hora": "06:06:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-23-2024",
  "Hora": "16:03:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-25-2024",
  "Hora": "08:29:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-25-2024",
  "Hora": "20:03:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-26-2024",
  "Hora": "06:01:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-26-2024",
  "Hora": "18:01:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-27-2024",
  "Hora": "09:09:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-27-2024",
  "Hora": "18:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-28-2024",
  "Hora": "08:29:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "03-28-2024",
  "Hora": "18:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-01-2024",
  "Hora": "08:28:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-01-2024",
  "Hora": "18:00:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-02-2024",
  "Hora": "08:30:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-02-2024",
  "Hora": "18:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-03-2024",
  "Hora": "08:28:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-03-2024",
  "Hora": "18:00:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-04-2024",
  "Hora": "08:26:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-04-2024",
  "Hora": "18:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-05-2024",
  "Hora": "08:28:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-05-2024",
  "Hora": "18:00:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-08-2024",
  "Hora": "08:27:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-08-2024",
  "Hora": "18:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-09-2024",
  "Hora": "08:28:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-09-2024",
  "Hora": "18:00:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-10-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-10-2024",
  "Hora": "18:00:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-11-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-11-2024",
  "Hora": "18:00:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-12-2024",
  "Hora": "08:29:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-12-2024",
  "Hora": "18:00:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-15-2024",
  "Hora": "08:28:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190931358,
  "Date": "04-15-2024",
  "Hora": "18:00:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-16-2024",
  "Hora": "04:51:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-16-2024",
  "Hora": "12:16:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-18-2024",
  "Hora": "05:54:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-18-2024",
  "Hora": "14:03:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-19-2024",
  "Hora": "04:53:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-19-2024",
  "Hora": "13:07:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-20-2024",
  "Hora": "05:23:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-20-2024",
  "Hora": "13:09:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-21-2024",
  "Hora": "04:52:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-21-2024",
  "Hora": "13:08:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-22-2024",
  "Hora": "04:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-22-2024",
  "Hora": "13:07:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-23-2024",
  "Hora": "04:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-23-2024",
  "Hora": "04:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-23-2024",
  "Hora": "04:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-23-2024",
  "Hora": "04:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-23-2024",
  "Hora": "04:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-23-2024",
  "Hora": "04:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-23-2024",
  "Hora": "04:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-23-2024",
  "Hora": "04:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-23-2024",
  "Hora": "04:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-23-2024",
  "Hora": "04:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-23-2024",
  "Hora": "11:06:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-25-2024",
  "Hora": "05:54:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-25-2024",
  "Hora": "14:01:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-26-2024",
  "Hora": "04:53:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-26-2024",
  "Hora": "13:08:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-27-2024",
  "Hora": "05:23:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-27-2024",
  "Hora": "13:07:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-28-2024",
  "Hora": "04:55:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "03-28-2024",
  "Hora": "13:00:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-01-2024",
  "Hora": "05:54:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-01-2024",
  "Hora": "14:06:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-02-2024",
  "Hora": "04:52:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-02-2024",
  "Hora": "13:09:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-03-2024",
  "Hora": "05:25:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-03-2024",
  "Hora": "13:13:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-04-2024",
  "Hora": "04:49:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-04-2024",
  "Hora": "13:06:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-05-2024",
  "Hora": "04:57:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-05-2024",
  "Hora": "13:01:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-06-2024",
  "Hora": "04:56:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-06-2024",
  "Hora": "13:02:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-08-2024",
  "Hora": "05:52:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-08-2024",
  "Hora": "14:03:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-09-2024",
  "Hora": "05:01:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-09-2024",
  "Hora": "13:03:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-10-2024",
  "Hora": "04:51:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-10-2024",
  "Hora": "13:09:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-12-2024",
  "Hora": "04:54:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-12-2024",
  "Hora": "13:05:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-13-2024",
  "Hora": "04:52:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-13-2024",
  "Hora": "13:03:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-15-2024",
  "Hora": "05:56:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206488778,
  "Date": "04-15-2024",
  "Hora": "14:07:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-19-2024",
  "Hora": "15:40:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-20-2024",
  "Hora": "01:17:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-20-2024",
  "Hora": "15:41:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-21-2024",
  "Hora": "01:23:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-21-2024",
  "Hora": "15:41:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-22-2024",
  "Hora": "01:28:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-22-2024",
  "Hora": "16:03:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-23-2024",
  "Hora": "00:21:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-23-2024",
  "Hora": "12:26:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-23-2024",
  "Hora": "20:19:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-25-2024",
  "Hora": "15:11:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-26-2024",
  "Hora": "01:22:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-26-2024",
  "Hora": "15:46:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-27-2024",
  "Hora": "01:20:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-27-2024",
  "Hora": "15:51:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-28-2024",
  "Hora": "01:16:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-28-2024",
  "Hora": "15:51:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "03-28-2024",
  "Hora": "23:56:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-01-2024",
  "Hora": "15:43:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-02-2024",
  "Hora": "01:43:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-02-2024",
  "Hora": "15:50:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-03-2024",
  "Hora": "02:33:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-03-2024",
  "Hora": "15:47:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-04-2024",
  "Hora": "01:25:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-04-2024",
  "Hora": "15:51:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-05-2024",
  "Hora": "01:26:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-05-2024",
  "Hora": "15:45:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-06-2024",
  "Hora": "00:04:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-08-2024",
  "Hora": "15:44:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-09-2024",
  "Hora": "01:24:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-09-2024",
  "Hora": "15:44:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-10-2024",
  "Hora": "01:22:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-10-2024",
  "Hora": "15:57:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-11-2024",
  "Hora": "01:12:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-11-2024",
  "Hora": "15:47:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-12-2024",
  "Hora": "01:13:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-12-2024",
  "Hora": "15:48:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-13-2024",
  "Hora": "00:18:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-13-2024",
  "Hora": "16:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271862156,
  "Date": "04-15-2024",
  "Hora": "15:44:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-16-2024",
  "Hora": "00:19:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-18-2024",
  "Hora": "15:41:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-19-2024",
  "Hora": "01:22:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-19-2024",
  "Hora": "15:41:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-20-2024",
  "Hora": "01:16:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-20-2024",
  "Hora": "15:41:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-21-2024",
  "Hora": "01:21:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-21-2024",
  "Hora": "15:41:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-22-2024",
  "Hora": "01:20:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-22-2024",
  "Hora": "16:03:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-23-2024",
  "Hora": "00:17:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-25-2024",
  "Hora": "15:44:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-26-2024",
  "Hora": "01:21:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-26-2024",
  "Hora": "15:46:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-27-2024",
  "Hora": "01:21:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-27-2024",
  "Hora": "15:51:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-28-2024",
  "Hora": "01:13:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-28-2024",
  "Hora": "15:52:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "03-28-2024",
  "Hora": "23:54:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-01-2024",
  "Hora": "15:43:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-02-2024",
  "Hora": "01:37:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-02-2024",
  "Hora": "15:50:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-03-2024",
  "Hora": "02:35:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-03-2024",
  "Hora": "03:31:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-03-2024",
  "Hora": "16:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-04-2024",
  "Hora": "01:22:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-04-2024",
  "Hora": "15:50:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-05-2024",
  "Hora": "01:25:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-05-2024",
  "Hora": "15:45:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-06-2024",
  "Hora": "00:01:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-08-2024",
  "Hora": "15:44:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-09-2024",
  "Hora": "01:21:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-09-2024",
  "Hora": "15:44:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-10-2024",
  "Hora": "01:12:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-10-2024",
  "Hora": "15:57:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-11-2024",
  "Hora": "01:03:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-11-2024",
  "Hora": "15:47:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-12-2024",
  "Hora": "00:54:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-12-2024",
  "Hora": "15:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-13-2024",
  "Hora": "00:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 173390327,
  "Date": "04-15-2024",
  "Hora": "15:45:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-16-2024",
  "Hora": "03:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-17-2024",
  "Hora": "18:49:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-18-2024",
  "Hora": "02:06:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-18-2024",
  "Hora": "17:58:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-19-2024",
  "Hora": "03:01:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-19-2024",
  "Hora": "17:52:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-20-2024",
  "Hora": "03:04:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-20-2024",
  "Hora": "18:00:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-21-2024",
  "Hora": "03:13:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-21-2024",
  "Hora": "18:03:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-22-2024",
  "Hora": "04:02:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-23-2024",
  "Hora": "12:35:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-23-2024",
  "Hora": "19:54:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-24-2024",
  "Hora": "18:49:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-25-2024",
  "Hora": "02:12:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-25-2024",
  "Hora": "17:50:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-26-2024",
  "Hora": "03:24:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-26-2024",
  "Hora": "18:52:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-27-2024",
  "Hora": "03:06:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-28-2024",
  "Hora": "19:10:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "03-29-2024",
  "Hora": "01:39:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-01-2024",
  "Hora": "17:53:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-02-2024",
  "Hora": "03:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-02-2024",
  "Hora": "18:02:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-03-2024",
  "Hora": "03:55:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-03-2024",
  "Hora": "18:05:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-04-2024",
  "Hora": "03:06:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-04-2024",
  "Hora": "17:45:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-05-2024",
  "Hora": "03:24:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-07-2024",
  "Hora": "18:50:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-08-2024",
  "Hora": "02:02:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-08-2024",
  "Hora": "17:02:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-09-2024",
  "Hora": "03:32:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-09-2024",
  "Hora": "18:05:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-10-2024",
  "Hora": "03:26:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-10-2024",
  "Hora": "18:06:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-11-2024",
  "Hora": "03:35:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-12-2024",
  "Hora": "18:06:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-13-2024",
  "Hora": "03:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-13-2024",
  "Hora": "22:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 160760168,
  "Date": "04-15-2024",
  "Hora": "18:58:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-16-2024",
  "Hora": "03:27:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-18-2024",
  "Hora": "18:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-19-2024",
  "Hora": "03:14:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-19-2024",
  "Hora": "17:55:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-20-2024",
  "Hora": "03:28:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-20-2024",
  "Hora": "17:59:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-21-2024",
  "Hora": "03:17:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-21-2024",
  "Hora": "17:52:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-22-2024",
  "Hora": "03:22:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-22-2024",
  "Hora": "18:54:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-23-2024",
  "Hora": "02:58:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-25-2024",
  "Hora": "18:00:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-26-2024",
  "Hora": "03:26:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-26-2024",
  "Hora": "18:00:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-27-2024",
  "Hora": "03:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-27-2024",
  "Hora": "18:00:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-28-2024",
  "Hora": "03:35:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-28-2024",
  "Hora": "03:36:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-28-2024",
  "Hora": "18:03:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "03-28-2024",
  "Hora": "23:50:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-01-2024",
  "Hora": "18:01:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-02-2024",
  "Hora": "03:44:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-02-2024",
  "Hora": "18:03:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-03-2024",
  "Hora": "03:49:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-03-2024",
  "Hora": "18:00:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-04-2024",
  "Hora": "03:20:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-04-2024",
  "Hora": "18:00:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-05-2024",
  "Hora": "03:21:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-05-2024",
  "Hora": "18:59:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-06-2024",
  "Hora": "02:59:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-07-2024",
  "Hora": "20:01:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-08-2024",
  "Hora": "02:04:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-09-2024",
  "Hora": "17:58:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-10-2024",
  "Hora": "03:23:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-10-2024",
  "Hora": "18:00:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-11-2024",
  "Hora": "03:31:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-11-2024",
  "Hora": "17:59:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-12-2024",
  "Hora": "03:14:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-12-2024",
  "Hora": "19:05:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-13-2024",
  "Hora": "03:05:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200603508,
  "Date": "04-15-2024",
  "Hora": "19:48:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 254916498,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-18-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-18-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-19-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-19-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-20-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-20-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-21-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-21-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-22-2024",
  "Hora": "10:29:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-22-2024",
  "Hora": "15:30:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-22-2024",
  "Hora": "16:30:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-22-2024",
  "Hora": "17:00:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-25-2024",
  "Hora": "07:04:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-25-2024",
  "Hora": "15:51:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-25-2024",
  "Hora": "16:42:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-25-2024",
  "Hora": "17:01:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-26-2024",
  "Hora": "07:01:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-26-2024",
  "Hora": "15:03:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-26-2024",
  "Hora": "16:02:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-26-2024",
  "Hora": "19:00:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-27-2024",
  "Hora": "07:06:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-27-2024",
  "Hora": "14:29:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-27-2024",
  "Hora": "15:31:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-27-2024",
  "Hora": "17:04:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-28-2024",
  "Hora": "07:17:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-28-2024",
  "Hora": "14:39:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-28-2024",
  "Hora": "15:39:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "03-28-2024",
  "Hora": "17:00:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-01-2024",
  "Hora": "06:56:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-01-2024",
  "Hora": "14:07:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-01-2024",
  "Hora": "15:07:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-01-2024",
  "Hora": "17:01:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-02-2024",
  "Hora": "06:54:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-02-2024",
  "Hora": "14:12:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-02-2024",
  "Hora": "15:12:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-02-2024",
  "Hora": "17:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-03-2024",
  "Hora": "07:00:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-03-2024",
  "Hora": "14:13:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-03-2024",
  "Hora": "15:13:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-03-2024",
  "Hora": "17:00:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-04-2024",
  "Hora": "06:57:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-04-2024",
  "Hora": "14:17:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-04-2024",
  "Hora": "15:17:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-04-2024",
  "Hora": "17:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-05-2024",
  "Hora": "06:56:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-05-2024",
  "Hora": "13:20:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-05-2024",
  "Hora": "14:19:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-05-2024",
  "Hora": "17:00:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-06-2024",
  "Hora": "07:46:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-06-2024",
  "Hora": "15:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-08-2024",
  "Hora": "06:58:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-08-2024",
  "Hora": "14:32:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-08-2024",
  "Hora": "17:01:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-09-2024",
  "Hora": "07:05:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-09-2024",
  "Hora": "15:03:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-09-2024",
  "Hora": "16:02:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-09-2024",
  "Hora": "17:00:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-10-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-10-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-11-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-11-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-12-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-12-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-15-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 154689648,
  "Date": "04-15-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-16-2024",
  "Hora": "09:33:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-16-2024",
  "Hora": "17:57:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-18-2024",
  "Hora": "09:31:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-18-2024",
  "Hora": "16:32:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-19-2024",
  "Hora": "09:33:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-19-2024",
  "Hora": "16:49:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-20-2024",
  "Hora": "09:34:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-20-2024",
  "Hora": "18:04:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-21-2024",
  "Hora": "09:30:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-21-2024",
  "Hora": "16:51:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-22-2024",
  "Hora": "09:28:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-22-2024",
  "Hora": "17:19:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-23-2024",
  "Hora": "09:32:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-23-2024",
  "Hora": "16:11:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-25-2024",
  "Hora": "09:37:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-25-2024",
  "Hora": "17:20:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-26-2024",
  "Hora": "09:34:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-26-2024",
  "Hora": "17:12:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-27-2024",
  "Hora": "09:28:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-27-2024",
  "Hora": "16:57:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-28-2024",
  "Hora": "09:25:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "03-28-2024",
  "Hora": "17:18:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-01-2024",
  "Hora": "09:36:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-01-2024",
  "Hora": "19:03:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-02-2024",
  "Hora": "09:28:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-02-2024",
  "Hora": "18:06:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-03-2024",
  "Hora": "09:31:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-03-2024",
  "Hora": "17:52:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-04-2024",
  "Hora": "09:40:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-04-2024",
  "Hora": "17:44:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-05-2024",
  "Hora": "09:27:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-05-2024",
  "Hora": "18:14:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-06-2024",
  "Hora": "09:22:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-06-2024",
  "Hora": "16:08:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-08-2024",
  "Hora": "09:26:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-08-2024",
  "Hora": "17:06:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-09-2024",
  "Hora": "09:27:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-09-2024",
  "Hora": "17:07:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-10-2024",
  "Hora": "09:34:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-10-2024",
  "Hora": "17:58:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-11-2024",
  "Hora": "09:28:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-11-2024",
  "Hora": "17:48:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-12-2024",
  "Hora": "09:30:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-12-2024",
  "Hora": "16:45:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-13-2024",
  "Hora": "09:27:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-13-2024",
  "Hora": "15:46:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-15-2024",
  "Hora": "12:12:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21072415K",
  "Date": "04-15-2024",
  "Hora": "16:41:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-16-2024",
  "Hora": "12:48:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-16-2024",
  "Hora": "20:58:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-18-2024",
  "Hora": "15:54:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-19-2024",
  "Hora": "01:18:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-19-2024",
  "Hora": "15:57:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-20-2024",
  "Hora": "01:03:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-20-2024",
  "Hora": "15:33:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-21-2024",
  "Hora": "01:03:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-21-2024",
  "Hora": "16:21:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-22-2024",
  "Hora": "01:10:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-22-2024",
  "Hora": "11:09:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-22-2024",
  "Hora": "21:44:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-25-2024",
  "Hora": "10:47:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-25-2024",
  "Hora": "22:16:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-26-2024",
  "Hora": "11:07:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-26-2024",
  "Hora": "22:11:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-27-2024",
  "Hora": "11:07:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-27-2024",
  "Hora": "22:00:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-28-2024",
  "Hora": "10:54:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "03-28-2024",
  "Hora": "21:43:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-01-2024",
  "Hora": "15:55:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-02-2024",
  "Hora": "01:42:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-02-2024",
  "Hora": "15:52:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-03-2024",
  "Hora": "01:32:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-03-2024",
  "Hora": "16:02:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-04-2024",
  "Hora": "01:07:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-04-2024",
  "Hora": "16:01:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-05-2024",
  "Hora": "01:12:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-05-2024",
  "Hora": "11:31:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-05-2024",
  "Hora": "21:35:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-08-2024",
  "Hora": "10:55:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-08-2024",
  "Hora": "22:10:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-09-2024",
  "Hora": "10:50:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-09-2024",
  "Hora": "22:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-10-2024",
  "Hora": "13:04:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-10-2024",
  "Hora": "22:00:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-11-2024",
  "Hora": "11:02:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-11-2024",
  "Hora": "21:54:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-13-2024",
  "Hora": "21:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-15-2024",
  "Hora": "08:31:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201395682,
  "Date": "04-15-2024",
  "Hora": "18:02:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-16-2024",
  "Hora": "03:47:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-16-2024",
  "Hora": "11:53:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-17-2024",
  "Hora": "22:03:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-18-2024",
  "Hora": "10:36:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-19-2024",
  "Hora": "03:50:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-19-2024",
  "Hora": "12:20:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-20-2024",
  "Hora": "04:10:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-20-2024",
  "Hora": "12:04:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-21-2024",
  "Hora": "01:50:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-21-2024",
  "Hora": "12:09:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-22-2024",
  "Hora": "01:44:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-22-2024",
  "Hora": "12:05:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-23-2024",
  "Hora": "03:52:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-23-2024",
  "Hora": "11:05:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-24-2024",
  "Hora": "21:58:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-25-2024",
  "Hora": "10:47:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-26-2024",
  "Hora": "05:11:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-26-2024",
  "Hora": "12:17:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-27-2024",
  "Hora": "03:55:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-27-2024",
  "Hora": "12:09:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-28-2024",
  "Hora": "03:53:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-28-2024",
  "Hora": "12:16:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "03-31-2024",
  "Hora": "21:59:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-01-2024",
  "Hora": "14:18:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-02-2024",
  "Hora": "05:21:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-02-2024",
  "Hora": "12:31:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-03-2024",
  "Hora": "03:52:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-03-2024",
  "Hora": "14:48:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-04-2024",
  "Hora": "04:46:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-04-2024",
  "Hora": "12:34:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-05-2024",
  "Hora": "03:56:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-05-2024",
  "Hora": "12:15:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-06-2024",
  "Hora": "04:03:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-06-2024",
  "Hora": "12:15:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-07-2024",
  "Hora": "22:01:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-08-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-09-2024",
  "Hora": "03:57:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-09-2024",
  "Hora": "12:13:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-10-2024",
  "Hora": "03:39:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-10-2024",
  "Hora": "12:00:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-11-2024",
  "Hora": "03:57:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-11-2024",
  "Hora": "12:12:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-12-2024",
  "Hora": "03:43:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-12-2024",
  "Hora": "11:59:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-13-2024",
  "Hora": "03:52:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-13-2024",
  "Hora": "11:48:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-14-2024",
  "Hora": "22:05:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-15-2024",
  "Hora": "01:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-15-2024",
  "Hora": "01:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-15-2024",
  "Hora": "02:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-15-2024",
  "Hora": "04:10:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260196804,
  "Date": "04-15-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "03-25-2024",
  "Hora": "12:48:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "03-25-2024",
  "Hora": "21:45:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "03-26-2024",
  "Hora": "12:49:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "03-26-2024",
  "Hora": "22:30:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "03-27-2024",
  "Hora": "12:50:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "03-27-2024",
  "Hora": "21:30:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "03-28-2024",
  "Hora": "12:55:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "03-28-2024",
  "Hora": "21:07:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-01-2024",
  "Hora": "12:51:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-01-2024",
  "Hora": "22:32:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-02-2024",
  "Hora": "12:50:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-02-2024",
  "Hora": "20:53:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-03-2024",
  "Hora": "12:48:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-03-2024",
  "Hora": "20:32:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-04-2024",
  "Hora": "12:52:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-04-2024",
  "Hora": "20:42:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-05-2024",
  "Hora": "12:52:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-05-2024",
  "Hora": "20:39:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-08-2024",
  "Hora": "12:47:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-08-2024",
  "Hora": "22:24:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-09-2024",
  "Hora": "12:48:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-09-2024",
  "Hora": "21:34:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-10-2024",
  "Hora": "12:49:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-10-2024",
  "Hora": "21:05:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-11-2024",
  "Hora": "13:01:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-11-2024",
  "Hora": "21:37:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-12-2024",
  "Hora": "12:51:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-12-2024",
  "Hora": "21:02:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-15-2024",
  "Hora": "12:49:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197807482,
  "Date": "04-15-2024",
  "Hora": "22:31:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "03-26-2024",
  "Hora": "05:44:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "03-26-2024",
  "Hora": "13:45:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "03-27-2024",
  "Hora": "05:43:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "03-27-2024",
  "Hora": "13:45:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "03-28-2024",
  "Hora": "05:39:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "03-28-2024",
  "Hora": "13:44:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-01-2024",
  "Hora": "06:00:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-01-2024",
  "Hora": "14:00:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-02-2024",
  "Hora": "05:40:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-02-2024",
  "Hora": "13:45:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-02-2024",
  "Hora": "13:45:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-03-2024",
  "Hora": "05:40:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-03-2024",
  "Hora": "13:46:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-04-2024",
  "Hora": "05:44:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-04-2024",
  "Hora": "13:44:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-05-2024",
  "Hora": "05:42:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-05-2024",
  "Hora": "13:47:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-06-2024",
  "Hora": "05:40:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-06-2024",
  "Hora": "13:45:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-08-2024",
  "Hora": "05:56:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-08-2024",
  "Hora": "14:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-09-2024",
  "Hora": "05:45:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-09-2024",
  "Hora": "13:46:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-10-2024",
  "Hora": "05:44:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-10-2024",
  "Hora": "13:45:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-11-2024",
  "Hora": "05:40:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-11-2024",
  "Hora": "13:45:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-12-2024",
  "Hora": "05:44:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-12-2024",
  "Hora": "13:45:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-13-2024",
  "Hora": "05:41:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-13-2024",
  "Hora": "13:48:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-15-2024",
  "Hora": "05:52:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198109150,
  "Date": "04-15-2024",
  "Hora": "13:59:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-18-2024",
  "Hora": "07:58:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-18-2024",
  "Hora": "18:05:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-19-2024",
  "Hora": "08:08:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-19-2024",
  "Hora": "18:12:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-20-2024",
  "Hora": "08:00:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-20-2024",
  "Hora": "18:19:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-21-2024",
  "Hora": "08:10:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-21-2024",
  "Hora": "18:08:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-22-2024",
  "Hora": "08:06:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-22-2024",
  "Hora": "17:03:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-25-2024",
  "Hora": "08:08:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-25-2024",
  "Hora": "18:08:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-26-2024",
  "Hora": "07:48:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-26-2024",
  "Hora": "18:07:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-27-2024",
  "Hora": "08:00:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-27-2024",
  "Hora": "18:08:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-28-2024",
  "Hora": "07:54:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "03-28-2024",
  "Hora": "18:08:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-01-2024",
  "Hora": "07:54:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-01-2024",
  "Hora": "18:08:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-01-2024",
  "Hora": "20:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-02-2024",
  "Hora": "07:51:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-02-2024",
  "Hora": "18:15:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-02-2024",
  "Hora": "18:15:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-03-2024",
  "Hora": "08:16:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-03-2024",
  "Hora": "18:25:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-04-2024",
  "Hora": "08:15:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-04-2024",
  "Hora": "08:15:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-04-2024",
  "Hora": "18:01:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-04-2024",
  "Hora": "22:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-05-2024",
  "Hora": "08:08:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-05-2024",
  "Hora": "17:11:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-05-2024",
  "Hora": "21:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-08-2024",
  "Hora": "07:49:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-08-2024",
  "Hora": "18:07:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-08-2024",
  "Hora": "20:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-09-2024",
  "Hora": "08:02:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-09-2024",
  "Hora": "19:51:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-10-2024",
  "Hora": "07:48:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-10-2024",
  "Hora": "07:48:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-10-2024",
  "Hora": "18:16:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-11-2024",
  "Hora": "07:53:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-11-2024",
  "Hora": "18:17:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-12-2024",
  "Hora": "07:59:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-12-2024",
  "Hora": "17:24:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-15-2024",
  "Hora": "07:41:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271695276,
  "Date": "04-15-2024",
  "Hora": "18:10:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-16-2024",
  "Hora": "04:48:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-16-2024",
  "Hora": "12:01:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-18-2024",
  "Hora": "05:50:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-18-2024",
  "Hora": "14:02:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-19-2024",
  "Hora": "04:52:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-19-2024",
  "Hora": "13:06:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-20-2024",
  "Hora": "04:49:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-20-2024",
  "Hora": "13:08:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-21-2024",
  "Hora": "04:57:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-21-2024",
  "Hora": "12:59:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-22-2024",
  "Hora": "04:57:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-22-2024",
  "Hora": "13:03:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-23-2024",
  "Hora": "04:55:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-23-2024",
  "Hora": "13:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-25-2024",
  "Hora": "05:56:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-25-2024",
  "Hora": "13:59:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-26-2024",
  "Hora": "04:54:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-26-2024",
  "Hora": "12:59:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-27-2024",
  "Hora": "04:58:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-27-2024",
  "Hora": "13:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-28-2024",
  "Hora": "04:59:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "03-28-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-01-2024",
  "Hora": "06:00:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-01-2024",
  "Hora": "12:59:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-02-2024",
  "Hora": "03:55:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-02-2024",
  "Hora": "12:02:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-03-2024",
  "Hora": "03:54:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-03-2024",
  "Hora": "12:03:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-04-2024",
  "Hora": "05:00:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-04-2024",
  "Hora": "12:02:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-05-2024",
  "Hora": "04:54:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-05-2024",
  "Hora": "11:59:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-06-2024",
  "Hora": "05:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-06-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-08-2024",
  "Hora": "06:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-08-2024",
  "Hora": "14:20:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-09-2024",
  "Hora": "05:01:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-09-2024",
  "Hora": "13:01:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-10-2024",
  "Hora": "04:56:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-10-2024",
  "Hora": "12:06:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-11-2024",
  "Hora": "04:56:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-11-2024",
  "Hora": "13:00:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-12-2024",
  "Hora": "04:57:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-12-2024",
  "Hora": "13:06:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-13-2024",
  "Hora": "04:54:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-15-2024",
  "Hora": "05:55:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 150102804,
  "Date": "04-15-2024",
  "Hora": "14:04:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-01-2024",
  "Hora": "10:23:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-01-2024",
  "Hora": "16:10:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-02-2024",
  "Hora": "11:13:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-02-2024",
  "Hora": "14:15:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-02-2024",
  "Hora": "16:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-02-2024",
  "Hora": "20:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-03-2024",
  "Hora": "10:34:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-03-2024",
  "Hora": "14:15:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-04-2024",
  "Hora": "10:13:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-04-2024",
  "Hora": "14:17:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-05-2024",
  "Hora": "10:15:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-05-2024",
  "Hora": "14:15:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-06-2024",
  "Hora": "10:17:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-06-2024",
  "Hora": "14:15:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-08-2024",
  "Hora": "10:21:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-08-2024",
  "Hora": "14:33:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-09-2024",
  "Hora": "10:23:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-09-2024",
  "Hora": "14:27:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-10-2024",
  "Hora": "10:13:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-10-2024",
  "Hora": "14:19:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-11-2024",
  "Hora": "10:21:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-11-2024",
  "Hora": "10:22:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-11-2024",
  "Hora": "10:22:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-11-2024",
  "Hora": "14:39:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-12-2024",
  "Hora": "10:13:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-12-2024",
  "Hora": "14:16:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-13-2024",
  "Hora": "10:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-13-2024",
  "Hora": "14:24:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-15-2024",
  "Hora": "10:28:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 126500157,
  "Date": "04-15-2024",
  "Hora": "14:24:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 164904725,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-16-2024",
  "Hora": "09:35:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-16-2024",
  "Hora": "17:56:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-18-2024",
  "Hora": "09:53:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-18-2024",
  "Hora": "16:32:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-19-2024",
  "Hora": "09:15:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-19-2024",
  "Hora": "16:52:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-20-2024",
  "Hora": "09:20:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-20-2024",
  "Hora": "17:42:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-21-2024",
  "Hora": "09:17:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-21-2024",
  "Hora": "16:48:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-22-2024",
  "Hora": "09:22:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-22-2024",
  "Hora": "17:14:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-23-2024",
  "Hora": "09:24:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-23-2024",
  "Hora": "16:12:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-25-2024",
  "Hora": "09:21:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-25-2024",
  "Hora": "17:20:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-26-2024",
  "Hora": "09:24:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-26-2024",
  "Hora": "17:12:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-27-2024",
  "Hora": "09:23:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-27-2024",
  "Hora": "16:53:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-28-2024",
  "Hora": "09:24:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "03-28-2024",
  "Hora": "16:56:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-01-2024",
  "Hora": "08:40:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-01-2024",
  "Hora": "19:02:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-02-2024",
  "Hora": "08:32:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-02-2024",
  "Hora": "18:05:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-03-2024",
  "Hora": "09:19:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-03-2024",
  "Hora": "17:49:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-04-2024",
  "Hora": "09:17:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-04-2024",
  "Hora": "16:38:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-05-2024",
  "Hora": "09:17:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-05-2024",
  "Hora": "18:06:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-06-2024",
  "Hora": "12:06:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-06-2024",
  "Hora": "16:07:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-08-2024",
  "Hora": "09:13:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-08-2024",
  "Hora": "17:03:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-09-2024",
  "Hora": "09:28:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-09-2024",
  "Hora": "17:07:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-10-2024",
  "Hora": "09:33:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-10-2024",
  "Hora": "18:00:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-11-2024",
  "Hora": "09:17:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-11-2024",
  "Hora": "17:48:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-12-2024",
  "Hora": "09:15:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-12-2024",
  "Hora": "16:43:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-13-2024",
  "Hora": "09:24:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-13-2024",
  "Hora": "15:48:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-15-2024",
  "Hora": "09:22:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209525208,
  "Date": "04-15-2024",
  "Hora": "16:45:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-16-2024",
  "Hora": "03:38:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-16-2024",
  "Hora": "10:57:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-18-2024",
  "Hora": "02:28:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-18-2024",
  "Hora": "11:05:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-19-2024",
  "Hora": "02:53:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-19-2024",
  "Hora": "11:04:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-20-2024",
  "Hora": "02:39:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-20-2024",
  "Hora": "11:04:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-22-2024",
  "Hora": "02:30:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-22-2024",
  "Hora": "11:04:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-23-2024",
  "Hora": "02:21:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-23-2024",
  "Hora": "11:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-25-2024",
  "Hora": "04:07:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-25-2024",
  "Hora": "12:05:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-26-2024",
  "Hora": "05:13:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-26-2024",
  "Hora": "12:06:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-27-2024",
  "Hora": "03:45:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-27-2024",
  "Hora": "12:05:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-28-2024",
  "Hora": "06:56:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "03-28-2024",
  "Hora": "11:56:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-01-2024",
  "Hora": "03:50:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-01-2024",
  "Hora": "12:09:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-02-2024",
  "Hora": "04:32:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-02-2024",
  "Hora": "12:09:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-03-2024",
  "Hora": "03:59:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-03-2024",
  "Hora": "12:10:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-04-2024",
  "Hora": "03:51:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-04-2024",
  "Hora": "11:55:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-05-2024",
  "Hora": "03:43:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-05-2024",
  "Hora": "12:11:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-06-2024",
  "Hora": "03:46:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-06-2024",
  "Hora": "11:04:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-08-2024",
  "Hora": "02:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-08-2024",
  "Hora": "04:10:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-08-2024",
  "Hora": "11:06:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-09-2024",
  "Hora": "02:49:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-09-2024",
  "Hora": "11:05:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-10-2024",
  "Hora": "04:05:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-10-2024",
  "Hora": "11:03:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-11-2024",
  "Hora": "02:43:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-11-2024",
  "Hora": "11:02:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-12-2024",
  "Hora": "02:32:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-12-2024",
  "Hora": "11:01:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-13-2024",
  "Hora": "02:41:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-13-2024",
  "Hora": "11:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-15-2024",
  "Hora": "04:51:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209235471,
  "Date": "04-15-2024",
  "Hora": "11:59:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-16-2024",
  "Hora": "10:26:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-16-2024",
  "Hora": "17:58:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-18-2024",
  "Hora": "10:24:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-18-2024",
  "Hora": "16:38:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-19-2024",
  "Hora": "10:28:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-19-2024",
  "Hora": "16:47:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-20-2024",
  "Hora": "10:29:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-20-2024",
  "Hora": "17:38:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-21-2024",
  "Hora": "10:19:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-21-2024",
  "Hora": "16:47:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-22-2024",
  "Hora": "10:20:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-22-2024",
  "Hora": "17:13:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-23-2024",
  "Hora": "10:08:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-23-2024",
  "Hora": "16:16:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-25-2024",
  "Hora": "10:22:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-25-2024",
  "Hora": "17:30:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-26-2024",
  "Hora": "11:20:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-26-2024",
  "Hora": "17:16:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-27-2024",
  "Hora": "11:07:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-27-2024",
  "Hora": "17:05:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-28-2024",
  "Hora": "10:23:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "03-28-2024",
  "Hora": "17:05:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-02-2024",
  "Hora": "10:21:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-02-2024",
  "Hora": "18:02:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-10-2024",
  "Hora": "10:18:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-10-2024",
  "Hora": "17:55:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-11-2024",
  "Hora": "10:02:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-11-2024",
  "Hora": "17:48:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-12-2024",
  "Hora": "10:16:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-12-2024",
  "Hora": "16:41:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-13-2024",
  "Hora": "10:16:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-13-2024",
  "Hora": "15:47:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-15-2024",
  "Hora": "10:47:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 252510370,
  "Date": "04-15-2024",
  "Hora": "16:47:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-16-2024",
  "Hora": "04:49:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-16-2024",
  "Hora": "12:00:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-18-2024",
  "Hora": "05:50:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-18-2024",
  "Hora": "14:02:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-19-2024",
  "Hora": "04:52:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-19-2024",
  "Hora": "13:01:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-20-2024",
  "Hora": "04:49:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-20-2024",
  "Hora": "13:02:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-21-2024",
  "Hora": "04:57:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-21-2024",
  "Hora": "13:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-22-2024",
  "Hora": "04:58:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-22-2024",
  "Hora": "13:01:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-23-2024",
  "Hora": "04:50:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-23-2024",
  "Hora": "04:50:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-23-2024",
  "Hora": "04:50:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-23-2024",
  "Hora": "04:50:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-23-2024",
  "Hora": "04:50:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-23-2024",
  "Hora": "04:50:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-23-2024",
  "Hora": "04:50:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-23-2024",
  "Hora": "04:50:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-23-2024",
  "Hora": "04:50:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-23-2024",
  "Hora": "04:50:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-23-2024",
  "Hora": "13:02:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-25-2024",
  "Hora": "05:56:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-25-2024",
  "Hora": "14:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-26-2024",
  "Hora": "04:48:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-26-2024",
  "Hora": "13:00:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-27-2024",
  "Hora": "04:59:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-27-2024",
  "Hora": "13:02:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-28-2024",
  "Hora": "05:00:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "03-28-2024",
  "Hora": "13:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-01-2024",
  "Hora": "04:49:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-01-2024",
  "Hora": "13:02:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-02-2024",
  "Hora": "03:48:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-02-2024",
  "Hora": "12:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-03-2024",
  "Hora": "03:49:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-03-2024",
  "Hora": "12:01:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-04-2024",
  "Hora": "05:01:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-04-2024",
  "Hora": "12:01:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-05-2024",
  "Hora": "04:47:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-05-2024",
  "Hora": "12:02:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-06-2024",
  "Hora": "04:51:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-06-2024",
  "Hora": "12:01:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-08-2024",
  "Hora": "06:10:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-08-2024",
  "Hora": "14:00:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-09-2024",
  "Hora": "03:49:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-09-2024",
  "Hora": "12:00:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-10-2024",
  "Hora": "04:41:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-10-2024",
  "Hora": "12:06:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-11-2024",
  "Hora": "04:57:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-11-2024",
  "Hora": "13:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-12-2024",
  "Hora": "04:58:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-12-2024",
  "Hora": "13:01:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-13-2024",
  "Hora": "04:55:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-13-2024",
  "Hora": "13:01:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-15-2024",
  "Hora": "05:56:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 166306728,
  "Date": "04-15-2024",
  "Hora": "14:00:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-16-2024",
  "Hora": "00:20:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-19-2024",
  "Hora": "15:42:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-20-2024",
  "Hora": "01:18:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-20-2024",
  "Hora": "15:41:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-21-2024",
  "Hora": "01:23:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-21-2024",
  "Hora": "15:42:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-22-2024",
  "Hora": "01:23:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-22-2024",
  "Hora": "16:04:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-23-2024",
  "Hora": "00:22:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-25-2024",
  "Hora": "15:27:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-26-2024",
  "Hora": "01:27:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-26-2024",
  "Hora": "15:48:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-27-2024",
  "Hora": "01:24:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-27-2024",
  "Hora": "15:52:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-28-2024",
  "Hora": "01:17:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-28-2024",
  "Hora": "15:52:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "03-29-2024",
  "Hora": "00:00:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-01-2024",
  "Hora": "15:44:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-02-2024",
  "Hora": "01:44:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-02-2024",
  "Hora": "15:51:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-03-2024",
  "Hora": "02:35:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-03-2024",
  "Hora": "03:07:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-03-2024",
  "Hora": "03:36:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-03-2024",
  "Hora": "15:48:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-04-2024",
  "Hora": "01:24:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-04-2024",
  "Hora": "15:51:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-05-2024",
  "Hora": "01:27:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-05-2024",
  "Hora": "15:46:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-06-2024",
  "Hora": "00:01:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-08-2024",
  "Hora": "15:45:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-09-2024",
  "Hora": "01:24:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-09-2024",
  "Hora": "16:08:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-10-2024",
  "Hora": "01:25:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-10-2024",
  "Hora": "15:59:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-11-2024",
  "Hora": "01:18:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-11-2024",
  "Hora": "15:49:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-12-2024",
  "Hora": "01:14:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-12-2024",
  "Hora": "15:49:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-13-2024",
  "Hora": "00:23:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "26191882K",
  "Date": "04-15-2024",
  "Hora": "15:48:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-18-2024",
  "Hora": "08:29:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-18-2024",
  "Hora": "18:16:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-19-2024",
  "Hora": "08:21:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-19-2024",
  "Hora": "18:03:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-20-2024",
  "Hora": "08:38:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-20-2024",
  "Hora": "18:16:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-21-2024",
  "Hora": "08:49:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-21-2024",
  "Hora": "18:01:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-22-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-22-2024",
  "Hora": "17:57:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-25-2024",
  "Hora": "08:31:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-25-2024",
  "Hora": "18:06:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-26-2024",
  "Hora": "08:34:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-26-2024",
  "Hora": "18:04:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-27-2024",
  "Hora": "08:31:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-27-2024",
  "Hora": "18:01:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-28-2024",
  "Hora": "08:25:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "03-28-2024",
  "Hora": "18:20:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-01-2024",
  "Hora": "08:21:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-01-2024",
  "Hora": "18:14:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-02-2024",
  "Hora": "08:25:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-02-2024",
  "Hora": "18:10:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-03-2024",
  "Hora": "08:23:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-03-2024",
  "Hora": "18:12:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-04-2024",
  "Hora": "08:33:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-04-2024",
  "Hora": "18:10:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-05-2024",
  "Hora": "08:36:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-05-2024",
  "Hora": "18:12:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-06-2024",
  "Hora": "09:07:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-06-2024",
  "Hora": "18:58:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-08-2024",
  "Hora": "08:30:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-08-2024",
  "Hora": "19:31:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-09-2024",
  "Hora": "08:30:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-09-2024",
  "Hora": "18:18:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-10-2024",
  "Hora": "08:27:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-10-2024",
  "Hora": "20:07:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-11-2024",
  "Hora": "08:44:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-11-2024",
  "Hora": "18:13:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-12-2024",
  "Hora": "08:34:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-12-2024",
  "Hora": "18:21:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-15-2024",
  "Hora": "08:33:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 188508995,
  "Date": "04-15-2024",
  "Hora": "18:07:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-18-2024",
  "Hora": "08:22:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-18-2024",
  "Hora": "18:03:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-19-2024",
  "Hora": "08:21:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-19-2024",
  "Hora": "18:03:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-21-2024",
  "Hora": "08:19:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-21-2024",
  "Hora": "19:44:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-22-2024",
  "Hora": "08:19:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-22-2024",
  "Hora": "08:20:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-22-2024",
  "Hora": "16:43:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-25-2024",
  "Hora": "08:17:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-25-2024",
  "Hora": "18:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-26-2024",
  "Hora": "08:21:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-26-2024",
  "Hora": "08:21:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-26-2024",
  "Hora": "18:01:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-27-2024",
  "Hora": "08:18:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-27-2024",
  "Hora": "17:41:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-28-2024",
  "Hora": "08:15:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "03-28-2024",
  "Hora": "23:27:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-01-2024",
  "Hora": "08:17:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-01-2024",
  "Hora": "18:02:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-02-2024",
  "Hora": "08:17:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-02-2024",
  "Hora": "08:17:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-02-2024",
  "Hora": "18:03:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-02-2024",
  "Hora": "18:03:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-03-2024",
  "Hora": "08:14:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-03-2024",
  "Hora": "14:59:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-04-2024",
  "Hora": "08:14:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-04-2024",
  "Hora": "18:02:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-05-2024",
  "Hora": "08:17:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-05-2024",
  "Hora": "17:02:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-08-2024",
  "Hora": "08:05:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-08-2024",
  "Hora": "18:03:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-09-2024",
  "Hora": "08:14:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-09-2024",
  "Hora": "17:55:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-10-2024",
  "Hora": "08:11:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-10-2024",
  "Hora": "18:01:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-11-2024",
  "Hora": "08:07:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-11-2024",
  "Hora": "17:54:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-11-2024",
  "Hora": "17:54:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-12-2024",
  "Hora": "08:13:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-12-2024",
  "Hora": "16:42:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-15-2024",
  "Hora": "08:12:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 193145213,
  "Date": "04-15-2024",
  "Hora": "18:02:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-16-2024",
  "Hora": "07:46:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-16-2024",
  "Hora": "13:57:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-18-2024",
  "Hora": "07:29:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-18-2024",
  "Hora": "07:29:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-18-2024",
  "Hora": "18:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-19-2024",
  "Hora": "07:23:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-19-2024",
  "Hora": "18:01:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-20-2024",
  "Hora": "07:18:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-20-2024",
  "Hora": "18:00:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-21-2024",
  "Hora": "07:20:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-21-2024",
  "Hora": "07:22:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-21-2024",
  "Hora": "20:00:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-22-2024",
  "Hora": "07:22:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-22-2024",
  "Hora": "17:02:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-23-2024",
  "Hora": "08:14:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-23-2024",
  "Hora": "08:14:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-23-2024",
  "Hora": "08:14:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-23-2024",
  "Hora": "08:14:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-23-2024",
  "Hora": "08:14:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-23-2024",
  "Hora": "08:14:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-23-2024",
  "Hora": "08:14:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-23-2024",
  "Hora": "08:14:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-23-2024",
  "Hora": "08:14:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-23-2024",
  "Hora": "08:14:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-23-2024",
  "Hora": "13:48:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-25-2024",
  "Hora": "07:31:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-25-2024",
  "Hora": "20:00:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-26-2024",
  "Hora": "07:29:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-26-2024",
  "Hora": "20:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-27-2024",
  "Hora": "07:25:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-27-2024",
  "Hora": "18:01:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-28-2024",
  "Hora": "07:29:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "03-28-2024",
  "Hora": "23:28:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-01-2024",
  "Hora": "07:26:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-01-2024",
  "Hora": "18:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-02-2024",
  "Hora": "07:37:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-02-2024",
  "Hora": "18:01:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-03-2024",
  "Hora": "07:26:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-03-2024",
  "Hora": "18:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-04-2024",
  "Hora": "07:25:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-04-2024",
  "Hora": "18:01:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-08-2024",
  "Hora": "07:19:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-08-2024",
  "Hora": "18:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-09-2024",
  "Hora": "07:25:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-09-2024",
  "Hora": "18:02:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-10-2024",
  "Hora": "07:26:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-10-2024",
  "Hora": "20:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-11-2024",
  "Hora": "11:03:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-11-2024",
  "Hora": "20:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-12-2024",
  "Hora": "07:31:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-12-2024",
  "Hora": "17:02:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-13-2024",
  "Hora": "07:44:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-13-2024",
  "Hora": "14:01:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-15-2024",
  "Hora": "09:56:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165186494,
  "Date": "04-15-2024",
  "Hora": "18:01:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-18-2024",
  "Hora": "08:05:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-18-2024",
  "Hora": "18:02:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-19-2024",
  "Hora": "08:12:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-19-2024",
  "Hora": "18:03:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-20-2024",
  "Hora": "08:05:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-20-2024",
  "Hora": "18:03:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-21-2024",
  "Hora": "08:12:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-21-2024",
  "Hora": "18:00:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-22-2024",
  "Hora": "08:18:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-22-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-25-2024",
  "Hora": "07:51:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-25-2024",
  "Hora": "18:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-26-2024",
  "Hora": "10:37:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-26-2024",
  "Hora": "18:01:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-27-2024",
  "Hora": "07:54:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-27-2024",
  "Hora": "20:00:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-28-2024",
  "Hora": "08:07:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "03-28-2024",
  "Hora": "23:24:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-02-2024",
  "Hora": "08:02:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-02-2024",
  "Hora": "08:39:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-03-2024",
  "Hora": "08:05:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-03-2024",
  "Hora": "18:02:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-04-2024",
  "Hora": "08:09:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-04-2024",
  "Hora": "18:04:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-05-2024",
  "Hora": "07:54:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-05-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-08-2024",
  "Hora": "08:01:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-08-2024",
  "Hora": "18:02:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-09-2024",
  "Hora": "08:02:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-09-2024",
  "Hora": "18:02:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-10-2024",
  "Hora": "07:55:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-10-2024",
  "Hora": "18:01:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-11-2024",
  "Hora": "07:56:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-11-2024",
  "Hora": "18:01:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-12-2024",
  "Hora": "08:00:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-12-2024",
  "Hora": "17:02:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203361939,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-01-2024",
  "Hora": "06:00:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-01-2024",
  "Hora": "12:59:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-02-2024",
  "Hora": "03:55:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-02-2024",
  "Hora": "10:09:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-03-2024",
  "Hora": "04:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-03-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-03-2024",
  "Hora": "12:04:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-04-2024",
  "Hora": "05:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-04-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-05-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-05-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-06-2024",
  "Hora": "05:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-06-2024",
  "Hora": "09:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-08-2024",
  "Hora": "06:09:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-08-2024",
  "Hora": "14:02:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-09-2024",
  "Hora": "05:01:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-09-2024",
  "Hora": "13:04:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-10-2024",
  "Hora": "08:46:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-10-2024",
  "Hora": "19:33:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-11-2024",
  "Hora": "04:56:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-11-2024",
  "Hora": "13:00:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-12-2024",
  "Hora": "08:23:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-12-2024",
  "Hora": "20:05:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-13-2024",
  "Hora": "05:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-13-2024",
  "Hora": "11:50:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-15-2024",
  "Hora": "05:55:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 174814929,
  "Date": "04-15-2024",
  "Hora": "14:03:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-18-2024",
  "Hora": "14:15:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-18-2024",
  "Hora": "22:22:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-19-2024",
  "Hora": "15:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-19-2024",
  "Hora": "22:17:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-20-2024",
  "Hora": "13:40:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-20-2024",
  "Hora": "14:53:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-21-2024",
  "Hora": "14:18:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-21-2024",
  "Hora": "22:06:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-25-2024",
  "Hora": "16:08:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-26-2024",
  "Hora": "01:19:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-26-2024",
  "Hora": "16:19:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-27-2024",
  "Hora": "01:17:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-27-2024",
  "Hora": "15:45:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-28-2024",
  "Hora": "01:15:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-28-2024",
  "Hora": "16:43:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "03-28-2024",
  "Hora": "23:55:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-01-2024",
  "Hora": "14:44:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-01-2024",
  "Hora": "22:27:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-02-2024",
  "Hora": "13:43:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-02-2024",
  "Hora": "22:27:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-09-2024",
  "Hora": "15:50:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-10-2024",
  "Hora": "01:00:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-10-2024",
  "Hora": "16:13:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-11-2024",
  "Hora": "01:02:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-11-2024",
  "Hora": "16:17:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-12-2024",
  "Hora": "01:14:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-12-2024",
  "Hora": "13:49:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-12-2024",
  "Hora": "21:56:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-15-2024",
  "Hora": "14:05:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 240854376,
  "Date": "04-15-2024",
  "Hora": "22:15:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 214278553,
  "Date": "04-15-2024",
  "Hora": "05:04:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214278553,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 214278553,
  "Date": "04-15-2024",
  "Hora": "11:38:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-18-2024",
  "Hora": "07:25:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-18-2024",
  "Hora": "17:10:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-19-2024",
  "Hora": "07:24:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-19-2024",
  "Hora": "17:56:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-20-2024",
  "Hora": "07:26:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-20-2024",
  "Hora": "18:01:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-21-2024",
  "Hora": "07:55:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-21-2024",
  "Hora": "18:00:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-22-2024",
  "Hora": "07:32:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-22-2024",
  "Hora": "17:01:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-23-2024",
  "Hora": "07:51:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-23-2024",
  "Hora": "14:01:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-25-2024",
  "Hora": "07:32:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-25-2024",
  "Hora": "18:00:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-26-2024",
  "Hora": "07:30:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-26-2024",
  "Hora": "18:00:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-27-2024",
  "Hora": "07:53:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-27-2024",
  "Hora": "17:54:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-28-2024",
  "Hora": "07:32:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "03-28-2024",
  "Hora": "23:28:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-01-2024",
  "Hora": "10:59:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-01-2024",
  "Hora": "18:01:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-02-2024",
  "Hora": "07:49:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-02-2024",
  "Hora": "17:58:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-03-2024",
  "Hora": "07:30:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-03-2024",
  "Hora": "18:00:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-04-2024",
  "Hora": "07:43:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-04-2024",
  "Hora": "17:59:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-08-2024",
  "Hora": "07:50:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-08-2024",
  "Hora": "18:01:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-09-2024",
  "Hora": "07:24:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-09-2024",
  "Hora": "16:59:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-10-2024",
  "Hora": "07:45:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-10-2024",
  "Hora": "18:00:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-11-2024",
  "Hora": "07:28:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-11-2024",
  "Hora": "17:54:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-12-2024",
  "Hora": "07:33:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-12-2024",
  "Hora": "17:01:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-15-2024",
  "Hora": "08:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182414751,
  "Date": "04-15-2024",
  "Hora": "18:01:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-16-2024",
  "Hora": "02:35:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-16-2024",
  "Hora": "11:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-18-2024",
  "Hora": "04:01:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-18-2024",
  "Hora": "12:03:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-19-2024",
  "Hora": "03:49:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-19-2024",
  "Hora": "12:22:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-20-2024",
  "Hora": "04:03:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-20-2024",
  "Hora": "11:58:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-21-2024",
  "Hora": "03:48:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-21-2024",
  "Hora": "12:01:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-22-2024",
  "Hora": "03:47:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-22-2024",
  "Hora": "12:10:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-23-2024",
  "Hora": "03:47:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-23-2024",
  "Hora": "12:05:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-25-2024",
  "Hora": "02:27:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-25-2024",
  "Hora": "11:03:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-26-2024",
  "Hora": "03:00:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-26-2024",
  "Hora": "11:02:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-27-2024",
  "Hora": "03:15:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-27-2024",
  "Hora": "11:03:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-28-2024",
  "Hora": "02:55:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "03-28-2024",
  "Hora": "11:05:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-02-2024",
  "Hora": "04:32:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-02-2024",
  "Hora": "12:10:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-03-2024",
  "Hora": "05:20:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-03-2024",
  "Hora": "12:08:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-04-2024",
  "Hora": "03:52:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-04-2024",
  "Hora": "11:55:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-05-2024",
  "Hora": "03:43:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-05-2024",
  "Hora": "12:05:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-06-2024",
  "Hora": "05:14:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-06-2024",
  "Hora": "10:58:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-08-2024",
  "Hora": "05:08:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-08-2024",
  "Hora": "11:58:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-09-2024",
  "Hora": "03:42:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-09-2024",
  "Hora": "11:57:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-10-2024",
  "Hora": "04:21:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-10-2024",
  "Hora": "11:52:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-11-2024",
  "Hora": "03:50:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-11-2024",
  "Hora": "11:56:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-12-2024",
  "Hora": "05:04:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-12-2024",
  "Hora": "12:00:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-13-2024",
  "Hora": "03:43:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-13-2024",
  "Hora": "10:57:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-15-2024",
  "Hora": "05:32:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20911786K",
  "Date": "04-15-2024",
  "Hora": "10:59:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-18-2024",
  "Hora": "08:45:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-18-2024",
  "Hora": "17:56:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-19-2024",
  "Hora": "08:41:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-19-2024",
  "Hora": "17:56:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-20-2024",
  "Hora": "08:39:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-20-2024",
  "Hora": "18:03:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-21-2024",
  "Hora": "08:38:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-21-2024",
  "Hora": "18:00:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-22-2024",
  "Hora": "08:36:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-22-2024",
  "Hora": "17:21:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-25-2024",
  "Hora": "08:39:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-25-2024",
  "Hora": "18:11:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-26-2024",
  "Hora": "08:40:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-26-2024",
  "Hora": "18:11:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-27-2024",
  "Hora": "08:38:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "03-27-2024",
  "Hora": "18:10:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-01-2024",
  "Hora": "08:42:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-01-2024",
  "Hora": "18:10:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-02-2024",
  "Hora": "08:44:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-02-2024",
  "Hora": "17:51:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-03-2024",
  "Hora": "08:41:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-03-2024",
  "Hora": "18:22:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-04-2024",
  "Hora": "08:58:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-04-2024",
  "Hora": "17:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-05-2024",
  "Hora": "08:37:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-05-2024",
  "Hora": "18:02:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-08-2024",
  "Hora": "08:36:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-08-2024",
  "Hora": "18:21:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-09-2024",
  "Hora": "08:39:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-09-2024",
  "Hora": "18:09:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-10-2024",
  "Hora": "08:31:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-10-2024",
  "Hora": "18:11:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-11-2024",
  "Hora": "08:30:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-11-2024",
  "Hora": "18:17:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-12-2024",
  "Hora": "08:37:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-12-2024",
  "Hora": "17:34:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-15-2024",
  "Hora": "08:33:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167899153,
  "Date": "04-15-2024",
  "Hora": "17:56:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-16-2024",
  "Hora": "12:33:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-16-2024",
  "Hora": "21:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-18-2024",
  "Hora": "16:08:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-19-2024",
  "Hora": "01:21:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-19-2024",
  "Hora": "16:09:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-20-2024",
  "Hora": "01:01:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-20-2024",
  "Hora": "16:14:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-21-2024",
  "Hora": "01:05:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-21-2024",
  "Hora": "16:19:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-22-2024",
  "Hora": "01:07:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-22-2024",
  "Hora": "13:05:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-22-2024",
  "Hora": "21:46:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-25-2024",
  "Hora": "13:12:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "03-25-2024",
  "Hora": "22:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-08-2024",
  "Hora": "16:09:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-08-2024",
  "Hora": "22:07:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-09-2024",
  "Hora": "13:06:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-09-2024",
  "Hora": "21:59:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-10-2024",
  "Hora": "13:07:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-10-2024",
  "Hora": "21:57:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-11-2024",
  "Hora": "13:20:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-11-2024",
  "Hora": "21:57:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-13-2024",
  "Hora": "21:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-15-2024",
  "Hora": "09:03:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197543280,
  "Date": "04-15-2024",
  "Hora": "18:00:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 259635322,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-18-2024",
  "Hora": "08:07:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-18-2024",
  "Hora": "18:01:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-18-2024",
  "Hora": "18:01:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-19-2024",
  "Hora": "08:03:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-19-2024",
  "Hora": "18:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-20-2024",
  "Hora": "08:05:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-20-2024",
  "Hora": "18:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-21-2024",
  "Hora": "08:11:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-21-2024",
  "Hora": "18:05:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-22-2024",
  "Hora": "08:09:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-22-2024",
  "Hora": "17:01:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-22-2024",
  "Hora": "17:01:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-25-2024",
  "Hora": "08:28:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-25-2024",
  "Hora": "18:00:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-26-2024",
  "Hora": "08:03:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-26-2024",
  "Hora": "20:01:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-27-2024",
  "Hora": "08:08:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-27-2024",
  "Hora": "08:08:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "03-27-2024",
  "Hora": "18:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-01-2024",
  "Hora": "08:16:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-01-2024",
  "Hora": "18:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-02-2024",
  "Hora": "08:07:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-02-2024",
  "Hora": "18:02:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-03-2024",
  "Hora": "08:06:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-03-2024",
  "Hora": "08:06:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-03-2024",
  "Hora": "18:03:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-04-2024",
  "Hora": "08:08:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-04-2024",
  "Hora": "18:02:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-05-2024",
  "Hora": "08:12:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-05-2024",
  "Hora": "17:02:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-06-2024",
  "Hora": "08:14:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-06-2024",
  "Hora": "14:01:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-08-2024",
  "Hora": "08:07:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-08-2024",
  "Hora": "18:04:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-09-2024",
  "Hora": "08:03:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-09-2024",
  "Hora": "18:01:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-11-2024",
  "Hora": "08:23:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-11-2024",
  "Hora": "20:01:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-12-2024",
  "Hora": "08:21:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-12-2024",
  "Hora": "17:02:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-12-2024",
  "Hora": "17:03:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-15-2024",
  "Hora": "08:06:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-15-2024",
  "Hora": "08:06:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20499983K",
  "Date": "04-15-2024",
  "Hora": "18:02:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-18-2024",
  "Hora": "04:47:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-18-2024",
  "Hora": "14:31:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-20-2024",
  "Hora": "04:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-20-2024",
  "Hora": "14:31:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-21-2024",
  "Hora": "04:46:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-21-2024",
  "Hora": "14:31:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-22-2024",
  "Hora": "04:45:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-22-2024",
  "Hora": "14:15:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-23-2024",
  "Hora": "04:42:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-23-2024",
  "Hora": "13:15:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-25-2024",
  "Hora": "04:43:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-25-2024",
  "Hora": "14:31:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-27-2024",
  "Hora": "04:43:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "03-27-2024",
  "Hora": "14:31:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-01-2024",
  "Hora": "04:48:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-01-2024",
  "Hora": "14:31:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-02-2024",
  "Hora": "04:58:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-02-2024",
  "Hora": "12:00:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-03-2024",
  "Hora": "04:55:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-03-2024",
  "Hora": "14:31:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-04-2024",
  "Hora": "04:40:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-04-2024",
  "Hora": "14:30:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-05-2024",
  "Hora": "04:43:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-05-2024",
  "Hora": "14:30:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-08-2024",
  "Hora": "04:45:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-08-2024",
  "Hora": "14:31:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-10-2024",
  "Hora": "04:44:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-10-2024",
  "Hora": "14:30:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-11-2024",
  "Hora": "04:41:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-11-2024",
  "Hora": "14:30:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-12-2024",
  "Hora": "04:44:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-12-2024",
  "Hora": "14:30:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-13-2024",
  "Hora": "04:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-13-2024",
  "Hora": "14:30:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-15-2024",
  "Hora": "04:43:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "17105656K",
  "Date": "04-15-2024",
  "Hora": "14:31:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132591121,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-16-2024",
  "Hora": "00:14:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-18-2024",
  "Hora": "16:00:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-19-2024",
  "Hora": "01:10:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-19-2024",
  "Hora": "15:52:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-20-2024",
  "Hora": "01:01:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-20-2024",
  "Hora": "15:54:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-21-2024",
  "Hora": "01:04:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-21-2024",
  "Hora": "15:33:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-22-2024",
  "Hora": "01:06:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-22-2024",
  "Hora": "15:34:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-23-2024",
  "Hora": "00:13:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-25-2024",
  "Hora": "15:57:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-26-2024",
  "Hora": "01:16:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-26-2024",
  "Hora": "15:56:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-27-2024",
  "Hora": "01:23:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-27-2024",
  "Hora": "15:55:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-28-2024",
  "Hora": "01:04:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-28-2024",
  "Hora": "15:34:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "03-28-2024",
  "Hora": "23:48:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-01-2024",
  "Hora": "15:55:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-02-2024",
  "Hora": "01:27:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-02-2024",
  "Hora": "16:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-03-2024",
  "Hora": "02:31:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-03-2024",
  "Hora": "16:00:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-04-2024",
  "Hora": "01:10:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-04-2024",
  "Hora": "15:59:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-05-2024",
  "Hora": "01:18:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-05-2024",
  "Hora": "15:40:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-05-2024",
  "Hora": "23:54:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-08-2024",
  "Hora": "15:56:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-09-2024",
  "Hora": "01:18:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-09-2024",
  "Hora": "15:39:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-10-2024",
  "Hora": "00:55:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-10-2024",
  "Hora": "15:46:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-11-2024",
  "Hora": "01:01:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-11-2024",
  "Hora": "15:30:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-12-2024",
  "Hora": "00:54:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-12-2024",
  "Hora": "15:38:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-13-2024",
  "Hora": "00:07:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167858600,
  "Date": "04-15-2024",
  "Hora": "15:32:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-16-2024",
  "Hora": "07:46:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-16-2024",
  "Hora": "14:03:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-18-2024",
  "Hora": "03:38:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-18-2024",
  "Hora": "07:12:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-18-2024",
  "Hora": "07:12:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-18-2024",
  "Hora": "18:01:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-19-2024",
  "Hora": "07:28:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-19-2024",
  "Hora": "20:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-20-2024",
  "Hora": "07:29:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-20-2024",
  "Hora": "18:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-22-2024",
  "Hora": "07:42:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-22-2024",
  "Hora": "17:00:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-23-2024",
  "Hora": "07:46:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-23-2024",
  "Hora": "14:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-25-2024",
  "Hora": "07:53:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-25-2024",
  "Hora": "18:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-26-2024",
  "Hora": "07:48:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-26-2024",
  "Hora": "18:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-27-2024",
  "Hora": "07:26:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-27-2024",
  "Hora": "17:56:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-28-2024",
  "Hora": "07:29:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "03-28-2024",
  "Hora": "23:24:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-01-2024",
  "Hora": "07:26:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-01-2024",
  "Hora": "18:00:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-02-2024",
  "Hora": "07:23:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-02-2024",
  "Hora": "18:00:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-03-2024",
  "Hora": "07:42:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-03-2024",
  "Hora": "18:00:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-04-2024",
  "Hora": "07:27:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-04-2024",
  "Hora": "18:00:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-05-2024",
  "Hora": "07:30:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-05-2024",
  "Hora": "17:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-08-2024",
  "Hora": "07:19:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-08-2024",
  "Hora": "18:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-09-2024",
  "Hora": "07:24:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-09-2024",
  "Hora": "18:00:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-10-2024",
  "Hora": "07:26:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-10-2024",
  "Hora": "20:01:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-11-2024",
  "Hora": "07:25:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-11-2024",
  "Hora": "20:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-12-2024",
  "Hora": "07:23:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-12-2024",
  "Hora": "17:00:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-13-2024",
  "Hora": "07:42:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-13-2024",
  "Hora": "14:00:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-15-2024",
  "Hora": "07:25:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 180833374,
  "Date": "04-15-2024",
  "Hora": "18:00:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 204275971,
  "Date": "04-15-2024",
  "Hora": "16:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-16-2024",
  "Hora": "05:39:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-16-2024",
  "Hora": "11:50:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-18-2024",
  "Hora": "05:57:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-18-2024",
  "Hora": "13:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-19-2024",
  "Hora": "05:22:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-19-2024",
  "Hora": "13:32:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-20-2024",
  "Hora": "05:33:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-20-2024",
  "Hora": "13:31:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-21-2024",
  "Hora": "05:22:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-21-2024",
  "Hora": "13:31:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-22-2024",
  "Hora": "05:24:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-22-2024",
  "Hora": "13:31:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-23-2024",
  "Hora": "05:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-23-2024",
  "Hora": "05:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-23-2024",
  "Hora": "05:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-23-2024",
  "Hora": "05:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-23-2024",
  "Hora": "05:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-23-2024",
  "Hora": "05:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-23-2024",
  "Hora": "05:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-23-2024",
  "Hora": "05:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-23-2024",
  "Hora": "05:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-23-2024",
  "Hora": "05:23:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-23-2024",
  "Hora": "11:10:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-25-2024",
  "Hora": "06:18:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-25-2024",
  "Hora": "13:02:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-26-2024",
  "Hora": "05:20:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-26-2024",
  "Hora": "13:31:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-27-2024",
  "Hora": "05:21:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-27-2024",
  "Hora": "13:31:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-28-2024",
  "Hora": "05:24:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "03-28-2024",
  "Hora": "13:31:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-01-2024",
  "Hora": "05:57:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-01-2024",
  "Hora": "14:02:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-02-2024",
  "Hora": "05:46:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-02-2024",
  "Hora": "13:36:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-03-2024",
  "Hora": "05:24:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-03-2024",
  "Hora": "13:35:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-04-2024",
  "Hora": "05:24:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-04-2024",
  "Hora": "13:36:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-05-2024",
  "Hora": "05:36:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-05-2024",
  "Hora": "13:31:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-06-2024",
  "Hora": "05:27:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-06-2024",
  "Hora": "12:34:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-08-2024",
  "Hora": "05:54:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-08-2024",
  "Hora": "14:00:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-09-2024",
  "Hora": "05:17:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-09-2024",
  "Hora": "13:33:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-10-2024",
  "Hora": "05:22:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-10-2024",
  "Hora": "13:30:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-11-2024",
  "Hora": "05:15:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-11-2024",
  "Hora": "13:32:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-12-2024",
  "Hora": "05:17:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-12-2024",
  "Hora": "13:32:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-13-2024",
  "Hora": "05:24:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-13-2024",
  "Hora": "12:02:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-15-2024",
  "Hora": "05:55:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 179557290,
  "Date": "04-15-2024",
  "Hora": "13:03:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-16-2024",
  "Hora": "05:55:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-16-2024",
  "Hora": "14:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-18-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-18-2024",
  "Hora": "18:00:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-19-2024",
  "Hora": "08:28:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-19-2024",
  "Hora": "17:59:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-20-2024",
  "Hora": "08:31:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-20-2024",
  "Hora": "17:59:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-21-2024",
  "Hora": "08:38:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-21-2024",
  "Hora": "17:58:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-23-2024",
  "Hora": "06:01:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-23-2024",
  "Hora": "16:02:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-25-2024",
  "Hora": "08:33:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-25-2024",
  "Hora": "20:02:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-26-2024",
  "Hora": "06:18:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-26-2024",
  "Hora": "17:54:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-27-2024",
  "Hora": "06:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-27-2024",
  "Hora": "20:01:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-28-2024",
  "Hora": "08:52:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "03-28-2024",
  "Hora": "20:01:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-01-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-01-2024",
  "Hora": "17:57:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-02-2024",
  "Hora": "08:20:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-02-2024",
  "Hora": "17:59:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-03-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-03-2024",
  "Hora": "17:58:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-04-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-04-2024",
  "Hora": "17:58:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-05-2024",
  "Hora": "08:34:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-05-2024",
  "Hora": "17:58:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-06-2024",
  "Hora": "06:04:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-06-2024",
  "Hora": "14:03:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-08-2024",
  "Hora": "08:35:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-08-2024",
  "Hora": "19:07:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-09-2024",
  "Hora": "08:39:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-09-2024",
  "Hora": "18:02:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-10-2024",
  "Hora": "08:18:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-10-2024",
  "Hora": "17:58:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-11-2024",
  "Hora": "08:22:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-11-2024",
  "Hora": "17:59:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-11-2024",
  "Hora": "21:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-12-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-12-2024",
  "Hora": "17:58:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-13-2024",
  "Hora": "05:58:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-13-2024",
  "Hora": "14:08:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-15-2024",
  "Hora": "06:06:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "16796091K",
  "Date": "04-15-2024",
  "Hora": "17:59:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-18-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-18-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-19-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-19-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-20-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-20-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-21-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-21-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-22-2024",
  "Hora": "10:14:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-22-2024",
  "Hora": "17:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-23-2024",
  "Hora": "07:49:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-23-2024",
  "Hora": "15:03:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-25-2024",
  "Hora": "07:01:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-25-2024",
  "Hora": "13:10:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-26-2024",
  "Hora": "06:58:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-26-2024",
  "Hora": "15:36:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-26-2024",
  "Hora": "16:27:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-26-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-27-2024",
  "Hora": "07:00:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-27-2024",
  "Hora": "15:27:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-27-2024",
  "Hora": "16:24:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-27-2024",
  "Hora": "19:01:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-28-2024",
  "Hora": "07:00:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-28-2024",
  "Hora": "15:14:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-28-2024",
  "Hora": "16:10:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "03-28-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-01-2024",
  "Hora": "06:57:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-01-2024",
  "Hora": "15:45:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-01-2024",
  "Hora": "16:44:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-01-2024",
  "Hora": "17:01:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-02-2024",
  "Hora": "06:55:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-02-2024",
  "Hora": "15:45:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-02-2024",
  "Hora": "16:38:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-02-2024",
  "Hora": "17:01:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-03-2024",
  "Hora": "07:01:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-03-2024",
  "Hora": "15:15:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-03-2024",
  "Hora": "16:11:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-03-2024",
  "Hora": "17:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-04-2024",
  "Hora": "06:58:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-04-2024",
  "Hora": "14:56:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-04-2024",
  "Hora": "15:51:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-04-2024",
  "Hora": "17:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-08-2024",
  "Hora": "06:59:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-08-2024",
  "Hora": "15:47:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-08-2024",
  "Hora": "17:01:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-09-2024",
  "Hora": "07:00:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-09-2024",
  "Hora": "15:28:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-09-2024",
  "Hora": "15:48:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-09-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-10-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-10-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-11-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-11-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-12-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-12-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-15-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "20051856K",
  "Date": "04-15-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-20-2024",
  "Hora": "10:54:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-20-2024",
  "Hora": "11:52:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-21-2024",
  "Hora": "04:00:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-21-2024",
  "Hora": "11:42:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-22-2024",
  "Hora": "04:04:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-22-2024",
  "Hora": "11:27:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-23-2024",
  "Hora": "04:00:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-23-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-25-2024",
  "Hora": "03:58:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-25-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-26-2024",
  "Hora": "04:03:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-26-2024",
  "Hora": "11:56:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-27-2024",
  "Hora": "03:57:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-27-2024",
  "Hora": "11:50:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-28-2024",
  "Hora": "04:02:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "03-28-2024",
  "Hora": "12:03:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-01-2024",
  "Hora": "03:58:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-01-2024",
  "Hora": "12:13:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-02-2024",
  "Hora": "04:06:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-02-2024",
  "Hora": "12:06:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-03-2024",
  "Hora": "03:38:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-03-2024",
  "Hora": "12:10:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-04-2024",
  "Hora": "04:05:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-04-2024",
  "Hora": "12:04:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-05-2024",
  "Hora": "03:53:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-05-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-06-2024",
  "Hora": "04:09:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-06-2024",
  "Hora": "11:57:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-08-2024",
  "Hora": "01:43:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-08-2024",
  "Hora": "10:09:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-09-2024",
  "Hora": "01:28:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-09-2024",
  "Hora": "10:10:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-10-2024",
  "Hora": "01:35:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-10-2024",
  "Hora": "10:06:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-11-2024",
  "Hora": "01:41:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-11-2024",
  "Hora": "10:06:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-12-2024",
  "Hora": "01:57:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-12-2024",
  "Hora": "10:06:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-13-2024",
  "Hora": "01:42:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-13-2024",
  "Hora": "10:03:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-15-2024",
  "Hora": "04:06:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 197527234,
  "Date": "04-15-2024",
  "Hora": "11:30:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-18-2024",
  "Hora": "14:08:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-18-2024",
  "Hora": "23:27:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-19-2024",
  "Hora": "14:07:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-19-2024",
  "Hora": "22:27:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-20-2024",
  "Hora": "13:54:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-20-2024",
  "Hora": "21:05:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-25-2024",
  "Hora": "13:43:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-26-2024",
  "Hora": "00:03:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-26-2024",
  "Hora": "14:15:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-26-2024",
  "Hora": "22:33:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-27-2024",
  "Hora": "14:20:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-27-2024",
  "Hora": "23:24:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-28-2024",
  "Hora": "13:52:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "03-28-2024",
  "Hora": "22:11:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-01-2024",
  "Hora": "13:52:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-02-2024",
  "Hora": "01:10:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-02-2024",
  "Hora": "13:50:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-02-2024",
  "Hora": "21:32:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-03-2024",
  "Hora": "14:06:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-03-2024",
  "Hora": "22:13:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-04-2024",
  "Hora": "13:55:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-04-2024",
  "Hora": "22:46:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-05-2024",
  "Hora": "13:59:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-05-2024",
  "Hora": "21:37:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-08-2024",
  "Hora": "13:54:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-08-2024",
  "Hora": "23:00:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-09-2024",
  "Hora": "13:56:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-09-2024",
  "Hora": "22:04:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-10-2024",
  "Hora": "14:13:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-10-2024",
  "Hora": "21:33:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-11-2024",
  "Hora": "14:13:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-11-2024",
  "Hora": "21:20:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-12-2024",
  "Hora": "14:00:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-12-2024",
  "Hora": "21:09:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-15-2024",
  "Hora": "14:13:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 184167794,
  "Date": "04-15-2024",
  "Hora": "22:35:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-16-2024",
  "Hora": "13:00:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-16-2024",
  "Hora": "20:58:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-16-2024",
  "Hora": "20:58:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-18-2024",
  "Hora": "15:55:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-19-2024",
  "Hora": "01:16:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-19-2024",
  "Hora": "02:17:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-19-2024",
  "Hora": "15:57:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-20-2024",
  "Hora": "01:04:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-20-2024",
  "Hora": "15:55:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-21-2024",
  "Hora": "01:01:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-21-2024",
  "Hora": "15:59:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-21-2024",
  "Hora": "22:30:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-22-2024",
  "Hora": "01:16:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-22-2024",
  "Hora": "12:55:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-22-2024",
  "Hora": "21:40:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-25-2024",
  "Hora": "12:52:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-25-2024",
  "Hora": "22:18:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-26-2024",
  "Hora": "12:51:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-26-2024",
  "Hora": "12:51:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-26-2024",
  "Hora": "22:08:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-27-2024",
  "Hora": "12:52:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-27-2024",
  "Hora": "12:52:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-27-2024",
  "Hora": "22:11:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-28-2024",
  "Hora": "12:50:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "03-28-2024",
  "Hora": "21:45:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-01-2024",
  "Hora": "15:42:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-02-2024",
  "Hora": "01:37:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-02-2024",
  "Hora": "15:57:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-03-2024",
  "Hora": "01:33:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-03-2024",
  "Hora": "15:48:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-04-2024",
  "Hora": "01:11:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-04-2024",
  "Hora": "15:47:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-05-2024",
  "Hora": "01:12:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-05-2024",
  "Hora": "12:55:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-05-2024",
  "Hora": "21:34:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-08-2024",
  "Hora": "12:51:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-08-2024",
  "Hora": "22:10:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-09-2024",
  "Hora": "12:55:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-09-2024",
  "Hora": "21:58:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-10-2024",
  "Hora": "12:57:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-10-2024",
  "Hora": "22:00:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-11-2024",
  "Hora": "12:53:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-11-2024",
  "Hora": "21:56:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-13-2024",
  "Hora": "21:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 76262098,
  "Date": "04-15-2024",
  "Hora": "15:49:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-18-2024",
  "Hora": "07:52:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-18-2024",
  "Hora": "18:05:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-19-2024",
  "Hora": "07:46:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-19-2024",
  "Hora": "18:01:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-20-2024",
  "Hora": "07:51:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-20-2024",
  "Hora": "18:01:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-21-2024",
  "Hora": "07:48:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-21-2024",
  "Hora": "18:01:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-22-2024",
  "Hora": "07:48:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-22-2024",
  "Hora": "17:02:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-23-2024",
  "Hora": "07:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-23-2024",
  "Hora": "07:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-23-2024",
  "Hora": "07:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-23-2024",
  "Hora": "07:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-23-2024",
  "Hora": "07:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-23-2024",
  "Hora": "07:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-23-2024",
  "Hora": "07:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-23-2024",
  "Hora": "07:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-23-2024",
  "Hora": "07:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-23-2024",
  "Hora": "07:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-23-2024",
  "Hora": "14:00:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-25-2024",
  "Hora": "08:06:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-25-2024",
  "Hora": "18:01:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-26-2024",
  "Hora": "07:49:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-26-2024",
  "Hora": "20:02:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-27-2024",
  "Hora": "07:49:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-27-2024",
  "Hora": "18:04:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-28-2024",
  "Hora": "07:48:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "03-28-2024",
  "Hora": "23:36:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-01-2024",
  "Hora": "07:51:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-01-2024",
  "Hora": "18:03:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-02-2024",
  "Hora": "07:44:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-02-2024",
  "Hora": "17:22:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-03-2024",
  "Hora": "07:49:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-03-2024",
  "Hora": "18:03:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-04-2024",
  "Hora": "07:44:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-04-2024",
  "Hora": "18:03:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-05-2024",
  "Hora": "07:46:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-05-2024",
  "Hora": "17:04:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-05-2024",
  "Hora": "17:04:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-08-2024",
  "Hora": "07:48:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-08-2024",
  "Hora": "18:03:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-09-2024",
  "Hora": "07:43:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-09-2024",
  "Hora": "18:02:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-10-2024",
  "Hora": "07:46:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-10-2024",
  "Hora": "18:05:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-11-2024",
  "Hora": "07:45:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-11-2024",
  "Hora": "18:00:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-12-2024",
  "Hora": "11:06:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-12-2024",
  "Hora": "17:02:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-13-2024",
  "Hora": "07:43:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-13-2024",
  "Hora": "14:01:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-15-2024",
  "Hora": "07:44:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 209024454,
  "Date": "04-15-2024",
  "Hora": "18:02:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-18-2024",
  "Hora": "17:32:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-19-2024",
  "Hora": "03:20:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-19-2024",
  "Hora": "17:36:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-20-2024",
  "Hora": "03:12:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-20-2024",
  "Hora": "17:59:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-21-2024",
  "Hora": "03:32:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-21-2024",
  "Hora": "17:40:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-22-2024",
  "Hora": "03:39:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-22-2024",
  "Hora": "19:00:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-23-2024",
  "Hora": "03:24:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-25-2024",
  "Hora": "17:30:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-26-2024",
  "Hora": "03:25:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-26-2024",
  "Hora": "17:32:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-27-2024",
  "Hora": "03:25:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-27-2024",
  "Hora": "17:35:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-28-2024",
  "Hora": "03:29:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-28-2024",
  "Hora": "17:29:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "03-29-2024",
  "Hora": "00:01:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-01-2024",
  "Hora": "17:32:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-02-2024",
  "Hora": "03:53:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-02-2024",
  "Hora": "17:38:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-03-2024",
  "Hora": "04:01:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-03-2024",
  "Hora": "17:40:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-04-2024",
  "Hora": "03:27:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-04-2024",
  "Hora": "17:57:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-05-2024",
  "Hora": "03:22:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-05-2024",
  "Hora": "18:58:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-06-2024",
  "Hora": "03:24:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-08-2024",
  "Hora": "17:38:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-09-2024",
  "Hora": "03:32:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-09-2024",
  "Hora": "17:36:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-10-2024",
  "Hora": "03:25:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-10-2024",
  "Hora": "17:40:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-11-2024",
  "Hora": "03:40:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-11-2024",
  "Hora": "17:38:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-12-2024",
  "Hora": "03:20:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-12-2024",
  "Hora": "18:41:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-13-2024",
  "Hora": "03:04:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 117687740,
  "Date": "04-15-2024",
  "Hora": "19:58:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-18-2024",
  "Hora": "07:53:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-18-2024",
  "Hora": "18:02:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-19-2024",
  "Hora": "07:31:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-19-2024",
  "Hora": "18:02:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-20-2024",
  "Hora": "07:48:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-20-2024",
  "Hora": "18:01:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-21-2024",
  "Hora": "08:00:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-21-2024",
  "Hora": "18:02:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-22-2024",
  "Hora": "07:42:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-22-2024",
  "Hora": "17:02:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-25-2024",
  "Hora": "07:52:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-25-2024",
  "Hora": "18:01:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-26-2024",
  "Hora": "07:28:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-26-2024",
  "Hora": "18:02:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-27-2024",
  "Hora": "07:33:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "03-27-2024",
  "Hora": "18:02:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19313758K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-18-2024",
  "Hora": "06:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-18-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-19-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-19-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-20-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-20-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-21-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-21-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-22-2024",
  "Hora": "10:39:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-22-2024",
  "Hora": "17:00:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-23-2024",
  "Hora": "07:40:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-23-2024",
  "Hora": "13:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-25-2024",
  "Hora": "06:38:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-25-2024",
  "Hora": "17:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-26-2024",
  "Hora": "06:30:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-26-2024",
  "Hora": "19:00:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-27-2024",
  "Hora": "06:32:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "03-27-2024",
  "Hora": "16:55:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-01-2024",
  "Hora": "06:31:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-01-2024",
  "Hora": "17:00:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-02-2024",
  "Hora": "06:30:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-02-2024",
  "Hora": "17:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-03-2024",
  "Hora": "06:33:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-03-2024",
  "Hora": "14:47:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-03-2024",
  "Hora": "15:45:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-03-2024",
  "Hora": "17:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-04-2024",
  "Hora": "06:36:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-04-2024",
  "Hora": "06:38:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-04-2024",
  "Hora": "18:56:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-05-2024",
  "Hora": "06:33:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-05-2024",
  "Hora": "17:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-06-2024",
  "Hora": "07:45:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-06-2024",
  "Hora": "13:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-08-2024",
  "Hora": "06:35:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-08-2024",
  "Hora": "17:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-09-2024",
  "Hora": "06:38:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-09-2024",
  "Hora": "17:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-10-2024",
  "Hora": "06:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-10-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-11-2024",
  "Hora": "06:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-11-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-12-2024",
  "Hora": "06:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-12-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-15-2024",
  "Hora": "06:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 157975676,
  "Date": "04-15-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-16-2024",
  "Hora": "10:15:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-16-2024",
  "Hora": "17:57:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-18-2024",
  "Hora": "10:17:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-18-2024",
  "Hora": "16:34:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-21-2024",
  "Hora": "10:15:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-21-2024",
  "Hora": "16:51:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-22-2024",
  "Hora": "10:18:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-22-2024",
  "Hora": "17:14:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-23-2024",
  "Hora": "10:20:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-23-2024",
  "Hora": "16:14:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-25-2024",
  "Hora": "10:20:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-25-2024",
  "Hora": "17:20:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-26-2024",
  "Hora": "10:27:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-26-2024",
  "Hora": "17:10:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-27-2024",
  "Hora": "09:59:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-27-2024",
  "Hora": "16:55:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-27-2024",
  "Hora": "16:55:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-28-2024",
  "Hora": "10:17:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "03-28-2024",
  "Hora": "16:54:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-01-2024",
  "Hora": "10:05:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-01-2024",
  "Hora": "18:58:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-02-2024",
  "Hora": "10:18:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-02-2024",
  "Hora": "18:04:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-03-2024",
  "Hora": "09:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-03-2024",
  "Hora": "17:50:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-04-2024",
  "Hora": "10:28:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-04-2024",
  "Hora": "10:28:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-04-2024",
  "Hora": "17:47:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-05-2024",
  "Hora": "10:17:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-05-2024",
  "Hora": "18:05:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-06-2024",
  "Hora": "10:12:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-06-2024",
  "Hora": "16:08:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-08-2024",
  "Hora": "10:10:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-08-2024",
  "Hora": "17:03:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-09-2024",
  "Hora": "10:11:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-09-2024",
  "Hora": "17:07:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-10-2024",
  "Hora": "10:08:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-10-2024",
  "Hora": "17:58:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-11-2024",
  "Hora": "10:33:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-11-2024",
  "Hora": "17:48:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-12-2024",
  "Hora": "10:16:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-12-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-13-2024",
  "Hora": "10:26:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-13-2024",
  "Hora": "15:50:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-15-2024",
  "Hora": "09:57:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 250160771,
  "Date": "04-15-2024",
  "Hora": "16:45:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-16-2024",
  "Hora": "03:41:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-16-2024",
  "Hora": "11:01:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-16-2024",
  "Hora": "11:01:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-18-2024",
  "Hora": "03:55:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-18-2024",
  "Hora": "12:04:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-19-2024",
  "Hora": "04:08:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-19-2024",
  "Hora": "12:17:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-20-2024",
  "Hora": "04:05:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-20-2024",
  "Hora": "04:05:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-20-2024",
  "Hora": "12:13:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-20-2024",
  "Hora": "12:13:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-21-2024",
  "Hora": "04:04:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-21-2024",
  "Hora": "04:04:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-21-2024",
  "Hora": "12:07:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-22-2024",
  "Hora": "03:53:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-22-2024",
  "Hora": "12:17:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-23-2024",
  "Hora": "03:54:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-23-2024",
  "Hora": "12:11:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-25-2024",
  "Hora": "03:50:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-25-2024",
  "Hora": "12:13:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-26-2024",
  "Hora": "03:52:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-26-2024",
  "Hora": "12:11:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-27-2024",
  "Hora": "03:58:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-27-2024",
  "Hora": "12:13:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-28-2024",
  "Hora": "03:48:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "03-28-2024",
  "Hora": "11:57:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-01-2024",
  "Hora": "03:50:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-01-2024",
  "Hora": "13:17:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-02-2024",
  "Hora": "04:32:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-02-2024",
  "Hora": "12:17:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-03-2024",
  "Hora": "04:00:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-03-2024",
  "Hora": "12:16:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-04-2024",
  "Hora": "03:52:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-04-2024",
  "Hora": "12:09:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-05-2024",
  "Hora": "03:43:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-05-2024",
  "Hora": "12:16:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-06-2024",
  "Hora": "03:46:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-06-2024",
  "Hora": "11:01:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-08-2024",
  "Hora": "03:39:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-08-2024",
  "Hora": "12:11:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-09-2024",
  "Hora": "03:36:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-09-2024",
  "Hora": "12:10:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-10-2024",
  "Hora": "03:23:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-10-2024",
  "Hora": "12:01:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-11-2024",
  "Hora": "03:28:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-11-2024",
  "Hora": "12:08:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-12-2024",
  "Hora": "03:27:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-12-2024",
  "Hora": "12:18:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-13-2024",
  "Hora": "03:25:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-13-2024",
  "Hora": "11:04:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-15-2024",
  "Hora": "02:38:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 229829637,
  "Date": "04-15-2024",
  "Hora": "11:08:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 207402516,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-18-2024",
  "Hora": "08:28:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-18-2024",
  "Hora": "11:24:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-19-2024",
  "Hora": "08:30:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-19-2024",
  "Hora": "12:24:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-20-2024",
  "Hora": "08:27:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-20-2024",
  "Hora": "11:12:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-21-2024",
  "Hora": "08:34:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-21-2024",
  "Hora": "10:57:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-22-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-22-2024",
  "Hora": "10:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-23-2024",
  "Hora": "08:11:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-23-2024",
  "Hora": "10:29:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-25-2024",
  "Hora": "08:32:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-25-2024",
  "Hora": "11:10:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-26-2024",
  "Hora": "08:33:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-26-2024",
  "Hora": "12:03:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-27-2024",
  "Hora": "08:19:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-27-2024",
  "Hora": "11:32:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-28-2024",
  "Hora": "08:31:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "03-28-2024",
  "Hora": "11:06:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-01-2024",
  "Hora": "08:39:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-01-2024",
  "Hora": "13:15:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-02-2024",
  "Hora": "08:28:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-02-2024",
  "Hora": "13:13:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-03-2024",
  "Hora": "08:33:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-03-2024",
  "Hora": "12:59:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-04-2024",
  "Hora": "08:27:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-04-2024",
  "Hora": "11:55:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-05-2024",
  "Hora": "08:31:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-05-2024",
  "Hora": "11:38:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-06-2024",
  "Hora": "08:17:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-06-2024",
  "Hora": "10:34:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-08-2024",
  "Hora": "08:28:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-08-2024",
  "Hora": "08:28:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-08-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-08-2024",
  "Hora": "12:03:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-09-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-09-2024",
  "Hora": "08:34:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-09-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-09-2024",
  "Hora": "13:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-10-2024",
  "Hora": "08:30:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-10-2024",
  "Hora": "11:50:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-11-2024",
  "Hora": "08:28:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-11-2024",
  "Hora": "12:00:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-12-2024",
  "Hora": "08:27:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-12-2024",
  "Hora": "12:06:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-13-2024",
  "Hora": "08:15:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-13-2024",
  "Hora": "10:38:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-15-2024",
  "Hora": "08:25:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 198055875,
  "Date": "04-15-2024",
  "Hora": "10:57:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-16-2024",
  "Hora": "05:55:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-16-2024",
  "Hora": "14:00:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-18-2024",
  "Hora": "08:21:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-18-2024",
  "Hora": "17:59:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-19-2024",
  "Hora": "08:18:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-19-2024",
  "Hora": "17:59:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-20-2024",
  "Hora": "08:30:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-20-2024",
  "Hora": "17:59:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-21-2024",
  "Hora": "08:21:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-21-2024",
  "Hora": "17:57:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-22-2024",
  "Hora": "08:34:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-22-2024",
  "Hora": "17:59:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-23-2024",
  "Hora": "06:00:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-23-2024",
  "Hora": "16:01:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-25-2024",
  "Hora": "08:20:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-25-2024",
  "Hora": "18:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-27-2024",
  "Hora": "08:23:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-27-2024",
  "Hora": "17:59:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-28-2024",
  "Hora": "08:25:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "03-28-2024",
  "Hora": "18:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-01-2024",
  "Hora": "08:26:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-01-2024",
  "Hora": "18:00:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-02-2024",
  "Hora": "08:21:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-02-2024",
  "Hora": "17:59:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-03-2024",
  "Hora": "08:22:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-03-2024",
  "Hora": "17:59:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-04-2024",
  "Hora": "08:17:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-04-2024",
  "Hora": "17:59:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-05-2024",
  "Hora": "08:20:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-05-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-08-2024",
  "Hora": "08:16:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-08-2024",
  "Hora": "17:58:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-09-2024",
  "Hora": "08:20:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-09-2024",
  "Hora": "17:59:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-10-2024",
  "Hora": "08:16:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-10-2024",
  "Hora": "17:59:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-11-2024",
  "Hora": "08:20:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-11-2024",
  "Hora": "17:59:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-12-2024",
  "Hora": "08:20:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-12-2024",
  "Hora": "17:58:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-13-2024",
  "Hora": "06:21:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-13-2024",
  "Hora": "14:08:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-15-2024",
  "Hora": "08:22:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 253083379,
  "Date": "04-15-2024",
  "Hora": "17:59:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-18-2024",
  "Hora": "07:50:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-18-2024",
  "Hora": "20:01:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-19-2024",
  "Hora": "11:06:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-19-2024",
  "Hora": "11:06:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-19-2024",
  "Hora": "18:01:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-20-2024",
  "Hora": "07:49:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-20-2024",
  "Hora": "18:00:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-21-2024",
  "Hora": "09:05:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-21-2024",
  "Hora": "20:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-22-2024",
  "Hora": "07:46:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-22-2024",
  "Hora": "17:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-23-2024",
  "Hora": "07:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-23-2024",
  "Hora": "07:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-23-2024",
  "Hora": "07:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-23-2024",
  "Hora": "07:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-23-2024",
  "Hora": "07:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-23-2024",
  "Hora": "07:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-23-2024",
  "Hora": "07:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-23-2024",
  "Hora": "07:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-23-2024",
  "Hora": "07:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-23-2024",
  "Hora": "07:46:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-23-2024",
  "Hora": "14:02:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-25-2024",
  "Hora": "07:48:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-25-2024",
  "Hora": "20:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-26-2024",
  "Hora": "07:48:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-26-2024",
  "Hora": "18:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-27-2024",
  "Hora": "07:46:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-27-2024",
  "Hora": "20:00:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-28-2024",
  "Hora": "07:46:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "03-28-2024",
  "Hora": "23:29:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-01-2024",
  "Hora": "07:48:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-01-2024",
  "Hora": "18:00:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-02-2024",
  "Hora": "07:43:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-02-2024",
  "Hora": "18:01:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-03-2024",
  "Hora": "07:46:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-03-2024",
  "Hora": "18:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-04-2024",
  "Hora": "07:43:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-04-2024",
  "Hora": "18:01:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-05-2024",
  "Hora": "07:45:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-05-2024",
  "Hora": "17:00:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-06-2024",
  "Hora": "07:45:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-06-2024",
  "Hora": "14:01:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-08-2024",
  "Hora": "07:46:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-08-2024",
  "Hora": "18:00:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-09-2024",
  "Hora": "07:41:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-09-2024",
  "Hora": "18:01:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-11-2024",
  "Hora": "07:43:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-11-2024",
  "Hora": "20:00:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-12-2024",
  "Hora": "07:44:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-12-2024",
  "Hora": "16:57:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-13-2024",
  "Hora": "07:42:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-13-2024",
  "Hora": "14:08:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-15-2024",
  "Hora": "07:43:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15668760K",
  "Date": "04-15-2024",
  "Hora": "18:01:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-16-2024",
  "Hora": "04:52:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-16-2024",
  "Hora": "12:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-19-2024",
  "Hora": "04:46:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-19-2024",
  "Hora": "13:05:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-20-2024",
  "Hora": "04:50:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-20-2024",
  "Hora": "13:03:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-21-2024",
  "Hora": "04:57:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-21-2024",
  "Hora": "13:01:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-22-2024",
  "Hora": "04:58:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-22-2024",
  "Hora": "13:03:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-23-2024",
  "Hora": "04:50:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-23-2024",
  "Hora": "04:50:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-23-2024",
  "Hora": "04:50:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-23-2024",
  "Hora": "04:50:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-23-2024",
  "Hora": "04:50:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-23-2024",
  "Hora": "04:50:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-23-2024",
  "Hora": "04:50:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-23-2024",
  "Hora": "04:50:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-23-2024",
  "Hora": "04:50:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-23-2024",
  "Hora": "04:50:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-23-2024",
  "Hora": "13:01:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-25-2024",
  "Hora": "05:57:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-25-2024",
  "Hora": "14:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-26-2024",
  "Hora": "04:48:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-26-2024",
  "Hora": "13:02:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-27-2024",
  "Hora": "04:59:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-27-2024",
  "Hora": "13:01:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-28-2024",
  "Hora": "05:00:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "03-28-2024",
  "Hora": "13:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-01-2024",
  "Hora": "06:00:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-01-2024",
  "Hora": "19:00:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-02-2024",
  "Hora": "03:48:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-02-2024",
  "Hora": "12:01:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-03-2024",
  "Hora": "03:48:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-03-2024",
  "Hora": "12:01:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-04-2024",
  "Hora": "05:01:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-04-2024",
  "Hora": "12:02:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-05-2024",
  "Hora": "05:00:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-05-2024",
  "Hora": "09:32:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-06-2024",
  "Hora": "05:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-06-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-08-2024",
  "Hora": "06:09:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-08-2024",
  "Hora": "14:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-09-2024",
  "Hora": "05:01:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-09-2024",
  "Hora": "13:03:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-10-2024",
  "Hora": "04:57:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-10-2024",
  "Hora": "12:05:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-11-2024",
  "Hora": "05:38:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-11-2024",
  "Hora": "12:58:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-12-2024",
  "Hora": "04:58:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-12-2024",
  "Hora": "13:08:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-13-2024",
  "Hora": "04:55:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-13-2024",
  "Hora": "12:58:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-15-2024",
  "Hora": "05:56:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201821436,
  "Date": "04-15-2024",
  "Hora": "14:02:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-18-2024",
  "Hora": "07:22:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-18-2024",
  "Hora": "18:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-19-2024",
  "Hora": "07:23:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-19-2024",
  "Hora": "18:00:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-20-2024",
  "Hora": "07:18:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-20-2024",
  "Hora": "20:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-22-2024",
  "Hora": "07:24:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-22-2024",
  "Hora": "17:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-23-2024",
  "Hora": "07:45:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-23-2024",
  "Hora": "07:45:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-23-2024",
  "Hora": "07:45:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-23-2024",
  "Hora": "07:45:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-23-2024",
  "Hora": "07:45:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-23-2024",
  "Hora": "07:45:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-23-2024",
  "Hora": "07:45:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-23-2024",
  "Hora": "07:45:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-23-2024",
  "Hora": "07:45:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-23-2024",
  "Hora": "07:45:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-23-2024",
  "Hora": "14:00:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-25-2024",
  "Hora": "07:28:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-25-2024",
  "Hora": "20:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-26-2024",
  "Hora": "07:29:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-26-2024",
  "Hora": "20:00:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-27-2024",
  "Hora": "07:25:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-27-2024",
  "Hora": "18:00:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-28-2024",
  "Hora": "07:29:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "03-28-2024",
  "Hora": "23:32:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-01-2024",
  "Hora": "07:26:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-01-2024",
  "Hora": "18:00:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-02-2024",
  "Hora": "07:21:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-02-2024",
  "Hora": "18:00:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-03-2024",
  "Hora": "07:25:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-03-2024",
  "Hora": "18:00:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-03-2024",
  "Hora": "18:00:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-04-2024",
  "Hora": "07:25:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-04-2024",
  "Hora": "18:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-05-2024",
  "Hora": "07:30:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-05-2024",
  "Hora": "17:00:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-06-2024",
  "Hora": "07:45:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-06-2024",
  "Hora": "14:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-08-2024",
  "Hora": "07:19:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-08-2024",
  "Hora": "18:00:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-09-2024",
  "Hora": "07:25:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-09-2024",
  "Hora": "18:00:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-09-2024",
  "Hora": "18:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-10-2024",
  "Hora": "07:26:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-10-2024",
  "Hora": "20:00:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-12-2024",
  "Hora": "07:31:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-12-2024",
  "Hora": "17:00:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-13-2024",
  "Hora": "07:35:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-13-2024",
  "Hora": "14:00:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-15-2024",
  "Hora": "07:25:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-15-2024",
  "Hora": "18:00:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 98304789,
  "Date": "04-15-2024",
  "Hora": "18:00:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-16-2024",
  "Hora": "03:43:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-16-2024",
  "Hora": "11:02:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-18-2024",
  "Hora": "04:03:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-18-2024",
  "Hora": "12:03:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-19-2024",
  "Hora": "03:51:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-19-2024",
  "Hora": "12:18:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-20-2024",
  "Hora": "03:52:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-20-2024",
  "Hora": "12:11:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-21-2024",
  "Hora": "03:48:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-21-2024",
  "Hora": "12:04:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-22-2024",
  "Hora": "03:46:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-22-2024",
  "Hora": "12:17:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-23-2024",
  "Hora": "03:43:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-23-2024",
  "Hora": "12:11:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-25-2024",
  "Hora": "03:53:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-25-2024",
  "Hora": "12:11:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-26-2024",
  "Hora": "03:48:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-26-2024",
  "Hora": "12:11:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-27-2024",
  "Hora": "04:20:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-27-2024",
  "Hora": "12:10:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-28-2024",
  "Hora": "04:02:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "03-28-2024",
  "Hora": "11:58:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-01-2024",
  "Hora": "04:02:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-01-2024",
  "Hora": "12:10:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-02-2024",
  "Hora": "04:06:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-02-2024",
  "Hora": "12:17:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-03-2024",
  "Hora": "03:45:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-03-2024",
  "Hora": "12:16:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-04-2024",
  "Hora": "03:39:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-04-2024",
  "Hora": "12:09:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-05-2024",
  "Hora": "03:38:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-05-2024",
  "Hora": "12:12:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-06-2024",
  "Hora": "03:35:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-06-2024",
  "Hora": "11:06:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-08-2024",
  "Hora": "03:38:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-08-2024",
  "Hora": "12:11:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-09-2024",
  "Hora": "03:31:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-09-2024",
  "Hora": "12:06:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-12-2024",
  "Hora": "03:34:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-12-2024",
  "Hora": "12:18:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-13-2024",
  "Hora": "03:27:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-13-2024",
  "Hora": "11:04:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-15-2024",
  "Hora": "02:39:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271333749,
  "Date": "04-15-2024",
  "Hora": "11:07:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-19-2024",
  "Hora": "04:46:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-19-2024",
  "Hora": "13:03:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-20-2024",
  "Hora": "04:54:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-20-2024",
  "Hora": "13:07:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-21-2024",
  "Hora": "04:52:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-21-2024",
  "Hora": "13:02:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-22-2024",
  "Hora": "04:52:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-22-2024",
  "Hora": "13:02:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-23-2024",
  "Hora": "04:52:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-23-2024",
  "Hora": "04:52:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-23-2024",
  "Hora": "04:52:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-23-2024",
  "Hora": "04:52:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-23-2024",
  "Hora": "04:52:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-23-2024",
  "Hora": "04:52:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-23-2024",
  "Hora": "04:52:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-23-2024",
  "Hora": "04:52:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-23-2024",
  "Hora": "04:52:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-23-2024",
  "Hora": "04:52:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-23-2024",
  "Hora": "13:00:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-25-2024",
  "Hora": "05:52:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-25-2024",
  "Hora": "14:00:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-26-2024",
  "Hora": "04:47:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-26-2024",
  "Hora": "13:02:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-27-2024",
  "Hora": "04:52:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-27-2024",
  "Hora": "13:01:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-28-2024",
  "Hora": "05:07:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "03-28-2024",
  "Hora": "13:01:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-01-2024",
  "Hora": "04:49:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-01-2024",
  "Hora": "13:01:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-02-2024",
  "Hora": "03:47:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-02-2024",
  "Hora": "12:11:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-03-2024",
  "Hora": "03:50:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-03-2024",
  "Hora": "12:03:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-04-2024",
  "Hora": "04:53:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-04-2024",
  "Hora": "12:02:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-05-2024",
  "Hora": "04:46:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-05-2024",
  "Hora": "12:01:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-06-2024",
  "Hora": "04:52:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-06-2024",
  "Hora": "12:02:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-08-2024",
  "Hora": "05:52:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-08-2024",
  "Hora": "14:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-09-2024",
  "Hora": "03:48:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-09-2024",
  "Hora": "12:00:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-10-2024",
  "Hora": "04:52:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-10-2024",
  "Hora": "12:06:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-11-2024",
  "Hora": "04:53:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-11-2024",
  "Hora": "12:59:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-12-2024",
  "Hora": "04:52:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-12-2024",
  "Hora": "13:01:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-13-2024",
  "Hora": "04:28:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-13-2024",
  "Hora": "13:01:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-15-2024",
  "Hora": "05:26:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201280699,
  "Date": "04-15-2024",
  "Hora": "14:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-17-2024",
  "Hora": "11:37:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-17-2024",
  "Hora": "14:33:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-18-2024",
  "Hora": "08:33:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-18-2024",
  "Hora": "20:25:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-19-2024",
  "Hora": "08:25:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-19-2024",
  "Hora": "18:46:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-20-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-20-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-20-2024",
  "Hora": "22:37:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-20-2024",
  "Hora": "22:37:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-21-2024",
  "Hora": "08:31:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-21-2024",
  "Hora": "18:25:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-22-2024",
  "Hora": "08:27:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-22-2024",
  "Hora": "18:13:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-24-2024",
  "Hora": "08:57:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-24-2024",
  "Hora": "13:14:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-25-2024",
  "Hora": "08:31:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-25-2024",
  "Hora": "17:55:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-26-2024",
  "Hora": "08:28:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-26-2024",
  "Hora": "18:33:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-27-2024",
  "Hora": "08:34:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-27-2024",
  "Hora": "18:21:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-28-2024",
  "Hora": "02:39:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-28-2024",
  "Hora": "02:58:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-28-2024",
  "Hora": "08:28:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-28-2024",
  "Hora": "17:57:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-29-2024",
  "Hora": "16:53:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "03-29-2024",
  "Hora": "19:25:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-01-2024",
  "Hora": "04:04:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-01-2024",
  "Hora": "19:23:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-02-2024",
  "Hora": "04:38:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-02-2024",
  "Hora": "18:14:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-03-2024",
  "Hora": "09:05:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-03-2024",
  "Hora": "16:44:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-04-2024",
  "Hora": "08:42:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-04-2024",
  "Hora": "18:46:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-05-2024",
  "Hora": "08:39:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-05-2024",
  "Hora": "18:04:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-08-2024",
  "Hora": "08:23:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-08-2024",
  "Hora": "19:30:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-09-2024",
  "Hora": "08:15:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-09-2024",
  "Hora": "18:20:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-10-2024",
  "Hora": "08:17:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-10-2024",
  "Hora": "20:09:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-11-2024",
  "Hora": "08:51:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-11-2024",
  "Hora": "18:04:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-12-2024",
  "Hora": "08:24:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-12-2024",
  "Hora": "18:28:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-14-2024",
  "Hora": "14:32:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-14-2024",
  "Hora": "16:29:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-15-2024",
  "Hora": "04:05:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19094137k",
  "Date": "04-15-2024",
  "Hora": "19:34:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-16-2024",
  "Hora": "00:13:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-18-2024",
  "Hora": "15:06:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-19-2024",
  "Hora": "01:10:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-19-2024",
  "Hora": "15:22:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-20-2024",
  "Hora": "01:05:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-20-2024",
  "Hora": "15:00:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-21-2024",
  "Hora": "01:03:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-21-2024",
  "Hora": "15:30:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-22-2024",
  "Hora": "01:09:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-22-2024",
  "Hora": "15:13:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-23-2024",
  "Hora": "00:10:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-25-2024",
  "Hora": "15:28:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-26-2024",
  "Hora": "01:19:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-26-2024",
  "Hora": "15:17:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-27-2024",
  "Hora": "01:16:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-27-2024",
  "Hora": "15:06:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-28-2024",
  "Hora": "01:07:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-28-2024",
  "Hora": "15:26:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "03-28-2024",
  "Hora": "23:54:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-01-2024",
  "Hora": "14:56:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-02-2024",
  "Hora": "01:29:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-02-2024",
  "Hora": "15:11:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-03-2024",
  "Hora": "02:30:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-03-2024",
  "Hora": "03:19:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-03-2024",
  "Hora": "15:18:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-04-2024",
  "Hora": "01:17:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-04-2024",
  "Hora": "15:22:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-05-2024",
  "Hora": "01:21:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-05-2024",
  "Hora": "15:26:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-05-2024",
  "Hora": "23:55:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-08-2024",
  "Hora": "15:14:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-09-2024",
  "Hora": "01:12:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-09-2024",
  "Hora": "15:04:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-10-2024",
  "Hora": "01:08:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-10-2024",
  "Hora": "15:21:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-11-2024",
  "Hora": "01:10:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-11-2024",
  "Hora": "15:10:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-12-2024",
  "Hora": "01:08:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-12-2024",
  "Hora": "15:07:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-13-2024",
  "Hora": "00:09:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 224955340,
  "Date": "04-15-2024",
  "Hora": "15:17:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-16-2024",
  "Hora": "04:05:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-16-2024",
  "Hora": "12:01:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-18-2024",
  "Hora": "03:45:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-18-2024",
  "Hora": "12:24:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-19-2024",
  "Hora": "04:19:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-19-2024",
  "Hora": "12:09:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-20-2024",
  "Hora": "04:36:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-20-2024",
  "Hora": "11:50:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-21-2024",
  "Hora": "03:50:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-21-2024",
  "Hora": "11:58:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-22-2024",
  "Hora": "04:28:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-22-2024",
  "Hora": "11:28:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "04:41:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "04:41:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "04:41:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "04:41:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "04:41:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "04:41:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "04:41:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "04:41:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "04:41:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "04:41:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "04:41:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-23-2024",
  "Hora": "11:02:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-25-2024",
  "Hora": "03:37:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-25-2024",
  "Hora": "11:38:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-26-2024",
  "Hora": "03:50:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-26-2024",
  "Hora": "12:02:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-27-2024",
  "Hora": "03:45:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-27-2024",
  "Hora": "11:59:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-28-2024",
  "Hora": "03:51:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "03-28-2024",
  "Hora": "12:08:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-01-2024",
  "Hora": "03:27:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-01-2024",
  "Hora": "13:20:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-02-2024",
  "Hora": "03:21:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-02-2024",
  "Hora": "12:11:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-03-2024",
  "Hora": "03:32:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-03-2024",
  "Hora": "12:26:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-04-2024",
  "Hora": "03:31:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-04-2024",
  "Hora": "12:08:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-05-2024",
  "Hora": "04:10:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-05-2024",
  "Hora": "12:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-06-2024",
  "Hora": "03:29:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-06-2024",
  "Hora": "12:01:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-09-2024",
  "Hora": "03:46:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-09-2024",
  "Hora": "12:13:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-10-2024",
  "Hora": "03:45:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-10-2024",
  "Hora": "11:33:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-11-2024",
  "Hora": "03:38:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-11-2024",
  "Hora": "11:45:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-12-2024",
  "Hora": "03:42:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-12-2024",
  "Hora": "11:45:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-13-2024",
  "Hora": "03:48:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-13-2024",
  "Hora": "11:45:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-14-2024",
  "Hora": "23:52:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-15-2024",
  "Hora": "10:13:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 271605064,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-16-2024",
  "Hora": "05:24:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-16-2024",
  "Hora": "11:49:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-18-2024",
  "Hora": "05:55:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-18-2024",
  "Hora": "13:01:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-19-2024",
  "Hora": "05:22:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-19-2024",
  "Hora": "13:30:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-20-2024",
  "Hora": "05:34:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-20-2024",
  "Hora": "13:32:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-21-2024",
  "Hora": "05:23:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-21-2024",
  "Hora": "13:30:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-22-2024",
  "Hora": "05:25:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-22-2024",
  "Hora": "13:32:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-23-2024",
  "Hora": "05:24:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-23-2024",
  "Hora": "05:24:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-23-2024",
  "Hora": "05:24:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-23-2024",
  "Hora": "05:24:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-23-2024",
  "Hora": "05:24:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-23-2024",
  "Hora": "05:24:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-23-2024",
  "Hora": "05:24:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-23-2024",
  "Hora": "05:24:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-23-2024",
  "Hora": "05:24:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-23-2024",
  "Hora": "05:24:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-23-2024",
  "Hora": "11:09:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-25-2024",
  "Hora": "05:57:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-25-2024",
  "Hora": "13:06:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-26-2024",
  "Hora": "05:20:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-26-2024",
  "Hora": "13:33:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-27-2024",
  "Hora": "05:22:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-27-2024",
  "Hora": "13:30:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-28-2024",
  "Hora": "05:25:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "03-28-2024",
  "Hora": "13:35:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-01-2024",
  "Hora": "05:57:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-01-2024",
  "Hora": "11:12:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-02-2024",
  "Hora": "05:19:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-02-2024",
  "Hora": "13:33:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-03-2024",
  "Hora": "05:25:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-03-2024",
  "Hora": "13:36:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-04-2024",
  "Hora": "05:25:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-04-2024",
  "Hora": "13:33:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-05-2024",
  "Hora": "05:19:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-05-2024",
  "Hora": "13:30:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-06-2024",
  "Hora": "05:28:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-06-2024",
  "Hora": "12:34:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-08-2024",
  "Hora": "05:55:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-08-2024",
  "Hora": "14:00:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-09-2024",
  "Hora": "05:18:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-09-2024",
  "Hora": "13:32:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-10-2024",
  "Hora": "05:23:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-10-2024",
  "Hora": "13:30:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-11-2024",
  "Hora": "05:15:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-11-2024",
  "Hora": "13:32:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-12-2024",
  "Hora": "05:19:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-12-2024",
  "Hora": "13:33:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-13-2024",
  "Hora": "05:32:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-13-2024",
  "Hora": "07:48:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-15-2024",
  "Hora": "05:46:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 167667104,
  "Date": "04-15-2024",
  "Hora": "13:00:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 121215640,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-16-2024",
  "Hora": "05:55:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-16-2024",
  "Hora": "14:01:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-18-2024",
  "Hora": "08:28:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-18-2024",
  "Hora": "18:02:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-19-2024",
  "Hora": "08:37:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-19-2024",
  "Hora": "18:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-20-2024",
  "Hora": "08:41:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-20-2024",
  "Hora": "18:00:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-22-2024",
  "Hora": "08:19:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-22-2024",
  "Hora": "17:59:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-23-2024",
  "Hora": "06:02:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-23-2024",
  "Hora": "06:02:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-23-2024",
  "Hora": "06:02:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-23-2024",
  "Hora": "06:02:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-23-2024",
  "Hora": "06:02:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-23-2024",
  "Hora": "06:02:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-23-2024",
  "Hora": "06:02:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-23-2024",
  "Hora": "06:02:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-23-2024",
  "Hora": "06:02:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-23-2024",
  "Hora": "06:02:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-23-2024",
  "Hora": "16:09:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-25-2024",
  "Hora": "08:25:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-25-2024",
  "Hora": "17:58:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-26-2024",
  "Hora": "08:16:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-26-2024",
  "Hora": "17:51:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-27-2024",
  "Hora": "08:17:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-27-2024",
  "Hora": "17:58:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-28-2024",
  "Hora": "08:21:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "03-28-2024",
  "Hora": "18:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-03-2024",
  "Hora": "08:17:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-03-2024",
  "Hora": "18:02:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-04-2024",
  "Hora": "08:11:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-04-2024",
  "Hora": "17:57:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-05-2024",
  "Hora": "08:15:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-05-2024",
  "Hora": "17:59:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-06-2024",
  "Hora": "06:37:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-06-2024",
  "Hora": "14:03:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-08-2024",
  "Hora": "08:23:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-08-2024",
  "Hora": "18:01:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-09-2024",
  "Hora": "08:18:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-09-2024",
  "Hora": "18:01:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-10-2024",
  "Hora": "08:28:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-10-2024",
  "Hora": "17:56:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-12-2024",
  "Hora": "08:13:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-12-2024",
  "Hora": "17:56:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-13-2024",
  "Hora": "06:39:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-13-2024",
  "Hora": "14:09:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-15-2024",
  "Hora": "08:15:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 190047717,
  "Date": "04-15-2024",
  "Hora": "18:05:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-16-2024",
  "Hora": "05:25:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-16-2024",
  "Hora": "11:47:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-18-2024",
  "Hora": "05:52:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-18-2024",
  "Hora": "13:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-19-2024",
  "Hora": "05:20:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-19-2024",
  "Hora": "13:30:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-20-2024",
  "Hora": "05:38:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-20-2024",
  "Hora": "13:30:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-21-2024",
  "Hora": "05:19:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-21-2024",
  "Hora": "13:31:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-22-2024",
  "Hora": "05:24:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-22-2024",
  "Hora": "13:30:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-23-2024",
  "Hora": "05:35:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-23-2024",
  "Hora": "11:08:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-25-2024",
  "Hora": "05:51:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-25-2024",
  "Hora": "13:00:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-26-2024",
  "Hora": "05:17:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-26-2024",
  "Hora": "13:30:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-27-2024",
  "Hora": "05:26:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-27-2024",
  "Hora": "13:30:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-28-2024",
  "Hora": "05:15:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "03-28-2024",
  "Hora": "13:31:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-04-2024",
  "Hora": "05:16:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-04-2024",
  "Hora": "13:33:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-05-2024",
  "Hora": "05:24:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-05-2024",
  "Hora": "13:30:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-06-2024",
  "Hora": "05:28:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-06-2024",
  "Hora": "12:31:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-08-2024",
  "Hora": "05:50:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-08-2024",
  "Hora": "14:01:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-09-2024",
  "Hora": "05:26:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-09-2024",
  "Hora": "13:30:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-10-2024",
  "Hora": "05:32:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-10-2024",
  "Hora": "13:31:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-11-2024",
  "Hora": "05:18:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-11-2024",
  "Hora": "13:31:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-12-2024",
  "Hora": "05:18:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-12-2024",
  "Hora": "13:30:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-13-2024",
  "Hora": "05:18:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-13-2024",
  "Hora": "12:02:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-15-2024",
  "Hora": "05:49:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 195903603,
  "Date": "04-15-2024",
  "Hora": "11:18:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-16-2024",
  "Hora": "04:48:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-16-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-18-2024",
  "Hora": "05:50:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-18-2024",
  "Hora": "14:02:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-19-2024",
  "Hora": "04:52:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-19-2024",
  "Hora": "13:03:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-20-2024",
  "Hora": "04:50:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-20-2024",
  "Hora": "13:02:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-21-2024",
  "Hora": "04:57:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-21-2024",
  "Hora": "13:00:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-22-2024",
  "Hora": "04:57:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-22-2024",
  "Hora": "13:01:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-23-2024",
  "Hora": "04:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-23-2024",
  "Hora": "04:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-23-2024",
  "Hora": "04:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-23-2024",
  "Hora": "04:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-23-2024",
  "Hora": "04:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-23-2024",
  "Hora": "04:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-23-2024",
  "Hora": "04:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-23-2024",
  "Hora": "04:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-23-2024",
  "Hora": "04:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-23-2024",
  "Hora": "04:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-23-2024",
  "Hora": "13:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-25-2024",
  "Hora": "05:56:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-25-2024",
  "Hora": "14:02:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-26-2024",
  "Hora": "04:54:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-26-2024",
  "Hora": "13:02:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-27-2024",
  "Hora": "04:58:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-27-2024",
  "Hora": "13:03:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-28-2024",
  "Hora": "04:59:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "03-28-2024",
  "Hora": "13:02:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-01-2024",
  "Hora": "04:48:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-01-2024",
  "Hora": "13:02:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-02-2024",
  "Hora": "03:55:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-02-2024",
  "Hora": "12:05:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-03-2024",
  "Hora": "03:53:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-03-2024",
  "Hora": "12:03:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-04-2024",
  "Hora": "05:00:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-04-2024",
  "Hora": "12:02:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-05-2024",
  "Hora": "04:53:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-05-2024",
  "Hora": "12:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-06-2024",
  "Hora": "04:50:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-06-2024",
  "Hora": "12:00:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-08-2024",
  "Hora": "06:09:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-08-2024",
  "Hora": "14:00:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-09-2024",
  "Hora": "03:47:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-09-2024",
  "Hora": "12:02:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-10-2024",
  "Hora": "04:56:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-10-2024",
  "Hora": "12:09:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-11-2024",
  "Hora": "04:56:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-11-2024",
  "Hora": "13:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-12-2024",
  "Hora": "04:57:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-12-2024",
  "Hora": "13:01:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-13-2024",
  "Hora": "04:54:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-13-2024",
  "Hora": "13:00:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-15-2024",
  "Hora": "05:55:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132274479,
  "Date": "04-15-2024",
  "Hora": "14:01:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "03-18-2024",
  "Hora": "13:55:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "03-18-2024",
  "Hora": "22:14:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "03-19-2024",
  "Hora": "12:47:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "03-19-2024",
  "Hora": "22:12:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "03-20-2024",
  "Hora": "12:50:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "03-20-2024",
  "Hora": "22:10:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "03-21-2024",
  "Hora": "12:46:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "03-21-2024",
  "Hora": "21:57:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "03-23-2024",
  "Hora": "13:08:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "03-23-2024",
  "Hora": "20:15:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-01-2024",
  "Hora": "12:37:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-01-2024",
  "Hora": "22:26:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-02-2024",
  "Hora": "12:48:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-02-2024",
  "Hora": "22:33:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-04-2024",
  "Hora": "12:37:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-04-2024",
  "Hora": "22:09:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-06-2024",
  "Hora": "12:41:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-06-2024",
  "Hora": "21:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-08-2024",
  "Hora": "15:44:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-09-2024",
  "Hora": "01:21:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-09-2024",
  "Hora": "15:45:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-10-2024",
  "Hora": "00:54:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-10-2024",
  "Hora": "15:58:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-11-2024",
  "Hora": "01:02:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-11-2024",
  "Hora": "15:48:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-12-2024",
  "Hora": "00:47:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-12-2024",
  "Hora": "12:49:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-12-2024",
  "Hora": "21:45:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-15-2024",
  "Hora": "12:41:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 265735800,
  "Date": "04-15-2024",
  "Hora": "22:23:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-18-2024",
  "Hora": "18:23:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-19-2024",
  "Hora": "03:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-19-2024",
  "Hora": "18:20:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-20-2024",
  "Hora": "03:05:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-20-2024",
  "Hora": "17:58:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-21-2024",
  "Hora": "03:17:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-21-2024",
  "Hora": "18:16:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-22-2024",
  "Hora": "03:31:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-22-2024",
  "Hora": "18:57:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-23-2024",
  "Hora": "03:16:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-25-2024",
  "Hora": "18:09:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-26-2024",
  "Hora": "03:23:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-26-2024",
  "Hora": "18:12:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-27-2024",
  "Hora": "03:22:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-27-2024",
  "Hora": "18:16:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-28-2024",
  "Hora": "03:17:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-28-2024",
  "Hora": "18:11:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "03-29-2024",
  "Hora": "00:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-01-2024",
  "Hora": "18:11:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-02-2024",
  "Hora": "03:44:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-02-2024",
  "Hora": "18:09:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-03-2024",
  "Hora": "03:59:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-03-2024",
  "Hora": "18:05:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-04-2024",
  "Hora": "03:19:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-04-2024",
  "Hora": "18:12:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-05-2024",
  "Hora": "03:26:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-05-2024",
  "Hora": "18:56:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-06-2024",
  "Hora": "03:23:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19779061K",
  "Date": "04-15-2024",
  "Hora": "19:37:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270244971,
  "Date": "03-16-2024",
  "Hora": "04:52:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270244971,
  "Date": "03-16-2024",
  "Hora": "12:15:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270244971,
  "Date": "04-09-2024",
  "Hora": "05:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270244971,
  "Date": "04-09-2024",
  "Hora": "13:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270244971,
  "Date": "04-11-2024",
  "Hora": "04:54:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270244971,
  "Date": "04-11-2024",
  "Hora": "13:05:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 270244971,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-16-2024",
  "Hora": "10:45:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-16-2024",
  "Hora": "20:30:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-18-2024",
  "Hora": "10:51:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-18-2024",
  "Hora": "20:30:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-19-2024",
  "Hora": "10:50:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-19-2024",
  "Hora": "20:30:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-20-2024",
  "Hora": "10:41:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-20-2024",
  "Hora": "20:34:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-21-2024",
  "Hora": "10:49:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-21-2024",
  "Hora": "20:30:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-22-2024",
  "Hora": "10:54:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-22-2024",
  "Hora": "20:31:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-23-2024",
  "Hora": "10:53:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-23-2024",
  "Hora": "20:30:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-25-2024",
  "Hora": "10:54:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-25-2024",
  "Hora": "20:30:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-26-2024",
  "Hora": "10:47:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-26-2024",
  "Hora": "20:30:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-27-2024",
  "Hora": "10:57:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-27-2024",
  "Hora": "20:34:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "03-28-2024",
  "Hora": "10:55:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-01-2024",
  "Hora": "10:53:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-01-2024",
  "Hora": "11:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-01-2024",
  "Hora": "20:00:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-01-2024",
  "Hora": "20:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-02-2024",
  "Hora": "10:54:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-02-2024",
  "Hora": "11:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-02-2024",
  "Hora": "19:31:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-02-2024",
  "Hora": "20:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-03-2024",
  "Hora": "10:55:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-03-2024",
  "Hora": "20:00:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-04-2024",
  "Hora": "10:44:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-04-2024",
  "Hora": "20:01:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-05-2024",
  "Hora": "10:42:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-05-2024",
  "Hora": "20:00:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-06-2024",
  "Hora": "10:43:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-06-2024",
  "Hora": "20:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-08-2024",
  "Hora": "10:51:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-08-2024",
  "Hora": "20:30:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-09-2024",
  "Hora": "10:41:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-09-2024",
  "Hora": "20:30:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-10-2024",
  "Hora": "10:51:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-10-2024",
  "Hora": "20:30:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-11-2024",
  "Hora": "10:47:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-11-2024",
  "Hora": "20:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-12-2024",
  "Hora": "10:53:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-12-2024",
  "Hora": "20:31:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-13-2024",
  "Hora": "10:43:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-13-2024",
  "Hora": "20:30:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-15-2024",
  "Hora": "10:48:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 187535700,
  "Date": "04-15-2024",
  "Hora": "20:31:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-16-2024",
  "Hora": "01:52:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-16-2024",
  "Hora": "10:11:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-19-2024",
  "Hora": "03:53:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-19-2024",
  "Hora": "12:16:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-20-2024",
  "Hora": "03:38:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-20-2024",
  "Hora": "11:56:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-21-2024",
  "Hora": "03:41:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-21-2024",
  "Hora": "11:50:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-22-2024",
  "Hora": "03:42:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-22-2024",
  "Hora": "11:40:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-23-2024",
  "Hora": "03:41:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-23-2024",
  "Hora": "11:02:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-25-2024",
  "Hora": "03:42:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-25-2024",
  "Hora": "11:46:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-26-2024",
  "Hora": "03:56:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-26-2024",
  "Hora": "12:08:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-27-2024",
  "Hora": "03:34:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-27-2024",
  "Hora": "11:59:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-28-2024",
  "Hora": "03:30:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "03-28-2024",
  "Hora": "12:12:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-01-2024",
  "Hora": "03:34:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-01-2024",
  "Hora": "12:13:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-02-2024",
  "Hora": "03:48:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-02-2024",
  "Hora": "12:19:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-03-2024",
  "Hora": "03:36:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-03-2024",
  "Hora": "12:18:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-04-2024",
  "Hora": "03:29:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-04-2024",
  "Hora": "12:10:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-05-2024",
  "Hora": "03:26:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-05-2024",
  "Hora": "12:03:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-06-2024",
  "Hora": "03:31:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-06-2024",
  "Hora": "11:59:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-08-2024",
  "Hora": "03:58:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-08-2024",
  "Hora": "11:59:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-09-2024",
  "Hora": "03:42:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-09-2024",
  "Hora": "12:11:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-10-2024",
  "Hora": "03:33:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-10-2024",
  "Hora": "11:56:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-11-2024",
  "Hora": "03:32:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-11-2024",
  "Hora": "11:48:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-12-2024",
  "Hora": "03:40:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-12-2024",
  "Hora": "11:58:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-13-2024",
  "Hora": "03:39:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-13-2024",
  "Hora": "11:49:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-15-2024",
  "Hora": "03:59:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 95029515,
  "Date": "04-15-2024",
  "Hora": "11:50:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-18-2024",
  "Hora": "04:47:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-18-2024",
  "Hora": "14:30:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-20-2024",
  "Hora": "04:45:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-20-2024",
  "Hora": "14:31:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-21-2024",
  "Hora": "04:46:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-21-2024",
  "Hora": "14:30:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-22-2024",
  "Hora": "04:45:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-22-2024",
  "Hora": "14:30:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-23-2024",
  "Hora": "04:43:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-23-2024",
  "Hora": "13:15:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-25-2024",
  "Hora": "04:43:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-25-2024",
  "Hora": "14:35:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-27-2024",
  "Hora": "04:43:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-27-2024",
  "Hora": "14:30:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-28-2024",
  "Hora": "04:46:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "03-28-2024",
  "Hora": "14:30:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-01-2024",
  "Hora": "04:48:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-01-2024",
  "Hora": "14:30:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-02-2024",
  "Hora": "04:58:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-02-2024",
  "Hora": "12:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-03-2024",
  "Hora": "04:51:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-03-2024",
  "Hora": "04:51:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-03-2024",
  "Hora": "14:31:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-04-2024",
  "Hora": "04:40:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-04-2024",
  "Hora": "14:30:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-05-2024",
  "Hora": "04:44:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-05-2024",
  "Hora": "14:31:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-08-2024",
  "Hora": "04:45:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-08-2024",
  "Hora": "14:31:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-10-2024",
  "Hora": "04:44:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-10-2024",
  "Hora": "14:30:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-11-2024",
  "Hora": "04:42:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-11-2024",
  "Hora": "14:30:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-12-2024",
  "Hora": "04:44:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-12-2024",
  "Hora": "14:30:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-13-2024",
  "Hora": "04:45:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-13-2024",
  "Hora": "14:30:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-15-2024",
  "Hora": "04:43:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-15-2024",
  "Hora": "04:43:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192706912,
  "Date": "04-15-2024",
  "Hora": "14:30:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-18-2024",
  "Hora": "08:47:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-18-2024",
  "Hora": "18:16:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-19-2024",
  "Hora": "08:53:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-19-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-20-2024",
  "Hora": "08:24:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-20-2024",
  "Hora": "18:18:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-20-2024",
  "Hora": "18:18:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-21-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-21-2024",
  "Hora": "18:05:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-22-2024",
  "Hora": "08:29:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-22-2024",
  "Hora": "18:17:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-25-2024",
  "Hora": "08:42:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-25-2024",
  "Hora": "18:07:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-26-2024",
  "Hora": "09:02:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-26-2024",
  "Hora": "18:07:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-27-2024",
  "Hora": "08:43:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "03-27-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 245409176,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-16-2024",
  "Hora": "05:50:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-16-2024",
  "Hora": "11:23:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-18-2024",
  "Hora": "05:51:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-18-2024",
  "Hora": "13:17:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-19-2024",
  "Hora": "05:53:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-19-2024",
  "Hora": "12:45:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-20-2024",
  "Hora": "05:57:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-20-2024",
  "Hora": "14:01:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-21-2024",
  "Hora": "05:56:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-21-2024",
  "Hora": "14:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-22-2024",
  "Hora": "05:53:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-22-2024",
  "Hora": "14:00:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-23-2024",
  "Hora": "06:00:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-23-2024",
  "Hora": "12:02:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-25-2024",
  "Hora": "05:52:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-25-2024",
  "Hora": "14:00:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-26-2024",
  "Hora": "05:52:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-26-2024",
  "Hora": "14:01:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-27-2024",
  "Hora": "05:55:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-27-2024",
  "Hora": "14:01:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-28-2024",
  "Hora": "05:53:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "03-28-2024",
  "Hora": "14:00:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-01-2024",
  "Hora": "05:56:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-01-2024",
  "Hora": "14:00:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-02-2024",
  "Hora": "05:55:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-02-2024",
  "Hora": "14:00:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-03-2024",
  "Hora": "05:52:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-03-2024",
  "Hora": "14:00:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-04-2024",
  "Hora": "05:55:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-04-2024",
  "Hora": "14:00:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-05-2024",
  "Hora": "05:55:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-05-2024",
  "Hora": "14:00:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-06-2024",
  "Hora": "05:50:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-06-2024",
  "Hora": "12:32:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-08-2024",
  "Hora": "05:45:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-08-2024",
  "Hora": "14:01:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-09-2024",
  "Hora": "05:54:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-09-2024",
  "Hora": "14:00:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-10-2024",
  "Hora": "05:51:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-10-2024",
  "Hora": "14:18:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-11-2024",
  "Hora": "05:47:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-11-2024",
  "Hora": "14:00:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-12-2024",
  "Hora": "05:53:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-12-2024",
  "Hora": "14:01:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-13-2024",
  "Hora": "05:48:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-13-2024",
  "Hora": "14:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-15-2024",
  "Hora": "05:51:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 201168775,
  "Date": "04-15-2024",
  "Hora": "13:00:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 166622824,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-16-2024",
  "Hora": "05:55:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-16-2024",
  "Hora": "14:00:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-18-2024",
  "Hora": "09:30:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-18-2024",
  "Hora": "18:00:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-19-2024",
  "Hora": "08:09:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-19-2024",
  "Hora": "08:34:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-19-2024",
  "Hora": "18:00:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-20-2024",
  "Hora": "08:09:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-20-2024",
  "Hora": "17:59:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-21-2024",
  "Hora": "08:24:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-21-2024",
  "Hora": "18:04:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-22-2024",
  "Hora": "08:49:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-22-2024",
  "Hora": "18:05:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-23-2024",
  "Hora": "06:00:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-23-2024",
  "Hora": "16:08:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-25-2024",
  "Hora": "08:23:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-25-2024",
  "Hora": "18:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-26-2024",
  "Hora": "09:06:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-26-2024",
  "Hora": "18:01:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-27-2024",
  "Hora": "06:10:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-27-2024",
  "Hora": "18:00:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-28-2024",
  "Hora": "05:56:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "03-28-2024",
  "Hora": "09:52:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-01-2024",
  "Hora": "08:21:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-01-2024",
  "Hora": "18:01:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-02-2024",
  "Hora": "08:31:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-02-2024",
  "Hora": "17:59:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-03-2024",
  "Hora": "08:04:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-03-2024",
  "Hora": "18:00:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-04-2024",
  "Hora": "09:02:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-04-2024",
  "Hora": "18:00:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-05-2024",
  "Hora": "08:14:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-05-2024",
  "Hora": "18:07:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-06-2024",
  "Hora": "06:11:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-06-2024",
  "Hora": "14:03:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-08-2024",
  "Hora": "07:59:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-08-2024",
  "Hora": "17:59:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-09-2024",
  "Hora": "08:33:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-09-2024",
  "Hora": "17:59:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-10-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-10-2024",
  "Hora": "18:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-11-2024",
  "Hora": "09:04:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-11-2024",
  "Hora": "18:00:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-12-2024",
  "Hora": "08:27:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-12-2024",
  "Hora": "18:01:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-13-2024",
  "Hora": "06:15:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-13-2024",
  "Hora": "14:06:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-15-2024",
  "Hora": "08:25:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0192829003",
  "Date": "04-15-2024",
  "Hora": "18:00:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-18-2024",
  "Hora": "15:52:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-19-2024",
  "Hora": "01:14:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-19-2024",
  "Hora": "15:54:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-20-2024",
  "Hora": "01:07:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-20-2024",
  "Hora": "15:58:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-21-2024",
  "Hora": "01:01:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-21-2024",
  "Hora": "15:57:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-22-2024",
  "Hora": "01:07:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-22-2024",
  "Hora": "16:00:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-23-2024",
  "Hora": "00:12:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-25-2024",
  "Hora": "15:57:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-26-2024",
  "Hora": "01:15:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-26-2024",
  "Hora": "15:57:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-27-2024",
  "Hora": "01:15:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-27-2024",
  "Hora": "16:05:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-28-2024",
  "Hora": "01:01:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-28-2024",
  "Hora": "16:06:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "03-28-2024",
  "Hora": "23:46:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-01-2024",
  "Hora": "15:58:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-02-2024",
  "Hora": "01:30:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-02-2024",
  "Hora": "16:10:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-03-2024",
  "Hora": "02:30:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-03-2024",
  "Hora": "16:01:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-04-2024",
  "Hora": "01:14:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-04-2024",
  "Hora": "16:02:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-05-2024",
  "Hora": "01:17:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-05-2024",
  "Hora": "16:10:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-05-2024",
  "Hora": "23:55:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-08-2024",
  "Hora": "16:06:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-09-2024",
  "Hora": "01:10:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-09-2024",
  "Hora": "15:50:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-10-2024",
  "Hora": "00:53:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-10-2024",
  "Hora": "16:08:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-11-2024",
  "Hora": "01:02:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-11-2024",
  "Hora": "16:08:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-12-2024",
  "Hora": "01:02:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-12-2024",
  "Hora": "15:52:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-13-2024",
  "Hora": "00:16:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 215750973,
  "Date": "04-15-2024",
  "Hora": "15:43:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-16-2024",
  "Hora": "00:14:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-18-2024",
  "Hora": "16:13:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-19-2024",
  "Hora": "01:10:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-19-2024",
  "Hora": "16:09:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-20-2024",
  "Hora": "01:01:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-20-2024",
  "Hora": "15:56:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-21-2024",
  "Hora": "01:12:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-21-2024",
  "Hora": "15:54:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-22-2024",
  "Hora": "01:08:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-22-2024",
  "Hora": "16:04:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-23-2024",
  "Hora": "00:14:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-25-2024",
  "Hora": "16:07:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-26-2024",
  "Hora": "01:16:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-26-2024",
  "Hora": "15:43:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-27-2024",
  "Hora": "01:14:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-27-2024",
  "Hora": "15:38:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-28-2024",
  "Hora": "01:00:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-28-2024",
  "Hora": "15:54:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "03-28-2024",
  "Hora": "23:49:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-01-2024",
  "Hora": "15:45:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-02-2024",
  "Hora": "01:27:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-02-2024",
  "Hora": "15:40:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-03-2024",
  "Hora": "02:31:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-03-2024",
  "Hora": "03:32:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-03-2024",
  "Hora": "15:51:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-04-2024",
  "Hora": "01:09:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-04-2024",
  "Hora": "16:05:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-05-2024",
  "Hora": "01:18:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-05-2024",
  "Hora": "16:16:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-05-2024",
  "Hora": "23:53:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-08-2024",
  "Hora": "15:26:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-09-2024",
  "Hora": "01:18:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-09-2024",
  "Hora": "15:58:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-10-2024",
  "Hora": "00:55:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-10-2024",
  "Hora": "15:56:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-11-2024",
  "Hora": "01:01:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-11-2024",
  "Hora": "15:43:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-12-2024",
  "Hora": "00:55:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 135903574,
  "Date": "04-15-2024",
  "Hora": "16:05:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-16-2024",
  "Hora": "06:18:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-16-2024",
  "Hora": "11:57:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-18-2024",
  "Hora": "01:49:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-18-2024",
  "Hora": "12:29:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-19-2024",
  "Hora": "01:48:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-19-2024",
  "Hora": "12:21:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-20-2024",
  "Hora": "01:52:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-20-2024",
  "Hora": "14:46:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-21-2024",
  "Hora": "01:57:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-21-2024",
  "Hora": "12:06:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-22-2024",
  "Hora": "01:49:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-22-2024",
  "Hora": "11:38:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-23-2024",
  "Hora": "01:38:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-23-2024",
  "Hora": "10:59:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-26-2024",
  "Hora": "03:38:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-26-2024",
  "Hora": "12:07:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-27-2024",
  "Hora": "03:55:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-27-2024",
  "Hora": "12:03:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-28-2024",
  "Hora": "04:06:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "03-28-2024",
  "Hora": "12:15:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-01-2024",
  "Hora": "04:02:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-01-2024",
  "Hora": "13:21:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-02-2024",
  "Hora": "04:00:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-02-2024",
  "Hora": "12:16:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-03-2024",
  "Hora": "03:49:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-03-2024",
  "Hora": "12:19:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-04-2024",
  "Hora": "03:49:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-04-2024",
  "Hora": "12:07:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-05-2024",
  "Hora": "04:33:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-05-2024",
  "Hora": "12:04:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-06-2024",
  "Hora": "03:35:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-06-2024",
  "Hora": "12:13:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-08-2024",
  "Hora": "03:32:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-08-2024",
  "Hora": "12:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-09-2024",
  "Hora": "03:17:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-09-2024",
  "Hora": "12:09:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-10-2024",
  "Hora": "03:16:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-10-2024",
  "Hora": "11:35:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-11-2024",
  "Hora": "03:34:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-11-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-12-2024",
  "Hora": "03:35:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-12-2024",
  "Hora": "12:03:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-13-2024",
  "Hora": "03:47:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-13-2024",
  "Hora": "11:47:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-15-2024",
  "Hora": "03:35:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18598771K",
  "Date": "04-15-2024",
  "Hora": "12:02:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-16-2024",
  "Hora": "07:46:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-16-2024",
  "Hora": "07:46:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-16-2024",
  "Hora": "14:03:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-18-2024",
  "Hora": "07:51:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-18-2024",
  "Hora": "07:51:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-18-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-18-2024",
  "Hora": "18:02:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-19-2024",
  "Hora": "07:59:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-19-2024",
  "Hora": "18:03:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-20-2024",
  "Hora": "07:51:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-20-2024",
  "Hora": "07:51:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-20-2024",
  "Hora": "20:01:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-21-2024",
  "Hora": "08:06:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-21-2024",
  "Hora": "20:01:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-22-2024",
  "Hora": "08:22:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-22-2024",
  "Hora": "17:02:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-23-2024",
  "Hora": "08:09:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-23-2024",
  "Hora": "14:03:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-25-2024",
  "Hora": "08:17:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-25-2024",
  "Hora": "20:01:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-25-2024",
  "Hora": "20:01:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-26-2024",
  "Hora": "08:11:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-26-2024",
  "Hora": "20:05:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-27-2024",
  "Hora": "08:04:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-27-2024",
  "Hora": "17:56:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-28-2024",
  "Hora": "08:22:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "03-28-2024",
  "Hora": "23:34:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-01-2024",
  "Hora": "08:02:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-01-2024",
  "Hora": "18:01:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-02-2024",
  "Hora": "07:44:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-02-2024",
  "Hora": "18:03:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-03-2024",
  "Hora": "07:48:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-03-2024",
  "Hora": "18:01:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-04-2024",
  "Hora": "07:58:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-04-2024",
  "Hora": "18:02:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-05-2024",
  "Hora": "07:46:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-05-2024",
  "Hora": "17:01:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-06-2024",
  "Hora": "07:58:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-06-2024",
  "Hora": "14:01:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-08-2024",
  "Hora": "07:56:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-08-2024",
  "Hora": "18:02:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-09-2024",
  "Hora": "07:42:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-09-2024",
  "Hora": "20:02:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-10-2024",
  "Hora": "07:45:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-10-2024",
  "Hora": "20:01:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-10-2024",
  "Hora": "20:01:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-11-2024",
  "Hora": "08:05:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-11-2024",
  "Hora": "18:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-12-2024",
  "Hora": "07:53:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-12-2024",
  "Hora": "17:03:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-13-2024",
  "Hora": "07:42:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-13-2024",
  "Hora": "07:42:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-13-2024",
  "Hora": "14:10:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-15-2024",
  "Hora": "08:16:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-15-2024",
  "Hora": "08:16:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-15-2024",
  "Hora": "18:03:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 138063798,
  "Date": "04-15-2024",
  "Hora": "18:03:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118812441,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-16-2024",
  "Hora": "02:26:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-16-2024",
  "Hora": "10:57:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-18-2024",
  "Hora": "03:54:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-18-2024",
  "Hora": "12:10:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-19-2024",
  "Hora": "04:07:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-19-2024",
  "Hora": "12:18:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-20-2024",
  "Hora": "04:05:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-20-2024",
  "Hora": "12:08:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-21-2024",
  "Hora": "04:04:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-21-2024",
  "Hora": "12:08:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-22-2024",
  "Hora": "03:52:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-22-2024",
  "Hora": "12:23:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-23-2024",
  "Hora": "03:53:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-23-2024",
  "Hora": "12:15:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-25-2024",
  "Hora": "03:49:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-25-2024",
  "Hora": "12:05:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-26-2024",
  "Hora": "03:51:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-26-2024",
  "Hora": "12:06:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-27-2024",
  "Hora": "04:59:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-27-2024",
  "Hora": "12:05:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-28-2024",
  "Hora": "04:00:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "03-28-2024",
  "Hora": "12:00:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-01-2024",
  "Hora": "04:03:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-01-2024",
  "Hora": "13:26:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-02-2024",
  "Hora": "03:50:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-02-2024",
  "Hora": "13:18:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-03-2024",
  "Hora": "03:43:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-03-2024",
  "Hora": "12:06:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-04-2024",
  "Hora": "03:18:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-04-2024",
  "Hora": "11:59:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-05-2024",
  "Hora": "03:35:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-05-2024",
  "Hora": "12:10:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-06-2024",
  "Hora": "03:32:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-06-2024",
  "Hora": "10:58:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-08-2024",
  "Hora": "02:25:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-08-2024",
  "Hora": "11:13:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-09-2024",
  "Hora": "02:48:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-09-2024",
  "Hora": "11:05:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-10-2024",
  "Hora": "03:29:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-10-2024",
  "Hora": "11:09:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-11-2024",
  "Hora": "02:42:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-11-2024",
  "Hora": "11:04:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-12-2024",
  "Hora": "03:34:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-12-2024",
  "Hora": "11:05:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-13-2024",
  "Hora": "02:40:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-13-2024",
  "Hora": "10:50:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-15-2024",
  "Hora": "03:46:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "21629324K",
  "Date": "04-15-2024",
  "Hora": "12:00:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 175001395,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-18-2024",
  "Hora": "08:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-18-2024",
  "Hora": "18:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-18-2024",
  "Hora": "18:02:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-19-2024",
  "Hora": "08:19:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-19-2024",
  "Hora": "20:00:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-20-2024",
  "Hora": "11:09:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-20-2024",
  "Hora": "18:01:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-21-2024",
  "Hora": "09:34:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-21-2024",
  "Hora": "20:01:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-25-2024",
  "Hora": "08:11:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-25-2024",
  "Hora": "18:01:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-26-2024",
  "Hora": "08:20:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-26-2024",
  "Hora": "20:02:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-27-2024",
  "Hora": "08:24:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-27-2024",
  "Hora": "20:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-28-2024",
  "Hora": "09:35:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "03-28-2024",
  "Hora": "23:39:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-01-2024",
  "Hora": "08:15:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-01-2024",
  "Hora": "18:02:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-02-2024",
  "Hora": "08:20:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-02-2024",
  "Hora": "18:02:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-03-2024",
  "Hora": "08:25:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-03-2024",
  "Hora": "18:03:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-04-2024",
  "Hora": "08:25:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-04-2024",
  "Hora": "18:01:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-05-2024",
  "Hora": "08:12:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-05-2024",
  "Hora": "16:42:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-08-2024",
  "Hora": "08:14:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-08-2024",
  "Hora": "18:01:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-09-2024",
  "Hora": "08:21:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-09-2024",
  "Hora": "20:00:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-10-2024",
  "Hora": "08:28:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-10-2024",
  "Hora": "20:01:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-11-2024",
  "Hora": "08:18:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-11-2024",
  "Hora": "20:00:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-12-2024",
  "Hora": "11:03:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-12-2024",
  "Hora": "17:02:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-15-2024",
  "Hora": "08:27:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 132515964,
  "Date": "04-15-2024",
  "Hora": "18:02:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-01-2024",
  "Hora": "08:01:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-01-2024",
  "Hora": "18:08:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-02-2024",
  "Hora": "07:53:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-02-2024",
  "Hora": "18:01:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-03-2024",
  "Hora": "08:05:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-03-2024",
  "Hora": "18:01:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-04-2024",
  "Hora": "07:59:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-04-2024",
  "Hora": "18:00:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-05-2024",
  "Hora": "08:18:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-05-2024",
  "Hora": "18:02:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-08-2024",
  "Hora": "08:02:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-08-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-09-2024",
  "Hora": "07:58:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-09-2024",
  "Hora": "18:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-10-2024",
  "Hora": "08:22:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-10-2024",
  "Hora": "18:04:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-11-2024",
  "Hora": "07:58:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-11-2024",
  "Hora": "18:00:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-12-2024",
  "Hora": "08:19:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-12-2024",
  "Hora": "18:00:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-15-2024",
  "Hora": "07:59:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 165301382,
  "Date": "04-15-2024",
  "Hora": "18:01:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-16-2024",
  "Hora": "00:18:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-18-2024",
  "Hora": "15:41:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-19-2024",
  "Hora": "01:19:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-19-2024",
  "Hora": "15:41:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-20-2024",
  "Hora": "01:16:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-20-2024",
  "Hora": "15:40:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-21-2024",
  "Hora": "01:20:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-21-2024",
  "Hora": "15:41:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-22-2024",
  "Hora": "01:20:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-22-2024",
  "Hora": "16:02:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-23-2024",
  "Hora": "00:18:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-25-2024",
  "Hora": "15:44:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-26-2024",
  "Hora": "01:23:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-26-2024",
  "Hora": "15:46:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-27-2024",
  "Hora": "01:22:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-27-2024",
  "Hora": "15:51:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-28-2024",
  "Hora": "01:04:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-28-2024",
  "Hora": "15:51:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "03-28-2024",
  "Hora": "23:54:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-01-2024",
  "Hora": "15:43:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-02-2024",
  "Hora": "01:39:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-02-2024",
  "Hora": "15:49:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-03-2024",
  "Hora": "01:26:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-03-2024",
  "Hora": "15:47:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-04-2024",
  "Hora": "01:24:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-04-2024",
  "Hora": "15:50:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-05-2024",
  "Hora": "01:25:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-05-2024",
  "Hora": "15:45:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-05-2024",
  "Hora": "23:58:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-08-2024",
  "Hora": "15:44:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-09-2024",
  "Hora": "01:20:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-09-2024",
  "Hora": "15:43:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-10-2024",
  "Hora": "01:17:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-10-2024",
  "Hora": "15:56:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-11-2024",
  "Hora": "01:04:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-11-2024",
  "Hora": "15:47:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-12-2024",
  "Hora": "01:05:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-12-2024",
  "Hora": "15:48:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-13-2024",
  "Hora": "00:17:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 118461223,
  "Date": "04-15-2024",
  "Hora": "15:44:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 177501999,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-18-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-18-2024",
  "Hora": "16:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-19-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-19-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-20-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-20-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-21-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-21-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-22-2024",
  "Hora": "10:19:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-22-2024",
  "Hora": "14:32:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-22-2024",
  "Hora": "15:32:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-22-2024",
  "Hora": "16:55:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-23-2024",
  "Hora": "07:48:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-23-2024",
  "Hora": "12:29:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-26-2024",
  "Hora": "07:08:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-26-2024",
  "Hora": "15:55:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-26-2024",
  "Hora": "16:51:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-26-2024",
  "Hora": "16:57:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-27-2024",
  "Hora": "07:03:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-27-2024",
  "Hora": "14:59:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-27-2024",
  "Hora": "14:59:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-27-2024",
  "Hora": "15:58:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-27-2024",
  "Hora": "16:55:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-28-2024",
  "Hora": "06:59:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "03-28-2024",
  "Hora": "13:07:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-01-2024",
  "Hora": "06:47:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-01-2024",
  "Hora": "14:55:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-01-2024",
  "Hora": "15:53:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-01-2024",
  "Hora": "16:57:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-02-2024",
  "Hora": "07:02:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-02-2024",
  "Hora": "15:10:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-02-2024",
  "Hora": "16:09:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-02-2024",
  "Hora": "16:55:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-03-2024",
  "Hora": "06:53:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-03-2024",
  "Hora": "15:09:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-03-2024",
  "Hora": "16:08:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-03-2024",
  "Hora": "16:51:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-04-2024",
  "Hora": "07:08:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-04-2024",
  "Hora": "15:01:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-04-2024",
  "Hora": "16:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-04-2024",
  "Hora": "16:58:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-05-2024",
  "Hora": "06:58:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-05-2024",
  "Hora": "15:10:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-05-2024",
  "Hora": "16:10:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-05-2024",
  "Hora": "16:59:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-06-2024",
  "Hora": "08:01:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-06-2024",
  "Hora": "13:00:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-06-2024",
  "Hora": "14:00:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-06-2024",
  "Hora": "15:00:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-09-2024",
  "Hora": "07:11:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-09-2024",
  "Hora": "15:12:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-09-2024",
  "Hora": "16:05:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-09-2024",
  "Hora": "16:57:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-10-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-10-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-11-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-11-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-12-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-12-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-15-2024",
  "Hora": "07:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "0177501999",
  "Date": "04-15-2024",
  "Hora": "17:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-16-2024",
  "Hora": "03:25:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-18-2024",
  "Hora": "18:06:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-19-2024",
  "Hora": "03:39:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-19-2024",
  "Hora": "17:58:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-20-2024",
  "Hora": "03:05:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-20-2024",
  "Hora": "17:49:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-21-2024",
  "Hora": "03:13:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-21-2024",
  "Hora": "18:13:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-22-2024",
  "Hora": "03:27:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-25-2024",
  "Hora": "18:16:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-26-2024",
  "Hora": "03:25:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-26-2024",
  "Hora": "18:08:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-27-2024",
  "Hora": "03:54:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-27-2024",
  "Hora": "18:19:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-28-2024",
  "Hora": "03:38:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-28-2024",
  "Hora": "18:15:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "03-29-2024",
  "Hora": "00:01:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-01-2024",
  "Hora": "17:57:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-02-2024",
  "Hora": "03:49:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-02-2024",
  "Hora": "18:07:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-03-2024",
  "Hora": "03:55:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-03-2024",
  "Hora": "17:45:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-04-2024",
  "Hora": "03:25:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-04-2024",
  "Hora": "17:56:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-05-2024",
  "Hora": "03:24:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-05-2024",
  "Hora": "18:53:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-06-2024",
  "Hora": "03:26:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-08-2024",
  "Hora": "17:46:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-09-2024",
  "Hora": "03:33:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-09-2024",
  "Hora": "17:47:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-10-2024",
  "Hora": "03:29:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-10-2024",
  "Hora": "17:52:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-11-2024",
  "Hora": "03:40:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-11-2024",
  "Hora": "17:44:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-12-2024",
  "Hora": "03:35:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-12-2024",
  "Hora": "19:04:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-13-2024",
  "Hora": "03:07:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 192389178,
  "Date": "04-15-2024",
  "Hora": "17:53:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-18-2024",
  "Hora": "15:53:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-19-2024",
  "Hora": "01:20:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-19-2024",
  "Hora": "15:51:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-20-2024",
  "Hora": "01:16:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-20-2024",
  "Hora": "15:37:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-21-2024",
  "Hora": "01:19:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-21-2024",
  "Hora": "15:52:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-22-2024",
  "Hora": "01:23:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-22-2024",
  "Hora": "15:49:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-23-2024",
  "Hora": "00:18:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-25-2024",
  "Hora": "15:27:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-26-2024",
  "Hora": "01:23:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-26-2024",
  "Hora": "15:42:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-27-2024",
  "Hora": "01:23:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-27-2024",
  "Hora": "16:00:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-28-2024",
  "Hora": "01:16:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-28-2024",
  "Hora": "15:55:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "03-29-2024",
  "Hora": "00:00:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "04-01-2024",
  "Hora": "15:52:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "04-02-2024",
  "Hora": "01:35:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "04-02-2024",
  "Hora": "15:40:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "04-03-2024",
  "Hora": "02:34:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "04-03-2024",
  "Hora": "15:52:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "04-04-2024",
  "Hora": "01:23:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "04-04-2024",
  "Hora": "15:49:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "04-05-2024",
  "Hora": "01:26:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "04-05-2024",
  "Hora": "15:56:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "04-05-2024",
  "Hora": "17:43:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 256546493,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "13082756K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 88241193,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-18-2024",
  "Hora": "23:53:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-19-2024",
  "Hora": "10:09:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-19-2024",
  "Hora": "23:51:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-20-2024",
  "Hora": "10:14:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-20-2024",
  "Hora": "23:53:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-21-2024",
  "Hora": "10:08:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-22-2024",
  "Hora": "00:00:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-22-2024",
  "Hora": "10:30:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-23-2024",
  "Hora": "00:02:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-23-2024",
  "Hora": "10:10:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-24-2024",
  "Hora": "23:53:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-25-2024",
  "Hora": "10:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-25-2024",
  "Hora": "23:50:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-26-2024",
  "Hora": "09:56:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-26-2024",
  "Hora": "23:52:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-27-2024",
  "Hora": "12:10:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-27-2024",
  "Hora": "23:59:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-28-2024",
  "Hora": "10:11:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "03-31-2024",
  "Hora": "23:55:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-01-2024",
  "Hora": "00:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-01-2024",
  "Hora": "10:11:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-02-2024",
  "Hora": "23:51:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-02-2024",
  "Hora": "23:51:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-03-2024",
  "Hora": "10:09:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-03-2024",
  "Hora": "23:51:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-04-2024",
  "Hora": "10:05:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-04-2024",
  "Hora": "23:50:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-05-2024",
  "Hora": "10:19:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-05-2024",
  "Hora": "23:53:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-06-2024",
  "Hora": "10:05:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-07-2024",
  "Hora": "23:53:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-08-2024",
  "Hora": "10:10:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-08-2024",
  "Hora": "23:55:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-09-2024",
  "Hora": "10:05:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-09-2024",
  "Hora": "23:53:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-10-2024",
  "Hora": "10:08:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-10-2024",
  "Hora": "23:53:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-11-2024",
  "Hora": "10:10:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-11-2024",
  "Hora": "23:53:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-12-2024",
  "Hora": "10:06:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 206426314,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-18-2024",
  "Hora": "08:02:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-18-2024",
  "Hora": "18:06:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-19-2024",
  "Hora": "08:02:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-19-2024",
  "Hora": "18:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-20-2024",
  "Hora": "08:13:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-20-2024",
  "Hora": "18:00:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-21-2024",
  "Hora": "08:00:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-21-2024",
  "Hora": "18:01:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-22-2024",
  "Hora": "08:11:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-22-2024",
  "Hora": "18:00:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-25-2024",
  "Hora": "08:02:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-25-2024",
  "Hora": "17:59:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-26-2024",
  "Hora": "08:01:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-26-2024",
  "Hora": "17:20:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-28-2024",
  "Hora": "08:05:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "03-28-2024",
  "Hora": "18:01:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-01-2024",
  "Hora": "08:01:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-01-2024",
  "Hora": "18:00:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-02-2024",
  "Hora": "08:02:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-02-2024",
  "Hora": "18:00:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-03-2024",
  "Hora": "08:02:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-03-2024",
  "Hora": "18:01:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-04-2024",
  "Hora": "08:02:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-04-2024",
  "Hora": "18:02:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-05-2024",
  "Hora": "10:39:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-05-2024",
  "Hora": "18:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-08-2024",
  "Hora": "09:04:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-08-2024",
  "Hora": "19:01:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-09-2024",
  "Hora": "09:01:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-09-2024",
  "Hora": "18:59:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-10-2024",
  "Hora": "09:07:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-10-2024",
  "Hora": "18:59:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-11-2024",
  "Hora": "09:04:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-11-2024",
  "Hora": "18:57:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-12-2024",
  "Hora": "09:09:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-12-2024",
  "Hora": "19:00:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-15-2024",
  "Hora": "09:01:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 147324057,
  "Date": "04-15-2024",
  "Hora": "18:05:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-16-2024",
  "Hora": "05:43:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-16-2024",
  "Hora": "13:46:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-18-2024",
  "Hora": "05:43:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-18-2024",
  "Hora": "14:01:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-19-2024",
  "Hora": "05:43:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-19-2024",
  "Hora": "13:47:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-20-2024",
  "Hora": "05:50:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-20-2024",
  "Hora": "13:46:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-21-2024",
  "Hora": "05:39:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-21-2024",
  "Hora": "13:46:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-22-2024",
  "Hora": "05:42:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-22-2024",
  "Hora": "13:45:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-23-2024",
  "Hora": "05:42:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-23-2024",
  "Hora": "13:46:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-25-2024",
  "Hora": "05:50:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-25-2024",
  "Hora": "14:02:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-26-2024",
  "Hora": "05:44:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-26-2024",
  "Hora": "13:50:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-27-2024",
  "Hora": "05:44:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-27-2024",
  "Hora": "13:46:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-28-2024",
  "Hora": "05:40:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "03-28-2024",
  "Hora": "13:45:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-01-2024",
  "Hora": "05:58:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-01-2024",
  "Hora": "14:00:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-02-2024",
  "Hora": "05:41:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-02-2024",
  "Hora": "13:45:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-03-2024",
  "Hora": "05:40:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-03-2024",
  "Hora": "08:39:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-03-2024",
  "Hora": "10:58:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-03-2024",
  "Hora": "13:49:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-04-2024",
  "Hora": "05:44:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-04-2024",
  "Hora": "13:46:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-05-2024",
  "Hora": "05:42:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-05-2024",
  "Hora": "13:46:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-06-2024",
  "Hora": "05:40:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-06-2024",
  "Hora": "13:45:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-08-2024",
  "Hora": "05:56:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-08-2024",
  "Hora": "14:00:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-09-2024",
  "Hora": "05:46:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-09-2024",
  "Hora": "13:45:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-10-2024",
  "Hora": "05:46:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-10-2024",
  "Hora": "13:45:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-11-2024",
  "Hora": "05:37:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-11-2024",
  "Hora": "13:45:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-12-2024",
  "Hora": "05:37:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-12-2024",
  "Hora": "13:45:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-13-2024",
  "Hora": "05:41:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-13-2024",
  "Hora": "13:55:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-15-2024",
  "Hora": "05:52:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 189299737,
  "Date": "04-15-2024",
  "Hora": "14:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-16-2024",
  "Hora": "07:45:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-16-2024",
  "Hora": "14:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-18-2024",
  "Hora": "07:51:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-18-2024",
  "Hora": "18:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-19-2024",
  "Hora": "07:45:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-19-2024",
  "Hora": "18:00:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-20-2024",
  "Hora": "07:49:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-20-2024",
  "Hora": "20:00:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-21-2024",
  "Hora": "07:47:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-21-2024",
  "Hora": "18:00:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-21-2024",
  "Hora": "18:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-22-2024",
  "Hora": "07:47:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-22-2024",
  "Hora": "17:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-22-2024",
  "Hora": "17:00:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-27-2024",
  "Hora": "07:47:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-27-2024",
  "Hora": "20:00:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-28-2024",
  "Hora": "07:48:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "03-28-2024",
  "Hora": "23:27:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-01-2024",
  "Hora": "07:49:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-01-2024",
  "Hora": "18:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-02-2024",
  "Hora": "07:44:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-02-2024",
  "Hora": "18:00:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-03-2024",
  "Hora": "07:47:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-03-2024",
  "Hora": "18:00:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-04-2024",
  "Hora": "07:43:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-04-2024",
  "Hora": "07:43:52",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-04-2024",
  "Hora": "18:00:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-05-2024",
  "Hora": "07:45:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-05-2024",
  "Hora": "17:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-06-2024",
  "Hora": "07:46:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-06-2024",
  "Hora": "14:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-08-2024",
  "Hora": "07:47:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-08-2024",
  "Hora": "18:00:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-09-2024",
  "Hora": "07:42:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-09-2024",
  "Hora": "18:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-10-2024",
  "Hora": "07:45:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-10-2024",
  "Hora": "20:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-11-2024",
  "Hora": "07:43:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-11-2024",
  "Hora": "18:00:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-12-2024",
  "Hora": "07:44:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-12-2024",
  "Hora": "17:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-13-2024",
  "Hora": "07:42:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-13-2024",
  "Hora": "07:42:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-13-2024",
  "Hora": "14:00:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-13-2024",
  "Hora": "14:00:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-15-2024",
  "Hora": "07:43:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 255518135,
  "Date": "04-15-2024",
  "Hora": "18:00:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-16-2024",
  "Hora": "03:28:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-18-2024",
  "Hora": "17:37:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-19-2024",
  "Hora": "03:21:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-19-2024",
  "Hora": "17:48:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-20-2024",
  "Hora": "03:05:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-20-2024",
  "Hora": "17:53:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-21-2024",
  "Hora": "03:44:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-21-2024",
  "Hora": "17:45:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-22-2024",
  "Hora": "03:45:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-22-2024",
  "Hora": "18:40:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-23-2024",
  "Hora": "03:30:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-25-2024",
  "Hora": "18:05:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-26-2024",
  "Hora": "03:26:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-26-2024",
  "Hora": "17:46:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-27-2024",
  "Hora": "03:52:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-27-2024",
  "Hora": "17:39:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-28-2024",
  "Hora": "03:39:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-28-2024",
  "Hora": "17:58:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-28-2024",
  "Hora": "18:15:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "03-29-2024",
  "Hora": "00:01:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-01-2024",
  "Hora": "17:41:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-02-2024",
  "Hora": "03:47:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-02-2024",
  "Hora": "17:36:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-03-2024",
  "Hora": "03:44:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-03-2024",
  "Hora": "17:47:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-04-2024",
  "Hora": "03:18:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-04-2024",
  "Hora": "17:30:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-05-2024",
  "Hora": "03:23:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-05-2024",
  "Hora": "18:55:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-06-2024",
  "Hora": "03:17:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-08-2024",
  "Hora": "17:47:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-09-2024",
  "Hora": "03:37:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-09-2024",
  "Hora": "17:40:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-10-2024",
  "Hora": "03:33:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-10-2024",
  "Hora": "17:51:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-11-2024",
  "Hora": "03:35:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-12-2024",
  "Hora": "18:36:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-13-2024",
  "Hora": "03:05:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 244108911,
  "Date": "04-15-2024",
  "Hora": "17:37:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 270167489,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-16-2024",
  "Hora": "08:04:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-16-2024",
  "Hora": "14:03:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-18-2024",
  "Hora": "08:22:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-18-2024",
  "Hora": "18:01:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-19-2024",
  "Hora": "08:06:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-19-2024",
  "Hora": "18:01:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-20-2024",
  "Hora": "08:20:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-20-2024",
  "Hora": "20:05:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-21-2024",
  "Hora": "08:20:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-21-2024",
  "Hora": "20:00:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-22-2024",
  "Hora": "08:03:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-22-2024",
  "Hora": "17:00:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-25-2024",
  "Hora": "08:18:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-25-2024",
  "Hora": "20:00:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-25-2024",
  "Hora": "20:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-26-2024",
  "Hora": "08:04:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-26-2024",
  "Hora": "20:00:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-27-2024",
  "Hora": "08:20:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-27-2024",
  "Hora": "18:03:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-28-2024",
  "Hora": "08:16:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "03-28-2024",
  "Hora": "18:00:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-01-2024",
  "Hora": "08:15:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-01-2024",
  "Hora": "08:15:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-01-2024",
  "Hora": "18:02:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-02-2024",
  "Hora": "08:23:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-02-2024",
  "Hora": "18:01:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-03-2024",
  "Hora": "07:59:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-03-2024",
  "Hora": "18:01:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-04-2024",
  "Hora": "08:18:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-04-2024",
  "Hora": "18:04:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-05-2024",
  "Hora": "08:13:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-05-2024",
  "Hora": "17:03:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-08-2024",
  "Hora": "08:05:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-08-2024",
  "Hora": "18:02:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-09-2024",
  "Hora": "08:10:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-09-2024",
  "Hora": "18:01:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-10-2024",
  "Hora": "07:57:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-10-2024",
  "Hora": "18:01:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-11-2024",
  "Hora": "08:11:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-11-2024",
  "Hora": "20:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-12-2024",
  "Hora": "09:51:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-12-2024",
  "Hora": "17:01:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-15-2024",
  "Hora": "08:13:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 203340591,
  "Date": "04-15-2024",
  "Hora": "18:02:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-16-2024",
  "Hora": "04:48:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-16-2024",
  "Hora": "13:01:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-18-2024",
  "Hora": "05:50:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-18-2024",
  "Hora": "14:00:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-19-2024",
  "Hora": "04:45:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-19-2024",
  "Hora": "13:00:14",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-20-2024",
  "Hora": "04:48:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-20-2024",
  "Hora": "13:01:54",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-21-2024",
  "Hora": "04:51:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-21-2024",
  "Hora": "13:00:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-22-2024",
  "Hora": "04:50:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-22-2024",
  "Hora": "13:03:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-23-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-23-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-23-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-23-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-23-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-23-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-23-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-23-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-23-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-23-2024",
  "Hora": "04:52:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-23-2024",
  "Hora": "13:01:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-25-2024",
  "Hora": "05:54:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-25-2024",
  "Hora": "14:01:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-26-2024",
  "Hora": "04:47:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-26-2024",
  "Hora": "13:07:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-27-2024",
  "Hora": "04:50:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-27-2024",
  "Hora": "13:02:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-28-2024",
  "Hora": "04:55:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "03-28-2024",
  "Hora": "13:05:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-01-2024",
  "Hora": "05:47:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-01-2024",
  "Hora": "14:01:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-02-2024",
  "Hora": "04:50:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-02-2024",
  "Hora": "13:05:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-03-2024",
  "Hora": "04:50:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-03-2024",
  "Hora": "13:03:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-04-2024",
  "Hora": "04:54:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-04-2024",
  "Hora": "13:03:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-05-2024",
  "Hora": "04:49:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-05-2024",
  "Hora": "13:06:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-06-2024",
  "Hora": "04:57:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-06-2024",
  "Hora": "13:01:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-08-2024",
  "Hora": "05:45:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-08-2024",
  "Hora": "14:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-09-2024",
  "Hora": "04:48:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-09-2024",
  "Hora": "13:02:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-10-2024",
  "Hora": "04:49:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-10-2024",
  "Hora": "13:06:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-11-2024",
  "Hora": "04:53:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-11-2024",
  "Hora": "13:01:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-12-2024",
  "Hora": "04:51:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-12-2024",
  "Hora": "13:03:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-13-2024",
  "Hora": "04:50:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-13-2024",
  "Hora": "11:39:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-15-2024",
  "Hora": "05:49:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "19983908K",
  "Date": "04-15-2024",
  "Hora": "14:01:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-18-2024",
  "Hora": "07:17:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-18-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-19-2024",
  "Hora": "08:46:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-19-2024",
  "Hora": "18:04:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-20-2024",
  "Hora": "08:30:40",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-20-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-21-2024",
  "Hora": "09:15:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-21-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-22-2024",
  "Hora": "08:30:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-22-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-29-2024",
  "Hora": "08:42:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-29-2024",
  "Hora": "18:00:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-30-2024",
  "Hora": "00:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-30-2024",
  "Hora": "09:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "03-30-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-01-2024",
  "Hora": "08:44:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-01-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-02-2024",
  "Hora": "08:30:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-02-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-03-2024",
  "Hora": "08:52:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-03-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-04-2024",
  "Hora": "09:04:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-04-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-05-2024",
  "Hora": "08:52:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-05-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-08-2024",
  "Hora": "08:47:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-08-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-09-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-09-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-10-2024",
  "Hora": "08:36:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-10-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-11-2024",
  "Hora": "08:30:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-11-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-12-2024",
  "Hora": "08:52:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-12-2024",
  "Hora": "18:00:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-15-2024",
  "Hora": "08:30:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 151000169,
  "Date": "04-15-2024",
  "Hora": "18:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-16-2024",
  "Hora": "03:37:47",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-16-2024",
  "Hora": "11:03:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-18-2024",
  "Hora": "02:38:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-18-2024",
  "Hora": "11:08:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-19-2024",
  "Hora": "02:53:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-19-2024",
  "Hora": "11:12:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-20-2024",
  "Hora": "02:38:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-20-2024",
  "Hora": "11:17:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-21-2024",
  "Hora": "02:26:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-21-2024",
  "Hora": "11:13:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-22-2024",
  "Hora": "02:17:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-22-2024",
  "Hora": "11:13:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-23-2024",
  "Hora": "02:14:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-23-2024",
  "Hora": "11:11:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-25-2024",
  "Hora": "05:10:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-25-2024",
  "Hora": "12:09:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-26-2024",
  "Hora": "03:52:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-26-2024",
  "Hora": "12:11:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-27-2024",
  "Hora": "03:58:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-27-2024",
  "Hora": "12:14:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-28-2024",
  "Hora": "04:01:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "03-28-2024",
  "Hora": "11:59:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-01-2024",
  "Hora": "02:28:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-01-2024",
  "Hora": "11:18:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-02-2024",
  "Hora": "02:25:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-02-2024",
  "Hora": "11:13:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-03-2024",
  "Hora": "03:48:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-03-2024",
  "Hora": "11:12:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-04-2024",
  "Hora": "02:25:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-04-2024",
  "Hora": "11:22:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-05-2024",
  "Hora": "02:34:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-05-2024",
  "Hora": "11:16:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-06-2024",
  "Hora": "02:52:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-06-2024",
  "Hora": "11:02:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-08-2024",
  "Hora": "03:58:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-08-2024",
  "Hora": "12:12:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-09-2024",
  "Hora": "03:55:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-09-2024",
  "Hora": "12:07:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-10-2024",
  "Hora": "03:29:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-10-2024",
  "Hora": "12:05:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-11-2024",
  "Hora": "03:34:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-11-2024",
  "Hora": "11:58:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-12-2024",
  "Hora": "03:39:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-12-2024",
  "Hora": "12:07:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-13-2024",
  "Hora": "03:33:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-13-2024",
  "Hora": "11:01:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-15-2024",
  "Hora": "03:45:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260144618,
  "Date": "04-15-2024",
  "Hora": "12:07:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-19-2024",
  "Hora": "03:50:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-19-2024",
  "Hora": "03:50:26",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-19-2024",
  "Hora": "12:13:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-20-2024",
  "Hora": "04:05:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-20-2024",
  "Hora": "04:05:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-20-2024",
  "Hora": "12:04:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-20-2024",
  "Hora": "12:04:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-21-2024",
  "Hora": "03:48:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-21-2024",
  "Hora": "03:49:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-21-2024",
  "Hora": "12:08:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-21-2024",
  "Hora": "12:08:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-22-2024",
  "Hora": "04:00:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-22-2024",
  "Hora": "04:00:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-22-2024",
  "Hora": "12:13:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-22-2024",
  "Hora": "12:13:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-23-2024",
  "Hora": "03:49:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-23-2024",
  "Hora": "03:49:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-23-2024",
  "Hora": "12:06:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-25-2024",
  "Hora": "04:07:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-25-2024",
  "Hora": "04:08:11",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-25-2024",
  "Hora": "12:05:45",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-25-2024",
  "Hora": "12:05:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-26-2024",
  "Hora": "05:13:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-26-2024",
  "Hora": "05:13:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-26-2024",
  "Hora": "12:08:53",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-26-2024",
  "Hora": "12:09:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-27-2024",
  "Hora": "03:45:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-27-2024",
  "Hora": "03:45:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-27-2024",
  "Hora": "12:12:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-28-2024",
  "Hora": "03:58:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-28-2024",
  "Hora": "03:58:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "03-28-2024",
  "Hora": "11:57:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-01-2024",
  "Hora": "04:18:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-01-2024",
  "Hora": "04:19:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-01-2024",
  "Hora": "12:17:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-02-2024",
  "Hora": "03:59:55",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-02-2024",
  "Hora": "03:59:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-02-2024",
  "Hora": "12:08:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-02-2024",
  "Hora": "12:08:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-03-2024",
  "Hora": "03:36:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-03-2024",
  "Hora": "03:36:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-03-2024",
  "Hora": "12:14:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-03-2024",
  "Hora": "12:14:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-04-2024",
  "Hora": "04:11:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-04-2024",
  "Hora": "04:11:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-04-2024",
  "Hora": "11:53:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-04-2024",
  "Hora": "11:53:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-05-2024",
  "Hora": "03:26:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-05-2024",
  "Hora": "03:27:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-05-2024",
  "Hora": "12:08:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-05-2024",
  "Hora": "12:08:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-06-2024",
  "Hora": "03:25:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-06-2024",
  "Hora": "03:25:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-06-2024",
  "Hora": "10:59:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-06-2024",
  "Hora": "10:59:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-08-2024",
  "Hora": "03:20:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-08-2024",
  "Hora": "03:20:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-08-2024",
  "Hora": "12:02:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-08-2024",
  "Hora": "12:02:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-09-2024",
  "Hora": "03:35:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-09-2024",
  "Hora": "03:36:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-09-2024",
  "Hora": "12:07:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-09-2024",
  "Hora": "12:07:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-10-2024",
  "Hora": "03:24:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-10-2024",
  "Hora": "03:24:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-10-2024",
  "Hora": "12:06:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-10-2024",
  "Hora": "12:06:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-11-2024",
  "Hora": "03:24:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-11-2024",
  "Hora": "03:24:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-11-2024",
  "Hora": "11:59:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-11-2024",
  "Hora": "11:59:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-11-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-12-2024",
  "Hora": "03:26:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-12-2024",
  "Hora": "03:26:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-12-2024",
  "Hora": "12:02:32",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-12-2024",
  "Hora": "12:02:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-13-2024",
  "Hora": "03:24:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-13-2024",
  "Hora": "03:24:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-13-2024",
  "Hora": "10:59:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-13-2024",
  "Hora": "10:59:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-15-2024",
  "Hora": "03:53:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-15-2024",
  "Hora": "03:53:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-15-2024",
  "Hora": "12:04:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 260367684,
  "Date": "04-15-2024",
  "Hora": "12:04:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 237738497,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-18-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-18-2024",
  "Hora": "18:01:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-19-2024",
  "Hora": "09:48:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-19-2024",
  "Hora": "18:03:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-20-2024",
  "Hora": "08:43:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-20-2024",
  "Hora": "18:00:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-21-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-21-2024",
  "Hora": "20:04:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-22-2024",
  "Hora": "08:37:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-22-2024",
  "Hora": "19:56:23",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-23-2024",
  "Hora": "07:26:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-23-2024",
  "Hora": "15:01:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-25-2024",
  "Hora": "08:25:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-25-2024",
  "Hora": "20:03:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-26-2024",
  "Hora": "08:18:14",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-26-2024",
  "Hora": "20:01:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-27-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-27-2024",
  "Hora": "20:02:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-28-2024",
  "Hora": "08:22:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "03-28-2024",
  "Hora": "18:06:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-01-2024",
  "Hora": "08:10:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-01-2024",
  "Hora": "18:04:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-02-2024",
  "Hora": "08:10:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-02-2024",
  "Hora": "18:05:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-03-2024",
  "Hora": "11:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-03-2024",
  "Hora": "18:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-04-2024",
  "Hora": "08:12:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-04-2024",
  "Hora": "18:03:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-05-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-05-2024",
  "Hora": "18:00:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-08-2024",
  "Hora": "09:38:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-08-2024",
  "Hora": "19:02:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-09-2024",
  "Hora": "09:19:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-09-2024",
  "Hora": "19:01:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-10-2024",
  "Hora": "08:30:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-10-2024",
  "Hora": "19:01:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-11-2024",
  "Hora": "09:13:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-11-2024",
  "Hora": "18:58:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-12-2024",
  "Hora": "09:15:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-12-2024",
  "Hora": "19:03:41",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-15-2024",
  "Hora": "09:16:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "18697154K",
  "Date": "04-15-2024",
  "Hora": "18:04:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-16-2024",
  "Hora": "07:52:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-16-2024",
  "Hora": "14:03:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-18-2024",
  "Hora": "07:51:51",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-18-2024",
  "Hora": "20:00:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-19-2024",
  "Hora": "07:48:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-19-2024",
  "Hora": "18:02:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-20-2024",
  "Hora": "07:50:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-20-2024",
  "Hora": "18:02:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-21-2024",
  "Hora": "07:48:43",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-21-2024",
  "Hora": "20:01:09",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-22-2024",
  "Hora": "07:49:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-22-2024",
  "Hora": "17:02:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "08:00:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-23-2024",
  "Hora": "14:02:05",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-25-2024",
  "Hora": "07:50:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-25-2024",
  "Hora": "18:02:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-26-2024",
  "Hora": "07:50:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-26-2024",
  "Hora": "20:01:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-27-2024",
  "Hora": "07:48:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-27-2024",
  "Hora": "20:00:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-28-2024",
  "Hora": "07:47:37",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "03-28-2024",
  "Hora": "18:01:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-01-2024",
  "Hora": "07:51:24",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-01-2024",
  "Hora": "18:02:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-02-2024",
  "Hora": "07:44:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-02-2024",
  "Hora": "18:02:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-03-2024",
  "Hora": "07:48:12",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-03-2024",
  "Hora": "18:02:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-04-2024",
  "Hora": "07:51:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-04-2024",
  "Hora": "18:02:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-05-2024",
  "Hora": "07:46:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-05-2024",
  "Hora": "17:01:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-06-2024",
  "Hora": "07:49:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-06-2024",
  "Hora": "14:01:06",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-08-2024",
  "Hora": "07:48:31",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-08-2024",
  "Hora": "18:03:02",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-09-2024",
  "Hora": "07:42:41",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-09-2024",
  "Hora": "18:01:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-10-2024",
  "Hora": "07:46:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-10-2024",
  "Hora": "20:01:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-11-2024",
  "Hora": "07:43:59",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-11-2024",
  "Hora": "18:01:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-12-2024",
  "Hora": "07:45:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-12-2024",
  "Hora": "17:01:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-13-2024",
  "Hora": "07:44:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-13-2024",
  "Hora": "14:01:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-15-2024",
  "Hora": "07:45:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": "15956956K",
  "Date": "04-15-2024",
  "Hora": "18:02:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-18-2024",
  "Hora": "14:00:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-18-2024",
  "Hora": "23:24:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-19-2024",
  "Hora": "13:52:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-19-2024",
  "Hora": "22:26:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-20-2024",
  "Hora": "13:54:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-20-2024",
  "Hora": "20:57:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-21-2024",
  "Hora": "13:50:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-22-2024",
  "Hora": "00:07:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-22-2024",
  "Hora": "13:52:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-22-2024",
  "Hora": "22:36:44",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-25-2024",
  "Hora": "13:45:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-25-2024",
  "Hora": "23:59:13",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-26-2024",
  "Hora": "13:44:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "03-26-2024",
  "Hora": "22:32:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-01-2024",
  "Hora": "13:51:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-02-2024",
  "Hora": "01:08:12",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-02-2024",
  "Hora": "13:50:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-02-2024",
  "Hora": "21:27:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-03-2024",
  "Hora": "13:40:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-03-2024",
  "Hora": "22:08:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-04-2024",
  "Hora": "13:55:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-04-2024",
  "Hora": "22:46:18",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-05-2024",
  "Hora": "13:55:01",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-05-2024",
  "Hora": "21:34:42",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-08-2024",
  "Hora": "13:54:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-08-2024",
  "Hora": "23:00:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-09-2024",
  "Hora": "13:42:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-09-2024",
  "Hora": "22:04:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-10-2024",
  "Hora": "13:41:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-10-2024",
  "Hora": "21:31:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-11-2024",
  "Hora": "13:43:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-11-2024",
  "Hora": "21:20:27",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-12-2024",
  "Hora": "13:57:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-12-2024",
  "Hora": "21:26:49",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-15-2024",
  "Hora": "13:44:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 205171428,
  "Date": "04-15-2024",
  "Hora": "22:35:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-16-2024",
  "Hora": "04:52:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-16-2024",
  "Hora": "11:30:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-18-2024",
  "Hora": "05:45:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-18-2024",
  "Hora": "14:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-19-2024",
  "Hora": "04:45:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-19-2024",
  "Hora": "13:03:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-20-2024",
  "Hora": "04:43:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-20-2024",
  "Hora": "13:00:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-21-2024",
  "Hora": "04:48:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-21-2024",
  "Hora": "13:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-22-2024",
  "Hora": "04:49:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-22-2024",
  "Hora": "13:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-23-2024",
  "Hora": "04:49:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-23-2024",
  "Hora": "12:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-25-2024",
  "Hora": "05:47:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-25-2024",
  "Hora": "14:01:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-26-2024",
  "Hora": "04:45:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-26-2024",
  "Hora": "12:32:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-27-2024",
  "Hora": "04:43:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-27-2024",
  "Hora": "13:00:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-28-2024",
  "Hora": "04:51:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "03-28-2024",
  "Hora": "13:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-01-2024",
  "Hora": "05:44:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-01-2024",
  "Hora": "13:00:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-02-2024",
  "Hora": "04:51:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-02-2024",
  "Hora": "13:00:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-03-2024",
  "Hora": "04:53:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-03-2024",
  "Hora": "13:00:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-04-2024",
  "Hora": "04:45:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-04-2024",
  "Hora": "13:00:48",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-05-2024",
  "Hora": "04:47:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-05-2024",
  "Hora": "13:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-06-2024",
  "Hora": "04:49:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-06-2024",
  "Hora": "12:30:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-08-2024",
  "Hora": "05:41:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-08-2024",
  "Hora": "14:00:37",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-09-2024",
  "Hora": "04:47:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-09-2024",
  "Hora": "13:00:10",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-10-2024",
  "Hora": "04:47:18",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-10-2024",
  "Hora": "13:01:31",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-11-2024",
  "Hora": "04:46:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-11-2024",
  "Hora": "13:00:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-12-2024",
  "Hora": "04:48:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-12-2024",
  "Hora": "13:00:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-13-2024",
  "Hora": "04:46:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-13-2024",
  "Hora": "13:00:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-15-2024",
  "Hora": "05:41:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 182456241,
  "Date": "04-15-2024",
  "Hora": "14:00:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-18-2024",
  "Hora": "04:57:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-18-2024",
  "Hora": "14:29:55",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-20-2024",
  "Hora": "04:56:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-20-2024",
  "Hora": "14:31:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-21-2024",
  "Hora": "04:59:09",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-21-2024",
  "Hora": "14:30:28",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-22-2024",
  "Hora": "04:59:03",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-22-2024",
  "Hora": "14:29:50",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-23-2024",
  "Hora": "04:58:10",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-23-2024",
  "Hora": "13:15:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-25-2024",
  "Hora": "04:59:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-25-2024",
  "Hora": "12:52:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-27-2024",
  "Hora": "04:56:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-27-2024",
  "Hora": "14:31:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-28-2024",
  "Hora": "04:57:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "03-28-2024",
  "Hora": "14:30:38",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-01-2024",
  "Hora": "04:59:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-01-2024",
  "Hora": "14:30:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-02-2024",
  "Hora": "04:53:02",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-02-2024",
  "Hora": "12:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-03-2024",
  "Hora": "04:53:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-03-2024",
  "Hora": "14:30:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-04-2024",
  "Hora": "04:53:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-04-2024",
  "Hora": "14:29:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-08-2024",
  "Hora": "04:53:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-08-2024",
  "Hora": "14:30:51",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-10-2024",
  "Hora": "04:54:08",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-10-2024",
  "Hora": "14:30:59",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-11-2024",
  "Hora": "04:58:57",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-11-2024",
  "Hora": "14:29:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-12-2024",
  "Hora": "04:53:35",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-12-2024",
  "Hora": "14:31:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-13-2024",
  "Hora": "04:55:39",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-13-2024",
  "Hora": "12:32:21",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-15-2024",
  "Hora": "04:54:49",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 200657381,
  "Date": "04-15-2024",
  "Hora": "14:30:34",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-18-2024",
  "Hora": "08:20:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-18-2024",
  "Hora": "18:04:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-19-2024",
  "Hora": "08:27:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-19-2024",
  "Hora": "18:04:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-20-2024",
  "Hora": "08:31:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-20-2024",
  "Hora": "18:01:56",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-21-2024",
  "Hora": "08:21:48",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-21-2024",
  "Hora": "18:02:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-22-2024",
  "Hora": "08:47:56",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-22-2024",
  "Hora": "18:02:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-25-2024",
  "Hora": "08:33:17",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "03-25-2024",
  "Hora": "20:03:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-01-2024",
  "Hora": "08:26:53",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-01-2024",
  "Hora": "18:02:36",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-02-2024",
  "Hora": "08:19:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-02-2024",
  "Hora": "18:00:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-03-2024",
  "Hora": "08:24:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-03-2024",
  "Hora": "18:02:24",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-04-2024",
  "Hora": "08:31:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-04-2024",
  "Hora": "17:59:52",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-05-2024",
  "Hora": "08:30:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-05-2024",
  "Hora": "18:00:58",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-08-2024",
  "Hora": "08:25:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-08-2024",
  "Hora": "18:01:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-09-2024",
  "Hora": "08:20:36",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-09-2024",
  "Hora": "18:01:26",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-10-2024",
  "Hora": "08:24:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-10-2024",
  "Hora": "18:00:33",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-11-2024",
  "Hora": "08:33:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-11-2024",
  "Hora": "18:00:19",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-12-2024",
  "Hora": "08:21:20",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-12-2024",
  "Hora": "18:03:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-15-2024",
  "Hora": "08:35:45",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 176703296,
  "Date": "04-15-2024",
  "Hora": "18:01:30",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-18-2024",
  "Hora": "15:21:15",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-19-2024",
  "Hora": "01:27:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-19-2024",
  "Hora": "15:16:58",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-20-2024",
  "Hora": "01:04:29",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-20-2024",
  "Hora": "15:29:42",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-21-2024",
  "Hora": "01:15:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-21-2024",
  "Hora": "15:38:38",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-22-2024",
  "Hora": "01:14:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-22-2024",
  "Hora": "15:15:33",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-23-2024",
  "Hora": "00:18:20",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-25-2024",
  "Hora": "15:04:32",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-26-2024",
  "Hora": "01:25:46",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-26-2024",
  "Hora": "15:21:21",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-27-2024",
  "Hora": "01:12:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-27-2024",
  "Hora": "15:41:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-28-2024",
  "Hora": "01:04:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-28-2024",
  "Hora": "15:31:29",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "03-28-2024",
  "Hora": "23:46:35",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-01-2024",
  "Hora": "15:06:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-02-2024",
  "Hora": "01:41:16",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-02-2024",
  "Hora": "15:16:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-03-2024",
  "Hora": "02:34:39",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-03-2024",
  "Hora": "15:24:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-04-2024",
  "Hora": "01:15:57",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-04-2024",
  "Hora": "15:29:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-05-2024",
  "Hora": "01:19:07",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-05-2024",
  "Hora": "15:13:46",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-06-2024",
  "Hora": "00:09:25",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-08-2024",
  "Hora": "15:07:50",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-09-2024",
  "Hora": "01:15:15",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-09-2024",
  "Hora": "15:26:27",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-10-2024",
  "Hora": "01:12:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-10-2024",
  "Hora": "15:13:04",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-11-2024",
  "Hora": "01:09:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-11-2024",
  "Hora": "15:14:54",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-12-2024",
  "Hora": "01:00:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-12-2024",
  "Hora": "15:16:25",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-13-2024",
  "Hora": "00:20:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-13-2024",
  "Hora": "13:00:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-13-2024",
  "Hora": "22:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-15-2024",
  "Hora": "10:53:00",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 196493719,
  "Date": "04-15-2024",
  "Hora": "14:58:06",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-16-2024",
  "Hora": "05:50:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-16-2024",
  "Hora": "11:22:43",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-18-2024",
  "Hora": "05:52:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-18-2024",
  "Hora": "13:14:17",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-19-2024",
  "Hora": "05:53:13",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-19-2024",
  "Hora": "12:44:47",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-20-2024",
  "Hora": "05:57:22",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-20-2024",
  "Hora": "14:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-20-2024",
  "Hora": "14:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-21-2024",
  "Hora": "05:56:28",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-21-2024",
  "Hora": "14:00:08",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-22-2024",
  "Hora": "05:53:34",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-22-2024",
  "Hora": "14:00:22",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-23-2024",
  "Hora": "06:00:16",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-23-2024",
  "Hora": "12:02:04",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-25-2024",
  "Hora": "05:53:05",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-25-2024",
  "Hora": "14:00:01",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-26-2024",
  "Hora": "05:52:44",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-26-2024",
  "Hora": "14:00:11",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-27-2024",
  "Hora": "05:55:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-27-2024",
  "Hora": "05:55:07",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-27-2024",
  "Hora": "14:00:40",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-28-2024",
  "Hora": "05:53:30",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "03-28-2024",
  "Hora": "14:00:03",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "04-01-2024",
  "Hora": "05:57:19",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "04-01-2024",
  "Hora": "14:00:00",
  "Type": "Salida"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "04-02-2024",
  "Hora": "05:56:23",
  "Type": "Ingreso"
 },
 {
  "UserIdentifier": 211219564,
  "Date": "04-02-2024",
  "Hora": "14:00:47",
 },
 {
 },