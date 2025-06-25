from sqlalchemy.orm import Session
from schemas.post import PostCreate
from models.post import Post


def create_postdb(db: Session, post: PostCreate):
    db_post = Post(
        **post.model_dump()
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
