- singleton pattern
- repository pattern
- model view controller pattern


CrudRepository <T>
- add(T)
- delete(T)
- edit(T)
- update(T)

class MongoRepository(CrudRepository):
    def add():
    delete() {}
    edit() {}
    update() {}

repository = new SQLRepository()
reposiory.add();
reposiory.delete();




view/controller layer -> business logic/service layer -> db/repository/data layer



