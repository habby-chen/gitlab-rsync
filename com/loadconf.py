#!/usr/bin/python3
# -- coding: utf-8 --**
import argparse

import yaml


class Conf:
    source_domain = ""
    source_token = ""
    source_protocol = ""
    target_domain = ""
    target_token = ""
    project_list = []
    webhook_token = ""
    repo_base_path = ""
    log_path = ""
    webhook_port = 0
    target_protocol = ""
    lock_path = ""


def load_conf():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="配置文件路径", default="./config.yml")
    args = parser.parse_args()
    if len(args.config) > 0:
        conf_path = args.config
    else:
        conf_path = "./config.yml"
    f = open(conf_path)
    yml_data = yaml.load(f, yaml.Loader)
    c = Conf()
    c.source_domain = yml_data["source_domain"]
    c.source_token = yml_data["source_token"]
    c.source_protocol = yml_data["source_protocol"]
    c.target_domain = yml_data["target_domain"]
    c.target_token = yml_data["target_token"]
    c.project_list = yml_data["project_list"]
    c.webhook_token = yml_data["webhook_token"]
    c.repo_base_path = yml_data["repo_base_path"]
    c.webhook_port = yml_data["webhook_port"]
    c.log_path = yml_data["log_path"]
    c.target_protocol = yml_data["target_protocol"]
    c.lock_path = yml_data["lock_path"]
    return c


def load_project_list():
    # 为了及时发现配置变化，每次都会去加载配置
    f = open("config.yml")
    yml_data = yaml.load(f, yaml.Loader)
    return yml_data["project_list"]


try:
    Config = load_conf()
except Exception as e:
    print("配置文件加载错误:%s" % e)
    exit(1)
