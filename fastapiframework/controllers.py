
from application.adapters.in_memory import InMemoryUserRepository
from application.domain.user import User

from fastapi import FastAPI

app = FastAPI()

vote_repository = InMemoryUserRepository()


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


router = app.router
