from fastapi import FastAPI, File, UploadFile
from redis import Redis
from pydantic import BaseModel
import yaml
import uvicorn
import logging

logger = logging.getLogger(__name__)

async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        data = yaml.safe_load(contents)
    except yaml.YAMLError as e:
        logger.error(f"Failed to parse YAML data: {e}")
        return {"status": "failure", "message": "Invalid file format. Please upload a YAML file."}
    person = Person(**data)
    logger.info(f"Received new person record: {person}")
    redis.set(person.first_name, person.json())
    return {"status": "success"}

app = FastAPI()

redis = Redis(host='localhost', port=6379, db=0)
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

@app.post('/upload/')
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    data = yaml.safe_load(contents)
    person = Person(**data)
    logger.info(f"Received new person record: {person}")
    redis.set(person.first_name, person.json())
    return {'status': 'success'}

@app.get('/person/{first_name}')
async def get_person(first_name: str):
    data = redis.get(first_name)
    if not data:
        return {'status': 'failure', 'message': 'Person not found'}
    person = Person.parse_raw(data)
    return person.dict()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

