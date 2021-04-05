import os

from aws_cdk import aws_codebuild as codebuild
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import core as cdk
from aws_cdk import pipelines

from .webservice_stage import WebServiceStage4


class PipelineStack4(cdk.Stack):
  def __init__(self, scope: cdk.Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    source_artifact = codepipeline.Artifact()
    cloud_assembly_artifact = codepipeline.Artifact()

    pipeline = pipelines.CdkPipeline(self, 'Pipeline4',
      cloud_assembly_artifact=cloud_assembly_artifact,
      pipeline_name='PipelineTest4',
      cross_account_keys=False, # NOTE save $1/month avoiding AWS KMS CMK
      self_mutating=True, # NOTE experiment failed with False

      # NOTE this codepipeline action is poorly named!
      # see https://github.com/aws/aws-cdk/issues/10632#issuecomment-702293070 for details
      source_action = cpactions.BitBucketSourceAction(
          connection_arn='arn:aws:codestar-connections:us-east-2:029003036509:connection/1ff00fef-3f27-4f35-b8ac-8ccdb2213f99',
          output=source_artifact,
          owner='jrobbins-LiveData',
          repo='pipeline-test4',
          branch='main',
          # code_build_clone_output=True, # works with False, also
          action_name="GitHub_V2_Source",
      ),

      synth_action=pipelines.SimpleSynthAction(
        source_artifact=source_artifact,
        cloud_assembly_artifact=cloud_assembly_artifact,
        install_command='npm install -g aws-cdk && pip install -r requirements.txt',
        # build_commands=['pytest unittests'],
        synth_command='cdk synth',
        environment=codebuild.BuildEnvironment(
            privileged=True,
            environment_variables={"BIBIM": codebuild.BuildEnvironmentVariable(value="BOP4_CONTAINER")},
            compute_type=codebuild.ComputeType.MEDIUM,
            build_image=codebuild.LinuxBuildImage.STANDARD_5_0)
      ))

    pipeline.add_application_stage(WebServiceStage4(self, 'Prod'))

