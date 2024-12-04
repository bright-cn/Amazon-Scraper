from pydantic import BaseModel


class Product(BaseModel):
    name: str
    current_price: str
    rating: str
    reviews: str
    asin: str
    link: str

    @staticmethod
    def csv_headers():
        return ["Name", "Current Price", "Rating", "Reviews", "ASIN", "Link"]

    def to_csv(self):
        return [
            self.name,
            self.current_price,
            self.rating,
            self.reviews,
            self.asin,
            self.link,
        ]
