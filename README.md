1. Write a Python API using the Fast API framework which:
Ans:
  - cd ~/hemanth/hemanth-assessment/
  - chmod +x app.py
  - python3 app.py

# if error debug with this command
uvicorn app:app --host=0.0.0.0 --port=8000 --log-level=debug  ## if error debugging


2. Write a Python CLI client to interact with the API for both:
Ans: 
 - cd ~/hemanth/hemanth-assessment/
 - chmod +x cli.py
 - python3 cli.py upload -f record.yaml
  
* run radis in container to test result temp
 - docker run -p 6379:6379 redis

* varify result

  - python3 cli.py get Hemanth
 

3. Containerise the Python API in a Dockerfile (with the intention of deploying the image on Kubernetes): 

* create a docker file and build image using app.py, cli.py and requirement.txt files with best practice
  
  - cd ~/hemanth/hemanth-assessment/
  - docker build -t lloydsbanking .


4. Create a Helm chart to deploy the API image
5. Prove you can add, update and retrieve person records with your Python client against the deployed API:

Ans: first run k8s cluster then create a chart update config files Chart.yaml values.yaml,  deployment.yaml, ingress.yaml etc and deply helm


- minikube start -p lloydsbanking --extra-config=apiserver.service-node-port-range=1-65535

- cd ~/hemanth-assessment/helm-k8s/hemanth/
- helm package .

- helm install my-hemanth ./hemanth-0.1.0.tgz 
- helm upgrade my-hemanth ./hemanth-0.1.0.tgz -f values.yaml

