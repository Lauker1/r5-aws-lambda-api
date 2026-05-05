# R5 - Despliegue en AWS (Lambda + API Gateway)

## 🧠 Arquitectura

Este proyecto implementa una arquitectura serverless en AWS basada en:

- AWS Lambda
- API Gateway (REST API)
- CloudWatch Logs

---

## 🚀 Endpoint desplegado

https://h6yss5y1y8.execute-api.eu-west-1.amazonaws.com/PROD/predict


---

## 🧪 Ejemplo de uso

```bash
curl -X GET "https://.../PROD/predict"
Respuesta:
{
  "status": "OK",
  "message": "Inferencia simulada correcta",
  "dataset": "test.csv",
  "prediction": "class_A"
}
⚙️ Función Lambda

Ver carpeta /lambda

☁️ Servicios usados
AWS Lambda
API Gateway
CloudWatch Logs
🔐 Seguridad
IAM con rol gestionado por AWS Learner Lab
Comunicación HTTPS
Acceso público para fines de demostración
