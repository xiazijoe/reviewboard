from django.utils import six
from reviewboard.deprecation import RemovedInReviewBoard50Warning
    convert_line_endings,
    convert_to_unicode,
    get_filediffs_match,
    get_filediff_encodings,
    split_line_endings,
        self.spy_on(Repository.get_file,
                    owner=Repository,
                    call_fake=get_file)
                    owner=Repository,
    def test_with_single_line_replace(self):
        """Testing get_diff_data_chunks_info with single-line diff with
        replaced line
        """
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -1,1 +1,1 @@\n'
                b'-# old line\n'
                b'+# new line\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 0,
                        'post_lines_of_context': 0,
                        'chunk_start': 0,
                        'chunk_len': 1,
                        'changes_start': 0,
                        'changes_len': 1,
                    },
                    'modified': {
                        'pre_lines_of_context': 0,
                        'post_lines_of_context': 0,
                        'chunk_start': 0,
                        'chunk_len': 1,
                        'changes_start': 0,
                        'changes_len': 1,
                    },
                },
            ])

    def test_with_insert_before_only_line(self):
        """Testing get_diff_data_chunks_info with insert before only line
        in diff
        """
        self.assertEqual(
            get_diff_data_chunks_info(
                b'@@ -1,1 +1,2 @@\n'
                b'+# new line\n'
                b' #\n'),
            [
                {
                    'orig': {
                        'pre_lines_of_context': 1,
                        'post_lines_of_context': 0,
                        'chunk_start': 0,
                        'chunk_len': 1,
                        'changes_start': 0,
                        'changes_len': 0,
                    },
                    'modified': {
                        'pre_lines_of_context': 0,
                        'post_lines_of_context': 1,
                        'chunk_start': 0,
                        'chunk_len': 2,
                        'changes_start': 0,
                        'changes_len': 1,
                    },
                },
            ])

            diff=b'diff1')
            diff=b'diff2')
            diff=b'diff3')
            diff=b'diff4')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'interdiff2')
            diff=b'interdiff3')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'interdiff2')
        # Expecting 1 query:
        #
        # 1. Select all FileDiffs for a DiffSet.
        with self.assertNumQueries(1):
        # Expecting 1 query:
        #
        # 1. Select all FileDiffs for a DiffSet.
        with self.assertNumQueries(1):
        diff_commit = DiffCommit.objects.get(pk=2)

        # Sanity-check how many FileDiffs we're working with, for the query
        # assertion.
        self.assertEqual(len(self.filediffs), 9)

        # Expecting 9 queries:
        #
        # 1. Select all FileDiffs for a DiffSet.
        # 2. Update extra_data on FileDiff id=1.
        # 3. Update extra_data on FileDiff id=3.
        # 4. Update extra_data on FileDiff id=6.
        # 5. Update extra_data on FileDiff id=7.
        # 6. Update extra_data on FileDiff id=2.
        # 7. Update extra_data on FileDiff id=5.
        # 8. Update extra_data on FileDiff id=8.
        # 9. Update extra_data on FileDiff id=9.
        with self.assertNumQueries(9):
                                   base_commit=diff_commit)
                    (3, 'corge', 'e69de29', 'corge', 'f248ba3'),
        tip_commit = DiffCommit.objects.get(pk=3)

        # Sanity-check how many FileDiffs we're working with, for the query
        # assertion.
        self.assertEqual(len(self.filediffs), 9)

        # Expecting 9 queries:
        #
        # 1. Select all FileDiffs for a DiffSet.
        # 2. Update extra_data on FileDiff id=1.
        # 3. Update extra_data on FileDiff id=3.
        # 4. Update extra_data on FileDiff id=6.
        # 5. Update extra_data on FileDiff id=7.
        # 6. Update extra_data on FileDiff id=2.
        # 7. Update extra_data on FileDiff id=5.
        # 8. Update extra_data on FileDiff id=8.
        # 9. Update extra_data on FileDiff id=9.
        with self.assertNumQueries(9):
                                   tip_commit=tip_commit)
                    (2, 'baz', '7601807', 'baz', '280beb2'),
                    (3, 'corge', 'e69de29', 'corge', 'f248ba3'),
        tip_commit = DiffCommit.objects.get(pk=3)

        # Expecting 1 query:
        #
        # 1. Select all FileDiffs for a DiffSet.
        with self.assertNumQueries(1):
                                   tip_commit=tip_commit)
                    (2, 'baz', '7601807', 'baz', '280beb2'),
                    (3, 'corge', 'e69de29', 'corge', 'f248ba3'),
        commits = DiffCommit.objects.in_bulk([2, 3])
        base_commit = commits[2]
        tip_commit = commits[3]

        # Sanity-check how many FileDiffs we're working with, for the query
        # assertion.
        self.assertEqual(len(self.filediffs), 9)

        # Expecting 8 queries:
        #
        # 1. Select all FileDiffs for a DiffSet.
        # 2. Update extra_data on FileDiff id=1.
        # 3. Update extra_data on FileDiff id=3.
        # 4. Update extra_data on FileDiff id=6.
        # 5. Update extra_data on FileDiff id=7.
        # 6. Update extra_data on FileDiff id=2.
        # 7. Update extra_data on FileDiff id=5.
        # 8. Update extra_data on FileDiff id=8.
        with self.assertNumQueries(8):
                                   base_commit=base_commit,
                                   tip_commit=tip_commit)
                    (3, 'corge', 'e69de29', 'corge', 'f248ba3'),
        commits = DiffCommit.objects.in_bulk([2, 3])
        base_commit = commits[2]
        tip_commit = commits[3]

        # Expecting 1 query:
        #
        # 1. Select all FileDiffs for a DiffSet.
        with self.assertNumQueries(1):
                                   base_commit=base_commit,
                                   tip_commit=tip_commit)
                    (3, 'corge', 'e69de29', 'corge', 'f248ba3'),
    @add_fixtures(['test_users', 'test_scmtools'])
    def test_get_diff_files_filename_normalization_extra_data(self):
        """Testing that filename normalization from get_diff_files receives
        FileDiff extra_data
        """
        repository = self.create_repository(tool_name='Git')
        review_request = self.create_review_request(repository=repository)

        diffset = self.create_diffset(review_request=review_request,
                                      revision=1)

        filediff = self.create_filediff(
            diffset=diffset,
            source_file='foo.txt',
            source_revision=123,
            dest_file='foo.txt',
            diff=b'diff1')
        filediff.extra_data['test'] = True

        tool_class = repository.scmtool_class
        self.spy_on(tool_class.normalize_path_for_display,
                    owner=tool_class)

        get_diff_files(diffset=diffset, filediff=filediff)

        self.assertSpyCalledWith(tool_class.normalize_path_for_display,
                                 'foo.txt', extra_data={'test': True})


