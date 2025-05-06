import os
from dotenv import load_dotenv #todas as variaveis que estiverem no meu arquivo .env ele vai ler pra mim.
import boto3 #bliboteca pra conseguir falar com a api da aws




load_dotenv()

AWS_ACCESS_KEY_ID: str = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY: str = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION: str = os.getenv('AWS_REGION')
BUCKET_NAME: str = os.getenv('BUCKET_NAME')