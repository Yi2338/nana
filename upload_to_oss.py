import oss2
import os

# 阿里云账号AccessKey拥有所有API的访问权限，风险很高。建议创建并使用RAM用户进行API访问
auth = oss2.Auth('your-access-key-id', 'your-access-key-secret')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'your-bucket-name')

def upload_directory(local_dir, oss_dir):
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            local_path = os.path.join(root, file)
            # 计算在OSS中的路径
            oss_path = os.path.join(oss_dir, file).replace('\\', '/')
            
            # 上传文件
            with open(local_path, 'rb') as fileobj:
                bucket.put_object(oss_path, fileobj)
            print(f"Uploaded {local_path} to {oss_path}")

# 上传视频文件
upload_directory('./static/videos', 'videos')
# 上传头像
upload_directory('./static/images', 'images') 