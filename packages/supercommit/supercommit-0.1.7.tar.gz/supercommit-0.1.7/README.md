# SuperCommit (git-sc)

`SuperCommit`是对Git命令的拓展，无侵入式的简化日常Git流程，于此同时也约束了代码规范。

# （一）环境依赖

* [SwiftLint](https://github.com/realm/SwiftLint)
* [Python3 (>= 3.5)](https://www.python.org/)

### 如果你已经配置完python环境，可以跳过本节

首先需要安装`Pyenv`:

```
brew install pyenv
```

通过`pyenv`安装`python3.6.1`(只要是大于3.5的版本都可以)。

```
pyenv install 3.6.1
pyenv rehash
```

随后将全局环境切换为`3.6.1`。

```
pyenv global 3.6.1
```

最后可以检查一下当前全局环境的`python`版本:

```
python --version
```

# （二）安装

```
pip install supercommit
```

# （三）使用

当安装完毕`supercommit`之后，提交代码的时候我们就可以需要`git commit`，取而代之的是`git sc`。

```
> git sc
```

之后您会看到如下的画面:

![main](https://assets.souche.com/assets/sccimg/supercommit/main.png)

当你选择完成一个`commit`类型之后，`supercommit`将会提示您输入本次修改所涉及的模块，如果工程本身只有一个模块，那么你可以选择直接回车跳过。

![module](https://assets.souche.com/assets/sccimg/supercommit/module-all.png)

之后你就可以填写`commit`信息了:

![](https://assets.souche.com/assets/sccimg/supercommit/commit.png)

> 注意，当你使用了一次`git sc`之后，该`Git`项目之后都会进行相关的规范检测，

# Lint

当`supercommit`发现本次提交所修改的文件包含合适的lint操作的时候，就会进行本地的lint。如果不通过，那么会强制要求进行修改。


![example](https://git.souche-inc.com/soucheclub/supercommit/raw/master/snapshot/lint-result.png)


# 进阶


## --no-lint

当然你也可以通过使用`--no-lint`flag来跳过本地的lint，但是这个方法不推荐使用。

## --bury

加上该flag之后，`supercommit`会强制更新lint规则以及本地的hook规则。

## --clip

该flag会使用lint工具对本地所追踪的改动（增量）进行自动修复，减少人工的修改。




# 可能遇到的问题

### 1. ZipImportError
<br />zipimport.ZipImportError: can't decompress data; zlib not available<br />![20190129101206.png](https://cdn.nlark.com/yuque/18/2019/png/167650/1548727937472-c94ed137-040e-4064-b6db-a86605c69685.png#align=left&display=inline&height=562&linkTarget=_blank&name=20190129101206.png&originHeight=852&originWidth=1130&size=198293&width=746)<br />解决方案：<br />安装zlib<br />10.14mojave以下系统
```
brew install zlib
```
for mojave:
```
sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
```
参考：https://stackoverflow.com/questions/23749530/brew-install-zlib-devel-on-mac-os-x-mavericks

