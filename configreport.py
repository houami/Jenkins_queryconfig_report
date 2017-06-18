#/usr/bin/python
import glob
import re
list_file=glob.glob('/var/lib/jenkins/jobs/*/con*.xml')
count=len(list_file)
print "Number of jobs:" + str(count)
a=[]
scm=[]
no=[]
poll_b=[]
poll_b1=[]
poll_s=[]
# a will have individual xml files like a[0],a[1]
#iterating through the xml files
for ite in list_file:
    with open(ite) as f:
        content_xml=f.readlines()
        #tags
        content = [x.strip() for x in content_xml]
        st=''.join(str(y) for y in content)
        match= re.search("\'*.*.TimerTrigger",st)
        match_s=re.search("\'*.*.SCMTrigger",st)
#        poll_schedule=re.search(r'<spec>([^<]+?)<\/spec>',st)
        match_n=re.search(r"<triggers/>",st)
        if match:
            a.append(ite.split('/')[-2])
            spec = ''.join(re.findall('<spec>(.*?)<\/spec>', st))
            poll_b.append(spec)
        elif match_s:
            scm.append(ite.split('/')[-2])
            spec = ''.join(re.findall('<spec>(.*?)<\/spec>', st))
            poll_b1.append(spec)
        else:
            no.append(ite.split('/')[-2])


bt=list(zip(a,poll_b))
sc=list(zip(a,poll_b1))



temp=[16,26]
print "Number of jobs built periodically:" + str(len(a))
print "__" * 40
print "+++List of Build periodically jobs+++" + "__" * 40
for row in bt:
     print(" ".join("{0:{1}}".format(item, length) for item, length in zip(row, temp)))

print "__" * 40
print "Number of jobs with Poll SCM" + str(len(scm))
print "+++List of SCM jobs+++" + "__" * 40
for row in sc:
    print(" ".join("{0:{1}}".format(item, length) for item, length in zip(row, temp)))
