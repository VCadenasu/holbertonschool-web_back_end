export default function getBudgetObject(income, gdp, capita) {
  const budget = [...arguments] => {
    income: income,
    gdp: gdp,
    capita: capita,
  };

  return budget;
}
