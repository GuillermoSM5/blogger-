from sqlalchemy.orm import Session, joinedload
from services.post_service import get_reading_time_minutes, get_slug
from schemas.post import PostCreate
from models.post import Post
from models.Tags import Tags


def create_postdb(db: Session, post: PostCreate):
    tag = db.query(Tags).filter(Tags.name == post.tags[0]).all()
    print(tag[0].id_tag)
    # Ejemplo de como desestructurar un objeto en python
    # db_post = Post(
    #     **post.model_dump(),
    # )
    db_post = Post(
        title=post.title,
        content=post.content,
        image_url='',
        id_autor=post.id_autor,
        tags=tag,
        minutes_to_read=get_reading_time_minutes(post.content),
        slug=get_slug(post.title)
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
