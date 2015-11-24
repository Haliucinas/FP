import System.Environment
import System.IO
import System.Exit
import Control.Monad
import NetworkLayer

main :: IO ()
main = do
    args <- getArgs
    case args of
        [aString, aInteger] | [(n,_)] <- (reads aInteger :: [(Int, String)]) ->
            run aString n
        _ -> do
            name <- getProgName
            hPutStrLn stderr $ "usage: " ++ name ++ " <string> <integer>"
            exitFailure