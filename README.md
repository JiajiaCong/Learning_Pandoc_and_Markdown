Pandoc & Markdown
======

for beginners like me

# 1. 安装pandoc

安装pandoc的过程非常简单，google pandoc, 下载windows对应的安装文件。安装之后，可以在cmd中输入pandoc，若是出现了pandoc的exe，那么就是安装成功了。

# 2. 使用pandoc

我使用sublime text写好了一个名为test.md的markdown, 下面想试试将其转化为其他的格式，尤其是pdf, doc, tex，html等。具体的说明在[pandoc的简要使用说明]（http://johnmacfarlane.net/pandoc/getting-started.html ）（需要特别注意的在markdown中写入url时，url结束后需要空一格，然后再写那半边括号），
这个官方文档中，但是是英语的，我翻译一下。

## 2.1 打开pandoc在windows中的终端

pandoc在windows中的终端称为PowerShell,我喜欢在cmd中输入powershell直接来找到。打开powershell。为了确定已经安装好了pandoc，可以再powershell中输入pandoc--version, 回车，会出现pandoc的一些相关信息。

## 2.2 获得和改变pandoc的工作目录

想要pandoc工作，必须让pandoc找到你文档所在的地方。这就涉及到如何修改pandoc的工作目录。有以下的一些命令，这些命令都是在powershell中操作的：

- 获得当前的工作目录，pwd
- 想要进入某个工作目录，如本人常用的markdown的工作目录，在powershell中输入 cd C:\Users\ms-off1\Dropbox\Markdown，就可以进入markdown的目录
- 回到上一级目录(one level up)，输入 cd ..
- 如果某个目录并不存在，你想要生成一个新的工作目录，就直接mkdir。比如现在的工作目录是C:\Users\ms-off1\Dropbox，如果输入mkdir  C:\Users\ms-off1\test，这样就会直接声称一个新的以前并不存在的test目录。但是只是新产生了一个新的工作目录而已，并没有改变当前的
工作目录，当前的工作目录仍旧是C:\Users\ms-off1\Dropbox
- 按住向上的方向键可以让你浏览以前的命令
- 输入一部分命令后，按住tab键可以自动补全
- 原文的总结如下
pwd (or echo %cd% on Windows) to see what the current working directory is.
cd foo to change to the foo subdirectory of your working directory.
cd .. to move up to the parent of the working directory.
mkdir foo to create a subdirectory called foo in the working directory.
up-arrow to go back through your command history.
tab to complete directories and file names.


## 2.3 转换文档格式
- 首先进入到你想要转换的文档所在的目录下，输入ls命令，就可以看到该目录下的所有文件，比如我们想要将test.md转化为其他格式。
- markdown转为html，pandoc test.md -f markdown -t html -s -o test.html,这个命令将test.md转换为了test.html格式。想打开转换的html文件，输入.\test.html
- markdown转为text, pandoc test.md -f markdown -t latex -s -o test.tex,或者更简化的pandoc test.md -s -o test.tex,打开tex文档，输入.\test.tex。在markdown中无法控制字体和边距等，可以在转换后的tex文档中，添加一些命令来让文档变得更好一些。
- markdown转为word，pandoc test.md -f markdown -t docx -s -o test.docx，或者更简化的 pandoc test.md -s -o test.docx，打开word,输入.\test.docx
- markdown转为pdf, pandoc test.md -f markdown -t pdf -s -o test.pdf，或者更简化的 pandoc test.md -s -o test.pdf，打开pdf,输入.\test.pdf


# 3. 区块引言

## 3.1 最简单的区块引言
区块可以是一行或者几行plain words，或者是一行或几行其他元素（如清单或者标题），可以通过行首由一个\> 符号加上一个空白作为开头来产生区块。一个偷懒的方式是，只要在引言区块的第一行行首输入\> 即可，后面几行的\>符号可以省略，但是不要通过空行进行断行，可以通过在行末添加空格来进行断行。

区块内可以通过＞＞来进行区块的嵌套。

需要的注意的是，在区块引言之前需要预留至少一个空白行。


## 3.2 保持原汁原味的区块引言，和latex中的verbatim环境类似
通过四个空白或者一个tab键进行开头的文字块，就会产生和latex verbatim类似的效果。


## 3.3 以\`开头和\`结尾的代码块 

通过至少三个 \` 开头和至少同一长度的 ` 结束，在这之间的代码就成为了代码块。


# 4. 行区块
|这是一个行区块的例子  
|  这也是一个行区块的例子  
|这仍是一个行区块的例子  
 这个也是可以的哦！    
|上面的例子很特殊 


# 5. 行内强调
以\*或者\_前后包住某一个或者某一段文字就会产生斜体，更强烈的强调可以采用**或者__包着算是强调。但是文字和符号之间不能有空格。

# 6. 删除线
以\~~和\~~包着的文字，会产生删除线，即文字上会产生删除的划线。

# 7. 上标和下标
下标用\~和\~夹着，h~2~o

上标用\^和\^夹着，2^3^=8


# 8. 添加图片
![图片标题]（图片所在的硬盘地址或者网络地址）

