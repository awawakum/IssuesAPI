from typing import List, Optional
import logging
from sqlalchemy.orm import Session
from models.issue import IssueModel
from schemas.issue import Issue, IssueCreate, IssueUpdate

logger = logging.getLogger(__name__)


class IssueRepository:
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_issues(self) -> List[Issue]:
        """Get all issues"""
        logger.debug("Querying all issues from database")
        issues = self.db.query(IssueModel).all()
        return [
            Issue(
                id=issue.id,
                text=issue.text,
                status=issue.status,
                source=issue.source,
                created_at=issue.created_at,
                updated_at=issue.updated_at,
            )
            for issue in issues
        ]
    
    def create_issue(self, issue: IssueCreate) -> Issue:
        """Create a new issue"""
        logger.info("Creating new issue: %s", issue)
        db_issue = IssueModel(
            text=issue.text,
            status=issue.status,
            source=issue.source,
        )
        self.db.add(db_issue)
        self.db.commit()
        self.db.refresh(db_issue)
        logger.debug("Created issue with id=%s", db_issue.id)
        return Issue(
            id=db_issue.id,
            text=db_issue.text,
            status=db_issue.status,
            source=db_issue.source,
            created_at=db_issue.created_at,
            updated_at=db_issue.updated_at,
        )

    def get_issues_by_status(self, status: str) -> List[Issue]:
        """Get issues by status"""
        issues = self.db.query(IssueModel).filter(IssueModel.status == status).all()
        return [
            Issue(
                id=issue.id,
                text=issue.text,
                status=issue.status,
                source=issue.source,
                created_at=issue.created_at,
                updated_at=issue.updated_at,
            )
            for issue in issues
        ]
    
    def delete_issue(self, issue_id: int) -> None:
        """Delete an issue by ID"""
        logger.info("Deleting issue id=%s", issue_id)
        issue = self.db.query(IssueModel).filter(IssueModel.id == issue_id).first()
        if issue:
            self.db.delete(issue)
            self.db.commit()
            logger.debug("Deleted issue id=%s", issue_id)
    
    def get_issue_by_id(self, issue_id: int) -> Optional[Issue]:
        logger.debug("Looking up issue by id=%s", issue_id)
        issue = self.db.query(IssueModel).filter(IssueModel.id == issue_id).first()
        if not issue:
            logger.debug("Issue id=%s not found", issue_id)
            return None
        return Issue(
            id=issue.id,
            text=issue.text,
            status=issue.status,
            source=issue.source,
            created_at=issue.created_at,
            updated_at=issue.updated_at,
        )
    def update_issue(self, issue_id: int, updated_issue: IssueUpdate) -> Optional[Issue]:
        """Update an existing issue"""
        logger.info("Updating issue id=%s with %s", issue_id, updated_issue)
        issue = self.db.query(IssueModel).filter(IssueModel.id == issue_id).first()
        if not issue:
            logger.debug("Issue id=%s not found for update", issue_id)
            return None

        if updated_issue.text is not None:
            issue.text = updated_issue.text
        if updated_issue.status is not None:
            issue.status = updated_issue.status
        if updated_issue.source is not None:
            issue.source = updated_issue.source

        self.db.commit()
        self.db.refresh(issue)
        logger.debug("Updated issue id=%s", issue_id)
        return Issue(
            id=issue.id,
            text=issue.text,
            status=issue.status,
            source=issue.source,
            created_at=issue.created_at,
            updated_at=issue.updated_at,
        )