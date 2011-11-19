<%page args="post, comments=None"/>

<article>
    <header>
        <title>${post.title}</title>
        <!-- date published or updated -->
        <time pubdate datetime="${self.post_time_full(post)}">
            <span class='time'>${post.date.strftime("%H:%M")}</span>
            <span class='daymonth'>${post.date.strftime("%d")} <abbr title="${post.date.strftime("%B")}">${post.date.strftime("%b")}</abbr></span>
            <span class='year'>${post.date.strftime("%Y")}</span>
        </time>
    </header>
    <section>
    <h1><a href="${post.permapath()}">${post.title}</a></h1>
    ${self.post_prose(post)}
    </section>
    ${self.categories(post)}

    % if comments is not None:
        ${comments(post)}
    % endif
</article>

<%def name="post_prose(post)">
  ${post.content}
</%def>

<%def name="post_time_full(post)">${post.date.strftime("%y-%m-%dT%H:%M:%S%z")}</%def>

<%def name="categories(post)">
    <ul class="categories">
    % for category in post.categories:
        % if post.draft == True:
        <li>${category.name}</li>
        % else:
        <li><a href='${category.path}'>${category.name}</a></li>
        % endif
    % endfor
    </ul>
</%def>
