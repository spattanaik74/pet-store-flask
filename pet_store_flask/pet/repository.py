from pet_store_flask.pet.models import Pet as PetModel


class PetRepository:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        It returns a list of dictionaries, where each dictionary is a pet
        :return: A list of dictionaries.
        """
        return [pets.dict() for pets in self.session.query(PetModel).all()]

    def get_all_by_id(self, id):
        # noqa: E501
        return [pets.dict() for pets in self.session.query(PetModel).filter_by(id=id).all()]

    def get_all_by_status(self, status):
        """
        It returns a list of dictionaries of all the pets in the database that have a status of the status parameter

        :param status: The status of the pet
        :return: A list of dictionaries.
        """
        return [pets.dict() for pets in self.session.query(PetModel).filter_by(status=status).all()]

    def add(self, name, id, catagory, status):
        """
        This function adds a new pet to the database

        :param name: The name of the pet
        :param id: The id of the pet to be added
        :param catagory: dog, cat, bird, fish, other
        :param status: available, pending, or sold
        :return: The string "Added"
        """
        model = PetModel(petname=name, id=id, catagory=catagory, status=status)
        self.session.add(model)
        self.session.commit()
        return "Added"

    def update_by_id(self, name, id, catagory, status):
        """
        It takes in the name, id, catagory, and status of a pet and updates the record in the database

        :param name: the name of the pet
        :param id: The id of the pet you want to update
        :param catagory: dog, cat, bird, fish, etc
        :param status: available, pending, sold
        :return: The record is being updated.
        """
        model = self.session.query(PetModel).filter_by(id=id).first()
        print(model)
        model.petname = name
        model.id = id
        model.catagory = catagory
        model.status = status
        self.session.commit()
        return "record updated"

    def delete_by(self, id):
        """
        It deletes a record from the database by id

        :param id: The id of the pet you want to delete
        :return: The record is being deleted.
        """
        self.session.query(PetModel).filter_by(id=id).delete()
        self.session.commit()
        return "record Deleted"
