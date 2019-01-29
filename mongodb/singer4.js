//No4
db.Singer.update( 
                {name: 'singer1'},
        { 
            $unset : {likecnt : 1}
        }
)
db.Singer.find()
