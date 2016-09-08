def books_n_mags(books, mags):
	print "you hav %d books" % int(books)
	print "you hav %d mags" % int(mags)

books_n_mags(5, 6)

print "---"

books_n_mags(5 + 10 + 20 - 9, 6 + 9 + 6 + 22)

print "---"

x = 77
y = 88
books_n_mags(x, y)

print "---"

books_n_mags(x + 1000, y + 2000)

print "---"

books_n_mags(raw_input(), raw_input())

print "---"

books_n_mags(raw_input("books> "), raw_input("mags> "))

print "---"

input_x = raw_input("books> ")
input_y = raw_input("mags> ")
books_n_mags(input_x, input_y)
