def find_ngrams(text, n, skip=None):

	from collections import Counter
	from nltk.tokenize import TweetTokenizer
	from nltk.util import skipgrams
	tokenizer = TweetTokenizer()

	##########stopwords#############
	from nltk.corpus import stopwords


	stop_words = list(set(stopwords.words('english')) )
	stop_words.extend(['̶ ','_','-','%','”',"’","'",'ur','v','vs','u',"I'm","i'm","i'll","I'll",' ', '-PRON-',".",'..','...',"'",";",'"','&','@','#','$','``','I','i','!','...',"'s",'It','it','Its','its','(',')','[',']','{','}',':','?','A','a',"'m",'..',',',"n't","'re","'ll","'ve",'-','ca','+','*','/'])
	stop_words.extend(['अंदर',u'अत',u'अदि',u'अप',u'अपना',u'अपनि',u'अपनी',u'अपने',u'अभि',u'अभी',u'आदि',u'आप',u'इंहिं',u'इंहें',u'इंहों',u'इतयादि',u'इत्यादि',u'इन',u'इनका',u'इन्हीं',u'इन्हें',u'इन्हों',u'इस',u'इसका',u'इसकि',u'इसकी',u'इसके',u'इसमें',u'इसि',u'इसी',u'इसे',u'उंहिं',u'उंहें',u'उंहों',u'उन',u'उनका',u'उनकि',u'उनकी',u'उनके',u'उनको',u'उन्हीं',u'उन्हें',u'उन्हों',u'उस',u'उसके',u'उसि',u'उसी',u'उसे',u'एक',u'एवं',u'एस',u'एसे',u'ऐसे',u'ओर',u'और',u'कइ',u'कई',u'कर',u'करता',u'करते',u'करना',u'करने',u'करें',u'कहते',u'का',u'कि',u'किंहें',u'किंहों',u'कितना',u'किन्हें',u'किन्हों',u'किया',u'किर',u'किस',u'किसि',u'किसी',u'किसे',u'की',u'कुछ',u'कुल',u'के',u'को',u'कोइ',u'कोई',u'कोन',u'कोनसा',u'कौन',u'कौनसा',u'गया',u'जब',u'जहाँ',u'जहां',u'जा',u'जिंहें',u'जिंहों',u'जितना',u'जिधर',u'जिन',u'जिन्हें',u'जिन्हों',u'जिस',u'जिसे',u'जीधर',u'जेसा',u'जेसे',u'जैसा',u'जैसे',u'जो',u'तक',u'तब',u'तरह',u'तिंहें',u'तिंहों',u'तिन',u'तिन्हें',u'तिन्हों',u'तिस',u'तिसे',u'तो',u'था',u'थि',u'थी',u'थे',u'दिया',u'द्वारा',u'न',u'नहिं',u'नहीं',u'ने',u'पर',u'पहले',u'पुरा',u'पूरा',u'पे',u'फिर',u'बनि',u'बनी',u'बहि',u'बही',u'बहुत',u'बाद',u'बाला',u'बिलकुल',u'भि',u'भितर',u'भी',u'भीतर',u'मगर',u'मानो',u'मे',u'में',u'यदि',u'यह',u'यहाँ',u'यहां',u'यहि',u'यही',u'या',u'यिह',u'ये',u'रखें',u'रवासा',u'रहा',u'रहे',u'ऱ्वासा',u'लिए',u'लिये',u'लेकिन',u'व',u'वगेरह',u'वरग',u'वर्ग',u'वह',u'वहाँ',u'वहां',u'वहिं',u'वहीं',u'वाले',u'वुह',u'वे',u'वग़ैरह',u'संग',u'सकता',u'सकते',u'सबसे',u'साथ',u'साबुत',u'साभ',u'सारा',u'से',u'सो',u'हि',u'ही',u'हुअ',u'हुआ',u'हुइ',u'हुई',u'हुए',u'हे',u'हें',u'है',u'हैं',u'हो',u'होता',u'होति',u'होती',u'होते',u'होना',u'होने'])    
	stop_words.extend(['outside','window','ke','ka','ki','bhi','aap','apna','apni','apne','abhi' ,'ko','koi','kon','konsa','gya','jab','jaha','ja','jinhe','jitna','jin','jis','jidhar','jaisa','jo','tak','tarah' ,'toh','tha','thi','the','diya' ,'pe','fir','bani','bohot','bahut','baad','bilkul','magar' ,'yadi','ya','rahe','liye' ,'lekin','waha','wahi','wale','sakta','sakte','sakti','sabse','sara','se','so','hi','hua','hui','hue','he','hai','hota','hoti','hote','hona','hone'])                           

	text=tokenizer.tokenize(text.lower())
	text=[x for x in text if x not in stop_words]

	if n==1:
		return Counter(text).most_common(100)
	else:

		if not skip:
			skip=1
		return Counter(list(skipgrams(text, n,skip))).most_common(100)

		
if __name__ == '__main__':
	print (find_ngrams("MY name is Yash",1,0))