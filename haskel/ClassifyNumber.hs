ClassifyNumber x = if x > 0 then 'nonnegative' else 'negative'
main = putStrLn (ClassifyNumber 5)