from django.utils import six
from djblets.util.filesystem import is_exe_in_path
        if not is_exe_in_path('hg'):
            raise nose.SkipTest('Hg is not installed')

        if not is_exe_in_path('hg'):
            raise nose.SkipTest('Hg is not installed')

        self.assertEqual(f.source_revision, revisions[0].decode('utf-8'))
        self.assertEqual(f.dest_detail, revisions[1].decode('utf-8'))
        original_file = get_original_file(filediff=f,
                                          request=None,
                                          encoding_list=['ascii'])
        patched_file = get_patched_file(source_data=original_file,
                                        filediff=f)
            b'5d36b88bb697a2d778f024048bafabd443d74503',
            b'9b32edcd37a88c6ada91efc562afa637ccfdad36',
            b'8a567d328293f85d68332bc693b0a98869b23b47',
        filediff = diffset.files.get()
        self.assertEqual(filediff.source_file, 'bar')
        self.assertEqual(filediff.dest_file, 'bar')
        self.assertEqual(filediff.source_revision, revisions[1].decode('utf-8'))
        self.assertEqual(filediff.dest_detail, revisions[2].decode('utf-8'))
        self.assertEqual(filediff.extra_data, {
            '__parent_diff_empty': False,
            'is_symlink': False,
            'parent_moved': True,
            'parent_source_filename': '/foo',
            'parent_source_revision': revisions[0].decode('utf-8'),
            'raw_delete_count': 0,
            'raw_insert_count': 1,
        })
        original_file = get_original_file(filediff=filediff,
                                          request=None,
                                          encoding_list=['ascii'])
        patched_file = get_patched_file(source_data=original_file,
                                        filediff=filediff)
    def test_create_missing_basedir(self):
    def test_create_with_parent_filediff_with_new_file(self):
        """Testing UploadDiffForm.create with a parent diff consisting of a
        newly-introduced file
        """
        revisions = [
            b'0000000000000000000000000000000000000000',
            b'9b32edcd37a88c6ada91efc562afa637ccfdad36',
            b'8a567d328293f85d68332bc693b0a98869b23b47',
        ]

        parent_diff = SimpleUploadedFile(
            'parent_diff',
            (b'diff --git a/foo b/foo\n'
             b'new file mode 100644\n'
             b'index %s..%s\n'
             b'--- /dev/null\n'
             b'+++ b/foo\n'
             b'@@ -0,0 +1,2 @@\n'
             b'+Foo\n'
             b'+Bar\n') % (revisions[0], revisions[1]),
            content_type='text/x-patch')

        diff = SimpleUploadedFile(
            'diff',
            (b'diff --git a/foo b/foo\n'
             b'index %s..%s 100644\n'
             b'--- a/foo\n'
             b'+++ b/foo\n'
             b'@@ -1,3 +1,4 @@\n'
             b' Foo\n'
             b' Bar\n'
             b'+Baz\n') % (revisions[1], revisions[2]),
            content_type='text/x-patch')

        repository = self.create_repository(tool_name='Test')
        self.spy_on(repository.get_file_exists,
                    call_fake=lambda *args, **kwargs: True)

        # We will only be making one call to get_file and we can fake it out.
        self.spy_on(repository.get_file,
                    call_fake=lambda *args, **kwargs: b'Foo\n')
        self.spy_on(patch)

        form = UploadDiffForm(
            repository=repository,
            data={
                'basedir': '/',
            },
            files={
                'parent_diff_path': parent_diff,
                'path': diff,
            })
        self.assertTrue(form.is_valid())

        diffset = form.create()
        self.assertEqual(diffset.files.count(), 1)

        filediff = diffset.files.get()
        self.assertEqual(filediff.source_file, 'foo')
        self.assertEqual(filediff.dest_file, 'foo')
        self.assertEqual(filediff.source_revision, revisions[1].decode('utf-8'))
        self.assertEqual(filediff.dest_detail, revisions[2].decode('utf-8'))
        self.assertEqual(filediff.extra_data, {
            '__parent_diff_empty': False,
            'is_symlink': False,
            'parent_source_filename': '/foo',
            'parent_source_revision': 'PRE-CREATION',
            'raw_delete_count': 0,
            'raw_insert_count': 1,
        })

        # Double-check the types.
        self.assertIsInstance(filediff.extra_data['parent_source_filename'],
                              six.text_type)
        self.assertIsInstance(filediff.extra_data['parent_source_revision'],
                              six.text_type)

        original_file = get_original_file(filediff=filediff,
                                          request=None,
                                          encoding_list=['ascii'])
        self.assertEqual(original_file, b'Foo\nBar\n')
        self.assertSpyCalled(patch)

        patched_file = get_patched_file(source_data=original_file,
                                        filediff=filediff)
        self.assertEqual(patched_file, b'Foo\nBar\nBaz\n')
        self.assertEqual(len(patch.calls), 2)

        validation_info = self._base64_json({
        })
        validation_info = self._base64_json({
        })
        validation_info = self._base64_json({
        })
        validation_info = self._base64_json({
        })
        validation_info = base64.b64encode(b'Not valid json.')

        # Python 2 and 3 differ in the error contents you'll get when
        # attempting to load non-JSON data.
        if six.PY3:
            expected_error = 'Expecting value: line 1 column 1 (char 0)'
        else:
            expected_error = 'No JSON object could be decoded'

                'Could not parse validation info "%s": %s'
                % (validation_info.decode('utf-8'), expected_error),
            b'index %s..%s 100644\n'
        validation_info = self._base64_json({
        })
        validation_info = self._base64_json({
        })
            with self.siteconfig_settings({'diffviewer_max_diff_size': 1},
                                          reload_settings=False):

    def _base64_json(self, data):
        """Return a Base64-encoded JSON payload.

        Args:
            data (object):
                The data to encode to JSON.

        Returns:
            bytes:
            The Base64-encoded JSON payload.
        """
        return base64.b64encode(json.dumps(data).encode('utf-8'))