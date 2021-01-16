import json
import download_youtube_subtitle.common as common
import download_youtube_subtitle.main as download_youtube_subtitle
import argparse
import sys



def Get_Captions(args):

	filename = args.urls_filename
	rootdir = args.saved_folder

	# Load urls
	keyslist = []
	with open(filename) as file:
	    for l in file:
	        informations = l.strip().split(";")
	        keyslist.append((informations[4],informations[6]))


	# Load Captions
	errors = 0
	taille = str(len(keyslist))
	for idurl,(key,title) in enumerate(keyslist):
	    
	    tempfile = rootdir + "/ben_shapiro_" + key + ".json"
	    
	    print("")
	    print(idurl+1,"/",taille)
	    print("key : ",key)
	    print("title : ",title)
	    print("errors : ",str(errors))
	    print("")
	    
	    try:
	        test = download_youtube_subtitle.main(videoID = key,
	                                              output_file = tempfile,
	                                              save_to_file = True,
	                                              translation = False,
	                                              to_json = True,
	                                              caption_num = 0)
	    except:
	        errors = errors + 1

	return None




if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='test arguments')
	parser.add_argument('-f', '--urls_filename')
	parser.add_argument('-s','--saved_folder')
	args = parser.parse_args()
	Get_Captions(args)