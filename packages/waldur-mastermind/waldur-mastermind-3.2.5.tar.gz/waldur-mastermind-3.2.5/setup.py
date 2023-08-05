#!/usr/bin/env python
from setuptools import setup, find_packages

# apache-libcloud is required by AWS and Azure plugin
# cryptography is required by Azure plugin
# defusedxml is required by djangosaml2
# jira is required by JIRA plugin
# lxml is required by waldur-auth-valimo
# passlib is required by Ansible plugin
# paypalrestsdk is required by PayPal plugin
# python-digitalocean is required by DigitalOcean plugin
# python-freeipa is required by FreeIPA plugin
install_requires = [
    'ansible-waldur-module>=0.8.2',
    'apache-libcloud>=1.1.0,<2.2.0',
    'Babel!=2.4.0,>=2.3.4',
    'Celery>=4.1.0',
    'cmd2<0.9.0',  # TODO: Drop restriction after Waldur is migrated to Python 3.
    'croniter>=0.3.4,<0.3.6',
    'cryptography>=1.7.2',
    'defusedxml>=0.4.1',
    'django-admin-tools==0.8.0',
    'django-auth-ldap>=1.3.0',
    'django-defender>=0.5.3',
    'django-filter==1.0.2',
    'django-fluent-dashboard==0.6.1',
    'django-fsm==2.3.0',
    'django-jsoneditor>=0.0.7',
    'django-model-utils==3.0.0',
    'django-openid-auth>=0.14',
    'django-redis-cache>=1.6.5',
    'django-rest-swagger==2.1.2',
    'django-reversion==2.0.8',
    'django-taggit>=0.20.2',
    'Django>=1.11,<2.0',
    'djangorestframework>=3.6.3,<3.7.0',
    'djangosaml2==0.17.1',
    'elasticsearch==5.4.0',
    'hiredis>=0.2.0',
    'influxdb>=4.1.0',
    'iptools>=0.6.1',
    'jira>=1.0.15',
    'lxml>=3.2.0',
    'passlib>=1.7.0',
    'paypalrestsdk>=1.10.0,<2.0',
    'pbr!=2.1.0',
    'pdfkit>=0.6.1',
    'Pillow>=2.0.0',
    'PrettyTable<0.8,>=0.7.1',
    'psycopg2>=2.5.4',  # https://docs.djangoproject.com/en/1.11/ref/databases/#postgresql-notes
    'pycountry>=1.20,<2.0',
    'python-ceilometerclient>=2.9.0',
    'python-cinderclient>=3.1.0',
    'python-digitalocean>=1.5',
    'python-freeipa>=0.1.2',
    'python-glanceclient>=2.8.0',
    'python-keystoneclient>=3.13.0',
    'python-neutronclient>=6.5.0',
    'python-novaclient>=9.1.0',
    'pyvat>=1.3.1,<2.0',
    'PyYAML>=3.10',
    'pyzabbix>=0.7.2',
    'redis==2.10.6',
    'requests>=2.6.0,!=2.12.2,!=2.13.0',
    'sqlparse>=0.1.11',
    'pyjwt>=1.5.3',
]

test_requires = [
    'ddt>=1.0.0,<1.1.0',
    'docker',
    'factory_boy==2.4.1',
    'freezegun==0.3.7',
    'mock>=1.0.1',
    'mock-django==0.6.9',
    'six>=1.9.0',
    'sqlalchemy>=1.0.12',
]

setup(
    name='waldur-mastermind',
    version='3.2.5',
    author='OpenNode Team',
    author_email='info@opennodecloud.com',
    url='http://waldur.com',
    description='Waldur MasterMind is a hybrid cloud orchestrator.',
    license='MIT',
    long_description=open('README.rst').read(),
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    install_requires=install_requires,
    extras_require={
        'test': test_requires,
    },
    zip_safe=False,
    entry_points={
        'console_scripts': (
            'waldur = waldur_core.server.manage:main',
        ),
        'waldur_extensions': (
            'waldur_auth_social = waldur_auth_social.extension:AuthSocialExtension',
            'waldur_auth_openid = waldur_auth_openid.extension:WaldurAuthOpenIDExtension',
            'waldur_auth_saml2 = waldur_auth_saml2.extension:SAML2Extension',
            'waldur_auth_valimo = waldur_auth_valimo.extension:AuthValimoExtension',
            'waldur_aws = waldur_aws.extension:AWSExtension',
            'waldur_azure = waldur_azure.extension:AzureExtension',
            'waldur_digitalocean = waldur_digitalocean.extension:DigitalOceanExtension',
            'openstack = waldur_openstack.openstack.extension:OpenStackExtension',
            'openstack_tenant = waldur_openstack.openstack_tenant.extension:OpenStackTenantExtension',
            'waldur_cost_planning = waldur_cost_planning.extension:CostPlanningExtension',
            'waldur_freeipa = waldur_freeipa.extension:FreeIPAExtension',
            'waldur_slurm = waldur_slurm.extension:SlurmExtension',
            'waldur_paypal = waldur_paypal.extension:PayPalExtension',
            'waldur_zabbix = waldur_zabbix.extension:ZabbixExtension',
            'waldur_jira = waldur_jira.extension:JiraExtension',
            'waldur_rijkscloud = waldur_rijkscloud.extension:RijkscloudExtension',
            'waldur_common = waldur_ansible.common.extension:AnsibleCommonExtension',
            'waldur_playbook_jobs = waldur_ansible.playbook_jobs.extension:PlaybookJobsExtension',
            'waldur_python_management = waldur_ansible.python_management.extension:PythonManagementExtension',
            'waldur_jupyter_hub_management = waldur_ansible.jupyter_hub_management.extension:JupyterHubManagementExtension',
            'waldur_packages = waldur_mastermind.packages.extension:PackagesExtension',
            'waldur_invoices = waldur_mastermind.invoices.extension:InvoicesExtension',
            'waldur_support = waldur_mastermind.support.extension:SupportExtension',
            'waldur_analytics = waldur_mastermind.analytics.extension:AnalyticsExtension',
            'waldur_experts = waldur_mastermind.experts.extension:ExpertsExtension',
            'waldur_billing = waldur_mastermind.billing.extension:BillingExtension',
            'waldur_slurm_invoices = waldur_mastermind.slurm_invoices.extension:SlurmInvoicesExtension',
            'waldur_ansible_estimator = waldur_mastermind.ansible_estimator.extension:AnsibleEstimatorExtension',
            'waldur_zabbix_openstack = waldur_mastermind.zabbix_openstack.extension:ZabbixOpenStackExtension',
            'waldur_marketplace = waldur_mastermind.marketplace.extension:MarketplaceExtension',
            'waldur_marketplace_openstack = waldur_mastermind.marketplace_openstack.extension:MarketplaceOpenStackExtension',
            'waldur_marketplace_support = waldur_mastermind.marketplace_support.extension:MarketplaceSupportExtension',
            'waldur_marketplace_slurm = waldur_mastermind.marketplace_slurm.extension:MarketplaceSlurmExtension',
            'waldur_support_invoices = waldur_mastermind.support_invoices.extension:SupportInvoicesExtension',
        ),
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
)