# 9. 添加脚注
脚注的格式如下：

这是一个脚注^[脚注内容]

# 10. 文内注释
这个例子来自下面的这个网址（http://celavie.me/lib/2013/10/19/Markdown%E5%86%99%E4%BD%9C%EF%BC%88%E4%BA%8C%EF%BC%89.html ）

    子曰[1]：“学[2]而时习[3]之，不亦说[4]乎？有朋[5]自远方来，不亦乐[6]乎？人不知[7]，而不愠[8]，不亦君子[9]乎？”
    [1] 子：中国古代对于有地位、有学问的男子的尊称，有时也泛称男子。《论语》书中“子曰”的子，都是指孔子而言。

    [2] 学：孔子在这里所讲的“学”，主要是指学习西周的礼、乐、诗、书等传统文化典籍。
    
    [3] 时习：在周秦时代，“时”字用作副词，意为“在一定的时候”或者“在适当的时候”。但朱熹在《论语集注》一书中把“时”解释为“时常”。“习”，指演习礼、乐；复习诗、书。也含有温习、实习、练习的意思。
    
    [4] 说：音ｙｕè，同悦，愉快、高兴的意思。
    
    [5] 有朋：一本作“友朋”。旧注说，“同门曰朋”，即同在一位老师门下学习的叫朋，也就是志同道合的人。
    
    [6] 乐：与说有所区别。旧注说，悦在内心，乐则见于外。
    
    [7] 人不知：此句不完整，没有说出人不知道什么。缺少宾语。一般而言，知，是了解的意思。人不知，是说别人不了解自己。
    
    [8] 愠：音ｙùｎ，恼怒，怨恨。
    
    [9] 君子：《论语》书中的君子，有时指有德者，有时指有位者。此处指孔子理想中具有高尚人格的人。
    
    为实现以上效果，在Markdown语法中应该这样写： 
    
      子曰<sup>[[1]](#[1])</sup>：“学<sup>[[2]](#[2])</sup>而时习<sup>[[3]](#[3])</sup>之，不亦说<sup>[[4]](#[4])</sup>乎？有朋<sup>[[5]](#[5])</sup>自远方来，不亦乐<sup>[[6]](#[6])</sup>乎？人不知<sup>[[7]](#[7])</sup>，而不愠<sup>[[8]](#[8])</sup>，不亦君子<sup>[[9]](#[9])</sup>乎？”
      
     <span id="[1]">[1]</span> 子：中国古代对于有地位、有学问的男子的尊称，有时也泛称男子。《论语》书中“子曰”的子，都是指孔子而言。
     
     <span id="[2]">[2]</span> 学：孔子在这里所讲的“学”，主要是指学习西周的礼、乐、诗、书等传统文化典籍。
     
     <span id="[3]">[3]</span> 时习：在周秦时代，“时”字用作副词，意为“在一定的时候”或者“在适当的时候”。但朱熹在《论语集注》一书中把“时”解释为“时常”。“习”，指演习礼、乐；复习诗、书。也含有温习、实习、练习的意思。
     
     <span id="[4]">[4]</span> 说：音ｙｕè，同悦，愉快、高兴的意思。
     
     <span id="[5]">[5]</span> 有朋：一本作“友朋”。旧注说，“同门曰朋”，即同在一位老师门下学习的叫朋，也就是志同道合的人。
     
     <span id="[6]">[6]</span> 乐：与说有所区别。旧注说，悦在内心，乐则见于外。 
     
     <span id="[7]">[7]</span> 人不知：此句不完整，没有说出人不知道什么。缺少宾语。一般而言，知，是了解的意思。人不知，是说别人不了解自己。
     
     <span id="[8]">[8]</span> 愠：音ｙùｎ，恼怒，怨恨。
     
     <span id="[9]">[9]</span> 君子：《论语》书中的君子，有时指有德者，有时指有位者。此处指孔子理想中具有高尚人格的人。


# 11. Pandoc Markdown 中进行文献的应用
想要进行文献的引用，首先应该在test.md的同一目录下具备两个东西，一是bib，一是csl文件（相当于latex中的ast文件，规定了文献的标注格式）。bib文件可以通过很多文献管理文件声称，csl文件可以通过以下两个网站找到很多不同格式的csl文件，[网站1]（https://zotero.org/styles ），[网站2]（https://github.com/citation-style-language/styles）

可以通过下面的命令来把markdown文件转化为pdf文件。

    pandoc -s -S --bibliography=test.bib --csl apa.csl  test.md -o test.pdf
    
好像-S是可以省略的，下面的命令也是可以成功的。
   
    pandoc -s --bibliography=test.bib --csl apa.csl test.md -o test.pdf

好像-s -S可以省略，下面的这个命令也是可以成功的。

    pandoc --bibliography=test.bib --csl apa.csl  test.md -o test.pdf
    
千万要记住，在markdown文本的最末尾要像latex一样说明一下我们使用的是哪个bib文件。比如使用的是test.bib, 所以要加上命令
   \bibliography{test.bib}

在文本中进行文献引用，有三种方式。

- 写法1：[@yangzhiping2001]，@符号后面直接写bib文件的引用文献的唯一编号，如yangzhiping2001.这样生成的格式是（yangzhiping,2001）
- 写法2：@yangzhiping2001，这种格式没有中括号，生成的格式是yangzhiping(2001)
- 写法3：如果有多個引用需要放在一起的話，需要用分號鏈接，[@Smith1990xh; @Smith1990ts]。如果是同一個作者的話，放心，pandoc會自動將他們声称成 (Smith, 1990a; 1990b) 


需要注意的是（目前这个问题我还没有弄得很清楚），pandoc markdown好像要求bib是UTF-8编码。并且，对于bib中出现的一些乱码，比如一些德国人名字，法国人名字中的特殊字符，如果在bib中没有很好的人工正确处理，在bib中是乱码，那么通过pandoc将markdown改编为pdf就会报错，往往不能成功。可以说在这一点上，pandoc markdown的兼容性比起latex还是差了不少，在我的印象中，latex的bib中即使有一些乱码，latex也能成功编译，只不过reference中显示的仍旧是乱码。


# 12. pandoc中寻求帮助

- 可以输入pandoc--help
- 另外，可以访问pandoc的使用文档，（http://johnmacfarlane.net/pandoc/README.html ）
- pandoc markdown的使用说明，有中文版，可以google一下，网址是 (http://pages.tzengyuxio.me/pandoc/ )
- 需要注意的是，pandoc中其实有很多地方可以控制的，比如在文档格式转化中，可以控制的地方还是挺多的。等需要的时候，好好钻研一下使用文档。


# 13. 使用Markdown来写邮件

chrome和火狐浏览器中都可以安装Markdown Here的插件。以gmail为例，在邮件正文采用markdown的格式写作。公式采用latex的格式，但是想要在邮件中显示公式就要在markdown选项中同意浏览器向谷歌发送请求，索要生成的公式的图片。如果没有同意这个，那么$\alpha+\beta$就不会被编译为数学公式。

写完邮件之后，可以鼠标右键，选择markdown转换。或者你可以采用markdown here的快捷键，我把快捷键设定为了ctrl+m. 这样采用markdown格式携程的邮件就会呈现漂亮的markdown形式啦！

需要注意一点，按一次ctrl+m，会把原文编译为markdown形式；再按一次ctrl+m就会又回到原文形式。一切的修改都要在原文中进行修改，切勿在markdown的显示下进行修改，这样修改好，按ctrl+m，修改的部分就会丢失。切记！

# 14. Markdown中含有中文时的编译
使用上述的命令来编译含有中文的markdown会报错，原因是pandoc默认选择的pdf引擎是pdflatex，而pdflatex是不支持中文的，因此会发生上述错误。因此在使用pandoc的时候，可以手动指明Latex引擎为xelatex，这是完全支持中文显示的。这样我们的命令就变成了:

    pandoc in.md -o out.pdf --latex-engine=xelatex
    
使用这个命令能够正常的编译出pdf文件，但是当你打开编译出来的pdf文件时，会发现其中的中文部分全是空白，这是字体的问题，因为Latex的默认字体是不支持中文的，因此我们可以继续修改命令：

    pandoc in.md -o out.pdf --latex-engine=xelatex -V mainfont=SimSun
其中mainfont参数是用来指明所使用的字体，SinSun表示的是宋体，你可以选择其他支持中文的字体。

但是这个命令还是有问题的，打开生成的pdf，你会发现其中的中文完全是没有断行的，这是因为pandoc本身对中文支持不够，但这不是说我们没有解决方案，解决方案是使用网友编辑好的latex模板来生成pdf，这里用到的是tzengyuxio提供的pm-template.latex4。 下载模板后将其中的LiHei Pro字体替换成系统中安装有的中文字体即可，然后编译命令改为

    pandoc in.md -o out.pdf --latex-engine=xelatex --template=pm-template.tex
这时就能生成一个比较完美的pdf文件了。这个pm-template.latex的模板下载地址是（https://github.com/tzengyuxio/pages/tree/gh-pages/pandoc ），将代码复制粘贴进一个tex文档，保存成tex文档，比如template.tex之后，将template.tex和要编译的markdown放在同一个目录下面就可以了。


# 14. vim中直接运行pandoc
比如我们要把test.md在vim中直接转成pdf，并且直接通过vim命令来打开。可以通过下面的命令来实现。

    :!pandoc test.md -s -o test.pdf  --latex-engine=xelatex --template=template.tex
    :!.\test.pdf
 这个！的意思是要在vim中运行cmd的命令，所以必须要加，不能省去。
 
 同样的方法可以将md转为其他的格式，语法和一般的pandoc语法是一样的，只是要在vim中加上:!这样一个表示vim命令状态（:），一个表示运行cmd的命令（！）。


# 15. pandoc的一些小技巧

- 如何强制断行？      
  就是在一行结束的时候，按两次空格或者更多的空格，再换行写下一行的命令（不用空一行），这样就会强制换行。
- 在vim中，多重的列表，每一级列表之间应该差一个tab的空格。

