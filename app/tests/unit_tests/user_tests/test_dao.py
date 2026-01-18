import pytest

from  app.Users.dao import UsersDao



@pytest.mark.parametrize("user_id,email, is_exist", [
    (99,"alonya@test.com",False),
    (10,"gamer777@example.com",True),
    (6,"lolik@mail.ru", False)

])
async  def test_find_by_id(user_id,email, is_exist):
    user = await UsersDao.find_by_id(user_id)


    if is_exist:
        assert  user.id == user_id
        assert  user.email == email
    else:
        assert not user
