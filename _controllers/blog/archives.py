################################################################################
## Archives controller
##
## Writes out yearly, monthly, and daily archives.
## Each archive is navigable to the next and previous archive
## in which posts were made.
################################################################################

import operator

from blogofile.cache import bf
import chronological

blog = bf.config.controllers.blog


def run():
    write_daily_archives()
    write_monthly_archives()
    write_yearly_archives()


def sort_into_archives():
    for post in blog.posts:
        day = post.date.strftime("%d")
        month = post.date.strftime("%m")
        year = post.date.strftime("%Y")

        blog.archive_posts_year.setdefault(year, list()).append(post)
        blog.archive_posts_yearmonth.setdefault((year, month), list()).append(post)
        blog.archive_posts_yearmonthday.setdefault((year, month, day), list()).append(post)

def write_daily_archives():
    for (year, month, day), posts in sorted(blog.archive_posts_yearmonthday.items(), key=operator.itemgetter(0), reverse=True):
        posts = sorted(posts, key=lambda p: p.date, reverse=True)
        link = '{year}/{month}/{day}'.format(year=year, month=month, day=day)
        chronological.write_daily_archive(posts, root=link, findex=True)

def write_monthly_archives():
    for (year, month), posts in sorted(blog.archive_posts_yearmonth.items(), key=operator.itemgetter(0), reverse=True):
        posts = sorted(posts, key=lambda p: p.date, reverse=True)
        link = '{year}/{month}'.format(year=year, month=month)
        chronological.write_monthly_archive(posts, root=link, findex=True)

def write_yearly_archives():
    years = blog.archive_posts_year.keys();
    years.sort()
    for (year), posts in sorted(blog.archive_posts_year.items(), key=operator.itemgetter(0), reverse=True):
        # Check to make sure index is within range of list length, if so set ynext to that value
        ynext = years.index(year) + 1 if years.index(year) + 1 < len(years) else None
        ynext = years[ynext] if ynext is not None else ynext

        # Check to make sure index is within range of list length, if so set yprev to that value
        yprev = years.index(year) - 1 if years.index(year) - 1 >= 0 else None
        yprev = years[yprev] if yprev is not None else yprev

        posts = sorted(posts, key=lambda p: p.date, reverse=True)
        link = '{year}'.format(year=year)
        
        monthly = {}
        for post in sorted(posts, reverse=True):
            print post.date
            monthly.setdefault((post.date.strftime("%m"), post.date.strftime("%B")), list()).append(post)

        print monthly
        monthly = sorted(monthly.items(), key=lambda x: x[0][0], reverse=True)
        chronological.write_yearly_archive(monthly, root=link, year=year, year_next=ynext, year_previous=yprev)

