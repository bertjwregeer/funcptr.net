<%inherit file="base.mako" />\
<!DOCTYPE html>
<html lang="en">
    <!-- Copyright (c) 2012 Bert JW Regeer -->
    <head>
        <title>${self.cur_title()}</title>
        <link rel="alternate" type="application/rss+xml" title="RSS 2.0" href="${bf.util.site_path_helper(bf.config.blog.path,'/feed/index.xml')}" />
        <link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="${bf.util.site_path_helper(bf.config.blog.path,'/feed/atom/index.xml')}" />
        <link rel="stylesheet" href="${bf.config.site.css}/0x58-blog.css" />
        <link rel="stylesheet" href="${bf.config.site.css}/pygments.css" />
        <link rel='stylesheet' href='${bf.config.filters.syntax_highlight.css_dir}/pygments_${bf.config.filters.syntax_highlight.style}.css' />
        <meta charset="utf-8" />
        <link rel="shortcut icon" href="/favicon.ico">
        <!--[if IE]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
        <!--[if lt IE 9]> <script type="text/javascript" src="http://ie7-js.googlecode.com/svn/version/2.1(beta3)/IE9.js"></script><![endif]-->
        <script type="text/javascript">
            var _gaq = _gaq || [];
//            _gaq.push(['_setAccount', 'UA-97351-3']);
            _gaq.push(['_trackPageview']);

            (function() {
                var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();
        </script>
    </head>
    <body>
        <div id="Mwrapper">
            <div id="MainContent">
                ${next.body()}
            </div>
        </div>
        <aside>
            <header>
                ${next.header()}
            </header>
            <nav>
                ${next.menu()}
            </nav>
        </aside>

        <footer>
        ${next.footer()}
        </footer>
    </body>
</html>

<%def name="header()">
    <%include file="header.mako" />
</%def>
<%def name="footer()">
    <%include file="footer.mako" />
</%def>
<%def name="menu()">
    <%include file="menu.mako" />
</%def>
<%def name="post_title()" />
<%def name="cur_title()">${bf.config.blog.name}${self.page_title()}</%def>
<%def name="page_title()"><%
        if len(capture(self.post_title)) > 0:
            return u' - {0}'.format(capture(self.post_title))
        else:
            return ''
%></%def>
