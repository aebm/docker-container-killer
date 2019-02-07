#!/usr/bin/env python

import unittest
import re
import dc_killer


class FakeContainer(object):

    def __init__(self, dict_):
        self.attrs = dict_


class TestDockerContainerKillerMethods(unittest.TestCase):

    def test_is_regex_match(self):
        pattern = re.compile('hug')
        empty = []
        names_match = ['sonia', 'hughie']
        names_no_match = ['sonia', 'albert']
        self.assertFalse(dc_killer.is_regex_match(pattern, empty))
        self.assertTrue(dc_killer.is_regex_match(pattern, names_match))
        self.assertFalse(dc_killer.is_regex_match(pattern, names_no_match))

    def test_filter_containers_by_regex(self):
        regex = 'test_'
        rm_1 = FakeContainer({u'Names': [u'alfa']})
        keep_1 = FakeContainer({u'Names': [u'test_one']})
        rm_2 = FakeContainer({u'Names': [u'beta']})
        keep_2 = FakeContainer({u'Names': [u'test_two']})
        containers = [
            rm_1,
            keep_1,
            rm_2,
            keep_2
        ]
        exp_containers = [
            keep_1,
            keep_2
        ]
        f_containers = dc_killer.filter_containers_by_regex(regex, containers)
        self.assertListEqual(f_containers,
                             exp_containers,
                             msg='Unexpected result')

    def test_beautify_container(self):
        container = {
            u'Command': u'COMMAND',
            u'Created': 1549467735,
            u'HostConfig': u'HOSTCONFIG',
            u'Id': u'ID',
            u'Image': u'IMAGE',
            u'ImageID': u'IMAGEID',
            u'Labels': u'LABELS',
            u'Mounts': u'MOUNTS',
            u'Names': [u'/john_doe'],
            u'NetworkSettings': u'NETWORKSETTINGS',
            u'Ports': u'PORTS',
            u'State': u'running',
            u'Status': 'Up 23 hours'
        }
        exp_container = {
            u'Created': u'2019-02-06 15:42:15',
            u'Image': u'IMAGE',
            u'Names': [u'/john_doe'],
            u'State': u'running',
            u'Status': 'Up 23 hours'
        }
        self.assertEqual(dc_killer.beautify_container(container),
                         exp_container,
                         msg='Unexpected result')

    def test_get_containers_to_delete(self):
        current_time = 1549467735
        minutes = 15
        keep_1 = FakeContainer({
            u'Names': [u'test_one'],
            u'Created': 1549467435})
        rm_1 = FakeContainer({
            u'Names': [u'test_two'],
            u'Created': 1549466295})
        keep_2 = FakeContainer({
            u'Names': [u'test_three'],
            u'Created': 1549467315})
        rm_2 = FakeContainer({
            u'Names': [u'test_four'],
            u'Created': 1549381335})
        containers = [
            keep_1,
            rm_1,
            keep_2,
            rm_2
        ]
        exp_containers = [
            rm_1,
            rm_2
        ]
        rm_containers = dc_killer.get_containers_to_delete(current_time,
                                                           minutes,
                                                           containers)
        self.assertListEqual(rm_containers,
                             exp_containers,
                             msg='Unexpected result')

    def test_get_datetime(self):
        timestamp = 1549467735
        exp_datetime = u'2019-02-06 15:42:15'
        self.assertEqual(dc_killer.get_datetime(timestamp),
                         exp_datetime,
                         msg='Unexpected datetime')

    def test_remove_keys_from_dict(self):
        dict_ = {i: i for i in range(5)}
        target_dict = {i: i for i in range(5) if i in [1, 3]}
        new_dict = dc_killer.remove_keys_from_dict([0, 2, 4], dict_)
        self.assertEqual(new_dict, target_dict,
                         msg='Did not get expected dict')


if __name__ == '__main__':
    unittest.main()
