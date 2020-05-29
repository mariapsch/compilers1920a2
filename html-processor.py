import re
#Άνοιγμα του αρχικού αρχείου testpage.txt και εναπόθεση του περιεχομένου του στο string text
with open('testpage.txt', 'r', encoding = 'utf-8') as file: 
    text = file.read()

#Ερώτημα 1
rexptitle = re.compile(r'<title>(.*)</title>') #Κανονική έκφραση για ανάγνωριση  οτιδήποτε είναι ανάμεσα σε <title> και</title>
for i in rexptitle.finditer(text):#Η finditer επιστρέφει ό,τι i ταιριάζει η κανονική έκφραση ψάχνοντας στο text με τη σειρά
    text = rexptitle.sub(i.group(1), text)#H sub επιστρέφει στο text ό,τι i ταιριάζει

#Ερώτημα 2
rexpsxolia = re.compile(r'<!.+?>')#Κανονική έκφραση για αναγνώριση οτιδήποτε είναι ανάμεσα σε <!--και-->
for i in rexpsxolia.finditer(text):
    text = rexpsxolia.sub('', text)#Κάθε i που ταιριάζει αντικαθιστάται με κενό στο text

#Ερώτημα 3
rexp3 = re.compile(r'<script.*?</script>|<style.*?</style>', re.DOTALL)#Κανονική έκφραση για αναγνώριση οτιδήποτε ανάμεσα σε <script> και </script> ή <style> και </style>.Χρήση του flag re.DOTALL για αναγνώριση και νέων γραμμών
for i in rexp3.finditer(text):
    text = rexp3.sub('', text)#Κάθε i που ταιριάζει αντικαθίσταται με κενό στο text

#Ερώτημα 4
rexpsynd = re.compile(r'<a.*? href="(.*)">.*</a>')#Κανονική έκφραση για αναγνώριση οτιδήποτε ανάμεσα σε <a και href και ανάμεσα σε href=" και "> και ανάμεσα σε > και</a>
for i in rexpsynd.finditer(text):
    text = rexpsynd.sub(i.group(1), text)#Στο text επιστρέφει μόνο ότι είναι ανάμεσα στα αυτάκια " "

#Ερώτημα 5
rexptag = re.compile(r'<.+?>', re.DOTALL)#Κανονική έκφραση για αναγνώριση το περιεχόμενο ανάμεσα σε < και >.Χρήση του flag re.DOTALL για να αναγνωρίζει και την αλλαγή σειράς
for i in rexptag.finditer(text):
    text = rexptag.sub('', text)#Στο text ό,τι ταιριάζει αντικαθίσταται με κενό

#Ερώτημα 6
def cb(i):                 #Ορισμός callback συνάρτησης για τις αντικαταστάσεις των html ονοτήτων με τους χαρακτήρες που δείχνει ο πίνακας της εκφώνησης
	if(i.group(0)=='&amp;'):
    		return '&'
	elif (i.group(0)=='&gt;'): 
		return '>'
	elif (i.group(0)=='&lt;'):
		return '<'
	elif (i.group(0)=='&nbsp;'):
		return ' '

rexpontothtwn = re.compile(r'(&amp;)|(&gt;)|(&lt;)|(&nbsp;)')#Κανονική έκφραση για την αναφνώριση των οντοτήτων &amp ή &gt ή &lt ή &nbsp
text = rexpontothtwn.sub(cb, text)#Στο text επιστρέφει ότι αντικαθιστά η cb στο text

#Ερώτημα 7
rexp7 = re.compile(r'\s+')#Κανονική έκφραση για αναγνώριση συνεχόμενων κενών
text = rexp7.sub(' ', text)#Στο text αντικαθίστανται τα συνεχόμενα κενά που ταιριάζουν με ένα κενό 

print(text) #Τύπωση του text όπως μετατράπηκε,δηλαδή μόνο των τίτλων,των συνδέσμων και των χαρακτήρων &,>,< και κενό
