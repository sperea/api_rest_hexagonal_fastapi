

def test_create_user_dto():
    now = unixtimestamp()
    user_dto = UserDTO(
        id="123",
        username="johndoe",
        password="password",
        email="johndoe@example.com",
        created_at=now,
        updated_at=now
    )
    assert user_dto.id == "123"
    assert user_dto.username == "johndoe"
    assert user_dto.password == "password"
    assert user_dto.email == "johndoe@example.com"
    assert user_dto.created_at == now
    assert user_dto.updated_at == now
    
    
def test_user_dto_to_entity():
    now = unixtimestamp()
    user_dto = UserDTO(
        id="123",
        username="johndoe",
        password="password",
        email="johndoe@example.com",
        created_at=now,
        updated_at=now
    )
    user = user_dto.to_entity()
    assert isinstance(user, User)
    assert user.id == "123"
    assert user.username == "johndoe"
    assert user.password == "password"
    assert user.email == "johndoe@example.com"
    assert user.created_at == now
    assert user.updated_at == now
    
def test_user_dto_to_read_model():
    now = unixtimestamp()
    user_dto = UserDTO(
        id="123",
        username="johndoe",
        password="password",
        email="johndoe@example.com",
        created_at=now,
        updated_at=now
    )
    read_model = user_dto.to_read_model()
    assert isinstance(read_model, UserReadModel)
    assert read_model.id == "123"
    assert read_model.username == "johndoe"
    assert read_model.password == "password"
    assert read_model.email == "johndoe@example.com"
    assert read_model.created_at == now
    assert read_model.updated_at == now
    
    
def test_user_dto_from_entity():
    now = unixtimestamp()
    user = User(
        id="123",
        username="johndoe",
        password="password",
        email="johndoe@example.com",
        created_at=now,
        updated_at=now
    )
    user_dto = UserDTO.from_entity(user)
    assert isinstance(user_dto, UserDTO)
    assert user_dto.id == "123"
    assert user_dto.username == "johndoe"
    assert user_dto.password == "password"
    assert user_dto.email == "johndoe@example.com"
    assert user_dto.created_at == now
    assert user_dto.updated_at == now