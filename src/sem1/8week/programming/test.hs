import Data.List ((\\))

getIncrementList :: Int -> [Int]
getIncrementList n = reverse (incrementListAcc n [])
  where
    incrementListAcc n list
      | n > 0 = n : incrementListAcc (n - 1) list
      | otherwise = list

allCoords (x, y) = include 1 (replicate x (getIncrementList y))
  where
    include n list
      | length (list) > 0 = (map (\x -> (x, n)) (list !! 0)) ++ (include (n + 1) (drop 1 list))
      | otherwise = []

data Direction = North | South | East | West
  deriving (Show, Eq)

data Food = Food Location Int | NoFood
  deriving (Show, Eq)

type Location = (Int, Int)

type Dimensions = (Int, Int)

data Snake = Snake Location Direction [Direction]
  deriving (Show, Eq)

data Habitat
  = Habitat Dimensions Int Food Snake

getBodyCoords :: Location -> [Direction] -> [Location]
getBodyCoords (x, y) list
  | length list > 0 = case (list !! 0) of
      North -> (x, y + 1) : (getBodyCoords (x, y + 1) (drop 1 list))
      South -> (x, y - 1) : (getBodyCoords (x, y - 1) (drop 1 list))
      East -> (x + 1, y) : (getBodyCoords (x + 1, y) (drop 1 list))
      West -> (x - 1, y) : (getBodyCoords (x - 1, y) (drop 1 list))
  | otherwise = []

isValidSnake :: Habitat -> Bool
isValidSnake (Habitat dim _ _ (Snake l dir list))
  | elem l (getBodyCoords l list) = False -- collidedwithself
  | not (elem l (allCoords dim)) = False -- left the habitat
  | null list = True -- boilerplate cause haskell is trash
  | dir == (list !! 0) = False -- facing 180
  | otherwise = True

turn :: Direction -> Habitat -> Habitat
turn moveDir (Habitat _1 _2 _3 (Snake l dir list))
  | elem (moveDir, dir) invalidTurns = Habitat _1 _2 _3 (Snake l dir list)
  | otherwise = Habitat _1 _2 _3 (Snake l moveDir list)
  where
    invalidTurns = [(North, South), (South, North), (East, West), (West, East)]

checkEat :: Direction -> Habitat -> Habitat
checkEat tailDir (Habitat dim time (Food (a, b) n) (Snake (x, y) dir list))
  | (a, b) == (x, y) = (Habitat dim time (Food randomPos n) (Snake (x, y) dir (list ++ [tailDir])))
  | otherwise = (Habitat dim time (Food (a, b) n) (Snake (x, y) dir list))
  where
    validCoords = (allCoords (12, 12)) \\ ((getBodyCoords (x, y) list) ++ [(a, b)])
    randomPos = validCoords !! ((nextSeed time) `mod` (length validCoords))

stepMove (Habitat dim time (Food (a, b) n) (Snake (x, y) dir list))
  | True = case dir of
      North -> (Habitat dim (time + 1) (Food (a, b) (n - 1)) (Snake (x, y + 1) (list !! 0) (drop 1 list)))
      South -> (Habitat dim (time + 1) (Food (a, b) (n - 1)) (Snake (x, y - 1) (list !! 0) (drop 1 list)))
      East -> (Habitat dim (time + 1) (Food (a, b) (n - 1)) (Snake (x + 1, y) (list !! 0) (drop 1 list)))
      West -> (Habitat dim (time + 1) (Food (a, b) (n - 1)) (Snake (x - 1, y) (list !! 0) (drop 1 list)))

stepHabitat :: Habitat -> Habitat
stepHabitat (Habitat dim time (Food (a, b) n) (Snake (x, y) dir list)) = ans
  where
    ans = checkEat (last list) (stepMove (Habitat dim time (Food (a, b) n) (Snake (x, y) dir list)))

nextSeed :: Int -> Int
nextSeed s = (1103515245 * s + 12345) `mod` 2147483648
