from django.db.models import Manager
from journal.models import Student


class StudentsManager(Manager):
    def get_students_by_squad(self, squad_id) -> [Student]:
        _ = self.model
        return [
            Student(
                first_name="Ivan",
                middle_name="Ivanovich",
                last_name="Pupkin",
                # squad="1702",
            )
        ]
        pass

