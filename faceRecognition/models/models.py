from django.db import models


class BaseModel(models.Model):
    """ Base Model
    """
    created_at = models.DateTimeField(auto_now_add=True) # 作成日
    
    class Meta:
        abstract = True


class UploadImages(BaseModel):
    """ Upload Image
    """
    image_name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'uploadImage'
    
    def __str__(self):
        return self.image_name


class DetectResult(BaseModel):
    """ detect result
    """
    upload_image = models.ForeignKey(UploadImages, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'detectResult'

