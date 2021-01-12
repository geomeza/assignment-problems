classifyNumber x = if x>0 then "nonnegative" else "negative"
main = putStrLn (classifyNumber 5)