import requests, json, time, random

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
Configuración
    token_from = login("Clave API", "Secreto") - Empresa de origen de las marcas
    token_to = login("Clave API", "Secreto") - Empresa destino de las marcas
"""
token_from = login("", "")
token_to = login("", "")

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

# /User/List
def user_list(token):
    url = "https://customerapi.geovictoria.com/api/v1/User/List"
    payload = {}
    headers = {
        'Authorization': f'Bearer {token["token"]}'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    users = json.loads(str(response.text))
    return users

# /Punch/ListByUsersDates
def punch_listbyusersdates(token, users_ids, start_date, end_date):
    url = "https://customerapi.geovictoria.com/api/v1/Punch/ListByUsersDates"

    payload = json.dumps({
        "UserIds": users_ids,
        "StartDate": start_date,
        "EndDate": end_date
    })
    headers = {
        'Authorization': f'{token["token"]}',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    punches = json.loads(str(response.text)) if type(json.loads(str(response.text))) is list else []

    return(punches)


# /Punch/AddMultiple
def punch_addmultiple(token, punches):
    url = "https://customerapi.geovictoria.com/api/v1/Punch/AddMultiple"
    headers = {
        'Authorization': token["token"],
        'Content-Type': 'application/json'
    }

    failed_batches = []

    batch_size = 50 if len(punches) >= 50 else len(punches)

    if len(punches) > 0:
        for i in range(0, len(punches), batch_size):
            print(punches)
            batch = punches[i:i+batch_size]
            formatted_batch = [
                {
                    "ReferenceIdentifier": random.getrandbits(64),
                    "BoxSerialNumber": punch["BoxSn"],
                    "Date": punch["Date"],
                    "UserIdentifier": punch["UserIdentifier"],
                    "Type": punch["Type"]
                }
                for punch in batch
            ]
            payload = json.dumps(formatted_batch)
            
            attempts = 0
            success = False
            
            while attempts < 3 and not success:
                try:
                    response = requests.request("POST", url, headers=headers, data=payload)
                    response.raise_for_status()
                    print(f"Lote de marcas {i//batch_size + 1} agregado de manera correcta: {response.text}")
                    success = True
                except requests.exceptions.RequestException as e:
                    attempts += 1
                    print(f"Error cargando el lote de marcas {i//batch_size + 1}, intento {attempts} de 3: {e}")
                    time.sleep(1)
            
            if not success:
                failed_batches.append(i//batch_size + 1)
    
    if failed_batches:
        print(f"Lotes de marcas con fallo en el envío: {failed_batches}")

    return(failed_batches)

users = user_list(token_from)
"""
Configuración
    start_date = "yyyymmddhhmmss"
    end_date = "yyyymmddhhmmss"
"""
start_date = ""
end_date = ""

for user in users:
    punches = punch_listbyusersdates(token_from, user["Identifier"], start_date, end_date)
    # print("*****", user["Identifier"], "*****")
    punch_addmultiple(token_to, punches)
