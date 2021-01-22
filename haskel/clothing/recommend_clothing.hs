recommendClothing :: (RealFloat a) => a -> String  
recommendClothing degreeCelsius 
    | degreeFarenheight >= shortsleeve = "You should wear a shortsleeve"  
    | degreeFarenheight >= longsleeve = "You should wear a longsleeve"
    | degreeFarenheight >= sweater = "You should wear a sweater"
    | otherwise = "You should wear a jacket"
    where degreeFarenheight = degreeCelsius*(9/5) + 32
          shortsleeve = 80.0  
          longsleeve = 65.0
          sweater = 50.0
main = putStrLn (recommendClothing 30)