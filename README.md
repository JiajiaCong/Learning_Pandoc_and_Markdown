Pandoc
======

Pandoc for beginners

# 安装pandoc

安装pandoc的过程非常简单，google pandoc, 下载windows对应的安装文件。安装之后，可以在cmd中输入pandoc，若是出现了pandoc的exe，那么就是安装成功了。

# 使用pandoc

我使用sublime text写好了一个名为test.md的markdown, 下面想试试将其转化为其他的格式，尤其是pdf, doc, tex，html等。具体的说明在[pandoc的简要使用说明]（http://johnmacfarlane.net/pandoc/getting-started.html ）（需要特别注意的在markdown中写入url时，url结束后需要空一格，然后再写那半边括号），
这个官方文档中，但是是英语的，我翻译一下。

## 打开pandoc在windows中的终端

pandoc在windows中的终端称为PowerShell,我喜欢在cmd中输入powershell直接来找到。打开powershell。为了确定已经安装好了pandoc，可以再powershell中输入pandoc--version, 回车，会出现pandoc的一些相关信息。

## 获得和改变pandoc的工作目录

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

## 转换文档格式

- 首先进入到你想要转换的文档所在的目录下，输入ls命令，就可以看到该目录下的所有文件，比如我们想要将test.md转化为其他格式。
- markdown转为html，pandoc test.md -f markdown -t html -s -o test.html,这个命令将test.md转换为了test.html格式。想打开转换的html文件，输入.\test.html
- markdown转为text, pandoc test.md -f markdown -t latex -s -o test.tex,或者更简化的pandoc test.md -s -o test.tex,打开tex文档，输入.\test.tex。在markdown中无法控制字体和边距等，可以在转换后的tex文档中，添加一些命令来让文档变得更好一些。
- markdown转为word，pandoc test.md -f markdown -t docx -s -o test.docx，或者更简化的 pandoc test.md -s -o test.docx，打开word,输入.\test.docx
- markdown转为pdf, pandoc test.md -f markdown -t pdf -s -o test.pdf，或者更简化的 pandoc test.md -s -o test.pdf，打开pdf,输入.\test.pdf


# pandoc中寻求帮助

- 可以输入pandoc--help
- 另外，可以访问pandoc的使用文档，（http://johnmacfarlane.net/pandoc/README.html ）
- 需要注意的是，pandoc中其实有很多地方可以控制的，比如在文档格式转化中，可以控制的地方还是挺多的。等需要的时候，好好钻研一下使用文档。


# pandoc中进行文献和网页的应用


