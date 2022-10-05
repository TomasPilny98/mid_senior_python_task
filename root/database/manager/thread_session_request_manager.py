from injector import singleton, inject
from sqlalchemy.orm import Session

from root.database.manager.repository_manager import RepositoryManager
from root.main.dependency_injection_init import injector


@singleton
class ThreadSessionRequestManager:

    @inject
    def __init__(self, repository_manager: RepositoryManager) -> None:
        self.session: Session = repository_manager.session_scope

    def __del__(self) -> None:
        if self.session:
            self.remove_session()

    def remove_session(self) -> None:
        if self.session:
            try:
                self.safe_commit()
            except Exception as e:
                print('Error occurred during remove_session in db', e)
            finally:
                injector.get(RepositoryManager).remove()
                del self.session
                self.session = None

    def safe_commit(self) -> None:
        if self.session:
            try:
                self.session.commit()
            except Exception as e:
                print('Error occurred during safe_commit in db', e)
                self.session.rollback()
                raise
