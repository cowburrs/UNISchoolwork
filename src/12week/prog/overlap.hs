type Center = (Double, Double)

type Radius = Double

type Width = Double

type Height = Double

type Rotation = Double

data Circle = MakeC Center Radius

data Rectangle = MakeR Center Width Height Rotation

testCircle :: Circle
testCircle = MakeC (0.0, 0.0) 1.0

testSquare :: Rectangle
testSquare = MakeR (0.0, 0.0) 1.0 1.0 0.0

-- | Check whether a rectangle and circle overlap.
--
-- Examples:
--
-- >>> overlapRectCirc (MakeR (3.2,4.4) 9.0 1.7 0.17) (MakeC (8.8,10.0) 4.3)
-- True
--
-- >>> overlapRectCirc (MakeR (3.2,4.4) 9.0 1.7 0.12) (MakeC (8.8,10.0) 4.3)
-- False
--
-- >>> overlapRectCirc (MakeR (3.2,4.4) 9.0 1.7 0.17) (MakeC (2.5,10.0) 4.5)
-- False
--
-- >>> overlapRectCirc (MakeR (3.2,4.4) 9.0 1.7 0.17) (MakeC (2.5,10.0) 4.9)
-- True
--
-- >>> overlapRectCirc (MakeR (3.2,4.4) 9.0 1.7 0.4) (MakeC (5.0,5.3) 0.6)
-- True
--
-- >>> overlapRectCirc (MakeR (3.2,4.4) 9.0 1.7 0.4) (MakeC (5.0,5.3) 8.9)
-- True
getRectanglePointsEqs (MakeR (x, y) w h r) = r

getNearestPointFromEq :: Double -> Double -> (Double, Double) -> (Double, Double)
getNearestPointFromEq m c (a, b) = (x, m * x + c)
  where
    x = (a + m * (b - c)) / (m ** 2 + 1)

-- overlapRectCirc :: Rect -> Circ -> Bool
-- getRectanglePoints :: Rectangle -> [Center]
-- overlapRectCirc :: Rectangle -> Circle -> Bool
-- implement overlapRectCirc here
