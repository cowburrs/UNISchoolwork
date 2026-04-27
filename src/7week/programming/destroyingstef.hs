-- | Find the median of two sorted arrays.
--
-- >>> findMedianSortedArrays [1,3] [2]
-- 2.0
--
-- >>> findMedianSortedArrays [1,2] [3,4]
-- 2.5
--
-- >>> findMedianSortedArrays [] [1]
-- 1.0
--
-- >>> findMedianSortedArrays [] [1,2]
-- 1.5
--
-- >>> findMedianSortedArrays [0,0] [0,0]
-- 0.0
--
-- >>> findMedianSortedArrays [] []
-- NaN
--
-- >>> findMedianSortedArrays [1,2,3] [4,5,6,7]
-- 4.0
-- findMedianSortedArrays :: [Int] -> [Int] -> Double
findMedianSortedArrays x y = helper x y []
  where
    helper [] [] returnlist = median returnlist
    helper [] (y : ys) returnlist = helper [] (ys) (y : returnlist)
    helper (x : xs) [] returnlist = helper xs [] (x : returnlist)
    helper (x : xs) (y : ys) returnlist
      | x >= y = helper (x : xs) (ys) (y : returnlist)
      | x < y = helper (xs) (y : ys) (x : returnlist)

median list = case mod (length (list)) 2 of
  0 -> ((fromIntegral (list !! (round ((fromIntegral (length list)) / 2) - 1))) + (fromIntegral (list !! (round ((fromIntegral (length list)) / 2)))))/2
  1 -> (fromIntegral (list !! (round ((fromIntegral (length list)) / 2) - 1))) * 1.1 / 1.1

-- 1 -> fromIntegral (list !! (round ((fromIntegral (length list)) / 2)))
