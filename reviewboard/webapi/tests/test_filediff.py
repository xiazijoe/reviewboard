"""Unit tests for reviewboard.webapi.resources.filediff."""

from __future__ import annotations

from djblets.webapi.errors import PERMISSION_DENIED
from reviewboard.scmtools.core import PRE_CREATION

    filtered_extra_data = {
        key: value
        for key, value in filediff.extra_data.items()
        if not key.startswith('_')
    }

    self.assertEqual(item_rsp['extra_data'], filtered_extra_data)
    self.assertEqual(item_rsp['encoding'], filediff.encoding)
    @webapi_test_template
    def test_binary_true(self) -> None:
        """Testing the GET <URL> API with ?binary=1"""
        repository = self.create_repository()
        review_request = self.create_review_request(
            repository=repository,
            submitter=self.user,
            public=True)

        diffset = self.create_diffset(review_request)

        self.create_filediff(diffset, source_file='/test1', dest_file='/test1')
        self.create_filediff(diffset, source_file='/test2', dest_file='/test2')
        self.create_filediff(diffset, source_file='/test3', dest_file='/test3')
        binary1 = self.create_filediff(diffset, source_file='/binary1',
                                       dest_file='/binary1', binary=True)
        binary2 = self.create_filediff(diffset, source_file='/binary2',
                                       dest_file='/binary2', binary=True)

        rsp = self.api_get(
            '%s?binary=1' % get_filediff_list_url(diffset, review_request),
            expected_mimetype=filediff_list_mimetype)
        assert rsp is not None

        self.assertIn('stat', rsp)
        self.assertEqual(rsp['stat'], 'ok')
        self.assertIn('files', rsp)
        self.assertEqual(rsp['total_results'], 2)

        self.assertEqual(rsp['files'][0]['id'], binary1.pk)
        self.assertEqual(rsp['files'][1]['id'], binary2.pk)

    @webapi_test_template
    def test_binary_false(self) -> None:
        """Testing the GET <URL> API with ?binary=0"""
        repository = self.create_repository()
        review_request = self.create_review_request(
            repository=repository,
            submitter=self.user,
            public=True)

        diffset = self.create_diffset(review_request)

        fd1 = self.create_filediff(diffset, source_file='/test1',
                                   dest_file='/test1')
        fd2 = self.create_filediff(diffset, source_file='/test2',
                                   dest_file='/test2')
        fd3 = self.create_filediff(diffset, source_file='/test3',
                                   dest_file='/test3')
        self.create_filediff(diffset, source_file='/binary1',
                             dest_file='/binary1', binary=True)
        self.create_filediff(diffset, source_file='/binary2',
                             dest_file='/binary2', binary=True)

        rsp = self.api_get(
            '%s?binary=0' % get_filediff_list_url(diffset, review_request),
            expected_mimetype=filediff_list_mimetype)
        assert rsp is not None

        self.assertIn('stat', rsp)
        self.assertEqual(rsp['stat'], 'ok')
        self.assertIn('files', rsp)
        self.assertEqual(rsp['total_results'], 3)

        self.assertEqual(rsp['files'][0]['id'], fd1.pk)
        self.assertEqual(rsp['files'][1]['id'], fd2.pk)
        self.assertEqual(rsp['files'][2]['id'], fd3.pk)

    @webapi_test_template
    def test_binary_None(self) -> None:
        """Testing the GET <URL> API with ?binary unspecified"""
        repository = self.create_repository()
        review_request = self.create_review_request(
            repository=repository,
            submitter=self.user,
            public=True)

        diffset = self.create_diffset(review_request)

        self.create_filediff(diffset, source_file='/test1', dest_file='/test1')
        self.create_filediff(diffset, source_file='/test2', dest_file='/test2')
        self.create_filediff(diffset, source_file='/test3', dest_file='/test3')
        self.create_filediff(diffset, source_file='/binary1',
                             dest_file='/binary1', binary=True)
        self.create_filediff(diffset, source_file='/binary2',
                             dest_file='/binary2', binary=True)

        rsp = self.api_get(
            get_filediff_list_url(diffset, review_request),
            expected_mimetype=filediff_list_mimetype)
        assert rsp is not None

        self.assertIn('stat', rsp)
        self.assertEqual(rsp['stat'], 'ok')
        self.assertIn('files', rsp)
        self.assertEqual(rsp['total_results'], 5)


    @webapi_test_template
    def test_get_with_diff_data(self):
        """Testing the GET <URL> API with diff data result"""
        repository = self.create_repository(tool_name='Git')
        review_request = self.create_review_request(
            repository=repository,
            publish=True)

        diffset = self.create_diffset(review_request)
        filediff = self.create_filediff(
            diffset,
            source_file='newfile.py',
            source_revision=PRE_CREATION,
            dest_file='newfile.py',
            dest_detail='20e43bb7c2d9f3a31768404ac71121804d806f7c',
            diff=(
                b"diff --git a/newfile.py b/newfile.py\n"
                b"new file mode 100644\n"
                b"index 0000000000000000000000000000000000000000.."
                b"8eaa5c1eacb55c43f5e00ed9dcd0c8da901f0c85\n"
                b"--- /dev/null\n"
                b"+++ b/newfile.py\n"
                b"@@ -0,0 +1 @@\n"
                b"+print('hello, world!')\n"
            ))

        rsp = self.api_get(
            get_filediff_item_url(filediff, review_request),
            HTTP_ACCEPT='application/vnd.reviewboard.org.diff.data+json',
            expected_status=200,
            expected_mimetype='application/json')

        self.assertEqual(
            rsp,
            {
                'diff_data': {
                    'binary': False,
                    'changed_chunk_indexes': [0],
                    'chunks': [
                        {
                            'change': 'insert',
                            'collapsable': False,
                            'index': 0,
                            'lines': [
                                [
                                    1,
                                    '',
                                    '',
                                    [],
                                    1,
                                    'print(&#x27;hello, world!&#x27;)',
                                    [],
                                    False,
                                ],
                            ],
                            'meta': {
                                'left_headers': [],
                                'right_headers': [],
                                'whitespace_chunk': False,
                                'whitespace_lines': [],
                            },
                            'numlines': 1,
                        },
                    ],
                    'new_file': True,
                    'num_changes': 1,
                },
                'stat': 'ok',
            })

    @webapi_test_template
    def test_get_with_diff_data_and_syntax_highlighting(self):
        """Testing the GET <URL> API with diff data result and
        ?syntax-highlighting=1
        """
        repository = self.create_repository(tool_name='Git')
        review_request = self.create_review_request(
            repository=repository,
            publish=True)

        diffset = self.create_diffset(review_request)
        filediff = self.create_filediff(
            diffset,
            source_file='newfile.py',
            source_revision=PRE_CREATION,
            dest_file='newfile.py',
            dest_detail='20e43bb7c2d9f3a31768404ac71121804d806f7c',
            diff=(
                b"diff --git a/newfile.py b/newfile.py\n"
                b"new file mode 100644\n"
                b"index 0000000000000000000000000000000000000000.."
                b"8eaa5c1eacb55c43f5e00ed9dcd0c8da901f0c85\n"
                b"--- /dev/null\n"
                b"+++ b/newfile.py\n"
                b"@@ -0,0 +1 @@\n"
                b"+print('hello, world!')\n"
            ))

        rsp = self.api_get(
            ('%s?syntax-highlighting=1'
             % get_filediff_item_url(filediff, review_request)),
            HTTP_ACCEPT='application/vnd.reviewboard.org.diff.data+json',
            expected_status=200,
            expected_mimetype='application/json')

        self.assertEqual(
            rsp,
            {
                'diff_data': {
                    'binary': False,
                    'changed_chunk_indexes': [0],
                    'chunks': [
                        {
                            'change': 'insert',
                            'collapsable': False,
                            'index': 0,
                            'lines': [
                                [
                                    1,
                                    '',
                                    '',
                                    [],
                                    1,
                                    '<span class="nb">print</span>'
                                    '<span class="p">(</span>'
                                    '<span class="s1">&#39;hello, '
                                    'world!&#39;</span>'
                                    '<span class="p">)</span>',
                                    [],
                                    False,
                                ],
                            ],
                            'meta': {
                                'left_headers': [],
                                'right_headers': [],
                                'whitespace_chunk': False,
                                'whitespace_lines': [],
                            },
                            'numlines': 1,
                        },
                    ],
                    'new_file': True,
                    'num_changes': 1,
                },
                'stat': 'ok',
            })

    @webapi_test_template
    def test_get_with_diff_data_and_inaccessible(self) -> None:
        """Testing the GET <URL> API with diff data result and inaccessible
        FileDiff
        """
        repository = self.create_repository(tool_name='Git',
                                            public=False)
        review_request = self.create_review_request(
            repository=repository,
            publish=True)

        self.assertNotEqual(self.user, review_request.owner)
        self.assertFalse(review_request.is_accessible_by(self.user))

        diffset = self.create_diffset(review_request)
        filediff = self.create_filediff(
            diffset,
            source_file='newfile.py',
            source_revision=PRE_CREATION,
            dest_file='newfile.py',
            dest_detail='20e43bb7c2d9f3a31768404ac71121804d806f7c',
            diff=(
                b"diff --git a/newfile.py b/newfile.py\n"
                b"new file mode 100644\n"
                b"index 0000000000000000000000000000000000000000.."
                b"8eaa5c1eacb55c43f5e00ed9dcd0c8da901f0c85\n"
                b"--- /dev/null\n"
                b"+++ b/newfile.py\n"
                b"@@ -0,0 +1 @@\n"
                b"+print('hello, world!')\n"
            ))

        rsp = self.api_get(
            get_filediff_item_url(filediff, review_request),
            HTTP_ACCEPT='application/vnd.reviewboard.org.diff.data+json',
            expected_status=403)

        self.assertEqual(
            rsp,
            {
                'err': {
                    'code': PERMISSION_DENIED.code,
                    'msg': PERMISSION_DENIED.msg,
                    'type': 'resource-permission-denied',
                },
                'stat': 'fail',
            })

    @webapi_test_template
    def test_get_with_patch_and_inaccessible(self) -> None:
        """Testing the GET <URL> API with patch result and inaccessible
        FileDiff
        """
        repository = self.create_repository(tool_name='Git',
                                            public=False)
        review_request = self.create_review_request(
            repository=repository,
            publish=True)

        self.assertNotEqual(self.user, review_request.owner)
        self.assertFalse(review_request.is_accessible_by(self.user))

        diffset = self.create_diffset(review_request)
        filediff = self.create_filediff(
            diffset,
            source_file='newfile.py',
            source_revision=PRE_CREATION,
            dest_file='newfile.py',
            dest_detail='20e43bb7c2d9f3a31768404ac71121804d806f7c',
            diff=(
                b"diff --git a/newfile.py b/newfile.py\n"
                b"new file mode 100644\n"
                b"index 0000000000000000000000000000000000000000.."
                b"8eaa5c1eacb55c43f5e00ed9dcd0c8da901f0c85\n"
                b"--- /dev/null\n"
                b"+++ b/newfile.py\n"
                b"@@ -0,0 +1 @@\n"
                b"+print('hello, world!')\n"
            ))

        rsp = self.api_get(
            get_filediff_item_url(filediff, review_request),
            HTTP_ACCEPT='text/x-patch',
            expected_status=403)

        self.assertEqual(
            rsp,
            {
                'err': {
                    'code': PERMISSION_DENIED.code,
                    'msg': PERMISSION_DENIED.msg,
                    'type': 'resource-permission-denied',
                },
                'stat': 'fail',
            })