def unicode(s, encoding='utf-8'):
    if isinstance(s, bytes):
        return s.decode(encoding)
    elif isinstance(s, str):
        return s
    else:
        raise TypeError(f"Expected bytes or str, got {type(s).__name__}")
