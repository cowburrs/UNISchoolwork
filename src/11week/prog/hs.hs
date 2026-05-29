mystery :: [Integer]
mystery = 0 : 1 : zipWith (+) mystery (tail mystery)
