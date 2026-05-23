module Lists where

import Prelude hiding (Either, Left, Right)

-- $setup
-- >>> import Data.List (sort)

-- | isSorted : Checks if a list is sorted from smallest to biggest.
--
-- >>> isSorted [1,2,3,4]
-- True
-- >>> isSorted [1,3,2,4]
-- False
-- >>> isSorted ([] :: [Int])
-- True
-- >>> isSorted [1]
-- True
isSorted :: (Ord a) => [a] -> Bool
isSorted = undefined

-- | insertSorted : Assuming that the input list is sorted, take an element and
-- insert it into the list in the correct place, so that the list is still sorted.
--
-- >>> insertSorted [1,3,5] 4
-- [1,3,4,5]
-- >>> insertSorted [] 1
-- [1]
-- >>> insertSorted [2,4,6] 1
-- [1,2,4,6]
insertSorted :: (Ord a) => [a] -> a -> [a]
insertSorted = undefined

-- | removeDup : Takes a list, and deletes any elements that have already
-- appeared in the list so far. (Don't use nub here.)
--
-- >>> removeDup [1,2,3,2,1]
-- [1,2,3]
-- >>> removeDup ([] :: [Int])
-- []
-- >>> removeDup "abracadabra"
-- "abrcd"
removeDup :: (Eq a) => [a] -> [a]
removeDup = undefined

-- | continuous : Takes a list of integers, and checks that each element
-- in the list is at most one away from the previous element.
--
-- >>> continuous [1,2,3,2,1]
-- True
-- >>> continuous [1,3,5]
-- False
-- >>> continuous []
-- True
-- >>> continuous [1]
-- True
continuous :: [Integer] -> Bool
continuous = undefined

-- | rotate : Takes a list, and a value, and rotates the list around
-- by the number of elements indicated.
--
-- >>> rotate [1,2,3,4,5] 2
-- [3,4,5,1,2]
-- >>> rotate [1,2,3] 0
-- [1,2,3]
-- >>> rotate [1,2,3] 3
-- [1,2,3]
rotate :: [a] -> Int -> [a]
rotate = undefined

-- | insertAt : Takes a list of `a`, an element of type `a`, an index `Int`,
-- and inserts that element into the list at that index.
--
-- >>> insertAt [1,2,3,4] 99 2
-- [1,2,99,3,4]
-- >>> insertAt [] 5 0
-- [5]
insertAt :: [a] -> a -> Int -> [a]
insertAt = undefined

-- | runLengthEncoding : Takes a list, and returns a list of tuples,
-- counting how many times that element was duplicated consecutively.
--
-- >>> runLengthEncoding "aaabbbcc"
-- [('a',3),('b',3),('c',2)]
-- >>> runLengthEncoding []
-- []
-- >>> runLengthEncoding [1]
-- [(1,1)]
runLengthEncoding :: (Eq a) => [a] -> [(a, Integer)]
runLengthEncoding = undefined

-- | runLengthDecoding : Take the output from `runLengthEncoding`, and
-- reconstruct the original list.
--
-- >>> runLengthDecoding [('a',3),('b',2)]
-- "aaabb"
-- >>> runLengthDecoding []
-- []
runLengthDecoding :: [(a, Integer)] -> [a]
runLengthDecoding = undefined

-- | transpose : Takes [[a]] as input, and transposes it
-- (swap rows with columns). (Don't use the transpose function in Data.List here)
--
-- >>> transpose [[1,2,3],[4,5,6],[7,8,9]]
-- [[1,4,7],[2,5,8],[3,6,9]]
-- >>> transpose [[1,2],[3,4]]
-- [[1,3],[2,4]]
-- >>> transpose ([] :: [[Int]])
-- []
transpose :: [[a]] -> [[a]]
transpose = undefined

-- There is already a type using these keywords,
-- so we wish to not import it.

-- The sum data type is representing the disjoint union
-- of two sets, tagged with either Left or Right, so
-- we can tell which set it came from.
data Sum a b = Left a | Right b
  deriving (Show)

-- | sumApply : Takes two functions, the first can take type `a` as input,
-- and the second can take type `b` as input. Also takes a disjoint union
-- of `a` and `b` as input. If the input was of the form `Left a`,
-- extract the variable of type `a` and apply the first function.
-- Else, apply the second function to the argument in `Right b`.
--
-- >>> sumApply (+1) (*2) (Left 3 :: Sum Int Int)
-- Left 4
-- >>> sumApply (+1) (*2) (Right 3 :: Sum Int Int)
-- Right 6
sumApply :: (a -> c) -> (b -> d) -> Sum a b -> Sum c d
sumApply = undefined

-- | fromLeft : Takes a sum union, and extracts the `a` from `Left a`.
-- If the input was `Right b`, throw an error.
--
-- >>> fromLeft (Left 5 :: Sum Int Int)
-- 5
fromLeft :: Sum a b -> a
fromLeft = undefined

-- | fromRight : Takes a sum union, and extracts the `b` from `Right b`.
-- If the input was `Left a`, throw an error.
--
-- >>> fromRight (Right 5 :: Sum Int Int)
-- 5
fromRight :: Sum a b -> b
fromRight = undefined

-- | lefts : Takes a list of sum unions, and returns a list containing
-- only the left elements.
--
-- >>> lefts [Left 1, Right 2, Left 3 :: Sum Int Int]
-- [1,3]
lefts :: [Sum a b] -> [a]
lefts = undefined

-- | rights : Takes a list of sum unions, and returns a list containing
-- only the right elements.
--
-- >>> rights [Left 1, Right 2, Right 3 :: Sum Int Int]
-- [2,3]
rights :: [Sum a b] -> [b]
rights = undefined

-- | sumMap : Takes a list of sums, and two functions, and maps
-- the appropriate function onto each element.
-- (Hint: This function should be easy once you've written `sumApply`)
--
-- >>> sumMap [Left 1, Right 2, Left 3 :: Sum Int Int] (+10) (*10)
-- [Left 11,Right 20,Left 13]
sumMap :: [Sum a b] -> (a -> c) -> (b -> d) -> [Sum c d]
sumMap = undefined

-- | sumExtract : Takes a list of sums, and returns a tuple
-- of two lists, separating all the Left a and Right b elements.
--
-- >>> sumExtract [Left 1, Right 2, Left 3 :: Sum Int Int]
-- ([1,3],[2])
sumExtract :: [Sum a b] -> ([a], [b])
sumExtract = undefined

-- Apollo Construction Company

-- This data type represents construction workers.
-- Each worker has a name, an age, and a job.
-- A crew is a list of workers.
data Job = Digger | Driver | Builder | Foreman | Manager
  deriving (Show, Eq)

data Worker = Worker Name Age Job
  deriving (Show)

type Name = String

type Age = Int

type Crew = [Worker]

apolloCrew :: Crew
apolloCrew =
  [ Worker "Alice" 26 Driver,
    Worker "Bob" 21 Digger,
    Worker "Charlie" 34 Foreman,
    Worker "Daniel" 24 Digger,
    Worker "Eve" 31 Builder,
    Worker "Frank" 38 Manager,
    Worker "Grace" 34 Builder
  ]

-- | reassign : Takes a worker, and gives them a new job.
--
-- >>> reassign (Worker "Alice" 26 Driver) Manager
-- Worker "Alice" 26 Manager
reassign :: Worker -> Job -> Worker
reassign = undefined

-- | birthday : A worker has had a birthday today! Increase their age by one.
--
-- >>> birthday (Worker "Bob" 21 Digger)
-- Worker "Bob" 22 Digger
birthday :: Worker -> Worker
birthday = undefined

-- | isOnCrew : Checks if a particular worker is on a crew.
--
-- >>> isOnCrew apolloCrew (Worker "Alice" 26 Driver)
-- True
-- >>> isOnCrew apolloCrew (Worker "Zara" 30 Driver)
-- False
isOnCrew :: Crew -> Worker -> Bool
isOnCrew = undefined

-- | findSenior : Finds and returns the name of the most senior (oldest) worker on a crew.
--
-- >>> findSenior apolloCrew
-- "Frank"
findSenior :: Crew -> Name
findSenior = undefined

-- | filterJob : Given a crew, returns all workers that match a given job.
--
-- >>> filterJob apolloCrew Digger
-- [Worker "Bob" 21 Digger,Worker "Daniel" 24 Digger]
filterJob :: Crew -> Job -> Crew
filterJob = undefined

type Dollars = Int

-- | Define a sensible type for PayRate, mapping each Job to a dollar amount per hour.
-- data PayRate = ???

-- apolloWages :: PayRate
apolloWages = undefined

-- | crewCost : Given a crew, a payrate, and a number of hours, determines how much
-- it would cost to hire the crew for that duration of time.
crewCost = undefined

-- | Computes the tribonacci sequence.
-- T(0) = 0, T(1) = 0, T(2) = 1, T(n) = T(n-1) + T(n-2) + T(n-3)
--
-- >>> tribonacci 0
-- 0
-- >>> tribonacci 1
-- 0
-- >>> tribonacci 2
-- 1
-- >>> tribonacci 5
-- 4
-- >>> tribonacci 10
-- 81
tribonacci :: Integer -> Integer
tribonacci n
  | n <= 0 = 0
  | n == 1 = 0
  | n == 2 = 1
  -- FIX: was `tribonacci n-2` which parsed as `(tribonacci n) - 2` due to precedence
  | otherwise = tribonacci (n - 1) + tribonacci (n - 2) + tribonacci (n - 3)

-- | chessboard : Given input of (n, m),
-- returns a list of all tuples from (1,1) to (n,m).
--
-- >>> chessboard (2,2)
-- [(1,1),(1,2),(2,1),(2,2)]
-- >>> chessboard (1,3)
-- [(1,1),(1,2),(1,3)]
chessboard :: (Integer, Integer) -> [(Integer, Integer)]
chessboard = undefined

-- | bisectSqrt : Computes the square root of a number by bisection.
-- Returns the root to within a given tolerance.
--
-- >>> abs (bisectSqrt 0.001 4.0 - 2.0) < 0.001
-- True
-- >>> abs (bisectSqrt 0.001 9.0 - 3.0) < 0.001
-- True
bisectSqrt :: Double -> Double -> Double
bisectSqrt = undefined

-- Implement the following functions using higher order functions.
-- Your solutions should be very succinct, and should
-- not use recursion (other than the recursion provided by a higher
-- order function).

-- | arithMean : Computes the average of a list of numbers.
--
-- >>> arithMean [1,2,3,4,5]
-- 3.0
-- >>> arithMean [10,20]
-- 15.0
arithMean :: (Fractional a) => [a] -> a
arithMean = undefined

-- | geoMean : Computes the geometric mean of a list of numbers.
--
-- >>> abs (geoMean [1,4,9] - 2.8844...) < 0.001
-- True
geoMean :: (Floating a) => [a] -> a
geoMean = undefined

-- | l1Norm : Takes a list of numbers, and computes the sum of the
-- absolute values of each term.
--
-- >>> l1Norm [1,-2,3,-4]
-- 10
-- >>> l1Norm []
-- 0
l1Norm :: (Num a) => [a] -> a
l1Norm = undefined

-- | l2Norm : Takes a list of numbers, and computes the Euclidean norm,
-- defined to be the square root of the sum of the squares of each element.
--
-- >>> abs (l2Norm [3,4] - 5.0) < 0.001
-- True
l2Norm :: (Floating a) => [a] -> a
l2Norm = undefined

-- | cesaroSum : Takes a list of numbers, and returns a list, where the nth element
-- is the average of the first n terms of the input list.
--
-- >>> cesaroSum [1,2,3,4]
-- [1.0,1.5,2.0,2.5]
cesaroSum :: (Fractional a) => [a] -> [a]
cesaroSum = undefined

-- | revMap : Takes an element, and feeds that element to each function in a list.
--
-- >>> revMap 3 [(+1), (*2), (^2)]
-- [4,6,9]
revMap :: a -> [(a -> b)] -> [b]
revMap = undefined

-- | superMap : Takes a list of elements, and a list of functions, and applies each element to
-- each function. Your output should be a list of lists.
--
-- >>> superMap [1,2,3] [(+10), (*10)]
-- [[11,12,13],[10,20,30]]
superMap :: [a] -> [(a -> b)] -> [[b]]
superMap = undefined

data BinaryTree a = Null | Node (BinaryTree a) a (BinaryTree a)
  deriving (Show)

type BSTree a = BinaryTree a

-- | I wonder what this function does.
-- (It mirrors/flips the tree left-to-right.)
--
-- >>> treeMystery (Node (Node Null 1 Null) 2 (Node Null 3 Null))
-- Node (Node Null 3 Null) 2 (Node Null 1 Null)
treeMystery :: BSTree a -> BSTree a
treeMystery tree = case tree of
  Null -> Null
  Node left x right -> Node (treeMystery right) x (treeMystery left)

-- =====================================

-- FIX: The original `data Ancestor` used `Grand Ancestor` where `Ancestor`
-- is the type itself (recursive), and `data Person` used `My Ancestor` the same way.
-- This is valid Haskell for a recursive type but the capitalisation of the

-- * type name* `Ancestor` clashes with the *constructor* name. Renamed the

-- type to `Relation` to avoid the clash and make intent clearer.

data Relation = Father | Mother | Grand Relation
  deriving (Show)

data Person = Me | My Relation
  deriving (Show)

type FamilyTree = BinaryTree Name

-- | ancestors : Takes a Person and a FamilyTree, and returns all matching ancestor names.
-- (Hint: depth in the tree corresponds to generation.)
ancestors :: Person -> FamilyTree -> [Name]
ancestors = undefined

-- | kindAncestor : Takes a family tree and a name, and returns what kind of
-- relation that person is, if they can be found.
kindAncestor :: FamilyTree -> Name -> Maybe Person
kindAncestor = undefined

-- | The family tree of David Quarel (3 generations back)
david :: FamilyTree
david =
  Node
    ( Node
        ( Node
            (Node Null "Luigi Quarel" Null)
            "Luigi Quarel"
            (Node Null "Rosa Randazzo" Null)
        )
        "John Quarel"
        ( Node
            (Node Null "Alfredo Parisotto" Null)
            "Maria Parisotto"
            (Node Null "Assunta Karsun" Null)
        )
    )
    "David Quarel"
    ( Node
        ( Node
            (Node Null "Joseph Corcoran" Null)
            "Mark Corcoran"
            (Node Null "Mary O'Sullivan" Null)
        )
        "Helen Corcoran"
        ( Node
            (Node Null "Kyran Dunn" Null)
            "Clare Dunn"
            (Node Null "Charlotte Ohlin" Null)
        )
    )

-- | The family tree of Prince George of Cambridge (royal bloodline only)
george :: FamilyTree
george =
  Node
    georgeDad
    "Prince George of Cambridge"
    (Node Null "Catherine, Duchess of Cambridge" Null)
  where
    georgeDad =
      Node
        willDad
        "Prince William, Duke of Cambridge"
        (Node Null "Diana Spencer" Null)
      where
        willDad =
          Node
            (Node Null "Phillip, Duke of Edinburgh" Null)
            "Charles, Prince of Wales"
            charlesMum
          where
            charlesMum =
              Node
                lizzieDad
                "Elizabeth II"
                (Node Null "Elizabeth Bowes-Lyon" Null)
              where
                lizzieDad =
                  Node
                    georgeVIDad
                    "George VI"
                    (Node Null "Mary of Teck" Null)
                  where
                    georgeVIDad =
                      Node
                        georgeVDad
                        "George V"
                        (Node Null "Alexandra of Denmark" Null)
                      where
                        georgeVDad =
                          Node
                            (Node Null "Queen Victoria" Null)
                            "Edward VII"
                            (Node Null "Albert, Prince Consort" Null)

-- Polynomial Evaluation

-- | polyEval [a0, a1, a2, ..., an] x = a0 + a1*x + a2*x^2 + ... + an*x^n
--
-- >>> polyEval [1,2,3] 2.0
-- 17.0
-- >>> polyEval [] 5.0
-- 0.0
polyEval :: [Double] -> Double -> Double
polyEval = undefined

-- | hornerEval : Same as polyEval, but uses Horner's rule
-- to speed up computation time.
--
-- >>> hornerEval [1,2,3] 2.0
-- 17.0
hornerEval :: [Double] -> Double -> Double
hornerEval = undefined

-- | isPrime : Checks if a number is prime. Try to be efficient!
--
-- >>> isPrime 2
-- True
-- >>> isPrime 17
-- True
-- >>> isPrime 1
-- False
-- >>> isPrime 100
-- False
isPrime :: Integer -> Bool
isPrime = undefined

-- | factor : Returns a prime factorisation of an input number.
--
-- >>> factor 12
-- [2,2,3]
-- >>> factor 17
-- [17]
-- >>> factor 1
-- []
factor :: Integer -> [Integer]
factor = undefined

type Distance = Double

type City = (Double, Double)

type Route = [City]

-- | dist : Returns the Euclidean distance between two cities.
--
-- >>> dist (0,0) (3,4)
-- 5.0
dist :: City -> City -> Distance
dist = undefined

-- | cost : Returns the total distance for a particular route.
--
-- >>> cost [(0,0),(3,4),(3,4)]
-- 5.0
cost :: Route -> Distance
cost = undefined

-- | tsp (travelling salesperson problem) : Takes a list of cities
-- (represented by coordinate points) and returns the list shuffled,
-- such that visiting each city in the order returned minimises the
-- total travel cost (Euclidean distance).
tsp :: [City] -> Route
tsp = undefined

-- Copy over your code from SetsWithTrees.hs from Lab 10.

data Set a = Set (BSTree a)
  deriving (Show)

{-
Exercise 6

Complete all these functions, and state their complexity class.

COMP1100:   setEquals,
            addElement,
            setUnion

Extensions: setEquals,
            addElement,
            setUnion,
            removeElement,
            setIntersection,
            setDifference
-}

-- | Returns the empty set.
-- Balanced tree: best O(1), worst O(1)
-- Any tree:      best O(1), worst O(1)
emptySet :: Set a
emptySet = Set Null

-- | The number of elements in a set.
-- Balanced tree: best O(log n), worst O(log n)
-- Any tree:      best O(n),     worst O(n)
setSize :: (Integral b) => Set a -> b
setSize (Set tree) = treeSize tree

treeSize :: (Integral b) => BinaryTree a -> b
treeSize = undefined

-- | Checks if an element is present in a set.
-- Balanced tree: best O(log n), worst O(log n)
-- Any tree:      best O(1),     worst O(n)
--
-- >>> containsElement (addElement 3 emptySet) 3
-- True
-- >>> containsElement emptySet 3
-- False
containsElement :: (Ord a) => Set a -> a -> Bool
containsElement (Set tree) = elemBSTree tree

elemBSTree :: (Ord a) => BSTree a -> a -> Bool
elemBSTree = undefined

-- | Equality on sets.
-- ([1,2,3] represents the same set as [3,2,1])
-- Balanced tree: best O(n log n), worst O(n log n)
-- Any tree:      best O(n),       worst O(n^2)
--
-- >>> setEquals emptySet (emptySet :: Set Int)
-- True
-- >>> setEquals (addElement 1 emptySet) (addElement 1 emptySet)
-- True
setEquals :: (Ord a) => Set a -> Set a -> Bool
setEquals = undefined

-- | Adds an element to a set, if it does not already exist.
-- Balanced tree: best O(log n), worst O(log n)
-- Any tree:      best O(1),     worst O(n)
--
-- >>> containsElement (addElement 5 emptySet) 5
-- True
addElement :: (Ord a) => a -> Set a -> Set a
addElement = undefined

-- | Computes the union of two sets.
-- Balanced tree: best O(n log n), worst O(n log n)
-- Any tree:      best O(n),       worst O(n^2)
--
-- >>> setEquals (setUnion (addElement 1 emptySet) (addElement 2 emptySet)) (addElement 2 (addElement 1 emptySet))
-- True
setUnion :: (Ord a) => Set a -> Set a -> Set a
setUnion = undefined

-- =================================
-- Functions below are extensions
-- =================================

-- | Removes an element from a set, if it is present.
-- Balanced tree: best O(log n), worst O(log n)
-- Any tree:      best O(1),     worst O(n)
removeElement :: (Ord a) => a -> Set a -> Set a
removeElement = undefined

-- | Computes the intersection of two sets.
-- Balanced tree: best O(n log n), worst O(n log n)
-- Any tree:      best O(n),       worst O(n^2)
setIntersection :: (Ord a) => Set a -> Set a -> Set a
setIntersection = undefined

-- | Computes the set difference (elements in first set but not second).
-- Balanced tree: best O(n log n), worst O(n log n)
-- Any tree:      best O(n),       worst O(n^2)
setDifference :: (Ord a) => Set a -> Set a -> Set a
setDifference = undefined
