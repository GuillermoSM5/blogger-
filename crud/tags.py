from sqlalchemy.orm import Session
from models.Tags import Tags
from schemas.tags import TagCreate


def get_all_tags_db(db: Session):
    result = db.query(Tags).offset(0).limit(100).all()
    return result


def create_tag_db(tag: TagCreate, db: Session):
    db_tag = Tags(
        **tag.model_dump(),
    )
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag
