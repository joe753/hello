db.Singer.update({name : 'singer3'}, 
                  { 
                      $push : { albums : 10}
                  }
)

db.Singer.find()