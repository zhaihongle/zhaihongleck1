id_card = {'name':'翟宏乐','age':19,'身份号':123456780987654322,'minzu':'汗','height':180,'weight':65}
print(id_card)
print(id_card["name"])
print(id_card.pop('weight'))
for i in id_card:
    print('%s:%s'%(i,id_card[i]))
