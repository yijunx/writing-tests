from datetime import datetime

from app.pay.credit_card import CreditCard


class PaymentProcessor:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def _check_api_key(self):
        return self.api_key == "correct api key, but its BAD to leave it here"

    def charge(self, card: CreditCard, amount: int) -> None:
        if not self.validate_card(card=card):
            raise ValueError("Invalid card")
        if not self._check_api_key():
            raise ValueError("Invalid API KEY")

        print(f"Charging card number {card} for ${amount/100:.2f}")

    def validate_card(self, card: CreditCard) -> bool:
        return (
            self.luhn_checksum(card.number)
            and datetime(card.expiry_year, card.expiry_month, 1) > datetime.now()
        )

    # bad example to put it here..
    # the self is not used
    def luhn_checksum(self, card_number: str) -> bool:
        def digits_of(card_nr: str):
            return [int(d) for d in card_nr]

        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for digit in even_digits:
            checksum += sum(digits_of(str(digit * 2)))
        return checksum % 10 == 0
