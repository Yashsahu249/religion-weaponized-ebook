import json
from markupsafe import escape


def generate_book_cover(request):
    """HTTP Cloud Function to generate book cover."""

    request_json = request.get_json(silent=True)
    request_args = request.args

    title = (
        request_json['title']
        if request_json and 'title' in request_json
        else request_args.get('title', 'Default Title')
    )
    author = (
        request_json['author']
        if request_json and 'author' in request_json
        else request_args.get('author', 'Default Author')
    )

    cover_url = (
        f"https://example.com/book_cover"
        f"?title={escape(title)}&author={escape(author)}"
    )

    return json.dumps({'cover_url': cover_url})