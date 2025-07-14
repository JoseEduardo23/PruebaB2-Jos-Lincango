# PruebaB2-Jos-Lincango-Michelle-Suarez
•	Levantar la aplicación web proporcionada con Docker Compose. 
	Crear dos contenedores que ejecuten la aplicación. 
	Conectarlos correctamente a su base de datos respectiva.
 
•	Implementar el balanceador de carga NGINX. 
	El contenedor de NGINX debe estar configurado para distribuir peticiones entre app1 y app2. 

•	Configurar dos nodos de base de datos (MySQL). 
	Configurar dos contenedores con MySQL 
	Realizar replicación. 

Descripcion general del sistema

<img width="889" height="281" alt="image" src="https://github.com/user-attachments/assets/e7e2edc5-d97f-46c2-9575-43e9bd537466" />

Listar la red creada y verificar que el contenedor esté conectado a la red.

<img width="842" height="612" alt="image" src="https://github.com/user-attachments/assets/3647863b-4f53-48ed-b3b8-7e0e79d85b87" />

 <img width="800" height="436" alt="image" src="https://github.com/user-attachments/assets/c43cd2a2-b34f-4460-8d6d-55f113b8f72f" />

Levantamiento y ejecución de múltiples contenedores Docker definidos en un archivo docker-compose.yml

 <img width="888" height="548" alt="image" src="https://github.com/user-attachments/assets/30d84956-734f-4ecf-bff5-5ff1769aad4f" />

Creación de la base de datos con sus campos respectivos 

 <img width="982" height="299" alt="image" src="https://github.com/user-attachments/assets/b8c783f8-b5e4-4856-8bc9-48a8285a8b28" />

Lista de los volúmenes creados 

 <img width="982" height="137" alt="image" src="https://github.com/user-attachments/assets/b33ac75a-c611-42e4-ac82-0dc34e67a5fa" />

Creación del usuario

 <img width="857" height="279" alt="image" src="https://github.com/user-attachments/assets/f1bdeabc-e844-46f5-a291-4213ce271995" />

Visualización del estado del maestro1 y del binlog

 <img width="829" height="229" alt="image" src="https://github.com/user-attachments/assets/057743c3-7860-4cba-a3fd-dc7c83869d14" />

Configuración del esclavo

 <img width="519" height="173" alt="image" src="https://github.com/user-attachments/assets/23c5c26d-8327-47e8-a2bf-bd095a3ef758" />

Verificar el estado del esclavo en funcionamiento 

 <img width="564" height="444" alt="image" src="https://github.com/user-attachments/assets/061fbe37-8147-4c99-9cf2-8a047af3cc0d" />

Envío de datos desde maestro

 <img width="982" height="245" alt="image" src="https://github.com/user-attachments/assets/ccbd6a7a-40a1-42ca-9462-7b057e6edec3" />

Confirmación de replicación desde maestro a esclavo

 <img width="972" height="294" alt="image" src="https://github.com/user-attachments/assets/488d3df9-9927-4319-b908-81a96bfc3bfa" />

Visualización de datos que fueron ingresados localmente a la base de datos

 <img width="976" height="266" alt="image" src="https://github.com/user-attachments/assets/2a80ac21-c462-4966-8c99-8ac84e4e88e2" />

Ingreso de datos desde el Frontend

 <img width="982" height="380" alt="image" src="https://github.com/user-attachments/assets/e7f7600e-a131-43d1-a0f0-0da989a7bc2b" />

Visualización de datos ingresados desde el Frontend a la base de datos

<img width="982" height="302" alt="image" src="https://github.com/user-attachments/assets/a4b75053-16bf-401b-977e-cf9ab7b442bb" />

Vista de la información en la réplica esclavo

<img width="982" height="338" alt="image" src="https://github.com/user-attachments/assets/8ca3870d-b0d4-47f5-b29f-706a3cc34637" />

 
