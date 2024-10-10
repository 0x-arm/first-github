class GitUser():
	def __init__(self, name, link):
		self.name = name
		self.link = link

	def about(self):
		return f'Nom d\'utilisateur : {self.name}\nLien du profil : {self.link}'

user = GitUser('0x-arm', 'https://github.com/0x-arm')

print(user.about())
