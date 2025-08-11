from sqlalchemy.orm import Session
from models.Tags import Tags
from schemas.tags import TagCreate, Tag


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


def edit_tag_db(tag: Tag, db: Session):
    tag_db = db.query(Tags).filter(Tags.id_tag == tag.id_tag).first()
    if tag_db:
        tag_db.name = tag.name
        db.commit()
        db.refresh(tag_db)
    return ''
