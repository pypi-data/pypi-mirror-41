# coding=utf-8
from __future__ import print_function
import argparse
import logging
import urllib3
from retry import retry
from outdated import warn_if_outdated

from watson_machine_learning_client import WatsonMachineLearningAPIClient
from ibm_ai_openscale_cli.lg_aios_client import AIOSClientLG
from ibm_ai_openscale_cli.ml_engines.watson_machine_learning.watson_machine_learning import WatsonMachineLearningEngine
from ibm_ai_openscale_cli.environments import Environments
from ibm_ai_openscale_cli.setup_classes.setup_env import setup_environment
from ibm_ai_openscale_cli.setup_classes.setup_services_cli import SetupIBMCloudServicesCli
from ibm_ai_openscale_cli.setup_classes.setup_services_rest import SetupIBMCloudServicesRest
from ibm_ai_openscale_cli.version import __version__
from ibm_ai_openscale_cli import logging_temp_file, name

from ibm_ai_openscale_cli.ml_engines.watson_machine_learning.models.drug_selection_model import DrugSelectionModel
from ibm_ai_openscale_cli.ml_engines.watson_machine_learning.models.german_credit_risk_model import GermanCreditRiskModel
from ibm_ai_openscale_cli.ml_engines.watson_machine_learning.models.scikit_digits_model import ScikitDigitsModel

logger = logging.getLogger(__name__)

def process_args():
    """Parse the CLI arguments

    Returns:
        dict -- dictionary with the arguments and values
    """

    parser = argparse.ArgumentParser()
    # required parameters
    requiredArgs = parser.add_argument_group('required arguments')
    requiredArgs.add_argument('-a', '--apikey', help='IBM Cloud APIKey', required=True)
    # Optional parameters
    optionalArgs = parser._action_groups.pop()
    parser.add_argument('--env', default='ypprod', help='Environment. Default "ypprod"', choices=['ypprod', 'ypqa', 'ys1dev', 'icp'])
    parser.add_argument('--resource-group', default='default', help='Resource Group to use. If not specified, then "default" group is used')
    parser.add_argument('--organization', help='Cloud Foundry Organization to use', required=False)
    parser.add_argument('--space', help='Cloud Foundry Space to use', required=False)
    parser.add_argument('--postgres', help='Path to postgres credentials file. If not specified, then the internal AIOS database is used')
    parser.add_argument('--icd', help='Path to IBM Cloud Database credentials file. If not specified, then the internal AIOS database is used')
    parser.add_argument('--db2', help='Path to IBM DB2 credentials file')
    parser.add_argument('--wml', help='Path to IBM WML credentials file')
    parser.add_argument('--username', help='ICP username. Required if "icp" environment is chosen')
    parser.add_argument('--password', help='ICP password. Required if "icp" environment is chosen')
    parser.add_argument('--url', help='ICP url. Required if "icp" environment is chosen')
    parser.add_argument('--datamart-name', default='aiosfastpath', help='Specify data mart name, default is "aiosfastpath"')
    parser.add_argument('--verbose', action='store_true', help='verbose flag')
    parser.add_argument('--version', action='version', version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('--bx', action='store_true', help=argparse.SUPPRESS)
    parser._action_groups.append(optionalArgs)

    # Optional parameters for LoadGenerator support
    lgArgs = parser._action_groups.pop()
    parser.add_argument('--lg_model', default='DrugSelectionModel', help='Default "DrugSelectionModel"', choices=['DrugSelectionModel','GermanCreditRiskModel','ScikitDigitsModel'])
    parser.add_argument('--lg_model_instance_num', default=1, help='Model instance number (default = 1)', type=int)
    parser.add_argument('--lg_score_requests', default=0, help='Number of score requests (default = 0)', type=int)
    parser.add_argument('--lg_scores_per_request', default=1, help='Number of scores per score request (default = 1)', type=int)
    parser.add_argument('--lg_explain_requests', default=0, help='Number of explain requests (default = 0)', type=int)
    parser.add_argument('--lg_max_explain_candidates', default=1000, help='Maximum number of candidate scores for explain (default = 1000)', type=int)
    parser.add_argument('--lg_explain_sync', action='store_true', help='User input initiates sending explain requests')
    parser.add_argument('--lg_pause', default=0.0, help='Pause in seconds between requests (default = 0.0)', type=float)
    parser.add_argument('--lg_verbose', action='store_true', help='Display individual request response times')
    parser.add_argument('--lg_checks', action='store_true', help='Trigger final fairness and quality checks')
    parser._action_groups.append(lgArgs)

    args = parser.parse_args()

    # validate environment
    if 'throw' in args:
        logger.error(args.throw)
        exit(1)

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.getLogger('handle_response').setLevel(logging.DEBUG)
        logging.getLogger('ibm_ai_openscale.utils.client_errors').setLevel(logging.DEBUG)

    warn_if_outdated(name, __version__)

    return args

def main():

    logger.info('ibm-ai-openscale-cli-{}'.format(__version__))
    logger.info('Log file: {0}'.format(logging_temp_file.name))

    args = process_args()

    if args.env == 'icp':
        logger.info('SSL verification is not used for requests in ICP Environment, disabling "InsecureRequestWarning"')
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    target_environment = Environments(args).getEnvironment()

    # setup IBM Cloud services and database
    ibm_cloud_services = None
    setup_environment(args, target_environment)
    if args.bx:
        ibm_cloud_services = SetupIBMCloudServicesCli(args, target_environment)
    else:
        ibm_cloud_services = SetupIBMCloudServicesRest(args, target_environment)
    aios_credentials = ibm_cloud_services.setup_aios()
    wml_credentials = ibm_cloud_services.setup_wml()
    postgres_credentials = ibm_cloud_services.setup_postgres_database()
    icd_credentials = ibm_cloud_services.setup_icd_database()
    db2_credentials = ibm_cloud_services.setup_db2_database()

    database_credentials = None
    if postgres_credentials is not None:
        database_credentials = postgres_credentials
    elif icd_credentials is not None:
        database_credentials = icd_credentials
    if db2_credentials is not None:
        database_credentials = db2_credentials

    # Instantiate ML Client, setup and deploy models
    model_instance_num = args.lg_model_instance_num
    if args.lg_model == 'DrugSelectionModel':
        model = DrugSelectionModel(target_environment, 0, model_instance_num)
    elif args.lg_model == 'GermanCreditRiskModel':
        model = GermanCreditRiskModel(target_environment, 0, model_instance_num)
    elif args.lg_model == 'ScikitDigitsModel':
        model = ScikitDigitsModel(target_environment, 0, model_instance_num)
    wml_engine = WatsonMachineLearningEngine(wml_credentials, target_environment, model)
    wml_model_deployment = wml_engine.get_existing_deployment()

    # AI Openscale operations
    logger.info('Use existing datamart {}'.format(args.datamart_name))
    aios_client = AIOSClientLG(aios_credentials, args.datamart_name, target_environment, model)
    ml_binding_guid = aios_client.get_existing_binding(wml_credentials)
    model_subscription = aios_client.get_existing_subscription(wml_model_deployment['model_guid'])
    aios_client.generate_scoring_requests(wml_model_deployment, ml_binding_guid, model_subscription, args)
    aios_client.generate_explain_requests(wml_model_deployment, model_subscription, args)
    aios_client.trigger_checks(wml_model_deployment, model_subscription, args)

    logger.info('Process completed')
    logger.info('The AI OpenScale dashboard can be accessed at: {}/aiopenscale'.format(target_environment['aios_url']))
