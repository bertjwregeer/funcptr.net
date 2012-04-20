<%inherit file="_templates/site.mako" />

<article>
<section>
<%self:filter chain="markdown">
[About this technical notebook](/About/)
========================================

This technical log/notebook was created by [Bert JW Regeer][1] and is mainly a
way for Bert to keep track of various different technical matters in a way that
could also help other people on the Internet by making his technical notes
public.

Topics
------

The topics on this technical log are going to be entirely based around topics
that come up in Bert's daily activities. This includes many different things,
ranging from system administration tasks to software engineering/architecting.
Bert currently works at a start-up and wears many hats throughout the day so
many interesting tasks are put on his plate.

If you are interested in more information about anything posted, please do not
hesitate to [contact][4] Bert. He is always willing to help people solve
problems, and if something isn't clear in one of his posts he would like to fix
it so that it can help more people.

The name
--------

The name `typedef void (*funcptr)();` comes from the C/C++ language where this
creates a [typedef][2] for a [function pointer][3]. The function this can point
to takes no arguments and returns void.

[1]: http://bertjwregeer.com/
[2]: http://en.wikipedia.org/wiki/Typedef
[3]: http://en.wikipedia.org/wiki/Function_pointer
[4]: http://bertjwregeer.com/Contact.html

</%self:filter>
</section>
</article>

<%def name="post_title()">About this technical notebook</%def>
