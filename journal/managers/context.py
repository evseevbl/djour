from journal.models import Squad, Subject
from maintenance.helpers.named_tuple import namedtuple_wrapper

tSquadSubject = namedtuple_wrapper(
    "tSquadSubject",
    [
        "id",
        "code",
        "subjects",
    ]
)


def get_squads_with_subjects():
    ans = []
    for s in Squad.objects.order_by('code'):
        q = Subject.objects.filter(curriculum__squad__code=s.code).prefetch_related(
            'curriculum_set__squad'
        )
        ans.append(tSquadSubject(
            code=s.code,
            id=s.id,
            subjects=q,
        ))
    return ans


tMarkValues = namedtuple_wrapper(
    "tMarkValues",
    [
        "id",
        "code",
        "subjects",
    ]
)



def with_context(d: dict):
    squads = get_squads_with_subjects()
    d["squad_list"] = squads
    return d
