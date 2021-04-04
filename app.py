#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from pipeline_test4.pipeline_test4_stack import PipelineTest4Stack


app = cdk.App()

env=core.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
PipelineTest4Stack(app, "PipelineTest4Stack", env)

app.synth()
