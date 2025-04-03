from pyblog.containers import Container
from pyblog.domain.blogpost import BlogPost
from pyblog.data.repositories.blogpost_repository import BlogPostRepository


def print_posts(blogs: BlogPostRepository):
    print()
    print(blogs.get_posts())

def main():

    container = Container()
    blogs = container.blogpost_repository()

    # Create an empty post
    post = BlogPost.new_empty_post()
    blogs.create_post(post)
    print_posts(blogs)

    # Set a title and update the empty post
    post.title = "Hello, world!"
    post.markdown = """
    # Hello, world!

    It's nice to have you here! 
    kthxbye 👋
    """
    blogs.update_post(post)
    print_posts(blogs)

    return app


if __name__ == "__main__":
    app = main()
