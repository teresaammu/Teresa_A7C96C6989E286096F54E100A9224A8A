def lsp(product, target):
  indices = []
  for index, product in enumerate(product):
    if product == target:
      indices.append(index)
  return indices


product = ["shoes", "loafer", "shoes", "boots", "sandles", "shoes"]
target = "shoes"
result = lsp(product, target)
print(result)
target1 = "apples"
result1 = lsp(product, target1)
print(result1)