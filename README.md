# Proyecto Billetera Virtual en AWS

Este repositorio contiene el código para un sistema de billetera virtual construido en AWS. La aplicación utiliza servicios como AWS Lambda, DynamoDB, y API Gateway para ofrecer funciones de transferencia de saldo, consulta de historial de transacciones y más.

## Estructura del Proyecto

- **sumar_saldo.py**: Lambda para sumar saldo a la cuenta del usuario.
- **RealizarTransferenciaLambda.py**: Lambda para realizar transferencias entre usuarios.
- **ConsultarHistorialLambda.py**: Lambda para consultar el historial de transacciones.
- **BilleteraLambda.py**: Lambda para la lógica general de la billetera.

Cada una de estas funciones Lambda está diseñada para interactuar con DynamoDB y manejar la lógica de negocio de la billetera virtual.

## Servicios de AWS Utilizados

- **AWS Lambda**: Para manejar la lógica de negocio sin necesidad de gestionar servidores.
- **Amazon DynamoDB**: Base de datos NoSQL para almacenar los datos de las transacciones.
- **Amazon API Gateway**: Para exponer las funciones Lambda como API HTTP.
- **Amazon VPC**: Proporciona aislamiento de red y control de seguridad adicional.

## Configuración de las Funciones Lambda

### 1. **sumar_saldo.py**
   Esta función permite añadir saldo a la cuenta de un usuario en la billetera virtual.

   - **Endpoint**: `/sumar_saldo`
   - **Método HTTP**: POST
   - **Cuerpo de la solicitud**: Puede consultarse en el repositorio para detalles específicos.
   - **Respuesta**: Devuelve el nuevo saldo del usuario después de la adición.

### 2. **RealizarTransferenciaLambda.py**
   Esta función permite realizar transferencias de saldo entre usuarios.

   - **Endpoint**: `/realizar_transferencia`
   - **Método HTTP**: POST
   - **Cuerpo de la solicitud**: Disponible en el repositorio.
   - **Respuesta**: Indica si la transferencia fue exitosa y muestra el nuevo saldo.

### 3. **ConsultarHistorialLambda.py**
   Esta función permite consultar el historial de transacciones de un usuario.

   - **Endpoint**: `/consultar_historial`
   - **Método HTTP**: GET
   - **Parámetros de consulta**: Información disponible en el repositorio.
   - **Respuesta**: Devuelve una lista de transacciones realizadas por el usuario.

### 4. **BilleteraLambda.py**
   Función general que maneja la lógica de la billetera virtual.

   - **Cuerpo de la solicitud**: Revisar detalles específicos en el repositorio.

## Instrucciones de Implementación en AWS

### 1. Crear Funciones Lambda
   - Subir cada archivo `.py` como código de la función Lambda correspondiente.
   - Configurar los permisos necesarios en IAM para que cada Lambda pueda acceder a DynamoDB.

### 2. Configurar DynamoDB
   - Crear una tabla en DynamoDB con un esquema adecuado para almacenar las transacciones.
   - Asegurarse de que los permisos de DynamoDB permitan a las funciones Lambda leer y escribir en la tabla.

### 3. Configurar Amazon API Gateway
   - Crear un API en Amazon API Gateway y exponer cada Lambda como un endpoint HTTP.
   - Configurar métodos HTTP (GET, POST) según corresponda para cada endpoint.
   - Habilitar el uso de HTTPS para asegurar el cifrado en tránsito.
