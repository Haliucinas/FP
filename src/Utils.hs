module Utils where

import System.Random
 
shuffle :: Int -> Int -> [a] -> [a]
shuffle seed 0   _  = []
shuffle seed len xs = 
        let
                n = fst $ randomR (0, len - 1) (mkStdGen seed)
                (y, ys) =  choose n xs
                ys' = shuffle seed (len - 1) ys
        in y:ys'
choose _ [] = error "choose: index out of range"
choose 0 (x:xs) = (x, xs)
choose i (x:xs) = let (y, ys) = choose (i - 1) xs in (y, x:ys)