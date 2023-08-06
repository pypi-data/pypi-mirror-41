OSPLO: OneSentencePerLineOpener
===============================

- Viele Computerlinguistische Verfahren profitieren davon, wenn der Text im one-sentence-per line Format vorliegt (z.b die Erstellung von dünnbesetzten Scipy Matrizen für Dokument-Term Matrizen, oder auch einfach Textauswertungen bis hin zu dem Input Format für Gensim.

- Oft ist das nicht der Fall, und in vielen Fällen ist es zu speicherintensiv, ein komplettes Korpus einzulesen, um dann eine Tokenisierung und Satztrennung durchzuführen.

- OSPLO ist die naivste Lösung für dieses Problem.
Es greift auf smart_open (Mit dem man auch komprimierte Archive und auch Webressourcen öffnen kann) zurück und verwendet den sehr guten Tokenizer und Satzsplitter SoMaJo.
Das Endergebnis ist nicht besonders schnell, erlaubt aber direkte Iteration über eine Datei als wäre sie im One-Sentence-per-Line Format, ohne die Datei gleichzeitig einlesen zu müssen.

z.B:
```python
from osplo import OSLOpen
for sentence in OSLOpen("https://www.gnu.org/licenses/gpl.txt"): 
    print(sentence)
    
```
Die ersten Zeilen des Outputs würden dann so aussehen:

```
                                                                                                                                                                          
    GNU GENERAL PUBLIC LICENSE Version 3 , 29 June 2007 Copyright ( C ) 2007 Free Software Foundation , Inc. < https://fsf.org/> Everyone is permitted to copy and distribute verbatim copies of this license document , but changing it is not allowed .
    Preamble The GNU General Public License is a free , copyleft license for software and other kinds of works .
    The licenses for most software and other practical works are designed to take away your freedom to share and change the works .
    By contrast , the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users .
    We , the Free Software Foundation , use the GNU General Public License for most of our software ; it applies also to any other work released this way by its authors .
    You can apply it to your programs , too .
    When we speak of free software , we are referring to freedom , not price .
    Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software ( and charge for them if you wish ) , that you receive source code or can get it if you want it , that you can change the software or use pieces of it in new free programs , and that you know you can do these things .
    To protect your rights , we need to prevent others from denying you these rights or asking you to surrender the rights .
    Therefore , you have certain responsibilities if you distribute copies of the software , or if you modify it : responsibilities to respect the freedom of others .
    For example , if you distribute copies of such a program , whether gratis or for a fee , you must pass on to the recipients the same freedoms that you received .
    You must make sure that they , too , receive or can get the source code .
``` 


Hinweis:
Die Software ist unter GPL3.0 lizensiert, ist allerdings nur ein Demo-Projekt für die Nutzung von Packaging.
