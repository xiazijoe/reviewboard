import json
from djblets.testing.decorators import add_fixtures
from kgb import SpyAgency
from reviewboard.scmtools.core import HEAD, PRE_CREATION, Revision
from reviewboard.scmtools.hg import (HgDiffParser,
                                     HgGitDiffParser,
                                     HgTool,
                                     HgWebClient)
from reviewboard.testing.testcase import TestCase
            self.tool.parse_diff_revision(filename=b'/dev/null',
                                          revision=b'bf544ea505f8')[1],
            PRE_CREATION)
        self.assertEqual(file.orig_filename, b'readme')
        self.assertEqual(file.orig_file_details, PRE_CREATION)
        self.assertEqual(file.orig_filename, b'empty')
        self.assertEqual(file.modified_file_details, b'4960455a8e88')
        self.assertEqual(file.modified_filename, b'empty')
        self.assertEqual(file.orig_file_details, b'356a6127ef19')
        self.assertEqual(file.orig_filename, b'empty')
        self.assertEqual(file.modified_file_details, b'4960455a8e88')
        self.assertEqual(file.modified_filename, b'empty')
        self.assertEqual(file.orig_file_details, b'bf544ea505f8')
        self.assertEqual(file.orig_filename, b'readme')
        self.assertEqual(file.modified_file_details, b'Uncommitted')
        self.assertEqual(file.modified_filename, b'readme')
        self.assertEqual(file.orig_file_details, b'356a6127ef19')
        self.assertEqual(file.orig_filename, b'readme')
        self.assertEqual(file.modified_file_details, b'4960455a8e88')
        self.assertEqual(file.modified_filename, b'readme')
        self.assertEqual(file.orig_file_details, b'356a6127ef19')
        self.assertEqual(file.orig_filename, b'readme')
        self.assertEqual(file.modified_file_details, b'4960455a8e88')
        self.assertEqual(file.modified_filename, b'readme')
        self.assertEqual(file.orig_file_details, b'bf544ea505f8')
        self.assertEqual(file.orig_filename, b'path/to file/readme.txt')
        self.assertEqual(file.modified_file_details, b'4960455a8e88')
        self.assertEqual(file.modified_filename, b'new/path to/readme.txt')
        self.assertEqual(file.orig_file_details, b'bf544ea505f8')
        self.assertEqual(file.orig_filename, 'réadme'.encode('utf-8'))
        self.assertEqual(file.modified_file_details, b'Uncommitted')
        self.assertEqual(file.modified_filename, 'réadme'.encode('utf-8'))
        self.assertEqual(file.orig_file_details, b'bf544ea505f8')
        self.assertEqual(file.orig_filename,
                         'path/to file/réadme.txt'.encode('utf-8'))
        self.assertEqual(file.modified_file_details, b'4960455a8e88')
        self.assertEqual(file.modified_filename,
                         'new/path to/réadme.txt'.encode('utf-8'))
            self.tool.parse_diff_revision(filename=b'doc/readme',
                                          revision=b'bf544ea505f8'),
            (b'doc/readme', b'bf544ea505f8'))
            self.tool.parse_diff_revision(filename=b'/dev/null',
                                          revision=b'bf544ea505f8'),
            (b'/dev/null', PRE_CREATION))
        self.assertNotIn(b'goodbye', value.diff)
        self.assertIn(b'goodbye', value.diff)
        tool = self.tool
        value = tool.get_file('doc/readme', Revision('661e5dd3c493'))
        self.assertIsInstance(value, bytes)
        with self.assertRaises(FileNotFoundError):
            tool.get_file('')

        with self.assertRaises(FileNotFoundError):
            tool.get_file('hello', PRE_CREATION)
    def test_file_exists(self):
        """Testing HgTool.file_exists"""
        rev = Revision('661e5dd3c493')
        self.assertTrue(self.tool.file_exists('doc/readme', rev))
        self.assertFalse(self.tool.file_exists('doc/readme2', rev))
                          path='https://www.mercurial-scm.org/repo/hg',
        self.assertTrue(tool.file_exists('mercurial/hgweb/common.py',
                                         Revision('f0735f2ce542')))
        self.assertFalse(tool.file_exists('mercurial/hgweb/common.py',
                                          Revision('abcdef123456')))

