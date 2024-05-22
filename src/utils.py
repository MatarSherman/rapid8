from collections import Counter
from tld import get_tld


def get_sorted_tlds_amounts(urls: list[str]) -> dict[str, int]:
    tlds = (get_tld(url, fail_silently=True) for url in urls)
    tlds_counts = Counter((tld for tld in tlds if tld))
    return dict(
        sorted(
            tlds_counts.items(),
            key=lambda countEntry: countEntry[1],
            reverse=True
        )
    )
