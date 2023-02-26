import dict

def checkocc(line):
  Dict= dict.dict()
  for key in Dict:
  
    allocc1= Dict[key][0]
    allocc2= Dict[key][1]
  
    for i in allocc1:
        if (line.upper().find(i.upper())) !=-1:
          for j in allocc2:
            if (line.upper().find(j.upper())) !=-1:
              return line
            else:
              continue
        else:
          continue
  return('')
  