class HgWebClientTests(SpyAgency, TestCase):
    """Unit tests for reviewboard.scmtools.hg.HgWebClient."""

    def setUp(self):
        super(HgWebClientTests, self).setUp()

        self.hgweb_client = HgWebClient(path='http://hg.example.com/',
                                        username='test-user',
                                        password='test-password')

    def test_cat_file_with_raw_file(self):
        """Testing HgWebClient.cat_file with URL using raw-file"""
        def _get_file_http(client, url, path, revision, *args, **kwargs):
            if url.startswith('http://hg.example.com/raw-file/'):
                return b'result payload'

            raise FileNotFoundError(path=path,
                                    revision=revision)

        spy = self.spy_on(self.hgweb_client.get_file_http,
                          call_fake=_get_file_http)

        rsp = self.hgweb_client.cat_file(path='foo/bar.txt',
                                         rev=HEAD)
        self.assertIsInstance(rsp, bytes)
        self.assertEqual(rsp, b'result payload')

        spy = self.hgweb_client.get_file_http.spy
        self.assertEqual(len(spy.calls), 1)
        self.assertTrue(spy.last_called_with(
            url='http://hg.example.com/raw-file/tip/foo/bar.txt',
            path='foo/bar.txt',
            revision='tip'))

    def test_cat_file_with_raw(self):
        """Testing HgWebClient.cat_file with URL using raw"""
        def _get_file_http(client, url, path, revision, *args, **kwargs):
            if url.startswith('http://hg.example.com/raw/'):
                return b'result payload'

            raise FileNotFoundError(path=path,
                                    revision=revision)

        spy = self.spy_on(self.hgweb_client.get_file_http,
                          call_fake=_get_file_http)

        rsp = self.hgweb_client.cat_file(path='foo/bar.txt',
                                         rev=HEAD)
        self.assertIsInstance(rsp, bytes)
        self.assertEqual(rsp, b'result payload')

        spy = self.hgweb_client.get_file_http.spy
        self.assertEqual(len(spy.calls), 2)
        self.assertTrue(spy.last_called_with(
            url='http://hg.example.com/raw/tip/foo/bar.txt',
            path='foo/bar.txt',
            revision='tip'))

    def test_cat_file_with_hg_history(self):
        """Testing HgWebClient.cat_file with URL using hg-history"""
        def _get_file_http(client, url, path, revision, *args, **kwargs):
            if url.startswith('http://hg.example.com/hg-history/'):
                return b'result payload'

            raise FileNotFoundError(path=path,
                                    revision=revision)

        self.spy_on(self.hgweb_client.get_file_http,
                    call_fake=_get_file_http)

        rsp = self.hgweb_client.cat_file(path='foo/bar.txt',
                                         rev=HEAD)
        self.assertIsInstance(rsp, bytes)
        self.assertEqual(rsp, b'result payload')

        spy = self.hgweb_client.get_file_http.spy
        self.assertEqual(len(spy.calls), 3)
        self.assertTrue(spy.last_called_with(
            url='http://hg.example.com/hg-history/tip/foo/bar.txt',
            path='foo/bar.txt',
            revision='tip'))

    def test_cat_file_with_base_commit_id(self):
        """Testing HgWebClient.cat_file with base_commit_id"""
        def _get_file_http(client, url, path, revision, *args, **kwargs):
            return b'result payload'

        spy = self.spy_on(self.hgweb_client.get_file_http,
                          call_fake=_get_file_http)

        rsp = self.hgweb_client.cat_file(
            path='foo/bar.txt',
            base_commit_id='1ca5879492b8fd606df1964ea3c1e2f4520f076f')
        self.assertIsInstance(rsp, bytes)
        self.assertEqual(rsp, b'result payload')

        self.assertEqual(len(spy.calls), 1)
        self.assertTrue(spy.last_called_with(
            url='http://hg.example.com/raw-file/'
                '1ca5879492b8fd606df1964ea3c1e2f4520f076f/foo/bar.txt',
            path='foo/bar.txt',
            revision='1ca5879492b8fd606df1964ea3c1e2f4520f076f'))

    def test_cat_file_with_not_found(self):
        """Testing HgWebClient.cat_file with file not found"""
        def _get_file_http(client, url, path, revision, *args, **kwargs):
            raise FileNotFoundError(path=path,
                                    revision=revision)

        spy = self.spy_on(self.hgweb_client.get_file_http,
                          call_fake=_get_file_http)

        with self.assertRaises(FileNotFoundError):
            self.hgweb_client.cat_file(path='foo/bar.txt')

        self.assertEqual(len(spy.calls), 3)

    def test_get_branches(self):
        """Testing HgWebClient.get_branches"""
        def _get_file_http(client, url, path, revision, mime_type, *args,
                           **kwargs):
            self.assertEqual(url, 'http://hg.example.com/json-branches')
            self.assertEqual(mime_type, 'application/json')
            self.assertEqual(path, '')
            self.assertEqual(revision, '')

            return self._dump_json({
                'branches': [
                    {
                        'branch': 'default',
                        'node': '1ca5879492b8fd606df1964ea3c1e2f4520f076f',
                        'status': 'open',
                    },
                    {
                        'branch': 'closed-branch',
                        'node': 'b9af6489f6f2004ad11b82c6057f7007e3c35372',
                        'status': 'closed',
                    },
                    {
                        'branch': 'release-branch',
                        'node': '8210c0d945ef893d40a903c9dc14cd072eee5bb7',
                        'status': 'open',
                    },
                ],
            })

        self.spy_on(self.hgweb_client.get_file_http,
                    call_fake=_get_file_http)

        branches = self.hgweb_client.get_branches()
        self.assertIsInstance(branches, list)
        self.assertEqual(len(branches), 2)

        branch = branches[0]
        self.assertEqual(branch.id, 'default')
        self.assertEqual(branch.commit,
                         '1ca5879492b8fd606df1964ea3c1e2f4520f076f')
        self.assertTrue(branch.default)

        branch = branches[1]
        self.assertEqual(branch.id, 'release-branch')
        self.assertEqual(branch.commit,
                         '8210c0d945ef893d40a903c9dc14cd072eee5bb7')
        self.assertFalse(branch.default)

    def test_get_branches_with_error(self):
        """Testing HgWebClient.get_branches with error fetching result"""
        def _get_file_http(client, url, path, revision, *args, **kwargs):
            raise FileNotFoundError(path, revision)

        self.spy_on(self.hgweb_client.get_file_http,
                    call_fake=_get_file_http)

        branches = self.hgweb_client.get_branches()
        self.assertEqual(branches, [])

    def test_get_change(self):
        """Testing HgWebClient.get_change"""
        def _get_file_http(client, url, path, revision, mime_type, *args,
                           **kwargs):
            if url.startswith('http://hg.example.com/raw-rev/'):
                self.assertEqual(
                    url,
                    'http://hg.example.com/raw-rev/'
                    '1ca5879492b8fd606df1964ea3c1e2f4520f076f')
                self.assertEqual(path, '')
                self.assertEqual(revision, '')
                self.assertIsNone(mime_type)

                return b'diff payload'
            elif url.startswith('http://hg.example.com/json-rev/'):
                self.assertEqual(
                    url,
                    'http://hg.example.com/json-rev/'
                    '1ca5879492b8fd606df1964ea3c1e2f4520f076f')
                self.assertEqual(mime_type, 'application/json')
                self.assertEqual(path, '')
                self.assertEqual(revision, '')

                return self._dump_json({
                    'node': '1ca5879492b8fd606df1964ea3c1e2f4520f076f',
                    'desc': 'This is the change description',
                    'user': 'Test User',
                    'date': [1583149219, 28800],
                    'parents': [
                        'b9af6489f6f2004ad11b82c6057f7007e3c35372'
                    ],
                })
            else:
                raise FileNotFoundError(path=path,
                                        revision=revision)

        self.spy_on(self.hgweb_client.get_file_http,
                    call_fake=_get_file_http)

        commit = self.hgweb_client.get_change(
            '1ca5879492b8fd606df1964ea3c1e2f4520f076f')
        self.assertEqual(commit.id, '1ca5879492b8fd606df1964ea3c1e2f4520f076f')
        self.assertEqual(commit.message, 'This is the change description')
        self.assertEqual(commit.author_name, 'Test User')
        self.assertEqual(commit.date, '2020-03-02T03:40:19')
        self.assertEqual(commit.parent,
                         'b9af6489f6f2004ad11b82c6057f7007e3c35372')

    def test_get_commits(self):
        """Testing HgWebClient.get_commits"""
        def _get_file_http(client, url, path, revision, mime_type, *args,
                           **kwargs):
            self.assertEqual(
                url,
                'http://hg.example.com/json-log/?rev=branch(.)')
            self.assertEqual(mime_type, 'application/json')
            self.assertEqual(path, '')
            self.assertEqual(revision, '')

            return self._dump_json({
                'entries': [
                    {
                        'node': '1ca5879492b8fd606df1964ea3c1e2f4520f076f',
                        'desc': 'This is the change description',
                        'user': 'Test User',
                        'date': [1583149219, 28800],
                        'parents': [
                            'b9af6489f6f2004ad11b82c6057f7007e3c35372'
                        ],
                    },
                    {
                        'node': 'b9af6489f6f2004ad11b82c6057f7007e3c35372',
                        'desc': 'This is another description',
                        'user': 'Another User',
                        'date': [1581897120, 28800],
                        'parents': [
                            '8210c0d945ef893d40a903c9dc14cd072eee5bb7',
                        ],
                    },
                ],
            })

        self.spy_on(self.hgweb_client.get_file_http,
                    call_fake=_get_file_http)

        commits = self.hgweb_client.get_commits()
        self.assertEqual(len(commits), 2)

        commit = commits[0]
        self.assertEqual(commit.id, '1ca5879492b8fd606df1964ea3c1e2f4520f076f')
        self.assertEqual(commit.message, 'This is the change description')
        self.assertEqual(commit.author_name, 'Test User')
        self.assertEqual(commit.date, '2020-03-02T03:40:19')
        self.assertEqual(commit.parent,
                         'b9af6489f6f2004ad11b82c6057f7007e3c35372')

        commit = commits[1]
        self.assertEqual(commit.id, 'b9af6489f6f2004ad11b82c6057f7007e3c35372')
        self.assertEqual(commit.message, 'This is another description')
        self.assertEqual(commit.author_name, 'Another User')
        self.assertEqual(commit.date, '2020-02-16T15:52:00')
        self.assertEqual(commit.parent,
                         '8210c0d945ef893d40a903c9dc14cd072eee5bb7')

    def test_get_commits_with_branch(self):
        """Testing HgWebClient.get_commits with branch"""
        def _get_file_http(client, url, path, revision, mime_type, *args,
                           **kwargs):
            self.assertEqual(
                url,
                'http://hg.example.com/json-log/?rev=branch(my-branch)')
            self.assertEqual(mime_type, 'application/json')
            self.assertEqual(path, '')
            self.assertEqual(revision, '')

            return self._dump_json({
                'entries': [
                    {
                        'node': '1ca5879492b8fd606df1964ea3c1e2f4520f076f',
                        'desc': 'This is the change description',
                        'user': 'Test User',
                        'date': [1583149219, 28800],
                        'parents': [
                            'b9af6489f6f2004ad11b82c6057f7007e3c35372'
                        ],
                    },
                    {
                        'node': 'b9af6489f6f2004ad11b82c6057f7007e3c35372',
                        'desc': 'This is another description',
                        'user': 'Another User',
                        'date': [1581897120, 28800],
                        'parents': [
                            '8210c0d945ef893d40a903c9dc14cd072eee5bb7',
                        ],
                    },
                ],
            })

        self.spy_on(self.hgweb_client.get_file_http,
                    call_fake=_get_file_http)

        commits = self.hgweb_client.get_commits(branch='my-branch')
        self.assertEqual(len(commits), 2)

        commit = commits[0]
        self.assertEqual(commit.id, '1ca5879492b8fd606df1964ea3c1e2f4520f076f')
        self.assertEqual(commit.message, 'This is the change description')
        self.assertEqual(commit.author_name, 'Test User')
        self.assertEqual(commit.date, '2020-03-02T03:40:19')
        self.assertEqual(commit.parent,
                         'b9af6489f6f2004ad11b82c6057f7007e3c35372')

        commit = commits[1]
        self.assertEqual(commit.id, 'b9af6489f6f2004ad11b82c6057f7007e3c35372')
        self.assertEqual(commit.message, 'This is another description')
        self.assertEqual(commit.author_name, 'Another User')
        self.assertEqual(commit.date, '2020-02-16T15:52:00')
        self.assertEqual(commit.parent,
                         '8210c0d945ef893d40a903c9dc14cd072eee5bb7')

    def test_get_commits_with_start(self):
        """Testing HgWebClient.get_commits with start"""
        def _get_file_http(client, url, path, revision, mime_type, *args,
                           **kwargs):
            self.assertEqual(
                url,
                'http://hg.example.com/json-log/'
                '?rev=ancestors(1ca5879492b8fd606df1964ea3c1e2f4520f076f)'
                '+and+branch(.)')
            self.assertEqual(mime_type, 'application/json')
            self.assertEqual(path, '')
            self.assertEqual(revision, '')

            return self._dump_json({
                'entries': [
                    {
                        'node': '1ca5879492b8fd606df1964ea3c1e2f4520f076f',
                        'desc': 'This is the change description',
                        'user': 'Test User',
                        'date': [1583149219, 28800],
                        'parents': [
                            'b9af6489f6f2004ad11b82c6057f7007e3c35372'
                        ],
                    },
                    {
                        'node': 'b9af6489f6f2004ad11b82c6057f7007e3c35372',
                        'desc': 'This is another description',
                        'user': 'Another User',
                        'date': [1581897120, 28800],
                        'parents': [
                            '8210c0d945ef893d40a903c9dc14cd072eee5bb7',
                        ],
                    },
                ],
            })

        self.spy_on(self.hgweb_client.get_file_http,
                    call_fake=_get_file_http)

        commits = self.hgweb_client.get_commits(
            start='1ca5879492b8fd606df1964ea3c1e2f4520f076f')
        self.assertEqual(len(commits), 2)

        commit = commits[0]
        self.assertEqual(commit.id, '1ca5879492b8fd606df1964ea3c1e2f4520f076f')
        self.assertEqual(commit.message, 'This is the change description')
        self.assertEqual(commit.author_name, 'Test User')
        self.assertEqual(commit.date, '2020-03-02T03:40:19')
        self.assertEqual(commit.parent,
                         'b9af6489f6f2004ad11b82c6057f7007e3c35372')

        commit = commits[1]
        self.assertEqual(commit.id, 'b9af6489f6f2004ad11b82c6057f7007e3c35372')
        self.assertEqual(commit.message, 'This is another description')
        self.assertEqual(commit.author_name, 'Another User')
        self.assertEqual(commit.date, '2020-02-16T15:52:00')
        self.assertEqual(commit.parent,
                         '8210c0d945ef893d40a903c9dc14cd072eee5bb7')

    def test_get_commits_with_not_implemented(self):
        """Testing HgWebClient.get_commits with server response of "not yet
        implemented"
        """
        def _get_file_http(client, url, path, revision, mime_type, *args,
                           **kwargs):
            self.assertEqual(url,
                             'http://hg.example.com/json-log/?rev=branch(.)')
            self.assertEqual(mime_type, 'application/json')
            self.assertEqual(path, '')
            self.assertEqual(revision, '')

            return b'not yet implemented'

        self.spy_on(self.hgweb_client.get_file_http,
                    call_fake=_get_file_http)

        commits = self.hgweb_client.get_commits()
        self.assertEqual(commits, [])

    def _dump_json(self, obj):
        """Dump an object to a JSON byte string.

        Args:
            obj (object):
                The object to dump.

        Returns:
            bytes;
            The JSON-serialized byte string.
        """
        return json.dumps(obj).encode('utf-8')


