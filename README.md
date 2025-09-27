# Equipo DevOps Assessment

## How to Build and Run
1. Clone the repo
   git clone https://github.com/MithunrajKurunthil/Equipo-DevOps-Assessment.git

   cd equipo

3. Build and start containers
   docker-compose build --no-cache
   docker-compose up -d

4. Check running services

   To view the images --> docker images
   
   <img width="1920" height="1032" alt="Image" src="https://github.com/user-attachments/assets/5046fc8a-bb92-431a-9afd-301be1d92c0b" />
   
   To view the running containers --> docker ps
   
   <img width="1920" height="1032" alt="Image" src="https://github.com/user-attachments/assets/6741cb1e-d244-48d5-b77b-fc6b7c628b37" />

## How to Test   

Open your browser:
1. nginx

   http://localhost

  <img width="1920" height="1032" alt="Image" src="https://github.com/user-attachments/assets/24671192-6f03-431a-a0de-d3d2613e7a55" />

2. Python API

   http://localhost/pyapi/

   <img width="1920" height="1032" alt="Image" src="https://github.com/user-attachments/assets/b4405545-d700-4afe-9974-18620377d9c9" />

   http://localhost/pyapi/hello

   <img width="1920" height="1032" alt="Image" src="https://github.com/user-attachments/assets/c391bb95-0515-4e5a-b8d7-07def2ac80b3" />

   http://localhost/pyapi/db-check

   <img width="1920" height="1032" alt="Image" src="https://github.com/user-attachments/assets/67d437b3-1d83-47f2-903c-6d8ebb5061e9" />

3. ReactApp

   http://localhost/reactapp/

   <img width="1920" height="1032" alt="Image" src="https://github.com/user-attachments/assets/907e1247-9b78-4bd0-9a78-193aa15e5d24" />

## Environment Variables

  Python API

  <img width="365" height="136" alt="Image" src="https://github.com/user-attachments/assets/9e4d54c2-ac89-4b61-9eec-8bbe3906a206" />
