import treepoem

def SaveBQCodetoFnm(codetype, val, fn):
  image = treepoem.generate_barcode(
    barcode_type=codetype,
    data=val,
    options=None
  )
  image.convert('1').save(fn)