from typing import List, Optional
import logging

from repositories.issue import IssueRepository
from schemas.issue import Issue, IssueCreate, IssueUpdate


logger = logging.getLogger(__name__)


class IssueService:
    def __init__(self, repository: IssueRepository) -> None:
        self.repository = repository

    def get_all_issues(self) -> List[Issue]:
        logger.debug("Service: get_all_issues called")
        return self.repository.get_all_issues()

    def create_issue(self, issue: IssueCreate) -> Issue:
        logger.info("Service: create_issue called")
        return self.repository.create_issue(issue)

    def get_issues_by_status(self, status: str) -> List[Issue]:
        logger.debug("Service: get_issues_by_status=%s", status)
        return self.repository.get_issues_by_status(status)

    def get_issue_by_id(self, issue_id: int) -> Optional[Issue]:
        logger.debug("Service: get_issue_by_id=%s", issue_id)
        return self.repository.get_issue_by_id(issue_id)

    def delete_issue(self, issue_id: int) -> None:
        logger.info("Service: delete_issue id=%s", issue_id)
        self.repository.delete_issue(issue_id)

    def update_issue(self, issue_id: int, updated_issue: IssueUpdate) -> Optional[Issue]:
        logger.info("Service: update_issue id=%s", issue_id)
        return self.repository.update_issue(issue_id, updated_issue)