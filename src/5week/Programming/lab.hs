module Expression where

-- | A token is plus, minus or a number
data Token
  = Plus
  | Minus
  | Times
  | DividedBy
  | Power
  | Num Double
  deriving (Show, Eq)

-- | Expression is a list of tokens
type Expression = [Token]

-- | The `tokenise` function reads a string to return a list of tokens
-- >>> tokenise "3.2 + 2.3"
-- [Num 3.2,Plus,Num 2.3]
tokenise :: String -> Expression
tokenise "" = []
tokenise (c : cs) = case c of
  '+' -> Plus : tokenise cs
  '-' -> Minus : tokenise cs
  '*' -> Times : tokenise cs
  '/' -> DividedBy : tokenise cs
  '^' -> Power : tokenise cs
  _
    | c `elem` ['0' .. '9'] -> case reads (c : cs) of
        [(value, rest)] -> Num value : tokenise rest
        _ -> error "Could not read number"
    | c `elem` [' ', '\t'] -> tokenise cs
    | otherwise -> error "Unknown Symbol"

-- | The `showExpression` function reads a list of tokens to return a string
-- >>> showExpression [Num 3.2,Plus,Num 2.3]
-- "3.2 + 2.3"
showExpression :: Expression -> String
showExpression [] = ""
showExpression (e : es) = case e of
  Plus -> " + " ++ showExpression es
  Minus -> " - " ++ showExpression es
  Times -> " * " ++ showExpression es
  DividedBy -> " / " ++ showExpression es
  Power -> " ^ " ++ showExpression es
  Num x -> show x ++ showExpression es

-- | `evalStringExpression` evaluates a string containing a valid numberical
-- expression and returns the evaluated expression
-- >>> evalStringExpression "3.2 - 4.2 - 5.3 + 6.3"
-- "0.0"
evalStringExpression :: String -> String
evalStringExpression s = showExpression (eval (tokenise s))

-- >>> showExpression [Num 3.2,Power,Num 2.3]
-- "3.2 ^ 2.3"

-- | Write your comment about the function here
eval :: Expression -> Expression
-- eval x = toPlusMinus (toMult (toPower x))
eval = toPlusMinus . toMult . toPower

toPower list = case list of
  (Num x : Power : Num y : ys) -> toPower ((Num (x ** y)) : ys)
  (Num x : []) -> (Num x : [])
  (Minus : Num x : ys) -> toPower (Num (-x) : ys)
  (x : y : ys) -> x : y : toPower ys
  [] -> []

toMult list = case list of
  (Num x : Times : Num y : ys) -> toMult ((Num (x * y)) : ys)
  (Num x : DividedBy : Num y : ys) -> toMult ((Num (x / y)) : ys)
  (Num x : []) -> (Num x : [])
  (x : y : ys) -> x : y : toMult ys
  [] -> []

toPlusMinus list = case list of
  (Num x : Plus : Num y : ys) -> toPlusMinus ((Num (x + y)) : ys)
  (Num x : Minus : Num y : ys) -> toPlusMinus ((Num (x - y)) : ys)
  (Num x : []) -> (Num x : [])
  (x : y : ys) -> x : y : toPlusMinus ys
  [] -> []
