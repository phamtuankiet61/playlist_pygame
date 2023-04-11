import pygame
import webbrowser

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

	def open(self):
		webbrowser.open(self.link)

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

class Textbutton:
	def __init__(self, text, possition):
		self.text = text
		self.possition = possition

	def draw(self):
		font = pygame.font.SysFont('sans', 30)
		text = font.render(self.text, True, (0, 0, 0))
		self.text_box = text.get_rect()
		if self.is_mou_on_text():
			text = font.render(self.text, True, (0, 0, 255))
			pygame.draw.line(screen, (0, 0, 255), (self.possition[0], self.possition[1] + self.text_box[3]), (self.possition[0] + self.text_box[2], self.possition[1] + self.text_box[3]))
		else:
			text = font.render(self.text, True, (0, 0, 0))

		screen.blit(text, self.possition)

	def is_mou_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if (mouse_x > self.possition[0]) and (mouse_x < self.possition[0] + self.text_box[2]) and (mouse_y > self.possition[1]) and (mouse_y < self.possition[1] + self.text_box[3]):
			return True
		else:
			return False

def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video

def read_videos_from_txt(file):
	videos = []
	total = file.readline()
	for i in range(int(total)):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos

def read_playlist_txt(file):
	name = file.readline()
	description = file.readline()
	rating = file.readline()
	videos = read_videos_from_txt(file)
	playlist = Playlist(name, description, rating, videos)
	return playlist

def read_playlists_txt():
	playlists = []
	with open("bin.txt", "r") as file:
		total = file.readline()
		for i in range(len(total)):
			playlist = read_playlist_txt(file)
			playlists.append(playlist)
	return playlists


pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('Playlist Gui')
clock = pygame.time.Clock()
running = True

# loadata
playlists = read_playlists_txt()
video_bth_list = []
playlist_bth = []
playlist_choi = None
for i in range(len(playlists)):
	playlist = Textbutton(playlists[i].name.rstrip(), (50, 50+50*i))
	playlist_bth.append(playlist)

while running:
	clock.tick(60)
	screen.fill((255, 255, 255))
	for videos_bth in video_bth_list:
		videos_bth.draw()
	for play in playlist_bth:
		play.draw()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for i in range(len(playlist_bth)):
					if playlist_bth[i].is_mou_on_text():
						playlist_choi = i
						video_bth_list = []
						for j in range(len(playlists[i].videos)):
							video = Textbutton(playlists[i].videos[j].title.rstrip(), (300, 50+50*j))
							video_bth_list.append(video)
				if playlist_choi != None:
					for i in range(len(video_bth_list)):
						if video_bth_list[i].is_mou_on_text():
							playlists[playlist_choi].videos[i].open()
					
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()