import sys , os 
from subprocess import call


print '*==*==*==*==*==*==*==*==*==*==*==* | R3K1NG |*==*==*==*==*==*==*==*==*==*==*==*'
print '*                                                                             *'
print '*                              Special thanks TO:                             *'
print '*                                                                             *'
print '*                                 UNKNOWN TEAM                                *'
print '*                                                                             *'
print '*                                AND TEAM secures                             *'
print '*                                                                             *'
print '*                                                                             *'
print '*                             www.Github.Com/Goblinor                           *'
print '*                                                                             *'
print '*==*==*==*==*==*==*==*==*==*==*[telegram:R3K1NG]*==*==*==*==*==*==*==*==*==*==*'


bg = raw_input('BACKGROUND COLOR >')
BGI = raw_input('YOUR LOGO (IMAGE) > ')
width = raw_input(' IMAGE width > ')
height = raw_input('IMAGE height > ')
TITLE = raw_input('TITLE > ')
BGSONG = raw_input('your SONG > ')
TXT = raw_input('YOUR  TXT >')
FONT = raw_input('FONT COLOR > ')
TXT2 = raw_input('YOUR  TXT2 (Optional) >')
FONT2 = raw_input('FONT COLOR > ')
TXT3 = raw_input('YOUR  Contact Information (Optional) >')
FONT3 = raw_input('FONT COLOR > ')
OUTPUT = raw_input('OUTPUT Location > ')
os.chdir(OUTPUT)
with open('d9.html', 'w') as f:
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title>'+str(TITLE)+'</title>\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write('<Center>\n')
    f.write('<body bgcolor="'+bg+'">\n')
    f.write('<img src="'+BGI+'"width="'+width+'" height="'+height+'">\n')
    f.write('<p><font size="6" face="Monospace" color="'+FONT+'">'+TXT+'</font><p>\n')
    f.write('<p><font size="5" face="Monospace" color="'+FONT2+'">'+TXT2+'</font><p>\n')
    f.write('<p><font size="4" face="Monospace" color="'+FONT3+'">'+TXT3+'</font><p>\n')
    f.write('<audio  autoplay>\n')
    f.write('     <source src="'+BGSONG+'" type="audio/mpeg">\n')
    f.write('</audio>\n')
    #-------------------------------------------------------------------------------------#
    f.write('<marquee direction="left" scrollamount="2" scrolldelay="70" onmouseout="this.start();" onmouseover="this.stop();" behavior="scroll">\n')
    f.write('<a class="mainlinks" target="_blank">'+TXT3+'</a>\n')
    f.write('<span style="color:#0DFF00;font-weight:bold">'+TXT3+'</span>&nbsp;&nbsp;\n')
    f.write('<span style="color:#0DFF00;font-weight:bold">'+TXT3+' </span>&nbsp;&nbsp;\n')
    f.write('<a class="mainlinks" target="_blank">'+TXT3+'</a>\n')
    f.write('<span style="color:#0DFF00;font-weight:bold">'+TXT3+' </span>&nbsp;&nbsp;\n')
    f.write('<span style="color:#0DFF00;font-weight:bold">'+TXT3+' </span>&nbsp;&nbsp;\n')
    f.write('<a class="mainlinks" target="_blank" >'+TXT3+'</a>')
    f.write('    	 </marquee>\n')
    f.write('</div>')
    #-------------------------------------------------------------------------------------#
    f.write('</Center>\n')
    f.write('</body>\n')
    f.write('</html>')
    
