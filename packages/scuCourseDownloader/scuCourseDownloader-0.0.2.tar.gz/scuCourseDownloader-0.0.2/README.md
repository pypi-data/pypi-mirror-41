# 四川大学课表器api
<p>
<img src='https://img.shields.io/badge/author-%E5%B0%8F%E5%B7%9D-ff69b4.svg'>
<img src='https://img.shields.io/github/license/2239559319/courseDownload.svg?style=flat'>
<img src='https://img.shields.io/badge/python-3.0%2B-blue.svg'>
<img src='https://img.shields.io/badge/python-3.6-blue.svg'>
</p>

-------------

## 运行环境:python3.6
```bash
# 需要第三方模块，包：requests,lxml,openpyxl
#如果是anaconda环境用conda命令
pip install lxml
pip install requests
pip install openpyxl
```
## 使用
```bash
# 安装
pip install scuCourseDownloader
# 卸载
pip uninstall scuCourseDownloader
```
```python
#使用示例
import scuCourseDownloader

scuCourseDownloader.save_to_excel("2018-2019-2-1")
```

## 注意:

 - save_to_excel,query函数参数的格式为 2018-2019-2-1，表示18年到19年第二学期
 格式必须严格按以上格式
 - 程序运行完后会在当前目录在生成一个course.xlsx文件，就是课表文件了
 - 由于没有采用并发且请求频率限制问题，程序的运行时间大概在10分钟左右，建议做点其他事哦
 -----------------
 bug,程序交流请发邮件到:w2239559319@outlook.com