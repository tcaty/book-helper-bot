from urllib.parse import quote


def quote_text(text: str) -> str:
    return quote(text.replace(' ', '+'), safe='[](){}⟨⟩:,‒–—―.!?""«»; +')
