import requests
#import sox
import os



os.environ["PYTHONIOENCODING"] = "UTF-8"
def test(file):

	files = {'audio_file' : open(file,'rb')}
	data = {'user_id':'bcHimBGrYqmjhLvXUvpfucZ9UtWbWhLp','token':'108797079642531502739912695442685342960457477775982160857960325149446013770090853503684800077368095705856631023415325580516278764101043774616084683939399461544979475618965833766928208952940673916241863678113041464396653732876307815673032576648401970876173340706901671237303677613092583215857645137057228991969','file_format':'mp3','language':'kan'}

	url = 'http://35.192.52.211/api/upload'
	res = requests.post(url,data=data,files = files)
	print(res._content.decode('UTF-8'))
	#print(file)



#file_for_google('/Users/aakashravi/PycharmProjects/callcenterautomation/a.wav','/Users/aakashravi/PycharmProjects/callcenterautomation/a1.wav')
test('/Users/aakashravi/PycharmProjects/callcenterautomation/chamraj_10.wav')

#

#flatworld1@gubagoo.com
#Flatworld123
