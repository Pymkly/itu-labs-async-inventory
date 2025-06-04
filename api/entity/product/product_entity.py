
def save_products(_cursor, _products):
    for _product in _products:
        _product.save(_cursor)
        print("vita")

def to_products(_products):
    return [ProductEntity(_id=-1, _title=_product.title, _no=_product.no) for _product in _products]

def create(_line):
    return ProductEntity(_line[0], _line[1], _line[2])


def get_products(_cursor):
    report_query = """
                SELECT id, title, no
                FROM product;
                """
    _cursor.execute(report_query)
    results = _cursor.fetchall()
    return [create(res) for res in results]


class ProductEntity:
    def __init__(self, _id, _title, _no):
        self._id = _id
        self._title = _title
        self._no = _no

    def save(self, _cursor):
        _query = """
            insert into product (title, no)
            values (%s, %s)
            returning id;
        """
        _cursor.execute(_query, (self._title, self._no))
        _id = _cursor.fetchone()[0]
        print(_id)
        return _id
