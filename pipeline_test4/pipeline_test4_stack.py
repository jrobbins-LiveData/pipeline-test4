from os import path

import aws_cdk.aws_gatewayv2 as apigwv2
import aws_cdk.aws_lambda as lambda_
from aws_cdk import core as cdk


class PipelineTest4Stack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        this_dir = path.dirname(__file__)

        handler = lambda_.Function(self, 'Handler4',
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler='handler.handler',
            code=lambda_.Code.from_asset(path.join(this_dir, 'lambda')))          
            
        apigwv2.HttpApi(self, "HttpProxyApi4",
            default_integration=apigwv2.LambdaProxyIntegration(
                handler=handler
            )
        ))