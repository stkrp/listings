lst = [1, 2, 3, 4, 5, 6, 7]
dct = {'a': 4, 'b': 5}
st = {6, 7, 8}

print(lst, dct, st, sep='\n')

# L.pop([index]) -> item -- remove and return item at index (default last).
# Raises IndexError if list is empty or index is out of range.
a1 = lst.pop()
a2 = lst.pop(-2)
a3 = lst.pop(2)
# a4 = lst.pop(-1000)  # Error

print(a1, a2, a3)

# L.insert(index, object) -- insert object before index
lst.insert(len(lst), 1002)
lst.insert(-1, 1001)
lst.insert(100, 1003)
print(lst)

# L.append(object) -> None -- append object to end
lst.append(lst.pop())
lst.append(2000)
print(lst)

print(dct)
# D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
# If key is not found, d is returned if given, otherwise KeyError is raised
b = dct.pop('a')
print(b, dct)

# D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
c1 = dct.get('a')
c2 = dct.get('a', -1)
c3 = dct.get('b')
print(c1, c2, c3, dct)

print(st)
# Remove and return an arbitrary set element.
# Raises KeyError if the set is empty.
d = st.pop()
# Add an element to a set.
# This has no effect if the element is already present.
st.add(9)
print(d, st)