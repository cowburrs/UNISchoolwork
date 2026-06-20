-- |
-- Module      : Extension
-- Author      : COMP1100/COMP1130 Team, Your name and UID here
-- Date        :
-- Description : Extensions for Lab 7
module Extension where

import Data.List (nub)

{-
Extension 1

Write a function `powerset` that takes a list, and generates all possible sublists,
ignoring ordering of the elements in the sublists.
The order that the sublists are listed also doesn't matter.

-}

-- \| doctests
-- >>> powerset [1,2,3]
-- [[1,2],[1,2,3],[1],[1,3],[2],[2,3],[],[3]]
-- powerset :: [a] -> [[a]]

powerset :: (Eq a) => [a] -> [[a]]
powerset x = nub (powerset' x)

-- powerset' [] = []
-- powerset' l = l : (removeN replicated 0) ++ (map powerset' (removeN replicated 0))
--   where
--     replicated = replicate (length l) l
--     removeN :: [[a]] -> Int -> [[a]]
--     removeN list acc
--       | acc >= length list = []
--       | otherwise = removeAt acc (list !! acc) : removeN list (acc + 1)
--     removeAt :: Int -> [a] -> [a]
--     removeAt i xs = take i xs ++ drop (i + 1) xs

-- powerset :: [a] -> [[a]]
-- powerset l = case l of
--   [] -> [[]]
--   (x : xs) -> map (x :) (powerset xs) ++ powerset xs

-- powerset l = helper l 1
--     where
--         helper list acc
--             | length list <= 2 = case list of
--                 (x:y:ys) -> [[x],[y],[x,y],[y,x]]
--             otherwise =

{-
Extension 2:

Write a function that accepts a list of positive integers and a target sum.
which returns all sub-sequences of the original list that add up to the
target sum.

-}

-- | doctests
-- >>> rucksack [3,7,5,9,13,17] 30
-- [[13,17],[3,5,9,13]]
rucksack :: [Integer] -> Integer -> [[Integer]]

rucksack list n = filter (\x -> sum x == n) (powerset list)

{-
Extension 3:

Try to come up with a definition for all integers, such that
each number has a unique representation.
-}

-- data MyInteger = ???
