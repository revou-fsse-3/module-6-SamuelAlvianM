from app.repositories.feeding_repo import Feeding_repo

class Feeding_service:

    def __init__(self):
        self.feeding_repo = Feeding_repo()

    def get_feeding(self):
        feeds = self.feeding_repo.get_list_feeding()
        print(feeds)
        return [feed.as_dict() for feed in feeds]

    def search_feeding(self, name):
        feeds = self.feeding_repo.search_feeding(name)
        return [feed.as_dict() for feed in feeds]

    def update_feeding(self, id, feed_data_dto):
        updated_feed = self.feeding_repo.update_feeding(id, feed_data_dto)
        if updated_feed:
            return updated_feed.as_dict(), 200
        else:
            return {"message": "Feeding schedule not found"}, 404

    def delete_feeding(self, id):
        is_deleted = self.feeding_repo.delete_feeding(id)
        if is_deleted:
            return {"message": "Feeding schedule deleted successfully"}, 200
        else:
            return {"message": "Feeding schedule not found"}, 404
