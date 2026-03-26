from sqladmin import ModelView
from models import Category, Post

class CategoryAdmin(ModelView, model=Category):
    # These configuration flags tell SQLAdmin how to render the UI
    column_list = [Category.id, Category.name]
    column_searchable_list = [Category.name]
    column_sortable_list = [Category.id, Category.name]
    icon = "fa-solid fa-folder"

class PostAdmin(ModelView, model=Post):
    column_list = [Post.id, Post.title, Post.category, Post.is_published]
    column_searchable_list = [Post.title, Post.content]
    column_sortable_list = [Post.id, Post.is_published]
    column_default_sort = ("id", True)
    
    # Hide raw content column on the list view to save space
    column_details_exclude_list = []
    
    icon = "fa-solid fa-file-lines"
