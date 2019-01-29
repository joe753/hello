var lst = []
for (var i=100; i <= 110; i++)
    lst.push(i)



db.Singer.update({name:'singer4'}, 
                    {
                     $addToSet: {albums : {$each : lst}
                                }
                    }
                 
)
db.Singer.find()