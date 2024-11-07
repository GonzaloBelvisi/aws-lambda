import json
from decimal import Decimal
import boto3
import uuid  # Importar la biblioteca uuid para generar IDs únicos

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

    # Extraer los valores de usuario_origen, usuario_destino, saldo_actual y monto_transferencia
    try:
        usuario_origen = data['usuario_origen']
        usuario_destino = data['usuario_destino']
        saldo_actual = Decimal(data['saldo_actual'])
        monto_transferencia = Decimal(data['monto_transferencia'])
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'mensaje': 'Faltan campos en el body: usuario_origen, usuario_destino, saldo_actual o monto_transferencia.'})
        }
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps({'mensaje': 'Los valores de saldo_actual y monto_transferencia deben ser numéricos.'})
        }

    # Verificar si el usuario tiene saldo suficiente
    if saldo_actual < monto_transferencia:
        return {
            'statusCode': 400,
            'body': json.dumps({'mensaje': 'Saldo insuficiente para realizar la transferencia.'})
        }

    # Calcular el nuevo saldo del usuario origen
    nuevo_saldo_origen = saldo_actual - monto_transferencia

    # Guardar la transacción en DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Transacciones')

    try:
        response = table.put_item(
            Item={
                'transaccion_id': str(uuid.uuid4()),  # Generar un ID único para la transacción
                'usuario_origen': usuario_origen,
                'usuario_destino': usuario_destino,
                'saldo_actual': saldo_actual,
                'monto_transferencia': monto_transferencia,
                'nuevo_saldo_origen': nuevo_saldo_origen
            }
        )
    except Exception as e:
        print("Error al guardar en DynamoDB:", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'mensaje': 'Error al guardar la transacción en la base de datos.'})
        }

    # Construir la respuesta
    respuesta = {
        'mensaje': 'Transferencia realizada con éxito.',
        'nuevo_saldo_origen': float(nuevo_saldo_origen),
        'monto_transferido': float(monto_transferencia),
        'usuario_destino': usuario_destino
    }

    # Retornar la respuesta con statusCode 200
    return {
        'statusCode': 200,
        'body': json.dumps(respuesta),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
