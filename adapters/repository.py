from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession
from config import settings
from asyncio import current_task


class Repository:
    def __init__(self, db_url: str, db_echo: bool = False):
        self.engine = create_async_engine(
            url=db_url,
            echo=db_echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(session_factory=self.session_factory,
                                       scopefunc=current_task)
        return session

    async def session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.remove()


repository_instance = Repository(settings.db_url, settings.db_echo)
