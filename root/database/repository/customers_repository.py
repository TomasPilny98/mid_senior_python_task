from injector import inject, singleton
from root.database.manager.thread_session_request_manager import ThreadSessionRequestManager
from root.json_convertor import JsonConvertor


class CustomersRepository:

    @inject
    def __init__(self, db_session: ThreadSessionRequestManager, json_convertor: JsonConvertor):
        self._db_session: ThreadSessionRequestManager = db_session
        self._json_convertor: JsonConvertor = json_convertor

    