# Write all the blog posts in reverse chronological order
import os
from blogofile.cache import bf

blog = bf.config.controllers.blog


def run():
    write_blog_chron(posts=blog.posts, root=blog.pagination_dir.lstrip("/"))
    write_blog_first_page()


def write_blog_chron(posts, root, findex=False):
    page_num = 1
    post_num = 0
    while len(posts) > post_num:
        #Write the pages, num_per_page posts per page:
        page_posts = posts[post_num:post_num + blog.posts_per_page]
        post_num += blog.posts_per_page
        if page_num > 1:
            if page_num - 1 == 1:
                if not blog.custom_index:
                    prev_link = bf.util.site_path_helper(blog.path)
                else:
                    prev_link = bf.util.site_path_helper(blog.path, blog.pagination_dir, str(page_num - 1))
            else:
                prev_link = bf.util.site_path_helper(blog.path, blog.pagination_dir, str(page_num - 1))
        else:
            prev_link = None
        if len(posts) > post_num:
            next_link = bf.util.site_path_helper(blog.path, blog.pagination_dir, str(page_num + 1))
        else:
            next_link = None
        if page_num > 1 or findex is False:
            page_dir = bf.util.path_join(blog.path, root, str(page_num))
        else:
            page_dir = bf.util.path_join(blog.path, root);
        fn = bf.util.path_join(page_dir, "index.html")
        env = {
            "posts": page_posts,
            "next_link": next_link,
            "prev_link": prev_link
        }
        bf.writer.materialize_template("chronological.mako", fn, env)
        page_num += 1

def write_daily_archive(posts, root, findex=False):
    return write_monthly_archive(posts, root, findex=findex)

def write_monthly_archive(posts, root, findex=False):
    page_num = 1
    post_num = 0
    while len(posts) > post_num:
        #Write the pages, num_per_page posts per page:
        page_posts = posts[post_num:post_num + blog.posts_per_page]
        post_num += blog.posts_per_page
        if page_num > 1:
            if page_num - 1 == 1:
                if not blog.custom_index:
                    prev_link = bf.util.site_path_helper(blog.path, root)
                else:
                    prev_link = bf.util.site_path_helper(blog.path, root, blog.pagination_dir, str(page_num - 1))
            else:
                prev_link = bf.util.site_path_helper(blog.path, root, blog.pagination_dir, str(page_num - 1))
        else:
            prev_link = None
        if len(posts) > post_num:
            next_link = bf.util.site_path_helper(blog.path, root, blog.pagination_dir, str(page_num + 1))
        else:
            next_link = None
        if page_num > 1 or findex is False:
            page_dir = bf.util.path_join(blog.path, root, str(page_num))
        else:
            page_dir = bf.util.path_join(blog.path, root);
        fn = bf.util.path_join(page_dir, "index.html")
        env = {
            "posts": page_posts,
            "next_link": next_link,
            "prev_link": prev_link
        }
        bf.writer.materialize_template("chronological.mako", fn, env)
        page_num += 1

def write_yearly_archive(monthly, root, year, year_next=None, year_previous=None):
    next_link = None
    prev_link = None

    if year_next is not None:
        next_link = bf.util.site_path_helper(blog.path, year_next)
    if year_previous is not None:
        prev_link = bf.util.site_path_helper(blog.path, year_previous)

    page_dir = bf.util.path_join(blog.path, root)
    fn = bf.util.path_join(page_dir, "index.html")
    env = {
            "year": year,
            "monthly": monthly,
            "next_link": next_link,
            "prev_link": prev_link,
    }
    bf.writer.materialize_template("yearly.mako", fn, env)

def write_blog_first_page():
    if not blog.custom_index:
        page_posts = blog.posts[:blog.posts_per_page]
        path = bf.util.path_join(blog.path, "index.html")
        blog.logger.info(u"Writing blog index page: " + path)
        if len(blog.posts) > blog.posts_per_page:
            next_link = bf.util.site_path_helper(
                    blog.path, blog.pagination_dir+"/2")
        else:
            next_link = None
        env = {
            "posts": page_posts,
            "next_link": next_link,
            "prev_link": None
        }
        bf.writer.materialize_template("chronological.mako", path, env)
