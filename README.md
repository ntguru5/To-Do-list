# Testing markdown formatting

# CarCar
CarCar is an car dealership application to manage your service and sales needs.

Team:
- Ken Yeh - Service Microservice
- Toran O'Brien - Sales Microservice

## Getting started
1. Fork this repository
2. Clone the forked repository to your local computer using: `git clone https://gitlab.com/toranaobrien/project-beta`
3. From the project directory run the following Docker commands:

    docker volume create beta-data
    docker compose build
    docker compose up

## Design
Inventory endpoints
Action                         | Method | URL
-------------------------------|--------|-------------------------------------------
List manufacturers             | GET    | http://localhost:8100/api/manufacturers/
Create a manufacturer          | POST   | http://localhost:8100/api/manufacturers/
Get a specific manufacturer    | GET    | http://localhost:8100/api/manufacturers/:id/
Update a specific manufacturer | PUT    | http://localhost:8100/api/manufacturers/:id/
Delete a specific manufacturer | DELETE | http://localhost:8100/api/manufacturers/:id/


Automobile endpoints
Action                       | Method | URL
--------------------------   |--------|-------------------------------------------
List automobiles             | GET    | http://localhost:8100/api/automobiles/
Create an automobile         | POST   | http://localhost:8100/api/automobiles/
Get a specific automobile    | GET    | http://localhost:8100/api/automobiles/:vin/
Update a specific automobile | PUT    | http://localhost:8100/api/automobiles/:vin/
Delete a specific automobile | DELETE | http://localhost:8100/api/automobiles/:vin/


Service endpoints
Action                                    | Method | URL
------------------------------------------|--------|-------------------------------------------
List technicians                          | GET    | http://localhost:8080/api/technicians/
Create a technician                       | POST   | http://localhost:8080/api/technicians/
Delete a specific technician              | DELETE | http://localhost:8080/api/technicians/:id/
List appointments                         | GET    | http://localhost:8080/api/appointments/
Create an appointment                     | POST   | http://localhost:8080/api/appointments/
Delete an appointment                     | DELETE | http://localhost:8080/api/appointments/:id/
Set appointment status to "canceled"      | PUT    | http://localhost:8080/api/appointments/:id/cancel/
Set appointment status to "finished"      | PUT    | http://localhost:8080/api/appointments/:id/finish/


Sales endpoints
Action                                | Method | URL
--------------------------------------|--------|----------------------------------------
List salespeople                      | GET    | http://localhost:8090/api/salespeople/
Create a salesperson                  | POST   | http://localhost:8090/api/salespeople/
Delete a specific salesperson         | DELETE | http://localhost:8090/api/salespeople/:id/
List customers                        | GET    | http://localhost:8090/api/customers/
Create a customer                     | POST   | http://localhost:8090/api/customers/
Delete a specific customer            | DELETE | http://localhost:8090/api/customers/:id/
List sales                            | GET    | http://localhost:8090/api/sales/
Create a sale                         | POST   | http://localhost:8090/api/sales/
Delete a sale                         | DELETE | http://localhost:8090/api/sales/:id/



## Service microservice

The service microservice consists of three models: An Appointment model, a Technician model, and an AutomobileVO value object model containing vin and sold fields. Technician is a foreign key to the Appointment model.

## Sales microservice

Explain your models and integration with the inventory
microservice, here.

### Diagram

![alt text goes here](CarCar.png "caption goes here when you hover over image")

