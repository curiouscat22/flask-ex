from api.db import get_one_country, get_top_10


def test_db():
    one_c, all_c = get_one_country(id_=12), get_top_10()

    assert one_c=={"error":"conneting to db"}
    assert all_c=={"error":"conneting to db"}
