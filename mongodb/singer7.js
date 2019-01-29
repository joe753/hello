db.Singer.update( {name : 'singer4'},
                  { 
                      $pull : {albums : 105}
                  }
)

db.Singer.find()