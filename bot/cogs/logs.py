import json

import os
import sys
import time

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine



Base = declarative_base()

class AttributionLogs(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)

    ninja_id = Column(String(100), nullable=False)
    mentor_id = Column(String(100), nullable=False)
    belt_attributed = Column(String(100), nullable=False)
    timestamp = Column(Integer, nullable=False)


engine = create_engine('sqlite:///daily_logs.db')
Base.metadata.create_all(engine)



def log_attribution(ninja, mentor, belt) -> None:
    ''' This function logs the belt attribution of a Ninja.'''

    timestamp = int(time.time())
    entry_logs = {
            "ninja_id": f"{ninja}",
            "mentor_id": f"{mentor}",
            "belt_attributed" : f"{belt}",
            "timestamp": f"{timestamp}"
        }

    data_logs.append(entry_logs)
    with open(filename, 'w') as json_file:
        json.dump(data_logs, json_file,
                indent=4,
                separators=(',', ': '))


if __name__ == '__main__':
    Base.metadata.create_all(engine)

