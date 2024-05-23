from collections import Counter
from tld import get_tld


def get_sorted_tlds_amounts(urls: set[str]) -> dict[str, int]:
    tlds = (get_tld(url, fail_silently=True) for url in urls)
    tlds_counts = Counter((tld for tld in tlds if tld))
    return dict(tlds_counts.most_common())
