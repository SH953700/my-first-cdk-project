from aws_cdk import core, aws_s3 as _s3


class MyCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="shilpabindra1",
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )
        #mybucketid is a logical identifier and not the name of the bucket
