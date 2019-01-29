for (let i = 1; i <= 10; i++){
                               db.Singer.update( {name:"singer" + i},
                                                 {
                                                     $inc: {likecnt : 1}
                                                 },true, true
                                   )
}