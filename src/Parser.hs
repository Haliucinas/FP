module Parser where

import Data.List.Extra

type InternalMap = [(String, String)]
data Player = X | O deriving (Show, Read, Eq)

playerToStr player =
    case player of
        Just X -> "x"
        Just O -> "o"

findParam :: InternalMap -> String -> String -> String
findParam map param errorMsg =
    case lookup param map of
        Just val -> val
        Nothing -> error errorMsg

stripElem :: String -> String -> String -> String
stripElem str elemPrefix errorMsg = 
    case stripPrefix (elemPrefix ++ "(") str of
        Just rest -> case stripSuffix ")" rest of
            Just rest -> rest
            Nothing -> error errorMsg
        Nothing -> error errorMsg

getMapInnards :: String -> InternalMap -> InternalMap
getMapInnards [] acc = acc
getMapInnards str acc =
    let 
        item = takeWhile (/= ',') str
        tuple = case (stripInfix "->" item) of
            Just (key, value) -> (key, value)
            Nothing -> error "Parser error."
        rest = drop (length item + 1) str
    in reverse $ getMapInnards rest (tuple : acc)

getMapElem :: String -> Maybe (String, String)
getMapElem [] = Nothing
getMapElem str =
    let 
        key = takeWhile (/= ')') str ++ ")"
        rest = drop (length key + 2) str
    in Just (key, rest)

parseList :: String -> [String] -> [String]
parseList [] acc = acc
parseList str acc =
    case getMapElem str of
        Just (key, rest) -> parseList rest (key : acc)
        Nothing -> error "Unknown error."

parseMaps :: [String] -> [InternalMap] -> [InternalMap]
parseMaps [] acc = acc
parseMaps (x:xs) acc =
    let
        striped = filter (/=' ') (stripElem x "Map" "Not a map.")
        parsed = getMapInnards striped []
    in parseMaps xs (parsed : acc)

serializeScalaMapInnards [] acc = acc
serializeScalaMapInnards (x:xs) acc =
    let
        xVal = findParam x "x" "x not defined."
        yVal = findParam x "y" "y not defined."
        player = findParam x "v" "v not defined."
        str = "Map(x -> " ++ xVal ++ ", y -> " ++ yVal ++ ", v -> " ++ player ++ ")"
    in serializeScalaMapInnards xs (str : acc)

serializeScalaGridInnards :: [Maybe Player] -> Int -> [String] -> [String]
serializeScalaGridInnards [] n acc = acc
serializeScalaGridInnards (x:xs) n acc =
    if x /= Nothing then let
        (xVal,yVal) = (divMod n 3)
        str = "Map(x -> " ++ (show xVal) ++ ", y -> " ++ (show yVal) ++ ", v -> " ++ (playerToStr x) ++ ")"
    in serializeScalaGridInnards xs (n+1) (str:acc)
    else serializeScalaGridInnards xs (n+1) acc

serializeScalaMap :: [InternalMap] -> String
serializeScalaMap map =
    let
        innards = intercalate ", " (reverse $ serializeScalaMapInnards map [])
    in "List(" ++ innards ++ ")"

serializeScalaGrid :: [Maybe Player] -> String
serializeScalaGrid list =
    let
        innards = intercalate ", " (reverse $ serializeScalaGridInnards list 0 [])
    in "List(" ++ innards ++ ")"

deserializeScala :: String -> [InternalMap]
deserializeScala str =
    let
        listInnards = stripElem str "List" "Not a list."
        parsedData = parseMaps (parseList listInnards []) []
    in parsedData