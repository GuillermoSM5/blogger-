from sqlalchemy.orm import Session, joinedload
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


def get_post_byid(post_id: int,  db: Session):
    post_db = db.query(Post).options(joinedload(Post.autor)
                                     ).filter(Post.id_post == post_id).all()
    if not post_db:
        return None
    return post_db[0]


def get_all_post_db(db: Session):
    result = db.query(Post).options(joinedload(
        Post.autor)).offset(0).limit(100).all()
    return result
