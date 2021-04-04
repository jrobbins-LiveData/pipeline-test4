#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from pipeline_test4.pipeline_test4_stack import PipelineTest4Stack
from pipeline_test4.pipeline_stack import PipelineStack4

app = cdk.App()

env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))

PipelineStack4(app, 'PipelineStack4', env=env)
PipelineTest4Stack(app, "PipelineTest4Stack", env=env)

app.synth()
