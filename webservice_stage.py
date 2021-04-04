from aws_cdk import core as cdk

from .pipeline_test4_stack import PipelineTest4Stack


class WebServiceStage4(cdk.Stage):
  def __init__(self, scope: cdk.Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    service = PipelineTest4Stack(self, 'WebService4')
