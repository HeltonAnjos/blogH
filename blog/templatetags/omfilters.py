from django import template

register = template.Library()


@register.filter(name='plural_comments')
def plural_comentarios(number_comments):
    try:
        number_comments = int(number_comments)

        if number_comments == 0:
            return f'Nenhum comentário'
        elif number_comments == 1:
            return f'{number_comments} comentário'
        else:
            return f'{number_comments} comentários'
    except:
        return f'{number_comments} comentário(s)'
