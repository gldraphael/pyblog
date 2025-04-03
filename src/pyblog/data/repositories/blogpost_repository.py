from sqlalchemy import select

from ...domain.blogpost import BlogPost
from ..database import AppDb
from ..models.blogpost import BlogPostDAO

class BlogPostRepository:

    def __init__(self, db: AppDb):
        self.__db = db

    def get_posts(self):
        with self.__db.session_maker().begin() as session:
            statement = select(BlogPostDAO).order_by(BlogPostDAO.created_on)
            result = session.scalars(statement).all()
            blog_posts = [
                BlogPost(
                    id=dao.id,
                    slug=dao.slug,
                    title=dao.title,
                    markdown=dao.markdown,
                    created_on=dao.created_on,
                    last_updated_on=dao.last_updated_on,
                    published_on=dao.published_on
                )
                for dao in result
            ]
        return blog_posts


    def create_post(self, post: BlogPost):
        dao = BlogPostDAO(
            id = post.id,
            title = post.title,
            slug = post.slug,
            markdown = post.markdown,
            created_on=post.created_on,
            published_on=post.published_on,
            last_updated_on=post.last_updated_on
        )

        with self.__db.session_maker().begin() as s:
            s.add(dao)


    def update_post(self, post: BlogPost):
        with self.__db.session_maker().begin() as s:
            db_post: BlogPostDAO = s.execute(select(BlogPostDAO).filter_by(id=post.id)).scalar_one()
            db_post.title = post.title
            db_post.slug = post.slug
            db_post.markdown = post.markdown
            db_post.created_on = post.created_on
            db_post.published_on = post.published_on
            db_post.last_updated_on = post.last_updated_on
