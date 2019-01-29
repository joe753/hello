//No2
var s1 = db.Singer.findOne({name: 'singer1'})
s1.album = [1,2,3]
db.Singer.save(s1)