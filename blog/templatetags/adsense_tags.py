from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.filter
def inarticle_ads(value):
    # Render the adsense code placed in html files
    ad_code = []
    ad_code.append(render_to_string("adsense/inarticle1.html"))
    ad_code.append(render_to_string("adsense/inarticle2.html"))
    ad_code.append(render_to_string("adsense/inarticle3.html"))
    ad_code.append(render_to_string("adsense/inarticle4.html"))
    ad_code.append(render_to_string("adsense/inarticle5.html"))
    ad_code.append(render_to_string("adsense/inarticle6.html"))

    # set adcode picker
    j = 0

    # Break down content into paragraphs
    paragraphs = value.split("</p>")

    # insert after every 10th paragraph
    for i in range(len(paragraphs)):
        if i % 10 == 0:
            if i == 0:
                continue
            paragraphs[i] = paragraphs[i] + "<p>" + ad_code[j] + "</p>"
            if j < 5:
                j += 1
            value = "</p>".join(paragraphs)
    return value

@register.filter
def two_para(value):
    paragraphs = value.split("</p>")
    for i in range(2):
        if i == 0:
            content = paragraphs[i] + "</p>"
        else:
            content = content + paragraphs[i] + "</p>"
    # remove links from content
    paragraphs = content.split("<a")
    content = paragraphs[0]
    for i in range(1, len(paragraphs)):
        for j in range(len(paragraphs[i])):
            temp = paragraphs[i]
            if (temp[j] == '>'):
                j=j+1
                paragraphs[i] = temp[j:]
                break
        content = content + paragraphs[i]
    paragraphs = content.split("</a>")
    content = ""
    for i in range(len(paragraphs)):
        content = content + paragraphs[i]
    return content

