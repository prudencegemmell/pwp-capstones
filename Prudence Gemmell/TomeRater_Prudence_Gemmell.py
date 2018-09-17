class DuplicateUserEmail(Exception):
	pass
	
class InvalidUserEmail(Exception):
	pass

class User(object):
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.books = {}

	def get_email(self):
		return self.email

	def change_email(self, address):
		self.email = address
		print('{user}\'s email has been updated.'.format(user = self.name))

	def __repr__(self):
		return 'User: {user}, email: {email}, books read: {books_read}'.format(user = self.name, email = self.email, books_read = len(self.books))

	def __eq__(self, other_user):
		if self.name == other_user.name and self.email == other_user.email:
			return True
		else:
			return False
		
	def read_book(self, book, rating = None):
		self.books[book] = rating
		
	def get_average_rating(self):
		total_rating = 0
		for value in self.books.values():
			if value != None:
				total_rating += value
		return total_rating/len(self.books)
		
		
class Book(object):
	def __init__(self, title, isbn):
		self.title = title
		self.isbn = isbn
		self.ratings = []
		
	def get_title(self):
		return self.title
		
	def get_isbn(self):
		return self.isbn

	def set_isbn(self, new_isbn):
		self.isbn = new_isbn
		print('{title}\'s ISBN has been updated'.format(title = self.title))

	def add_rating(self, rating):
		if rating != None:
			if rating >=0 and rating <= 4:
				self.ratings.append(rating)
			else:
				print('Invalid Rating')

	def __eq__(self, other_book):
		if self.title == other_book.title and self.isbn == other_book.isbn:
			return True
		else:
			return False

	def get_average_rating(self):
		total_rating = 0
		for value in self.ratings:
			if value != None:
				total_rating += value
		return total_rating/len(self.ratings)

	def __hash__(self):
		return hash((self.title, self.isbn))


class Fiction(Book):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		self.author = author
		
	def get_author(self):
		return self.author
		
	def __repr__(self):
		return '{title} by {author}'.format(title = self.title, author = self.author)


class NonFiction(Book):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		self.subject = subject
		self.level = level

	def get_subject(self):
		return self.subject

	def get_level(self):
		return self.level

	def __repr__(self):
		return '{title}, a {level} manual on {subject}'.format(title = self.title, level = self.level, subject = self.subject)
		
		
class TomeRater():
	def __init__(self):
		self.users = {}
		self.books = {}
		
	def create_book(self, title, isbn):
		book = Book(title, isbn)
		return book
	
	def create_novel(self, title, author, isbn):
		fiction = Fiction(title, author, isbn)
		return fiction
	
	def create_non_fiction(self, title, subject, level, isbn):
		non_fiction = NonFiction(title, subject, level, isbn)
		return non_fiction
	
	def add_book_to_user(self, book, email, rating = None):
		if not self.users[email]:
			print('No user with email {email}!'.format(email = email))
		else:
			self.users[email].read_book(book, rating)
			book.add_rating(rating)
			if book in self.books:
				self.books[book] += 1
			else:
				self.books[book] = 1
	
	def add_user(self, name, email, user_books = None):
		try:
			user = User(name, email)
			self.users[email] = user
			if user_books != None:
				for book in user_books:
					self.add_book_to_user(book, email)
		except DuplicateUserEmail:
			print('ERROR: Account already exists with this email.')
		except InvalidUserEmail:
			print('ERROR: Email does not exist.')
			
	def print_catalog(self):
		for key in self.books.keys():
			print(key)
	
	def print_users(self):
		for value in self.users.values():
			print(value)
	
	def get_most_read_book(self):
		max_book = None
		max_count = 0
		for key, value in self.books.items():
			if value > max_count:
				max_count = value
				max_book = key
		return key
	
	def highest_rated_book(self):
		high_book = None
		high_count = 0
		for book in self.books.keys():
			if book.get_average_rating() > high_count:
				high_count = book.get_average_rating()
				high_book = book
		return high_book
	
	def most_positive_user(self):
		high_user = None
		high_count = 0
		for user in self.users.values():
			if user.get_average_rating() > high_count:
				high_count = user.get_average_rating()
				high_book = user
		return high_user