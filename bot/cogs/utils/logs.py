import json
import os
import sys
import time

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class AttributionLogs(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)

    ninja_id = Column(String(100), nullable=False)
    mentor_id = Column(String(100), nullable=False)
    belt_attributed = Column(String(100), nullable=False)
    timestamp = Column(Integer, nullable=False)


engine = create_engine("sqlite:///bot/data/daily_logs.db")
Base.metadata.create_all(engine)


def log_attribution(ninja, mentor, belt) -> None:
    """This function logs the belt attribution of a Ninja."""

    timestamp = int(time.time())
    entry_logs = {
        "ninja_id": f"{ninja}",
        "mentor_id": f"{mentor}",
        "belt_attributed": f"{belt}",
        "timestamp": f"{timestamp}",
    }


if __name__ == "__main__":
    Base.metadata.create_all(engine)
