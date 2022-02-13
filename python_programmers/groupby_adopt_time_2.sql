SET @h = -1;
SELECT @h:=@h+1 as hour, ( 
                          SELECT count(*)
                          FROM animal_outs
                          WHERE @h = hour(DATETIME)                               
                         ) as count
FROM animal_outs
WHERE @h < 23;