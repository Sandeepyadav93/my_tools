import argparse
import os

# Create an argument parser to parse command line arguments
parser = argparse.ArgumentParser(description='Clone a GitHub repo locally using SSH')
parser.add_argument('repo_name', metavar='repo-name', type=str, help='the name of the GitHub repo')
parser.add_argument('-o', '--org', type=str, default='openstack-k8s-operators', help='the name of the GitHub organization')

# Parse the command line arguments
args = parser.parse_args()

# Construct the GitHub repo URL
github_url = f'git@github.com:{args.org}/{args.repo_name}.git'

# Clone the repo locally using SSH
os.system(f'git clone {github_url}')
