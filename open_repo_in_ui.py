import argparse
import webbrowser

# Create an argument parser to parse command line arguments
parser = argparse.ArgumentParser(description='Open a GitHub repo in your default web browser')
parser.add_argument('repo_name', metavar='repo-name', type=str, help='the name of the GitHub repo')
parser.add_argument('-o', '--org', type=str, default='openstack-k8s-operators', help='the name of the GitHub organization')

# Parse the command line arguments
args = parser.parse_args()

# Construct the GitHub repo URL
github_url = f'https://github.com/{args.org}/{args.repo_name}'

# Open the URL in the default web browser
webbrowser.open(github_url)
