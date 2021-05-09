import dns.resolver

lista=["A","NS","AAAA","SOA","MX","TXT"]

for c in lista:
  try:
    consulta=dns.resolver.query("google.cl",c)
    for i in consulta:
      print(i)
  except:
    print("No se pudo obtener la consulta")