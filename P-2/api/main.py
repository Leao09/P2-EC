from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing import List
from loggin_config import LoggerSetup

#Cria o logger para o módulo
logger_setup = LoggerSetup()
LOGGER = logger_setup.logger
app = FastAPI()

blog_posts = []

class BlogPost(BaseModel):
    id: int
    title: str
    content: str

@app.post('/blog')
async def create_blog_post(post: BlogPost = Body(default=None)):
    LOGGER.info({"message": "Creating a new blog post"})
    LOGGER.warning({"message": "Creating a new blog post"})
    blog_posts.append(post)
    return {'status': 'success'}

@app.get('/blog', response_model=List[BlogPost])
async def get_blog_posts():
    LOGGER.info({"message": "Reading all blogs post"})
    LOGGER.warning({"message": "Reading all blogs post"})
    return blog_posts

@app.get('/blog/{id}', response_model=BlogPost)
async def get_blog_post(id: int):
    LOGGER.info({"message": "Reading a blog post"})
    LOGGER.warning({"message": "Reading a blog post"})
    for post in blog_posts:
        if post.id == id:
            return post
    return {'error': 'Post not found'}

@app.delete('/blog/{id}')
async def delete_blog_post(id: int):
    LOGGER.info({"message": "Delete a blog post"})
    LOGGER.warning({"message": "Delete a blog post"})
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            return {'status': 'success'}
    return {'error': 'Post not found'}

@app.put('/blog/{id}')
async def update_blog_post(id: int, post: BlogPost = Body(default=None)):
    LOGGER.info({"message": "Update a blog post"})
    LOGGER.warning({"message": "Update a blog post"})
    for index, existing_post in enumerate(blog_posts):
        if existing_post.id == id:
            blog_posts[index] = post
            return {'status': 'success'}
    return {'error': 'Post not found'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)