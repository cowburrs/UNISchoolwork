succ = \n f x. f (n f x)
zero = \f x. x
num  = ... (need built-in natural number support)

true  = \x y. x
false = \x y. y
if    = \b t f. b t f

mul   = \m n f x. m (n f) x
pred' = \n f x. fst (n (\p. pair (snd p) (f (snd p))) (pair x x))
pair  = \x y f. f x y
fst   = \p. p (\x y. x)
snd   = \p. p (\x y. y)

iszero = \n. n (\x. false) true
