import json

def lambda_handler(event, context):
    # Registrar el evento recibido para depuración
    print("Evento recibido:", json.dumps(event))

    # Verificar si el body está presente en el evento
    if "body" in event:
        body = event["body"]
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'mensaje': 'No se recibió el body en la solicitud.'})
        }

    # Si el body es una cadena, intentar cargarlo como JSON
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'mensaje': 'El body no es un JSON válido.'})
        }

    # Extraer los valores de saldo_actual y cantidad
    try:
        saldo_actual = float(data['saldo_actual'])
        cantidad = float(data['cantidad'])
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'mensaje': 'Faltan campos en el body: saldo_actual o cantidad.'})
        }
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps({'mensaje': 'Los valores de saldo_actual y cantidad deben ser numéricos.'})
        }

    # Calcular el nuevo saldo
    nuevo_saldo = saldo_actual + cantidad

    # Construir la respuesta
    respuesta = {
        'mensaje': 'Saldo agregado exitosamente.',
        'nuevo_saldo': nuevo_saldo
    }

    # Retornar la respuesta con statusCode 200.
    return {
        'statusCode': 200,
        'body': json.dumps(respuesta),
        'headers': {
            'Content-Type': 'application/json'
        }
    }

