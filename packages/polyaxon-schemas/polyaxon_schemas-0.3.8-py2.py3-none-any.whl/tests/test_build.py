# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from unittest import TestCase

from marshmallow import ValidationError

from polyaxon_schemas.build import BuildConfig


class TestBuildConfigs(TestCase):
    def test_valid_image(self):
        config_dict = {
            'image': None,
        }
        with self.assertRaises(ValidationError):
            BuildConfig.from_dict(config_dict)

        config_dict = {
            'image': '',
        }
        with self.assertRaises(ValidationError):
            BuildConfig.from_dict(config_dict)

        config_dict = {
            'image': 'some_image_name:sdf:sdf:foo',
        }
        with self.assertRaises(ValidationError):
            BuildConfig.from_dict(config_dict)

        config_dict = {
            'image': 'registry.foobar.com/my/docker/some_image_name:foo:foo',
        }
        with self.assertRaises(ValidationError):
            BuildConfig.from_dict(config_dict)

        config_dict = {
            'image': 'registry.foobar.com:foo:foo/my/docker/some_image_name:foo',
        }
        with self.assertRaises(ValidationError):
            BuildConfig.from_dict(config_dict)

        config_dict = {
            'image': 'registry.foobar.com:foo:foo/my/docker/some_image_name',
        }
        with self.assertRaises(ValidationError):
            BuildConfig.from_dict(config_dict)

        config_dict = {
            'image': 'registry.foobar.com:/my/docker/some_image_name:foo',
        }
        with self.assertRaises(ValidationError):
            BuildConfig.from_dict(config_dict)

    def test_build_config(self):
        config_dict = {
            'image': 'some_image_name',
        }
        config = BuildConfig.from_dict(config_dict)
        assert config.to_dict() == config_dict
        assert config.image_tag == 'latest'
        assert config.nocache is None

    def test_build_config_image_use_cases(self):
        # Latest
        config_dict = {
            'image': 'some_image_name',
        }
        config = BuildConfig.from_dict(config_dict)
        assert config.image_tag == 'latest'

        # Latest from with docker registry url
        config_dict = {
            'image': 'registry.foobar.com/my/docker/some_image_name',
        }
        config = BuildConfig.from_dict(config_dict)
        assert config.image_tag == 'latest'

        # Latest from with docker registry url with port
        config_dict = {
            'image': 'registry.foobar.com:4567/some_image_name',
        }
        config = BuildConfig.from_dict(config_dict)
        assert config.image_tag == 'latest'

        # Some tag
        config_dict = {
            'image': 'some_image_name:4567',
        }
        config = BuildConfig.from_dict(config_dict)
        assert config.image_tag == '4567'

        # Some tag
        config_dict = {
            'image': 'some_image_name:foo',
        }
        config = BuildConfig.from_dict(config_dict)
        assert config.image_tag == 'foo'

        # Some tag from with docker registry url
        config_dict = {
            'image': 'registry.foobar.com/my/docker/some_image_name:foo',
        }
        config = BuildConfig.from_dict(config_dict)
        assert config.image_tag == 'foo'

        # Some tag from with docker registry url with port
        config_dict = {
            'image': 'registry.foobar.com:4567/some_image_name:foo',
        }
        config = BuildConfig.from_dict(config_dict)
        assert config.image_tag == 'foo'

    def test_build_nocache(self):
        config_dict = {
            'image': 'some_image_name',
            'nocache': True
        }
        config = BuildConfig.from_dict(config_dict)
        assert config.to_dict() == config_dict
        assert config.image_tag == 'latest'
        assert config.nocache is True

    def test_build_from_git_repo_with_install_step_config(self):
        config_dict = {
            'image': 'tensorflow:1.3.0',
            'build_steps': ['pip install tensor2tensor'],
            'env_vars': [['LC_ALL', 'en_US.UTF-8']],
            'git': 'https://github.com/tensorflow/tensor2tensor.git'
        }
        config = BuildConfig.from_dict(config_dict)
        assert config.to_dict() == config_dict
        assert config.image_tag == '1.3.0'
