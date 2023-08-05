# ----------------------------------------------------------------------------------------------------
# IBM Confidential
# OCO Source Materials
# 5900-A3Q, 5737-J33
# Copyright IBM Corp. 2018
# The source code for this program is not published or other-wise divested of its trade 
# secrets, irrespective of what has been deposited with the U.S.Copyright Office.
# ----------------------------------------------------------------------------------------------------

import unittest

from ibm_ai_openscale import APIClient, APIClient4ICP
from ibm_ai_openscale.engines import *
from ibm_ai_openscale.supporting_classes import *
from preparation_and_cleaning import *
from models.spark import CustomerSatisfaction
from datasets_classes import TelcoCustomerChurnDataset


class TestAIOpenScaleClient(unittest.TestCase):
    deployment_uid = None
    model_uid = None
    aios_model_uid = None
    scoring_url = None
    labels = None
    ai_client = None
    wml_client = None
    subscription = None
    test_uid = str(uuid.uuid4())
    transaction_id = None
    binding_uid = None

    model = CustomerSatisfaction()

    @classmethod
    def setUpClass(cls):
        cls.cos_resource = get_cos_resource()
        cls.bucket_names = prepare_cos(cls.cos_resource)
        TelcoCustomerChurnDataset.upload_to_cos(cls.cos_resource, cls.bucket_names['data'])

        cls.schema = get_schema_name()
        cls.aios_credentials = get_aios_credentials()
        cls.database_credentials = get_database_credentials()

        if "ICP" in get_env():
            cls.ai_client = APIClient4ICP(cls.aios_credentials)
        else:
            cls.ai_client = APIClient(cls.aios_credentials)
            cls.wml_credentials = get_wml_credentials()

        prepare_env(cls.ai_client)

    def test_01_setup_data_mart(self):
        TestAIOpenScaleClient.ai_client.data_mart.setup(db_credentials=self.database_credentials, schema=self.schema)

    def test_02_data_mart_get_details(self):
        details = TestAIOpenScaleClient.ai_client.data_mart.get_details()
        print(details)
        self.assertTrue(len(json.dumps(details)) > 10)

    def test_03_bind_wml_instance(self):
        if "ICP" in get_env():
            TestAIOpenScaleClient.binding_uid = self.ai_client.data_mart.bindings.add("WML instance on ICP",
                                                                                      WatsonMachineLearningInstance4ICP())
        else:
            TestAIOpenScaleClient.binding_uid = self.ai_client.data_mart.bindings.add("WML instance on Cloud",
                                                                                      WatsonMachineLearningInstance(
                                                                                          self.wml_credentials))

    def test_04_get_wml_client(self):
        TestAIOpenScaleClient.binding_uid = TestAIOpenScaleClient.ai_client.data_mart.bindings.get_uids()[0]
        TestAIOpenScaleClient.wml_client = TestAIOpenScaleClient.ai_client.data_mart.bindings.get_native_engine_client(
            self.binding_uid)

    def test_05_prepare_deployment(self):
        TestAIOpenScaleClient.model_uid, TestAIOpenScaleClient.deployment_uid = self.model.deploy_to_wml(
            self.wml_client)

        print("Model id: {}".format(self.model_uid))
        print("Deployment id: {}".format(self.deployment_uid))

    def test_06_subscribe(self):
        subscription = TestAIOpenScaleClient.ai_client.data_mart.subscriptions.add(WatsonMachineLearningAsset(
            TestAIOpenScaleClient.model_uid,
            #prediction_column='prediction',
            #probability_column='probability',
            #label_column='TotalCharges',
            problem_type=ProblemType.REGRESSION,
            input_data_type=InputDataType.STRUCTURED
        ))
        TestAIOpenScaleClient.aios_model_uid = subscription.uid

    def test_07_select_asset_and_get_details(self):
        TestAIOpenScaleClient.subscription = TestAIOpenScaleClient.ai_client.data_mart.subscriptions.get(TestAIOpenScaleClient.aios_model_uid)

    def test_08_list_deployments(self):
        TestAIOpenScaleClient.subscription.list_deployments()

    def test_09_score(self):
        TestAIOpenScaleClient.transaction_id = str(uuid.uuid4()).replace("-", "")
        print(TestAIOpenScaleClient.transaction_id)

        deployment_details = self.wml_client.deployments.get_details(TestAIOpenScaleClient.deployment_uid)
        scoring_endpoint = self.wml_client.deployments.get_scoring_url(deployment_details)

        payload_scoring = self.model.get_scoring_payload()
        print("Payload scoring:\n{}".format(payload_scoring))

        self.wml_client.deployments.score(scoring_endpoint, payload_scoring, transaction_id=TestAIOpenScaleClient.transaction_id)
        import time
        time.sleep(30)

    def test_10_setup_explainability(self):
        print(TestAIOpenScaleClient.subscription.payload_logging.get_table_content(format="python", limit=1))
        TestAIOpenScaleClient.subscription.explainability.enable(
            training_data_reference=BluemixCloudObjectStorageReference(
                get_cos_credentials(),
                self.bucket_names['data'] + '/WA_FnUseC_TelcoCustomerChurn.csv',
                first_line_header=True
            ),
            feature_columns=["gender", "SeniorCitizen", "PaymentMethod", "MonthlyCharges"],
            categorical_columns=["gender", "SeniorCitizen", "PaymentMethod"]
        )

    def test_11_get_explainability_details(self):
        TestAIOpenScaleClient.subscription.explainability.get_details()

    def test_12_run(self):
        TestAIOpenScaleClient.status = TestAIOpenScaleClient.subscription.explainability.run(
            transaction_id="{}-1".format(TestAIOpenScaleClient.transaction_id),
            background_mode=False
        )['entity']['status']

        pandas_df = TestAIOpenScaleClient.subscription.explainability.get_table_content()
        print(str(pandas_df))
        self.assertTrue(pandas_df.size > 1)
        self.assertTrue(TestAIOpenScaleClient.status == 'finished')

    def test_13_print_schema(self):
        TestAIOpenScaleClient.subscription.explainability.print_table_schema()
        TestAIOpenScaleClient.subscription.explainability.show_table()
        TestAIOpenScaleClient.subscription.explainability.describe_table()

    def test_14_disable_explainability(self):
        TestAIOpenScaleClient.subscription.explainability.disable()

    def test_15_get_metrics(self):
        print(TestAIOpenScaleClient.ai_client.data_mart.get_deployment_metrics())
        print(TestAIOpenScaleClient.ai_client.data_mart.get_deployment_metrics(deployment_uid=TestAIOpenScaleClient.deployment_uid))
        print(TestAIOpenScaleClient.ai_client.data_mart.get_deployment_metrics(subscription_uid=TestAIOpenScaleClient.subscription.uid))
        print(TestAIOpenScaleClient.ai_client.data_mart.get_deployment_metrics(asset_uid=TestAIOpenScaleClient.subscription.source_uid))
        print(TestAIOpenScaleClient.ai_client.data_mart.get_deployment_metrics(metric_type='quality'))

    def test_16_unsubscribe(self):
        self.ai_client.data_mart.subscriptions.delete(self.subscription.uid)

    def test_17_unbind(self):
        self.ai_client.data_mart.bindings.delete(self.binding_uid)

    @classmethod
    def tearDownClass(cls):
        print("Deleting DataMart.")
        cls.ai_client.data_mart.delete()


if __name__ == '__main__':
    unittest.main()
