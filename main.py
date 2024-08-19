def helper():
  counter = 0
  def _helper():
    nonlocal counter
    if counter>10:
      return
    counter = counter + 1
    _helper()
    
  _helper()
  print(counter)



helper()