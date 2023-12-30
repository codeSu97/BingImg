import os

from constant import IMG_PATH_4K


def upload_qiniu(access_key: str, secret_key: str, bucket_name: str, key: str) -> None:
    """
    上传图片到七牛云
    :param access_key: 七牛云 Access Key
    :param secret_key: 七牛云 Secret Key
    :param bucket_name: 七牛云存储空间名称
    :param key: 七牛云存储空间中的文件名
    :return: None
    """

    from qiniu import Auth, BucketManager, put_file

    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    # 查找该文件是否存在
    ret, _ = bucket.stat(bucket_name, key)
    if ret:
        bucket.delete(bucket_name, key)
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 30)
    # 要上传文件的本地路径
    put_file(token, key, IMG_PATH_4K, version="v2")


if __name__ == "__main__":
    access_key = os.environ["QINIU_ACCESS_KEY"]
    secret_key = os.environ["QINIU_SECRET_KEY"]
    bucket_name = os.environ["BUCKET_NAME"]
    key = os.environ["KEY"]
    upload_qiniu(access_key, secret_key, bucket_name, key)
