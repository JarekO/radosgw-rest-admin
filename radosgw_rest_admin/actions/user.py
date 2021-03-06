# Copyright 2013 Deutsche Telekom AG
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from base import RadosgwRestAdminAction


class User(RadosgwRestAdminAction):

    def add_arguments(self, subparser):
        parser = subparser.add_parser(name=self.name)
        parser.add_argument('-u', '--uid', help="User uid")
        parser.add_argument('--display-name', help="Display name")
        parser.add_argument('--subuser', help="Subuser name")
        parser.add_argument('--email', help="The email address associated with the user")
        parser.add_argument('--max-buckets', help="Specify the maximum number of buckets the user can own")

    @property
    def request_type(self):
        raise NotImplementedError()

    def url_base(self):
        return 'admin/user'

    def get_params(self, args):
        params = []
        if args.uid:
            params.append('uid=%s' % args.uid)
        if args.display_name:
            params.append('display-name=%s' % args.display_name)
        if args.subuser:
            params.append('subuser=%s' % args.subuser)
        if args.email:
            params.append('email=%s' % args.email)
        if args.max_buckets:
            params.append('max-buckets=%s' % args.max_buckets)
            
        return params


class UserInfo(User):
    @property
    def name(self):
        return 'user-info'

    def request_type(self):
        return 'get'


class UserCreate(User):
    @property
    def name(self):
        return 'user-create'

    def request_type(self):
        return 'put'
