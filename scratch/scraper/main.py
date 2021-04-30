#!/usr/bin/env python

import json
import typing
import urllib.parse
from pathlib import Path

import requests


# https://en.scratch-wiki.info/wiki/Scratch_API#GET_.2Fusers.2F.3Cusername.3E.2Fprojects
# https://scratch.mit.edu/discuss/topic/373138/?page=1#post-3734203


API_BASE_URL = 'https://api.scratch.mit.edu'
PROJECTS_BASE_URL = 'https://projects.scratch.mit.edu'


# wrote this because I thought the other api calls used user id but it turns out they don't
def get_user_info(username: str) -> typing.List[typing.Dict]:
    api_users_url = urllib.parse.urljoin(API_BASE_URL, 'users/')
    api_this_user_url = urllib.parse.urljoin(api_users_url, username)

    r = requests.get(api_this_user_url)
    return r.json()


def get_user_projects(username: str) -> typing.List[typing.Dict]:
    api_users_url = urllib.parse.urljoin(API_BASE_URL, 'users/')
    api_this_user_url = urllib.parse.urljoin(api_users_url, f'{username}/')
    api_this_user_projects_url = urllib.parse.urljoin(api_this_user_url, 'projects')

    r = requests.get(api_this_user_projects_url)
    return r.json()


def download_project(project_id: int) -> bytes:
    project_url = urllib.parse.urljoin(PROJECTS_BASE_URL, str(project_id))
    r = requests.get(project_url)
    return r.content


def sterilise_filename(filename: str) -> str:
    # thanks to https://stackoverflow.com/a/295152/8766519 for the idea
    return ''.join([s for s in filename if s.isalnum()])


def main():
    output_folder = Path().resolve().parent

    username = input('Scratch username: ')
    print('Getting projects list')
    user_projects = get_user_projects(username)
    print(f'Got list of {len(user_projects)} projects')

    projects_file_path = output_folder / 'projects.json'
    with open(projects_file_path, 'w') as projects_file:
        json.dump(user_projects, projects_file, indent=4)
    print(f'Saved list of projects to {projects_file_path}')

    print('Downloading projects')
    for project in user_projects:
        print(f"Downloading project {project['title']} with id {project['id']}")
        project_bytes = download_project(project['id'])

        project_title_sterilised = sterilise_filename(project['title'])
        output_file_path = output_folder.joinpath(project_title_sterilised).with_suffix('.sb3')
        print(f'Saving to {output_file_path}')
        with open(output_file_path, 'wb') as output_file:
            output_file.write(project_bytes)
        print('Saved project')

    input('Done, press enter to exit')


if __name__ == '__main__':
    main()
