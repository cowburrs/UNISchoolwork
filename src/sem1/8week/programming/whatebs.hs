{-|
Module      : Extension
Author      : COMP1100 Team, Your name and UID here
Date        : 
Description : Optional Extensions (Trees)
-}

module Extension where

data BinaryTree a = Null | Node (BinaryTree a) a (BinaryTree a)
    deriving (Eq,Show)

{-

Extension 1

Write a function 
that verifies if a tree is **balanced**, that is, there is no other way to
restructure the tree such that it has smaller depth.
-}
tree1 :: BinaryTree Integer
tree1 = Node (Node (Node Null 2 (Node Null 11 Null)) 4 (Node (Node Null 0 Null) 
    1 (Node Null (-3) Null))) 5 (Node (Node (Node Null (-4) Null) 8 
    (Node Null 7 Null)) 3 Null)
helper (Node Null x Null) = [1]
helper (Node Null y x) = map (+1) (helper x)
helper (Node x y Null) = map (+1) (helper x)
helper (Node x y z) = map (+1) (helper x) ++ map (+1) (helper z)
-- isBalanced :: BinaryTree a -> Bool
-- isBalanced x = (treeMinimum x) == (treeMaximum x) 
-- isBalanced (Node x y z) = 1 + ((isBalanced x) == (isBalanced y))

-- Tricky Extension

{-
Part 1: foldTree 

Write a function foldTree that takes an operator and a base case, 
and folds the tree into one element.
-}

foldTree :: (b -> a -> b -> b) -> b -> BinaryTree a -> b
foldTree op base tree = undefined

{-
Part 2: 

Rewrite the functions treeSize and treeDepth 
using your new foldTree function.
-}

treeSize :: BinaryTree a -> Integer
treeSize tree = foldTree op base tree
  where
    op = error "treeSize: op undefined"
    base = error "treeSize: base case undefined"

treeDepth :: BinaryTree a -> Integer
treeDepth tree = foldTree op base tree
  where
    op = error "treeDepth: op undefined"
    base = error "treeDepth: base case undefined"

{-
Part 3: foldrTree and foldlTree

Write the functions foldrTree and foldlTree that should 
behave consistently with foldl and foldr.
-}

foldrTree :: (a -> b -> b) -> b -> BinaryTree a -> b
foldrTree op base tree = undefined

foldlTree :: (b -> a -> b) -> b -> BinaryTree a -> b
foldlTree op base tree = undefined

{-
Part 4: 

Rewrite the function treeFlatten 
using foldlTree or foldrTree as appropriate.
-}

flattenTree :: BinaryTree a -> [a]
flattenTree tree = fold op base tree
  where
    op = error "flattenTree: op undefined"
    base = error "flattenTree: base undefined"
    fold = error "flattenTree: Replace with either foldlTree or foldrTree"
