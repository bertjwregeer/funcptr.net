<ul>
    <li><h1></h1>
        <ul>
        <li><a href="/">Main</a></li>
        <li><a href="http://bertjwregeer.com/About_me.html">About Me</a></li>
        <li><a href="http://bertjwregeer.com/Contact.html">Contact</a></li>
    </ul>
    </li>
    <li><h1>Networking</h1>
    <ul>
    <% bf.config.social.sort(key=lambda p: p.get("title")) %>
    % for urls in bf.config.social:
        <li><a href="${urls['url']}" alt="${urls['alt']}">${urls['title']}</a></li>
    % endfor
    </ul>
    </li>
    <li><h1>&#x2015;</h1>
    <ul>
        <li><a href="${bf.util.site_path_helper(bf.config.blog.path,'/feed/index.xml')}">RSS</a></li>
        <li><a href="${bf.util.site_path_helper(bf.config.blog.path,'/feed/atom/index.xml')}">Atom</a></li>
    </ul>
    </li>
</ul>