class HgAuthFormTests(TestCase):
    """Unit tests for HgTool's authentication form."""

    def test_fields(self):
        """Testing HgTool authentication form fields"""
        form = HgTool.create_auth_form()

        self.assertEqual(list(form.fields), ['username', 'password'])
        self.assertEqual(form['username'].help_text, '')
        self.assertEqual(form['username'].label, 'Username')
        self.assertEqual(form['password'].help_text, '')
        self.assertEqual(form['password'].label, 'Password')

    @add_fixtures(['test_scmtools'])
    def test_load(self):
        """Tetting HgTool authentication form load"""
        repository = self.create_repository(
            tool_name='Mercurial',
            username='test-user',
            password='test-pass')

        form = HgTool.create_auth_form(repository=repository)
        form.load()

        self.assertEqual(form['username'].value(), 'test-user')
        self.assertEqual(form['password'].value(), 'test-pass')

    @add_fixtures(['test_scmtools'])
    def test_save(self):
        """Tetting HgTool authentication form save"""
        repository = self.create_repository(tool_name='Mercurial')

        form = HgTool.create_auth_form(
            repository=repository,
            data={
                'username': 'test-user',
                'password': 'test-pass',
            })
        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(repository.username, 'test-user')
        self.assertEqual(repository.password, 'test-pass')


