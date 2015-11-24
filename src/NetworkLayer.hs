module NetworkLayer where

import Control.Concurrent
import Network.URI
import Network.HTTP
import Network.TCP as TCP
import Data.IORef
import Text.Printf
import TicTacToe
import Parser

data Req = GET_REQ | POST_REQ deriving (Show, Read, Eq)
nextReq GET_REQ = POST_REQ
nextReq POST_REQ = GET_REQ
getReq GET_REQ id = reqGET id
getReq POST_REQ id = reqPOST id

run id times = do
    conn <- TCP.openStream "tictactoe.homedir.eu" 80
    let firstMove = serializeScalaGrid $ concat $ randomMove emptyGrid X times
    listen conn id times 0 firstMove POST_REQ

updateURI id = case parseURI ("http://tictactoe.homedir.eu/game/" ++ id ++ "/player/1") of
    Just url -> url

reqGET id moves = Request { 
    rqURI = updateURI id :: URI, 
    rqMethod = GET :: RequestMethod, 
    rqHeaders = [
        Header HdrAccept "application/scala+list"
    ] :: [Header],
    rqBody = ""
}

reqPOST id moves = Request { 
    rqURI = updateURI id :: URI, 
    rqMethod = POST :: RequestMethod,
    rqHeaders = [
        Header HdrContentType "application/scala+list",
        Header HdrContentLength (show (length moves) :: String)
    ] :: [Header],
    rqBody = moves
}

listen h id times idx dat req =
    if idx < times then do
        rawResponse <- sendHTTP h (getReq req (id ++ (show idx)) dat)
        respBody <- getResponseBody rawResponse
        (x,_,_) <- getResponseCode rawResponse
        case x of
            2 -> do
                case req of
                    GET_REQ -> do
                        printf ">>: %s\n" respBody
                        case (winner respBody) of 
                            Just player -> listen h id times (idx+1) (serializeScalaGrid $ concat $ randomMove emptyGrid X (idx+1)) POST_REQ
                            _ -> do
                                let dat = serializeScalaGrid $ concat $ randomMove (fillTheGrid (deserializeScala respBody) (concat emptyGrid)) X idx
                                listen h id times idx dat (nextReq req)
                    POST_REQ -> do
                        printf "<<: %s\n" dat
                        case (length $ deserializeScala dat) of
                            9 -> listen h id times (idx+1) (serializeScalaGrid $ concat $ randomMove emptyGrid X (idx+1)) POST_REQ
                            _ -> do 
                                case (winner dat) of 
                                    Just player -> listen h id times (idx+1) (serializeScalaGrid $ concat $ randomMove emptyGrid X (idx+1)) POST_REQ
                                    _ -> listen h id times idx dat (nextReq req)
            _ -> do
                printf "%d - [%s]\n" idx respBody
                case respBody of
                    "Invalid game state" -> listen h id times (idx+1) (serializeScalaGrid $ concat $ randomMove emptyGrid X (idx+1)) POST_REQ
                    _ -> listen h id times idx dat req
    else return ()
