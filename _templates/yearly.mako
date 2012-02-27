<%inherit file="site.mako" />
<h1>${year}</h1>

% for ((unused, month), posts) in monthly: 
<% curday = 0; first = True %>
    <div class="monthly">
        <h1>${month}</h1>
        <ul>
        % for post in posts:
                <% postday = post.date.strftime("%d") %>
                % if curday != postday:
                    % if first == False:
                    </ul>
                    % endif
                    <% curday = postday; first= False %>
                    <h2>${postday}</h2>
                    <ul>
                % endif
                <li>${post.title}</li>
        % endfor
                    </ul>
        </ul>
    </div>
% endfor

<ul class="prevnext">
    % if prev_link:
        <li><a href="${prev_link}">« Previous Year</a></li>
    % endif
    % if next_link and prev_link:
        <li>•</li>
    % endif
    % if next_link:
        <li><a href="${next_link}">Next Year »</a></li>
    % endif
</ul>