class HgRepositoryFormTests(TestCase):
    """Unit tests for HgTool's repository form."""

    def test_fields(self):
        """Testing HgTool repository form fields"""
        form = HgTool.create_repository_form()

        self.assertEqual(list(form.fields), ['path', 'mirror_path'])
        self.assertEqual(form['path'].help_text,
                         'The path to the repository. This will generally be '
                         'the URL you would use to check out the repository.')
        self.assertEqual(form['path'].label, 'Path')
        self.assertEqual(form['mirror_path'].help_text, '')
        self.assertEqual(form['mirror_path'].label, 'Mirror Path')

    @add_fixtures(['test_scmtools'])
    def test_load(self):
        """Tetting HgTool repository form load"""
        repository = self.create_repository(
            tool_name='Mercurial',
            path='https://hg.example.com/repo',
            mirror_path='https://hg.mirror.example.com/repo')

        form = HgTool.create_repository_form(repository=repository)
        form.load()

        self.assertEqual(form['path'].value(), 'https://hg.example.com/repo')
        self.assertEqual(form['mirror_path'].value(),
                         'https://hg.mirror.example.com/repo')

    @add_fixtures(['test_scmtools'])
    def test_save(self):
        """Tetting HgTool repository form save"""
        repository = self.create_repository(tool_name='Mercurial')

        form = HgTool.create_repository_form(
            repository=repository,
            data={
                'path': 'https://hg.example.com/repo',
                'mirror_path': 'https://hg.mirror.example.com/repo',
            })
        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(repository.path, 'https://hg.example.com/repo')
        self.assertEqual(repository.mirror_path,
                         'https://hg.mirror.example.com/repo')