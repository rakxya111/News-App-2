from django.db import models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampModel):
    
    name = models.CharField(max_length=100)

    def __str__(self):
            return self.name
    

class Tag(TimeStampModel):
    
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(TimeStampModel):
    
    STATUS_CHOICES = [
        ("active","Active"),
        ("inactive","Inactive"),
    ]
   
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d",blank=False)
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="active")
    published_at = models.DateTimeField(blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts")
    tag = models.ManyToManyField(Tag,related_name="posts")
    views_count = models.PositiveBigIntegerField(default=0)


    def __str__(self):
        return self.title

class Comment(TimeStampModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email} | {self.comment[:7]}"
    
class Contact(TimeStampModel):
    message = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class UserProfile(TimeStampModel):
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="user_images/%Y/%m/%d",blank=True)
    address = models.TextField(max_length=200)
    biography = models.TextField()
    
    def __str__(self):
        return self.user.username
    
class Newsletter(TimeStampModel):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email