from typing import List, Dict

def paginate(items: List[Dict], page: int = 1, pageSize: int = 100):
    if page < 1:
        page = 1
    if pageSize < 1:
        pageSize = 1
    start = (page - 1) * pageSize
    end = start + pageSize
    return {
        "data": items[start:end],
        "page": page,
        "pageSize": pageSize,
        "total": len(items),
    }
