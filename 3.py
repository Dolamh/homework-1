def main():
#التابع الرئيسي
    print('answer with yes or no')
    user=input('enter username: ')
    quiz(user)
def quiz(name):
    #التابع الخاص بالاسئلة
    #قائمة فارغة لوضع الأسطر من الملف بداخلها من أجل المعالجة
    l=[]
    #عداد الاجابات الصحيحة
    count=0
    #فتح ملف الأسئلة للقراءة منه
    q=open('questions.csv','r')
    #فتح ملف لكتابة النتيجة داخله
    res=open('answers.csv','w')
    
    for i in q:
        #تحويل كل سؤال من سلسلة محرفية إلى قائمة بعنصرين هما السئوال والجواب
        l1=i.rstrip().split(',')
        l.append(l1)
   # طباعة السؤال والسماح للمستخدم بإدخال الإجابة
    for i in l:
        print(i[0])
        ans=input().lower()
        #مقارنة الإجابة بالإجابة الموجودة ضمن الملف  
        if ans==i[1].lower():
            count+=1
            print('correct')
        else:
            print('incorrect')
    print(name)
    print('true answers is ',count,'from 20')
    #كتابة الاسم والنتيجة ضمن الملف
    res.write(name+'true answers is '+ str(count))
    q.close()
    res.close()
#استدعاء التابع الرئيسي
main()
