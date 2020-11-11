from djongo import models


class UserDetails(models.Model):
    usrId = models.TextField()
    usrName = models.TextField()
    usrFirstName = models.TextField()
    usrLastName = models.TextField()
    usrMail = models.EmailField()
    usrImage = models.ImageField()
    usrPassword = models.TextField()
    usrCreated = models.TimeField() #models.DateTimeField()

    def __str__(self):
        return self.usrName


class Blog(models.Model):
    blogId = models.TextField()
    blogHeading = models.TextField()
    blogContent = models.TextField()
    blogImage = models.ImageField(upload_to='BlogImage/')
    blogCreatorName = models.TextField()
    blogCreatorMail = models.EmailField()
    blogCreatorImage = models.ImageField(upload_to='BlogerImage/')
    blogLikedBy = models.ListField(default=[])
    blogDisLikeBy = models.ListField(default=[])
    blogComment = models.ListField(default={})
    blogLikeCount = models.IntegerField()
    blogDisLikeCount = models.IntegerField()
    blogPostTime = models.DateTimeField()

    def __str__(self):
        return self.blogId