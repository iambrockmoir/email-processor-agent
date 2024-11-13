import os
from dataclasses import dataclass
from typing import Dict

@dataclass
class Config:
    GMAIL_USER: str
    CLAUDE_API_KEY: str
    POLL_INTERVAL: int = 60
    SUPPORTED_MIME_TYPES: Dict[str, str] = {
        'text/plain': '.txt',
        'application/pdf': '.pdf',
        'application/msword': '.doc',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document': '.docx'
    }

def load_config() -> Config:
    return Config(
        GMAIL_USER=os.environ['GMAIL_USER'],
        CLAUDE_API_KEY=os.environ['CLAUDE_API_KEY']
    )