class GetFileDiffsMatchTests(TestCase):
    """Unit tests for get_filediffs_match."""

    fixtures = ['test_scmtools', 'test_users']

    def setUp(self):
        super(GetFileDiffsMatchTests, self).setUp()

        review_request = self.create_review_request(create_repository=True)
        self.diffset = self.create_diffset(review_request)

    def test_with_filediff_none(self):
        """Testing get_filediffs_match with either filediff as None"""
        filediff = self.create_filediff(self.diffset, save=False)

        self.assertFalse(get_filediffs_match(filediff, None))
        self.assertFalse(get_filediffs_match(None, filediff))

        message = 'filediff1 and filediff2 cannot both be None'

        with self.assertRaisesMessage(ValueError, message):
            self.assertFalse(get_filediffs_match(None, None))

    def test_with_diffs_equal(self):
        """Testing get_filediffs_match with diffs equal"""
        filediff1 = self.create_filediff(self.diffset,
                                         diff=b'abc',
                                         save=False)
        filediff2 = self.create_filediff(self.diffset,
                                         diff=b'abc',
                                         save=False)

        self.assertTrue(get_filediffs_match(filediff1, filediff2))

    def test_with_deleted_true(self):
        """Testing get_filediffs_match with deleted flags both set"""
        self.assertTrue(get_filediffs_match(
            self.create_filediff(self.diffset,
                                 diff=b'abc',
                                 status=FileDiff.DELETED,
                                 save=False),
            self.create_filediff(self.diffset,
                                 diff=b'def',
                                 status=FileDiff.DELETED,
                                 save=False)))

    def test_with_sha256_equal(self):
        """Testing get_filediffs_match with patched SHA256 hashes equal"""
        filediff1 = self.create_filediff(self.diffset,
                                         diff=b'abc',
                                         save=False)
        filediff2 = self.create_filediff(self.diffset,
                                         diff=b'def',
                                         save=False)

        filediff1.extra_data['patched_sha256'] = 'abc123'
        filediff2.extra_data['patched_sha256'] = 'abc123'

        self.assertTrue(get_filediffs_match(filediff1, filediff2))

    def test_with_sha1_equal(self):
        """Testing get_filediffs_match with patched SHA1 hashes equal"""
        filediff1 = self.create_filediff(self.diffset,
                                         diff=b'abc',
                                         save=False)
        filediff2 = self.create_filediff(self.diffset,
                                         diff=b'def',
                                         save=False)

        filediff1.extra_data['patched_sha1'] = 'abc123'
        filediff2.extra_data['patched_sha1'] = 'abc123'

        self.assertTrue(get_filediffs_match(filediff1, filediff2))

    def test_with_sha1_not_equal(self):
        """Testing get_filediffs_match with patched SHA1 hashes not equal"""
        filediff1 = self.create_filediff(self.diffset,
                                         diff=b'abc',
                                         save=False)
        filediff2 = self.create_filediff(self.diffset,
                                         diff=b'def',
                                         save=False)

        filediff1.extra_data['patched_sha1'] = 'abc123'
        filediff2.extra_data['patched_sha1'] = 'def456'

        self.assertFalse(get_filediffs_match(filediff1, filediff2))

    def test_with_sha256_not_equal_and_sha1_equal(self):
        """Testing get_filediffs_match with patched SHA256 hashes not equal
        and patched SHA1 hashes equal
        """
        filediff1 = self.create_filediff(self.diffset,
                                         diff=b'abc',
                                         save=False)
        filediff2 = self.create_filediff(self.diffset,
                                         diff=b'def',
                                         save=False)

        filediff1.extra_data.update({
            'patched_sha256': 'abc123',
            'patched_sha1': 'abcdef',
        })
        filediff2.extra_data.update({
            'patched_sha256': 'def456',
            'patched_sha1': 'abcdef',
        })

        self.assertFalse(get_filediffs_match(filediff1, filediff2))


            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'diff1')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'diff1')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'diff1')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'interdiff3')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'diff1')
            diff=b'diff2')
            diff=b'diff3')
            diff=b'diff1')
            diff=b'interdiff1')
            diff=b'interdiff2')
            diff=b'interdiff3')
            diff=b'interdiff4')
            diff=b'interdiff5')
            diff=b'diff1')
            diff=b'interdiff1')
            diff=b'diff2')
            diff=b'interdiff2')
            diff=b'diff3')
            diff=b'interdiff3')

        siteconfig_settings = {
            'diffviewer_syntax_highlighting': False,
        }

        with self.siteconfig_settings(siteconfig_settings,
                                      reload_settings=False):
            header = get_last_header_before_line(context=context,
                                                 filediff=filediff,
                                                 interfilediff=None,
                                                 target_line=line_number)
            chunks = get_file_chunks_in_range(
                context=context,
                filediff=filediff,
                interfilediff=None,
                first_line=1,
                num_lines=get_last_line_number_in_diff(
                    context=context,
                    filediff=filediff,
                    interfilediff=None))
        siteconfig_settings = {
            'diffviewer_syntax_highlighting': False,
        }

        with self.siteconfig_settings(siteconfig_settings,
                                      reload_settings=False):
            header = get_last_header_before_line(context=context,
                                                 filediff=filediff,
                                                 interfilediff=None,
                                                 target_line=line_number)
            chunks = get_file_chunks_in_range(
                context=context,
                filediff=filediff,
                interfilediff=None,
                first_line=1,
                num_lines=get_last_line_number_in_diff(
                    context=context,
                    filediff=filediff,
                    interfilediff=None))
        patched = patch(diff=diff,
                        orig_file=old,
                        filename='foo.c')
            patch(diff=diff,
                  orig_file=old,
                  filename='foo.c')
        patched = patch(diff=diff,
                        orig_file=old,
                        filename='test.c')
        patched = patch(diff=diff,
                        orig_file=old,
                        filename='README')
        patched = patch(diff=diff,
                        orig_file=old,
                        filename='README')
        patched = patch(diff=diff,
                        orig_file=old,
                        filename='README')
        patched = patch(diff=diff,
                        orig_file=old,
                        filename='README')
