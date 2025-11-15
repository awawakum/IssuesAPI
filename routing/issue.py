from typing import List
import logging

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.issue import Issue, IssueCreate, IssueUpdate
from services.issue import IssueService
from repositories.issue import IssueRepository

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/issue", tags=["issue"])


@router.get(
    "/issues",
    responses={400: {"description": "Bad request"}},
    response_model=List[Issue],
    description="Get all issues",
)
async def get_all_issues(
    db: Session = Depends(get_db),
) -> List[Issue]:
    repository = IssueRepository(db=db)
    issue_service = IssueService(repository)
    logger.debug("API: get_all_issues called")
    issues = issue_service.get_all_issues()
    return issues


@router.get(
    "/status/{status}",
    response_model=List[Issue],
    description="Get issues by status",
)
async def get_issues_by_status(
    status: str,
    db: Session = Depends(get_db),
) -> List[Issue]:
    repository = IssueRepository(db=db)
    issue_service = IssueService(repository)
    logger.debug("API: get_issues_by_status=%s called", status)
    issues = issue_service.get_issues_by_status(status)
    return issues


@router.post(
    "/",
    response_model=Issue,
    status_code=status.HTTP_201_CREATED,
    description="Create a new issue",
)
async def create_issue(
    payload: IssueCreate,
    db: Session = Depends(get_db),
) -> Issue:
    repository = IssueRepository(db=db)
    issue_service = IssueService(repository)
    logger.info("API: create_issue payload=%s", payload)
    created = issue_service.create_issue(payload)
    return created


@router.put(
    "/{issue_id}",
    response_model=Issue,
    description="Update an existing issue",
)
async def update_issue(
    issue_id: int,
    payload: IssueUpdate,
    db: Session = Depends(get_db),
) -> Issue:
    repository = IssueRepository(db=db)
    issue_service = IssueService(repository)
    logger.info("API: update_issue id=%s payload=%s", issue_id, payload)
    updated = issue_service.update_issue(issue_id, payload)
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    return updated


@router.delete(
    "/{issue_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Delete an issue",
)
async def delete_issue(
    issue_id: int,
    db: Session = Depends(get_db),
) -> None:
    repository = IssueRepository(db=db)
    issue_service = IssueService(repository)
    logger.info("API: delete_issue id=%s", issue_id)
    issue_service.delete_issue(issue_id)
    return None


@router.get(
    "/{issue_id}",
    response_model=Issue,
    description="Get issue by id",
)
async def get_issue_by_id(
    issue_id: int,
    db: Session = Depends(get_db),
) -> Issue:
    repository = IssueRepository(db=db)
    issue_service = IssueService(repository)
    logger.debug("API: get_issue_by_id id=%s", issue_id)
    issue = issue_service.get_issue_by_id(issue_id)
    if issue is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
    return issue