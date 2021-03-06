### 2019-05-17
1. 优化email模板，新增测试数据统计功能
2. 优化用例格式，新增前后置条件编写


### 2019-05-16
1. 新增自动生成随机测试数据功能


### 2019-05-14
1. 新增用例跳过功能


### 2019-05-13
1. 更新断言逻辑，新增断言Response指定字段长度
2. 更新落库校验逻辑，支持多字段断言
3. 更新部分文档


### 2019-05-09
1. 修复部分参数文件&配置文件错误
2. 重构部分代码
3. 数据库操作由Mysql改为Sqlserver
4. 增加数据落库校验
5. SQL语句使用Yaml文件编写
6. TODO 代码与校验逻辑待优化，暂只支持一个字段的落库校验


### 2019-03-27
1.完成关联参数配置


### 2019-03-22
1.用例管理文件格式变更为Yaml  json.load =》yaml.load，方便contextor更优雅的实现传参方式
2.添加res_index方便动态传参，保存入临时变量文件(用例执行完自动回溯)
```text
用例中的变量名以{临时变量文件名}的方式书写
1. 用例编写文件目录cases，生成临时yaml用例文件目录caseAll, test_cases根据caseAll自动生成py用例文件，并执行
```

### 2018-12-26
1. 搭建travis-ci + coveralls
2. 使用 coverage
3. setup.py done


### 2018-12-24
1. 修改CustomRules文件代码,使Fiddler能自动保存会话进指定的目录
2. 分析录制接口文件并生成新的request的对象
3. 生成录制接口的用例数据对象, 运行逻辑采用之前的手动编写用例规则
4. 完成V1.3.0 TODO， 接口性能与用例模型待补充


### 2018-12-14
1. 完成Email模板，样式已调试完毕
2. 用例基本可跑批
3. 查看项目代码, 使用FIXME对待完善代码就行标签注释(共计14个TODO)


### V1.3.0 TODO
1. 对Fiddler进行改造使之能够完成接口录制功能，python对录制接口分析并自动运行


### V1.2.0 TODO
1. 使用locust库二次开发，完成接口性能测试


### V1.1.0 TODO
1. 测试模型设计并编写完毕
2. 服务器部署, 接入Jenkins, 持续集成


### V1.0.0 TODO
1. 项目配置层代码优化, 当前代码过于繁琐复杂
2. 测试用例的校验器设计[Response结构体分析->返回数据类型 code等多重断言]
3. 测试模板的重新定义, 使之功能更为全面
4. 测试阶段，编写用例测试，框架逻辑是否有所遗漏
5. 第一版本基本用例编写功能完成
6. 后期完善之前老代码，重构告警机制代码


### 2018-12-13
1. 完成用例的基本运行编写
2. 生成测试报告
3. 检查当前所有代码是否符合PEP8代码规范标准


### 2018-12-12
1. 测试模板设计与编写
2. 用例生成主体逻辑
3. Json文件用例编写设计
4. Https/Http关键字模块编写
5. 代码PEP8编码规范检查并修改


### 2018-12-11 以前的日志忘写了,写一下现阶段完成的Modules
1. Xml配置文件类, 配置层基本完成
2. Mysql操作类(本次使用Yaml文件管理数据操作), 包含一个装饰器, 业务数据层基本完成
3. 数据安全模式, 一个简单加密解密类
4. fp文件操作采用以前的代码
5. Excel操作类, 支持动态参数, 沿用先前的代码
6. 多层嵌套Json解析操作类
7. 日志操作类, 依旧沿用以前的代码
8. 时间日期方法, 沿用先前代码
9. 完善了代码风格与注释
10. 明确了代码的基本分层与风格
