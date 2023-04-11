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

def read_video():
	title = input("nhập title: ") + "\n"
	link = input("nhập link: ") + "\n"
	video = Video(title, link)
	return video

def print_video(video):
	print("video title: " + video.title, end = "")
	print("video link: " + video.link, end = "")

def read_videos():
	videos = []
	total_video = input("nhập video: ")
	for i in range(int(total_video)):
		print("video số: " + str(i+1))
		vid = read_video()
		videos.append(vid)
	return videos

def print_videos(videos):
	for i in range(len(videos)):
		print("video số " + str(i+1) + ":")
		print_video(videos[i])

def write_video_txt(video, file):
	file.write(video.title)
	file.write(video.link)
	
def write_videos_txt(videos, file):
	file.write(str(len(videos)) + "\n")
	for i in range(len(videos)):
		write_video_txt(videos[i], file)

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

def read_playlist():
	playlist_name = input("nhập name: ") + "\n"
	playlist_description = input("nhập description: ") + "\n"
	playlist_rating = input("nhập rating: ") + "\n"
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def write_playlist_txt(playlist):
	with open("bin.txt", "w") as file:
		file.write(playlist.name)
		file.write(playlist.description)
		file.write(playlist.rating)
		write_videos_txt(playlist.videos, file)
	print("Successfully write playlist to txt")
	
def read_playlist_txt():
	with open("bin.txt", "r") as file:
		name = file.readline()
		description = file.readline()
		rating = file.readline()
		videos = read_videos_from_txt(file)
		playlist = Playlist(name, description, rating, videos)
	return playlist

def print_playlist(playlist):
	print("------------")
	print("playlist name: " + playlist.name, end="")
	print("playlist desciption: " + playlist.description, end="")
	print("playlist rating: " + playlist.rating, end="")
	print_videos(playlist.videos)

def show_menu():
	print("Main menu: ")
	print("-----------------------------")
	print("| option 1: creat videos    |")
	print("| option 2: show videos     |")
	print("| option 3: play videos     |")
	print("| option 4: add videos      |")
	print("| option 5: updates videos  |")
	print("| option 6: delete videos   |")
	print("| option 7: save and exit   |")
	print("-----------------------------")

def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(prompt)
	choice = int(choice)
	return choice
	
def play_videos(playlist):
	print("------------------------")
	print_videos(playlist.videos)
	total = len(playlist.videos)
	choice = select_in_range("bạn muốn chơi video nào? (1-" + str(total) + "): "  , 1, total)
	print("Open video: " + playlist.videos[choice-1].title + "---" + playlist.videos[choice-1].link )
	playlist.videos[choice-1].open()

def add_video(playlist):
	new_title = input("nhập title mới: ") + "\n"
	new_link = input("nhập link mới: ") + "\n"
	video = Video(new_title, new_link)
	playlist.videos.append(video)
	return playlist

def update_playlist(playlist):
	print("Update playlist? ")
	print("1. Are you name: ")
	print("2. Are you description: ")
	print("3. Are you rating: ")
	choice = select_in_range("Enter what you want to update (1-3):", 1,3)

	if choice == 1:
		new_name = input("update name mới: ") + "\n"
		playlist.name = new_name
		print("Updated Successfully !")
		return playlist
	if choice == 2:
		new_discription = input("update discription mới: ") + "\n"
		playlist.description = new_discription
		print("Updated Successfully !")
		return playlist
	if choice == 3:
		new_rating = input("update rating mới: ") + "\n"
		playlist.rating = new_rating
		print("Updated Successfully !")
		return playlist

def delete_video(playlist):
	print_videos(playlist.videos)
	choice = select_in_range("you are delete video (1-" + str(len(playlist.videos)) + ")? " ,1 ,len(playlist.videos))
	del playlist.videos[choice-1]
	print("delete video susccesfully! ")
	return playlist

def main():
	try:
		playlist = read_playlist_txt()
		print("Loaded data successfully !!")
	except:
		print("Welcome firts user !!")

	while True:
		show_menu()
		choice = select_in_range("bạn chọn option nào (1-7): ", 1, 7)
		if choice == 1:
			playlist = read_playlist()
			input("\n Press enter continue. ")
		elif choice == 2:
			print_playlist(playlist)
			input("\nPress enter continue. ")
		elif choice == 3:
			play_videos(playlist)
			input("\nPress enter continue. ")
		elif choice == 4:
			playlist = add_video(playlist)
			input("\nPress enter continue. ")
		elif choice == 5:
			playlist = update_playlist(playlist)
			input("\nPress enter continue. ")
		elif choice == 6:
			playlist = delete_video(playlist)
			input("\nPress enter continue. ")
		else:
			write_playlist_txt(playlist)
			input("\n Press enter continue. ")
			break
			
main()