class GetFileDiffEncodingsTests(TestCase):
    """Unit tests for get_filediff_encodings."""

    fixtures = ['test_scmtools']

    def setUp(self):
        super(GetFileDiffEncodingsTests, self).setUp()

        self.repository = self.create_repository(encoding='ascii,iso-8859-15')
        self.diffset = self.create_diffset(repository=self.repository)

    def test_with_stored_encoding(self):
        """Testing get_filediff_encodings with recorded FileDiff.encoding"""
        filediff = self.create_filediff(self.diffset,
                                        encoding='utf-16')

        self.assertEqual(get_filediff_encodings(filediff),
                         ['utf-16', 'ascii', 'iso-8859-15'])

    def test_with_out_stored_encoding(self):
        """Testing get_filediff_encodings without recorded FileDiff.encoding"""
        filediff = self.create_filediff(self.diffset)

        self.assertEqual(get_filediff_encodings(filediff),
                         ['ascii', 'iso-8859-15'])

    def test_with_custom_encodings(self):
        """Testing get_filediff_encodings with custom encoding_list"""
        filediff = self.create_filediff(self.diffset)

        self.assertEqual(
            get_filediff_encodings(filediff,
                                   encoding_list=['rot13', 'palmos']),
            ['rot13', 'palmos'])


        self.set_up_filediffs()

        self.assertEqual(get_original_file(filediff=filediff), b'bar\n')
            filediff=filediff,
            request=None,
            encoding_list=None))
        self.set_up_filediffs()

        self.assertEqual(get_original_file(filediff=filediff), b'baz\n')
        self.set_up_filediffs()

        self.assertEqual(get_original_file(filediff=filediff), b'')
        self.set_up_filediffs()

        self.assertEqual(get_original_file(filediff=filediff), b'foo\n')
        self.set_up_filediffs()

                filename=filename,
                error_output=_PATCH_GARBAGE_INPUT,
                orig_file=orig_file,
                new_file='tmp123-new',
                diff=b'',
                rejects=None)
            orig = get_original_file(filediff=filediff)
            orig = get_original_file(filediff=filediff)
        self.set_up_filediffs()

            orig = get_original_file(filediff=filediff)
            orig = get_original_file(filediff=filediff)
        self.set_up_filediffs()

            orig = get_original_file(filediff=filediff)

    def test_with_encoding_list(self):
        """Testing get_original_file with encoding_list is deprecated"""
        self.set_up_filediffs()

        filediff = FileDiff.objects.get(dest_file='bar',
                                        dest_detail='8e739cc',
                                        commit_id=1)

        message = (
            'The encoding_list parameter passed to get_original_file() is '
            'deprecated and will be removed in Review Board 5.0.'
        )

        with self.assert_warns(RemovedInReviewBoard50Warning, message):
            get_original_file(filediff, encoding_list=['ascii'])

    def test_parent_diff_with_rename_and_modern_fields(self):
        """Testing get_original_file with a file renamed in parent diff
        with modern parent_source_* keys in extra_data
        """
        parent_diff = (
            b'diff --git a/old-name b/new-name\n'
            b'rename from old-name\n'
            b'rename to new-name\n'
            b'index b7a8c9f..e69de29 100644\n'
            b'--- a/old-name\n'
            b'+++ a/new-name\n'
            b'@@ -1,1 +1,1 @@\n'
            b'-orig file\n'
            b'+abc123\n'
        )

        diff = (
            b'diff --git a/new-name b/new-name\n'
            b'index e69de29..0e4b0c7 100644\n'
            b'--- a/new-name\n'
            b'+++ a/new-name\n'
            b'@@ -1,1 +1,1 @@\n'
            b'+abc123\n'
            b'+def456\n'
        )

        repository = self.create_repository(tool_name='Git')
        diffset = self.create_diffset(repository=repository)
        filediff = FileDiff.objects.create(
            diffset=diffset,
            source_file='new-name',
            source_revision='e69de29',
            dest_file='new-name',
            dest_detail='0e4b0c7',
            extra_data={
                'encoding': 'ascii',
                'parent_source_filename': 'old-file',
                'parent_source_revision': 'b7a8c9f',
            })
        filediff.parent_diff = parent_diff
        filediff.diff = diff
        filediff.save()

        request_factory = RequestFactory()

        def _get_file(_self, path, revision, *args, **kwargs):
            self.assertEqual(path, 'old-file')
            self.assertEqual(revision, 'b7a8c9f')

            return b'orig file\n'

        self.spy_on(repository.get_file, call_fake=_get_file)

        with self.assertNumQueries(0):
            orig = get_original_file(filediff=filediff,
                                     request=request_factory.get('/'),
                                     encoding_list=['ascii'])

        self.assertEqual(orig, b'abc123\n')

        # Refresh the object from the database with the parent diff attached
        # and then verify that re-calculating the original file does not cause
        # additional queries.
        filediff = (
            diffset.files
            .select_related('parent_diff_hash')
            .get(pk=filediff.pk)
        )

        with self.assertNumQueries(0):
            orig = get_original_file(filediff=filediff,
                                     request=request_factory.get('/'),
                                     encoding_list=['ascii'])

    def test_with_filediff_with_encoding_set(self):
        """Testing get_original_file with FileDiff.encoding set"""
        content = 'hello world'.encode('utf-16')

        repository = self.create_repository()
        self.spy_on(repository.get_file,
                    call_fake=lambda *args, **kwargs: content)
        self.spy_on(convert_to_unicode)
        self.spy_on(convert_line_endings)

        diffset = self.create_diffset(repository=repository)
        filediff = self.create_filediff(diffset,
                                        encoding='utf-16')

        self.assertEqual(get_original_file(filediff=filediff), content)
        self.assertTrue(convert_to_unicode.called_with(
            content, ['utf-16', 'iso-8859-15']))
        self.assertTrue(convert_line_endings.called_with('hello world'))

    def test_with_filediff_with_repository_encoding_set(self):
        """Testing get_original_file with Repository.encoding set"""
        content = 'hello world'.encode('utf-16')

        repository = self.create_repository(encoding='utf-16')
        self.spy_on(repository.get_file,
                    call_fake=lambda *args, **kwargs: content)
        self.spy_on(convert_to_unicode)
        self.spy_on(convert_line_endings)

        diffset = self.create_diffset(repository=repository)
        filediff = self.create_filediff(diffset)

        self.assertEqual(get_original_file(filediff=filediff), content)
        self.assertTrue(convert_to_unicode.called_with(content, ['utf-16']))
        self.assertTrue(convert_line_endings.called_with('hello world'))


class SplitLineEndingsTests(TestCase):
    """Unit tests for reviewboard.diffviewer.diffutils.split_line_endings."""

    def test_with_byte_string(self):
        """Testing split_line_endings with byte string"""
        lines = split_line_endings(
            b'This is line 1\n'
            b'This is line 2\r\n'
            b'This is line 3\r'
            b'This is line 4\r\r\n'
            b'This is line 5'
        )

        for line in lines:
            self.assertIsInstance(line, bytes)

        self.assertEqual(
            lines,
            [
                b'This is line 1',
                b'This is line 2',
                b'This is line 3',
                b'This is line 4',
                b'This is line 5',
            ])

    def test_with_unicode_string(self):
        """Testing split_line_endings with unicode string"""
        lines = split_line_endings(
            'This is line 1\n'
            'This is line 2\r\n'
            'This is line 3\r'
            'This is line 4\r\r\n'
            'This is line 5'
        )

        for line in lines:
            self.assertIsInstance(line, six.text_type)

        self.assertEqual(
            lines,
            [
                'This is line 1',
                'This is line 2',
                'This is line 3',
                'This is line 4',
                'This is line 5',
            ])