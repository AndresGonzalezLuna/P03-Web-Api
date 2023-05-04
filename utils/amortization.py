import pandas as pd


class Amortization:
    def __init__(self, amount: float, rate: float, t: int):
        self.amount = amount
        self.rate = rate
        self.t = t

    @property
    def payment_amount(self) -> float:
        return self.amount * self.rate / (1 - (1 + self.rate) ** (-self.t))

    def to_dataframe(self) -> pd.DataFrame:
        times = list(range(1, self.t + 1))
        payments = [self.payment_amount for _ in range(self.t)]

        initial_interes = self.amount * self.rate
        initial_principal = self.payment_amount - initial_interes
        balances = [self.amount]
        interests = [initial_interes]
        principals = [initial_principal]
        new_balances = [self.amount - initial_principal]

        for _ in times[1:]:
            balances.append(new_balances[-1])
            interests.append(balances[-1] * self.rate)
            principals.append(self.payment_amount - interests[-1])
            new_balances.append(balances[-1] - principals[-1])

        df = pd.DataFrame.from_dict({
            "T": times,
            "Balance": balances,
            "Interest": interests,
            "Principal": principals,
            "New Balance": new_balances
        })

        df.to_html("demo.html")
        return df


amortization = Amortization(560_000, 0.01075, 36)

print(amortization.payment_amount)
print(amortization.to_dataframe())
