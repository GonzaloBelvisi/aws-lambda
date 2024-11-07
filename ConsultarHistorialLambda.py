import json
import boto3
from decimal import Decimal

# Función para convertir Decimal a float
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def lambda_handler(event, context):
    # Conectar a DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Transacciones')
    
    # Obtener todas las transacciones
    try:
        response = table.scan()
        historial_transacciones = response['Items']
    except Exception as e:
        print("Error al obtener historial:", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'mensaje': 'Error al obtener el historial de transacciones.'})
        }
    
    # Retornar el historial de transacciones, sin usar json.dumps en el cuerpo
    return {
        'statusCode': 200,
        'body': {'historial_transacciones': historial_transacciones},
        'headers': {
            'Content-Type': 'application/json'
        }
    }
