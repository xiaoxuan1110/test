import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='汉字谜盒')
#挂载静态文件的存放目录
#app.mount("/static", StaticFiles(directory="static"), name="static")
#第一个是输出的URL前缀，没有的mount会404.第二个是静态文件存放的具体目录名字，最后一个是FASTAPI内部使用的名字
@app.get("/")
def root():
    print("访问项目首页",flush=True)
    return FileResponse('static/index.html')

#1新建游戏=新建会话
#2 中间就是AI交互
#3 左侧会话列表查询
#4 点击左侧展示会话信息
#5 点击叉号删除会话
#





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


