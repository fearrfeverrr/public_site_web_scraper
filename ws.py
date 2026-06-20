import urllib.request
with urllib.request.urlopen('') as f:
    # The response may be compressed (for example, 'gzip').
    print(f.headers.get(''))
    data = f.read()
    if f.headers.get('') == 'gzip':
        import gzip
        data = gzip.decompress(data)
    print(data[:300].decode('utf-8', errors='replace'))