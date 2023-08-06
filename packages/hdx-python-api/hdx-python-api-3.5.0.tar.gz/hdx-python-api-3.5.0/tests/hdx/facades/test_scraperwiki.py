# -*- coding: UTF-8 -*-
"""ScraperWiki Facade Tests"""
from os.path import join

from hdx.facades import logging_kwargs

logging_kwargs.update({
    'smtp_config_yaml': join('tests', 'fixtures', 'config', 'smtp_config.yml'),
})

from . import my_testfn, my_excfn, testresult
from hdx.facades.hdx_scraperwiki import facade


class TestScraperWiki:
    def test_facade(self, hdx_config_yaml, project_config_yaml):
        testresult.actual_result = None
        facade(my_testfn, user_agent='test', hdx_config_yaml=hdx_config_yaml, project_config_yaml=project_config_yaml)
        assert testresult.actual_result == 'https://data.humdata.org/'

    def test_exception(self, hdx_config_yaml, project_config_yaml):
        testresult.actual_result = None
        facade(my_excfn, user_agent='test', hdx_config_yaml=hdx_config_yaml, project_config_yaml=project_config_yaml)
        assert testresult.actual_result == 'https://data.humdata.org/'
