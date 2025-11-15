"""
Script for adding test data to the DB
"""
from database import SessionLocal
from models.issue import IssueModel


def add_test_data():
    """Add test data to the database"""
    
    db = SessionLocal()
    
    try: 
        # Test issues
        issues = [
            IssueModel(
                text="First issue example",
                status="open",
                source="operator"
            ),
            IssueModel(
                text="Second issue example",
                status="closed",
                source="monitoring"
            ),
            IssueModel(
                text="Third issue example",
                status="in_progress",
                source="partner"
            ),
        ]

        for issue in issues:
            db.add(issue)
        
        db.commit()
        print("Тестовые данные успешно добавлены!")
        print(f"  - Добавлено {len(issues)} issues")
        
    except Exception as e:
        db.rollback()
        print(f"Ошибка при добавлении данных: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    add_test_data()
