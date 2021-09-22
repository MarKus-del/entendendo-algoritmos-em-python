# maior substring
if palavra_a[i] == palavra_b[j]:
  celula[i][j] = celula[i-1][j-1] + 1
else:
  celula[i][j] = max(celula[i-1][j], celula[i][j-1])