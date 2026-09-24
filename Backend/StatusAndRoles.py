from enum import Enum
class Status(Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    AVALIABLE = "Available"
    UNAVAILABLE = "Unavailable"

class Roles(Enum):
    MANAGER = "Manager"
    WORKER = "Worker"
    TICKET_ASSISTANT = "Ticket Assistant"