from application.adapters.in_memory import InMemoryUserRepository
from fastapi import FastAPI
from fastapiframework import controllers
import logging
from logging import config

from application.domain.user import (
    UserNotFoundError,
    UserRepository,
    UsersNotFoundError,
)
from application.infrastructure.sqlite.user import (
    UserCommandUseCaseUnitOfWorkImpl,
    UserQueryServiceImpl,
    UserRepositoryImpl,
)
from application.infrastructure.sqlite.database import SessionLocal, create_tables
from application.presentation.schema.user.user_error_message import (
    ErrorMessageUserIsbnAlreadyExists,
    ErrorMessageUserNotFound,
    ErrorMessageUsersNotFound,
)
from application.usecase.user import (
    UserCommandUseCase,
    UserCommandUseCaseImpl,
    UserCommandUseCaseUnitOfWork,
    UserCreateModel,
    UserQueryService,
    UserQueryUseCase,
    UserQueryUseCaseImpl,
    UserReadModel,
    UserUpdateModel,
)

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get(
    "/users",
    response_model=List[UserReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageUsersNotFound,
        },
    },
)
async def get_users(
    user_query_usecase: UserQueryUseCase = Depends(user_query_usecase),
):
    try:
        users = user_query_usecase.fetch_users()

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if len(users) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=UsersNotFoundError.message,
        )

    return users


@app.get(
    "/users/{user_id}",
    response_model=UserReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": ErrorMessageUserNotFound,
        },
    },
)
async def get_user(
    user_id: str,
    user_query_usecase: UserQueryUseCase = Depends(user_query_usecase),
):
    try:
        user = user_query_usecase.fetch_user_by_id(user_id)
    except UserNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return user