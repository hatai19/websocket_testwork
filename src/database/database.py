from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import postgres_url

async_engine = create_async_engine(postgres_url)
async_session = async_sessionmaker(async_engine)