## 图说理工

图说理工项目后台代码

| 环境 | Python3 |
| :---: | :---: |
| 依赖包 | 见 `TS_WHUT/requirements.txt` |
| 数据库 | MySQL |

## API文档

- [用户操作](#用户操作)
    - [登录状态获得用户信息](#登录状态获得用户信息)
    - [注册新用户](#注册新用户)
    - [删除用户](#删除用户)
    - [修改用户信息](#修改用户信息)
    - [登录](#登录)
    - [非登录状态获取用户信息](#非登录状态获取用户信息)
    - [登出](#登出)
    - [获取用户上传,下载记录,按照时间倒序](#获取用户上传_下载记录_按照时间倒序)
    - [获取用户一定数量下载的图片](#获取用户一定数量下载的图片)
    - [获取用户一定数量的上传图片](#获取用户一定数量的上传图片)
    - [查询粉丝名单](#查询粉丝名单)
    - [关注他人](#关注他人)
    - [取消关注](#取消关注)
    - [已关注哪些人](#已关注哪些人)
    - [判断是否登录](#判断是否登录)
    - [获取用户关注了多少人的数量](#获取用户关注了多少人的数量)
    - [获取粉丝数](#获取粉丝数)
    - [检索](#检索)
- [图片操作](#图片操作)
    - [上传图片](#上传图片)
    - [删除图片](#删除图片)
    - [获得一定数量的缩略图片_按时间倒序](#获得一定数量的缩略图片_按时间倒序)
    - [获取一定数量的缩略图片_按图片种类_时间倒序](#获取一定数量的缩略图片_按图片种类_时间倒序)
    - [获取一定数量的缩略图片_按图片格式_时间倒序](#获取一定数量的缩略图片_按图片格式_时间倒序)
    - [获取一定数量的缩略图片_按上传者_时间倒序](#获取一定数量的缩略图片_按上传者_时间倒序)
    - [登录状态下获取一定数量的已点赞的缩略图片](#登录状态下获取一定数量的已点赞的缩略图片)
    - [点赞某图片](#点赞某图片)
    - [取消点赞](#取消点赞)
    - [登录状态下获取一定数量的已收藏的缩略图片](#登录状态下获取一定数量的已收藏的缩略图片)
    - [收藏某图片](#收藏某图片)
    - [取消收藏](#取消收藏)
    - [获取轮播图](#获取轮播图)
    - [下载原图](#下载原图)
    - [通过图片id获取低质量图片](#通过图片id获取低质量图片)
- [其他](#其他)
    - [获取一定数量的类别名](#获取一定数量的类别名)

## 用户操作
### 登录状态获得用户信息
```
url:
    /user/
method:
    GET
success:
    status_code: 200
    json={
        "id": int,
        "username": str,
        "email": str,
        "gender": str, (male或female)
        "image": str, (url)
        "birthday": data,
        "upload_nums": int, (上传数)
        "fan_nums": int, (粉丝数)
        "follow_nums": int (关注者数)
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```
### 注册新用户
```
url:
    /user/
method:
    POST
params:
    *:username (formData)
    *:password (formData)
    *:email (formData)
success:
    status_code=200
    json={
        "status": "true",
        "message": "请前往邮箱验证"
    }
failure:
    status_code=400
    json={
        "error": "邮箱已被注册"
    }
failure:
    status_code=400
    json={
        "error": "用户名已经存在"
    }
```
### 删除用户
```
url:
    /user/
method:
    DELETE
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```
### 修改用户信息
```
url:
    /user/
method:
    PUT 
params:
    :username (formData)
    :email (formData)
    :image (formData)
    :gender (formData)
    :birthday (formData)
    :password (formData)
success:
    status_code: 200
    json={
        "status": "true"
    }
success:
    status_code: 200
    json={
        "status": "true",
        "message": "请前往邮箱验证"
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
failure:
    status_code: 400
    json={
        "error": "邮箱已经存在"
    }
failure:
    status_code: 400
    json={
        "error": "用户名已经存在"
    }
```
### 登录
```
url:
    /user/login/
method:
    POST
params:
    *:username (formData)
    *:password (formData)
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 400
    json={
        "error": "用户名或密码错误"
    }
failure:
    status_code: 404
    json={
        "error": "用户未激活"
    }
```
### 非登录状态获取用户信息
```
url:
    /user/msg/<username>/
method:
    GET
params:
    *:username (path)
success:
    status_code: 200
    json={
        "id": int,
        "username": str,
        "email": str,
        "gender": str, (male或female)
        "image": str, (url)
        "fan_nums": int,
        "follow_nums": int,
    }
failure:
    status_code: 400
    json={
        "error": "用户不存在"
    }
```
### 登出
```
url:
    /user/logout/
method:
    POST
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```
### 获取用户上传_下载记录_按照时间倒序
```
url:
    /user/history/
method:
    POST
params:
    *:num (formData)
success:
    status_code: 200
    json={
        "download_images":[
            {
            "id": int,
            "image": str, (url)
            "desc": str,
            "user": str,
            "pattern": str,
            "like": int,
            "collection": int,
            "cates": str,
            "height": int,
            "width": int,
            "download_nums": int
            }
        ],
        "upload_images":[
            {
            "id": int,
            "image": str, (url)
            "is_active": str,
            "desc": str,
            "user": str, (上传者用户名)
            "pattern": str, (格式)
            "like": int,
            "cates": str,
            "collection": int,
            "height": int,
            "width": int,
            "download_nums": int
            }
        ]
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```
### 获取用户一定数量下载的图片
```
url:
    /user/download
method:
    GET
params:
    *:num
success:
    status_code: 200
    json={
        "id": int,
        "image": str,
        "desc": str,
        "user": str,
        "pattern": str,
        "cates": str,
        "like": int,
        "collection": int,
        "height": int,
        "width": int,
        "download_nums": int,
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```
### 获取用户一定数量的上传图片
```
url:
    /user/upload
method:
    GET
params:
    *:num
success:
    status_code: 200
    json={
        "id": int,
        "image": str,
        "desc": str,
        "user": str,
        "pattern": str,
        "cates": str,
        "like": int,
        "collection": int,
        "height": int,
        "width": int,
        "download_nums": int,
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```
### 查询粉丝名单
```
url:
    /user/follow/
method:
    GET
success:
    status_code: 200
    json=[
        {
            "id": int,
            "username": str,
            "image": str, (url)
            "if_sign": str,
        },
    ]
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```
### 关注他人
```
url:
    /user/follow/
method:
    POST
params:
    *:id
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
```
### 取消关注
```
url:
    /user/follow/
method:
    DELETE
params:
    *:id
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
```
### 已关注哪些人
```
url:
    /user/following/
method:
    GET
success:
    status_code: 200
    json=[
        {
            "id": int,
            "username": str,
            "image": str, (url)
            "if_sign": str,
        },
    ]
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```
### 判断是否登录
```
url:
    /user/is_login/
method:
    GET 
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```
### 获取用户关注了多少人的数量
```
url:
    /user/follow/nums/
method:
    GET 
success:
    status_code: 200
    json={
        "num": int
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```
### 获取粉丝数
```
url:
    /user/fan/nums/
method:
    GET 
success:
    status_code: 200
    json={
        "num": int
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
```
### 检索
```
url:
    /search/
method:
    GET 
params:
    ：keywords(formData 关键字)
success:
    status_code: 200
    json={
        "id": int,
        "image": str,
        "desc": str,
        "cates": str,
        "user": str,
        "user_image": str, 
        "pattern": str,
        "like": int,
        "collection": int,
        "height": int,
        "width": int,
        "download_nums": int,
    }
failure:
    status_code: 400
    json={
        "error": "未找到相关图片"
    }
```
## 图片操作
### 上传图片
```
url:
    /image/
method:
    POST
params:
    :image (FILES)
    :desc (formData 描述)
    :cates (formData 分类字符串)
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
failure:
    status_code: 400
    json={
        "error": "没有图片文件"
    }
```
### 删除图片
```
url:
    /image/
method:
    DELETE
params:
    *:image-id (formData)
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
failure:
    status_code: 400
    json={
        "error": "没有图片文件"
    }
```
### 获得一定数量的缩略图片_按时间倒序
```
url:
    /image/
method:
    GET 
params:
    *:num (url)
    *:page (分页)
success:
    status_code: 200
    json=[
        {
            "id": int,
            "image": str,
            "desc": str,
            "cates": str,
            "user": str,
            "user_image": str, (用户头像)
            "pattern": str,
            "like": int,
            "collection": int,
            "height": int,
            "width": int,
            "download_nums": int
        }
    ]
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
```
### 获取一定数量的缩略图片_按图片种类_时间倒序
```
url:
    /image/cate/
method:
    GET 
params:
    *:num (url)
    *:page (分页)
success:
    status_code: 200
    json=[
        {
            "id": int,
            "image": str,
            "desc": str,
            "user": str,
            "cates": str,
            "pattern": str,
            "like": int,
            "collection": int,
            "height": int,
            "width": int,
            "download_nums": int
        }
    ]
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
```
### 获取一定数量的缩略图片_按图片格式_时间倒序
```
url:
    /image/pattern/
method:
    GET 
params:
    *:num (url)
    *:page (分页)
success:
    status_code: 200
    json=[
        {
            "id": int,
            "image": str,
            "desc": str,
            "user": str,
            "cates": str,
            "pattern": str,
            "like": int,
            "collection": int,
            "height": int,
            "width": int,
            "download_nums": int
        }
    ]
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
```
### 获取一定数量的缩略图片_按上传者_时间倒序
```
url:
    /image/user/
method:
    GET 
params:
    *:num (url)
    *:id (用户id)
    *:page (分页)
success:
    status_code: 200
    json=[
        {
            "id": int,
            "image": str,
            "cates": str,
            "desc": str,
            "user": str,
            "pattern": str,
            "like": int,
            "collection": int,
            "height": int,
            "width": int,
            "download_nums": int
        }
    ]
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
```
### 登录状态下获取一定数量的已点赞的缩略图片
```
url:
    /image/like/
method:
    GET 
params:
    *:num (url)
success:
    status_code: 200
    json=[
        {
            "id": int,
            "image": str,
            "desc": str,
            "user": str,
            "cates": str,
            "pattern": str,
            "like": int,
            "collection": int,
            "height": int,
            "width": int,
            "download_nums": int
        }
    ]
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
```
### 点赞某图片
```
url:
    /image/like/
method:
    POST
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
failure:
    status_code: 404
    json={
        "error": "图片未审查"
    }
```
### 取消点赞
```
url:
    /image/like/
method:
    DELETE 
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
```
### 登录状态下获取一定数量的已收藏的缩略图片
```
url:
    /image/collect/
method:
    GET 
params:
    *:num (url)
success:
    status_code: 200
    json=[
        {
            "id": int,
            "image": str,
            "desc": str,
            "cates": str,
            "user": str,
            "pattern": str,
            "like": int,
            "collection": int,
            "height": int,
            "width": int,
            "download_nums": int,
        }
    ]
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
```
### 收藏某图片
```
url:
    /image/collect/
method:
    POST
params:
    *:num (url)
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
failure:
    status_code: 404
    json={
        "error": "图片未审查"
    }
```
### 取消收藏
```
url:
    /image/collect/
method:
    DELETE
params:
    *:num (url)
success:
    status_code: 200
    json={
        "status": "true"
    }
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
```
### 获取轮播图
```
url:
    /image/banner/
method:
    GET
success:
    status_code: 200
    json=[
        "title": str,
        "image": str, (src的url)
        "target": str, (url)
        "index": int
    ]
```
### 下载原图
```
url:
    /image/download
method:
    GET
params:
    *:id (图片id)
success:
    status_code: 200
    json={
        "id": int,
        "image": str,
        "desc": str,
        "user": str,
        "pattern": str,
        "like": int,
        "user_image": str, (用户头像)
        "cates": str,
        "collection": int,
        "height": int,
        "width": int,
        "download": int (下载量)
    }
failure:
    status_code: 404
    json={
        "error": "参数错误"
    }
failure:
    status_code: 404
    json={
        "error": "用户未登录"
    }
failure:
    status_code: 404
    json={
        "error": "图片未审查"
    }
```
### 通过图片id获取低质量图片
```
url:
    /image/id
method:
    GET 
params:
    *:id
success:
    status_code: 200
    json= {
        "id": int,
        "image": str,
        "desc": str,
        "user": str,
        "pattern": str,
        "cates": str,
        "like": int,
        "collection": int,
        "height": int,
        "width": int,
        "download_nums": int,
    }
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
failure:
    status_code: 404
    json={
        "error": "图片未审查"
    }
```
## 其他
### 获取一定数量的类别名
```
url:
    /cates/
method:
    GET
params:
    *:num
success:
    status_code: 200
    json=[
        str (种类名)
    ]
failure:
    status_code: 400
    json={
        "error": "参数错误"
    }
```
