from models import Dog

def create_table(Base, engine):
    Base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)

def get_all(session):
    return [dog for dog in session.query(Dog)]

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()