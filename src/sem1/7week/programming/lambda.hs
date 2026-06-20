num :: Int -> (a -> a) -> a -> a
num 0 f x = x
num n f x = f (num (n-1) f x)

y :: (a -> a) -> a
y a = a (y a)

f :: (Int -> Int) -> Int -> Int
f fn n = if n == 0 then 1 else (n * (fn (pred n)))

fac :: Int -> Int
fac = y f
