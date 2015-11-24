module TicTacToe where

import Data.List.Extra
import Parser
import Utils

-- Size of the grid
n :: Int
n = 3

type Marking = Maybe Player
type Position = (Int, Int)

type Grid = [[Marking]]

strToPlayer :: String -> Player
strToPlayer "x" = X
strToPlayer "X" = X
strToPlayer "o" = O
strToPlayer "O" = O
strToPlayer "0" = O

-- An empty grid of size n x n.
emptyGrid :: Grid
emptyGrid = replicate n $ replicate n Nothing

replaceNth :: Int -> Marking -> [Marking] -> [Marking]
replaceNth n newVal (x:xs)
     | n == 0 = newVal:xs
     | otherwise = x:replaceNth (n-1) newVal xs

fillTheGrid :: [InternalMap] -> [Marking] -> Grid
fillTheGrid [] grid = chunksOf n grid
fillTheGrid (x:xs) grid =
    let
        pos1 = read (findParam x "x" "x not defined.") :: Int
        pos2 = read (findParam x "y" "y not defined.") :: Int
        player = findParam x "v" "player not defined."
        index = n * pos1 + pos2
        newGrid = replaceNth index (Just (strToPlayer player)) grid
    in fillTheGrid xs newGrid

firstAvailableMove :: Grid -> Player -> Grid
firstAvailableMove grid player = 
    let
        cGrid = concat grid
        (h:t) = findIndices (==Nothing) cGrid
    in chunksOf n (replaceNth h (Just player) cGrid)

randomMove :: Grid -> Player -> Int -> Grid
randomMove grid player seed = 
    let
        cGrid = concat grid
        list = findIndices (==Nothing) cGrid
        len = length list
        idx = seed `mod` len
        shuffledList = shuffle seed len list
        h = list !! (len-idx-1)
    in chunksOf n (replaceNth h (Just player) cGrid)


getWinSeqs :: Grid -> [[Marking]]
getWinSeqs grid = horizontal ++ vertical ++ [fDiag, bDiag]
  where horizontal = grid
        vertical = transpose grid
        fDiag = zipWith (!!) (reverse grid) [0..]
        bDiag = zipWith (!!) grid [0..]

winner :: String -> Maybe Char
winner map
    | winner' X  = Just 'x'
    | winner' O  = Just 'o'
    | otherwise = Nothing
    where
        grid = fillTheGrid (deserializeJson map) (concat emptyGrid)
        winner' :: Player -> Bool
        winner' player = any (all (== Just player)) $ getWinSeqs grid