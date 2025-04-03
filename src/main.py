from pyblog.api.app import create_app
from pyblog.app import container
from pyblog.core.domain.blogpost import BlogPost
from pyblog.infrastructure.data.repositories.blogpost_repository import BlogPostRepository



def print_posts(blogs: BlogPostRepository):
    print()
    print(blogs.get_posts())

def main():

    blogs = container.blogpost_repository()

    # Create an empty post
    post = BlogPost.new_empty_post()
    blogs.create_post(post)
    print_posts(blogs)

    # Set a title and update the empty post
    post.title = "Hello, world!"
    post.markdown = """
    # Hello, world!

    It's nice to have you here! Bye 👋
    """
    blogs.update_post(post)
    print_posts(blogs)

    return app


if __name__ == "__main__":
    app = main()
