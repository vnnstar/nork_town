from src.domain.client.model import ClientModel
from src.domain.cars.model import CarModel
from src.infrastructures.sqlite.infrastructure import SqliteInfrastructure


class SqliteRepository:

    infra = SqliteInfrastructure

    @classmethod
    def insert_client(cls, client: ClientModel):
        session = cls.infra.get_session()
        session.add(client)
        session.commit()
        session.close()

    @classmethod
    def insert_car(cls, car: CarModel):
        session = cls.infra.get_session()
        session.add(car)
        session.commit()
        session.close()

    @classmethod
    def update_sale_opportunity_status(cls, client_id: int):
        session = cls.infra.get_session()
        client = session.query(ClientModel).get(client_id)
        client.sale_opportunity = False
        session.commit()
        session.close()

    @classmethod
    def get_all_cars_by_id(cls, client_id: int):
        session = cls.infra.get_session()
        cars = session.query(CarModel).filter(CarModel.client_id == client_id)
        return cars

    @classmethod
    def get_client_by_id(cls, client_id: int):
        session = cls.infra.get_session()
        client = session.query(ClientModel).get(client_id)
        return client

    @classmethod
    def get_all_clients(cls):
        session = cls.infra.get_session()
        clients = session.query(ClientModel).all()
        return clients

    @classmethod
    def get_all_cars(cls):
        session = cls.infra.get_session()
        clients = session.query(CarModel).all()
        return clients






